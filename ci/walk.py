#!/usr/bin/env python3
"""Sanad screen walker for CI.

Reads ci/screens.txt. Each non-comment line:
    package|activity|extras|name[|taps]
  - extras: passed verbatim to `am start` (e.g. `--es screen agent`).
  - taps:   fallback path of Arabic labels separated by `>` (substring match on the
            on-screen text, tapped at the text's bounds; scrolls to find it).
            `*` = explore: tap every card title on the current page one level deep.
With --deeplink 1 and non-empty extras, taps are skipped (the app opens the screen).
First launch of each package runs an onboarding pass (taps Next/Start/Skip-like
buttons until the home page shows) and saves each step as <pkg>_onboard_NN.png.
"""
import argparse, os, re, subprocess, sys, time, xml.etree.ElementTree as ET

def sh(cmd, t=40):
    try:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=t).stdout
    except subprocess.TimeoutExpired:
        return ""

def adb(c, t=40): return sh("adb shell " + c, t)

OUT = "shots"
def shot(name):
    p = os.path.join(OUT, re.sub(r"[^\w.\-]+", "_", name) + ".png")
    sh(f"adb exec-out screencap -p > '{p}'", 30)
    sz = os.path.getsize(p) if os.path.exists(p) else 0
    print(f"  shot {p} ({sz} bytes)"); return p

def dump():
    for _ in range(3):
        sh("adb shell rm -f /sdcard/w.xml"); adb("uiautomator dump /sdcard/w.xml", 30)
        x = sh("adb exec-out cat /sdcard/w.xml", 20)
        if x.strip().startswith("<?xml"):
            try: return ET.fromstring(x)
            except ET.ParseError: pass
        time.sleep(1.5)
    return None

