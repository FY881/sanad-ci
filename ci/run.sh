#!/usr/bin/env bash
# Runs inside reactivecircus/android-emulator-runner (emulator already booted).
set -u
OUT=shots; mkdir -p "$OUT"
LOG="$OUT/run.log"; exec > >(tee -a "$LOG") 2>&1
adb wait-for-device
adb shell getprop ro.product.cpu.abilist
adb shell settings put global window_animation_scale 0
adb shell settings put global transition_animation_scale 0
adb shell settings put global animator_duration_scale 0
adb shell settings put system screen_off_timeout 1800000
adb shell svc power stayon true
adb shell input keyevent KEYCODE_WAKEUP
adb shell wm dismiss-keyguard || true
adb logcat -c || true
adb logcat -b crash -c || true

install() { # $1 apk
  [ -f "$1" ] || { echo "MISSING $1"; return 1; }
  adb install -r -g "$1" && return 0
  echo "plain install failed, retrying with --abi arm64-v8a (ARM translation)"
  adb install -r -g --abi arm64-v8a "$1"
}
install apks/sanad.apk || echo "INSTALL FAILED sanad.apk"
install apks/sanad-admin.apk || echo "INSTALL FAILED sanad-admin.apk"
adb shell pm list packages | grep -i sanad

PERMS="READ_CONTACTS RECORD_AUDIO POST_NOTIFICATIONS READ_CALENDAR ACCESS_FINE_LOCATION ACCESS_COARSE_LOCATION CAMERA READ_MEDIA_IMAGES READ_MEDIA_VIDEO READ_EXTERNAL_STORAGE"
for pkg in com.sanad.app com.sanad.admin; do
  for p in $PERMS; do adb shell pm grant $pkg android.permission.$p 2>/dev/null || true; done
  adb shell appops set $pkg SCHEDULE_EXACT_ALARM allow 2>/dev/null || true
  adb shell appops set $pkg GET_USAGE_STATS allow 2>/dev/null || true
  adb shell cmd deviceidle whitelist +$pkg 2>/dev/null || true
done

python3 ci/walk.py --screens ci/screens.txt --out "$OUT" --deeplink "${DEEPLINK:-0}" || echo "walk.py exited $?"

# Crashes: crash buffer + fatal/ANR lines from main log
{
  echo "=== logcat -b crash ==="; adb logcat -d -b crash
  echo; echo "=== FATAL / ANR / AndroidRuntime (main) ==="
  adb logcat -d | grep -E -A 25 "FATAL EXCEPTION|ANR in|E AndroidRuntime" | grep -v "^--$" | head -800
} > "$OUT/crashes.txt" 2>&1
adb logcat -d -v time > "$OUT/logcat_full.txt" 2>&1 || true
if grep -qE "FATAL EXCEPTION|ANR in" "$OUT/crashes.txt"; then echo "CRASHES FOUND" | tee "$OUT/CRASHES_FOUND"; else echo "no crashes"; fi
ls -la "$OUT"
exit 0