def nodes(root):
    if root is None: return []
    out = []
    for n in root.iter("node"):
        b = re.findall(r"\d+", n.get("bounds", ""))
        if len(b) != 4: continue
        x1, y1, x2, y2 = map(int, b)
        if x2 - x1 < 4 or y2 - y1 < 4: continue
        out.append(dict(text=(n.get("text") or "") + " " + (n.get("content-desc") or ""), pkg=n.get("package", ""),
                        rid=n.get("resource-id", ""), click=n.get("clickable") == "true",
                        scroll=n.get("scrollable") == "true", cls=n.get("class", ""), c=((x1 + x2) // 2, (y1 + y2) // 2), b=(x1, y1, x2, y2)))
    return out

def norm(s):  # drop diacritics / tatweel / emoji so "سَنَد" matches "سند"
    s = re.sub(r"[\u064B-\u0652\u0670\u0640]", "", s)
    return re.sub(r"[^\w\s]", "", s).strip()

def tap(x, y): adb(f"input tap {x} {y}"); time.sleep(2.2)
def back(): adb("input keyevent KEYCODE_BACK"); time.sleep(1.5)
def screen_h():
    m = re.search(r"(\d+)x(\d+)", adb("wm size")); return (int(m.group(1)), int(m.group(2))) if m else (1080, 2400)
W, H = 1080, 2400
def swipe_up(): adb(f"input swipe {W//2} {int(H*0.78)} {W//2} {int(H*0.30)} 350"); time.sleep(1.2)
def swipe_down(): adb(f"input swipe {W//2} {int(H*0.30)} {W//2} {int(H*0.80)} 300"); time.sleep(0.8)
def to_top():
    for _ in range(5): swipe_down()

def find(label, ns):
    L = norm(label)
    best = None
    for n in ns:
        t = norm(n["text"])
        if L and L in t and n["b"][1] > 60 and n["b"][3] < H - 20:
            if best is None or len(t) < len(norm(best["text"])): best = n
    return best

def tap_label(label, pkg):
    for i in range(8):
        ns = nodes(dump())
        n = find(label, ns)
        if n: print(f"  tap '{label}' @ {n['c']}"); tap(*n["c"]); return True
        if any(x["rid"].startswith("android:id/button") for x in ns) and i == 0:
            print("  dialog in the way -> back"); back(); continue
        swipe_up()
    print(f"  NOT FOUND '{label}'"); return False

def focused_pkg():
    m = re.search(r"mCurrentFocus=Window\{\S+ \S+ ([\w.]+)/", adb("dumpsys window | grep mCurrentFocus"))
    return m.group(1) if m else ""

def is_home(ns, pkg):
    txt = " ".join(norm(n["text"]) for n in ns)
    if pkg == "com.sanad.app": return "عقل الوكيل" in txt and ("الاتمتة" in txt or "الأتمتة" in txt or "مركز الخصوصية" in txt)
    return False

GO = ["بعدين", "لاحقا", "مش دلوقتي", "من غير", "ادخل", "خلصت", "يلا بينا", "تخطي", "تخطى", "ابدأ", "ابدا", "يلا", "التالي", "كمل", "كمّل", "متابعة", "موافق", "تمام", "دخول", "افتح", "السماح", "Allow", "Next", "Start", "Skip", "OK", "Continue"]
BAD = ["إمكانية الوصول", "امكانية الوصول", "معلومات التطبيق", "الإعدادات المقيدة", "بالإعدادات المقيدة", "Allow restricted", "الخطوة"]
PIN = "135790"

def launch(pkg, act, extras="", wait=6.0):
    adb(f"am force-stop {pkg}"); time.sleep(0.8)
    a = act if act.startswith(pkg) or "/" in act else (pkg + "/" + act)
    if "/" not in a: a = pkg + "/" + act
    print(f"  am start -n {a} {extras}"); print(adb(f"am start -W -n {a} {extras}", 60).strip()[-200:])
    time.sleep(wait)

def onboard(pkg, act):
    launch(pkg, act, "", 7)
    tapped = {}
    for step in range(24):
        if focused_pkg() not in (pkg, ""):
            print(f"  left app ({focused_pkg()}) -> back"); back(); continue
        ns = nodes(dump())
        if is_home(ns, pkg): print("  home reached"); return True
        shot(f"{pkg.split('.')[-1]}_onboard_{step:02d}")
        edits = [n for n in ns if n["pkg"] == pkg and "EditText" in n["cls"]]
        if edits and pkg == "com.sanad.admin":  # owner PIN (fresh emulator: choose then confirm a throwaway PIN)
            tap(*edits[0]["c"]); adb(f"input text {PIN}"); time.sleep(0.8)
            adb("input keyevent KEYCODE_BACK"); time.sleep(0.8)
            ns = nodes(dump()); b = find("دخول", ns) or find("تأكيد", ns) or find("حفظ", ns)
            if b: print("  admin PIN entered"); tap(*b["c"]); time.sleep(2)
            continue
        cands = [n for n in ns if n["pkg"] == pkg and norm(n["text"]) and not any(norm(b) in norm(n["text"]) for b in BAD)]
        pick = None
        for g in GO:
            for n in cands:
                t = norm(n["text"])
                if norm(g) and norm(g) in t and len(t) < 30 and tapped.get(t, 0) < 2: pick = n; break
            if pick: break
        if not pick:
            btns = [n for n in ns if n["pkg"] == pkg and n["click"] and tapped.get(norm(n["text"]), 0) < 2
                    and not any(norm(b) in norm(n["text"]) for b in BAD)]
            if btns and step % 2 == 0: pick = max(btns, key=lambda n: n["b"][3])  # bottom-most clickable
            else: print("  scroll for more"); swipe_up(); swipe_up(); continue
        t = norm(pick["text"]); tapped[t] = tapped.get(t, 0) + 1
        print(f"  onboarding tap '{pick['text'].strip()[:40]}'"); tap(*pick["c"])
    if pkg == "com.sanad.app":  # last resort: mark onboarded (works only if the APK is debuggable)
        print("  run-as fallback:", adb("run-as com.sanad.app sh -c 'ls shared_prefs'"))
    return False

def page_scrollable(ns): return any(n["scroll"] for n in ns)

def capture(name, deep):
    shot(name)
    ns = nodes(dump())
    if page_scrollable(ns):
        swipe_up(); swipe_up(); shot(name + "_b")

def explore(pkg, act, name):
    """Tap every short text on the page one level deep (used for the admin app)."""
    ns = nodes(dump())
    labels = []
    for n in ns:
        t = n["text"].strip()
        if n["pkg"] == pkg and 1 < len(norm(t)) < 30 and t not in labels and n["b"][1] > 150: labels.append(t)
    print(f"  explore {len(labels)} labels")
    for i, l in enumerate(labels[:14]):
        launch(pkg, act, "", 5)
        if tap_label(l, pkg): capture(f"{name}_{i:02d}", False)

def main():
    global OUT, W, H
    ap = argparse.ArgumentParser(); ap.add_argument("--screens"); ap.add_argument("--out", default="shots"); ap.add_argument("--deeplink", default="0")
    a = ap.parse_args(); OUT = a.out; os.makedirs(OUT, exist_ok=True); W, H = screen_h()
    deep = a.deeplink == "1"
    done = set(); ok = 0; total = 0
    for line in open(a.screens, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"): continue
        f = (line.split("|") + ["", "", "", "", ""])[:5]
        pkg, act, extras, name, taps = [x.strip() for x in f]
        if pkg not in adb("pm list packages"): print(f"SKIP {name}: {pkg} not installed"); continue
        total += 1; print(f"== {name}")
        try:
            if pkg not in done: onboard(pkg, act); done.add(pkg)
            if deep and extras:
                launch(pkg, act, extras, 6); capture(name, True); ok += 1; continue
            launch(pkg, act, "", 6)
            if focused_pkg() not in (pkg, ""): back()
            if taps == "*": shot(name); explore(pkg, act, name); ok += 1; continue
            good = True
            for lbl in [t for t in taps.split(">") if t.strip()]:
                if not tap_label(lbl.strip(), pkg): good = False; break
            capture(name if good else name + "_NOTFOUND", deep); ok += good
        except Exception as e:
            print(f"  ERROR {name}: {e}")
    print(f"walk done: {ok}/{total} screens reached")

if __name__ == "__main__": main()
