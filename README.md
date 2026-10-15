<!-- سَنَد · Sanad — project showcase. Assets live in ./assets (self-hosted, no third-party widgets except shields.io badges). -->

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img alt="سَنَد · Sanad — the Egyptian-Arabic AI agent for Android" src="assets/hero-dark.svg" width="100%">
</picture>

<br/>

<img src="assets/typing.svg" alt="وكيل ذكي بيفهم مصري · An Egyptian-Arabic AI agent for Android" width="760"/>

<br/><br/>

<img alt="v6.0.0 «الأفق»" src="https://img.shields.io/badge/v6.0.0-%C2%AB%D8%A7%D9%84%D8%A3%D9%81%D9%82%C2%BB-f5a524?style=for-the-badge"/> <img alt="stable: 6.0.0" src="https://img.shields.io/badge/stable-6.0.0-10b981?style=for-the-badge"/> <img alt="Android: 7.0+ (API 24)" src="https://img.shields.io/badge/Android-7.0%2B_%28API_24%29-3ddc84?style=for-the-badge&logo=android&logoColor=white"/> <img alt="JDK tests: 9,799 / 0 failed" src="https://img.shields.io/badge/JDK_tests-9%2C799_%2F_0_failed-22c55e?style=for-the-badge"/> <img alt="server tests: 1,235 / 0 failed" src="https://img.shields.io/badge/server_tests-1%2C235_%2F_0_failed-22c55e?style=for-the-badge"/> <img alt="red team: 189 / 189" src="https://img.shields.io/badge/red_team-189_%2F_189-ef4444?style=for-the-badge"/> <img alt="emulator: 249 / 249 screens · 0 crashes" src="https://img.shields.io/badge/emulator-249_%2F_249_screens_%C2%B7_0_crashes-0ea5e9?style=for-the-badge"/> <img alt="AI: on-device first" src="https://img.shields.io/badge/AI-on--device_first-7c4dff?style=for-the-badge"/> <img alt="privacy: first" src="https://img.shields.io/badge/privacy-first-8b5cf6?style=for-the-badge"/> <img alt="server: Cloudflare Worker" src="https://img.shields.io/badge/server-Cloudflare_Worker-f38020?style=for-the-badge&logo=cloudflare&logoColor=white"/> <img alt="license: proprietary · private" src="https://img.shields.io/badge/license-proprietary_%C2%B7_private-64748b?style=for-the-badge"/>

<br/><br/>

<b><a href="#ar">العربية</a></b> &nbsp;·&nbsp; <b><a href="#en">English</a></b> &nbsp;·&nbsp; <a href="#showcase">العرض</a> &nbsp;·&nbsp; <a href="#new6">الجديد في 6.0</a> &nbsp;·&nbsp; <a href="#features">الميزات</a> &nbsp;·&nbsp; <a href="#gallery">المعرض</a> &nbsp;·&nbsp; <a href="#architecture">المعمار</a> &nbsp;·&nbsp; <a href="#roadmap">الخطة</a> &nbsp;·&nbsp; <a href="#promises">وعودنا</a>

</div>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""/></p>

<a id="ar"></a>
<div dir="rtl" align="right">

## <img src="assets/emoji/sparkles.png" width="30" alt=""/> سَنَد في سطرين

**سَنَد** وكيل ذكي للموبايل بيفهم **مصري** وبيشتغل **على موبايلك إنت**: بيقرا الشاشة، وبيكمّل المهام خطوة بخطوة، وبيفتكر اللي يهمّك، وبيحمي عيلتك.
في 6.0 «الأفق» بقى عنده **جيش وكلاء** بيشتغل لحسابك أيام وأسابيع، جوه **دستور** واضح وقوانين و**موافقات**، وبيحرسه فريق أمن من وكلاء الذكاء الاصطناعي، و**القرار الأخير دايمًا لإنسان**.

> [!NOTE]
> المستودع ده خاص بالـCI بتاع سَنَد: بناء الـAPK والاختبارات واللقطات الحقيقية من محاكي Android. كل الصور هنا **لقطات حقيقية من المحاكي** لنسخة 6.0.0 (والأقسام القديمة من 5.0)، ببيانات تجريبية فاضية، ومفيهاش أي بيانات لمستخدم أو لطفل.

</div>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""/></p>

<a id="showcase"></a>
<div align="center">

## <img src="assets/emoji/rocket.png" width="30" alt=""/> العرض · Showcase

<img src="assets/showcase.gif" width="340" alt="جولة في سَنَد: لقطات حقيقية من محاكي Android"/>

<sub>لقطات حقيقية من محاكي Android 14 · Real Android 14 emulator captures, sanad 6.0.0</sub>

</div>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""/></p>

<a id="new6"></a>
<div dir="rtl">

## <img src="assets/emoji/sparkles.png" width="30" alt=""/> الجديد في 6.0 «الأفق» · What's new in 6.0

6.0.0 اتبنت على 7 موجات، كل موجة بإصدار داخلي واختباراتها:

| الموجة | الإصدار | اللي اتعمل | What shipped |
|:--:|:--:|:--|:--|
| **A** | 5.1.0 | جيش الوكلاء: القائد العام، و12 كتيبة، ووكلاء أحرار، والمراجع والمحاسب، ودستور من 10 مواد، و4 مستويات موافقة | Agent army, constitution, 4 approval levels |
| **B** | 5.2.0 | محرك العضويات الـ8 ونظام العدل: تذكير قبل التجديد، وإلغاء بضغطتين، واسترداد، واعتراض يراجعه إنسان | 8-tier membership engine + fairness system |
| **C** | 5.3.0 | 13 ميزة عبقرية: التوأم الرقمي، والمحاكي، والأوراق والفواتير، والفرص، والإرث الرقمي، ووكيل الموظف… | 13 «genius» features (digital twin, bills, legacy…) |
| **D** | 5.4.0 | المطوّرين وسوق الوكلاء 2.0 والـSDK، والتطوير الذاتي، و7 مستندات قانونية (151/2020، 181/2018، 175/2018، 15/2004) | Developer market + SDK, self-development, Egyptian legal docs |
| **E** | 5.5.0 | المالك + 5 رتب، وقاعدة الشخصين، ودخول الأدمن بمفتاح، ووكلاء الرتب، وسجل تدقيق مسلسل | Owner + 5 ranks, two-person rule, chained audit |
| **F** | 5.6.0 | مركز الأمن الذكي بـ6 وكلاء، والفريق الأحمر 189/189 سيناريو، وتقوية التطبيق | AI security center + red team (189/189) |
| **G** | 6.0.0 | مراجعة ثوابت الأمان، وإصلاح أخطاء حقيقية، وبناء الإصدار، ولقطات المحاكي 249/249 من غير ولا كراش | Safety-invariant QA, release build, 249/249 emulator screens |

**الاختبارات:** JDK **9,799 / 0** · السيرفر **1,235 / 0** · الفريق الأحمر **189 / 189** · المحاكي **249 / 249 شاشة، 0 كراش**.<br/>
<sub>Tests: JDK 9,799 / 0 failed · server 1,235 / 0 failed · red team 189 / 189 · emulator 249 / 249 screens, 0 crashes.</sub>

> [!NOTE]
> الأسعار **مقترحة** والدفع **مقفول**، والسيرفر لسه مش متنشر، فشاشات الرتب ومركز الأمن بتظهر في الوضع المحلي.<br/>
> <sub>Prices are proposed, payments are off, and the server is not deployed yet, so rank and security screens show their local/offline state.</sub>

</div>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""/></p>

<a id="features"></a>
<div dir="rtl">

## <img src="assets/emoji/zap.png" width="30" alt=""/> الميزات · Features

<table>
<tr>
<td width="33%" valign="top">
<img src="assets/emoji/brain.png" width="52" alt=""/>
<h3>الأقسام الخمسة</h3>
<sub><b>Five home sections</b></sub><br/>
عقل الوكيل، والأتمتة، والعيلة، وصحة الموبايل، والخصوصية. كل ميزة جديدة لازم تدخل تحت واحد منهم.<br/>
<sub>Agent brain · Automations · Family · Phone health · Privacy</sub>
</td>
<td width="33%" valign="top">
<img src="assets/emoji/robot.png" width="52" alt=""/>
<h3>جيش الوكلاء · 12 كتيبة</h3>
<sub><b>The 6.0 agent army</b></sub><br/>
قائد عام، و12 كتيبة (المال، والسفر، والدراسة، والصحة، والشغل…)، ووكلاء أحرار بيتولدوا عند الطلب، ومهام لحد 30 يوم.<br/>
<sub>Commander, 12 battalions, free agents, a Reviewer and an Accountant</sub>
</td>
<td width="33%" valign="top">
<img src="assets/emoji/scroll.png" width="52" alt=""/>
<h3>دستور الوكلاء</h3>
<sub><b>The constitution</b></sub><br/>
10 مواد بتتفحص في الكود قبل كل فعل: الإنسان صاحب القرار، ومفيش تخفّي، ومفيش فعل غير قانوني.<br/>
<sub>10 articles enforced in code before every action</sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="assets/emoji/scales.png" width="52" alt=""/>
<h3>4 مستويات موافقة</h3>
<sub><b>4 approval levels</b></sub><br/>
🟢 حر · 🟡 بإذن عام · 🟠 بموافقة كل مرة · 🔴 بموافقة مشددة (بصمة + 10 ثواني للتراجع + سقف مبلغ).<br/>
<sub>Free · standing grant · per-action · strict (biometric + undo window)</sub>
</td>
<td width="33%" valign="top">
<img src="assets/emoji/gem.png" width="52" alt=""/>
<h3>8 عضويات</h3>
<sub><b>8 membership tiers</b></sub><br/>
مجاني، وبلَس، وبرو، وعائلي، وأعمال، والأسود، والماسي «الأوائل»، والسيادي. <b>الأسعار مقترحة</b> والدفع مقفول.<br/>
<sub>Free → Sovereign. Prices are <b>proposed</b>; payments are off</sub>
</td>
<td width="33%" valign="top">
<img src="assets/emoji/crown.png" width="52" alt=""/>
<h3>المالك + 5 رتب</h3>
<sub><b>Owner + 5 admin ranks</b></sub><br/>
نائب المالك، ومدير العمليات، ومشرف العضويات، ومراجع السوق، والمحلل. قاعدة الشخصين وسجل تدقيق محدش يمسحه.<br/>
<sub>Two-person rule, passkey, append-only audit log</sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="assets/emoji/shield.png" width="52" alt=""/>
<h3>مركز الأمن الذكي</h3>
<sub><b>AI security center</b></sub><br/>
الحارس، وصائد الاحتيال، والفريق الأحمر، والمصلّح، وقائد الطوارئ، والمدقق. ميشوفوش محتوى أي مستخدم.<br/>
<sub>Six security agents that work on numbers and patterns only</sub>
</td>
<td width="33%" valign="top">
<img src="assets/emoji/handshake.png" width="52" alt=""/>
<h3>نظام العدل</h3>
<sub><b>The fairness system</b></sub><br/>
تذكير قبل التجديد بـ3 أيام، وإلغاء بضغطتين، واسترداد كامل 7 أيام، واعتراض يراجعه إنسان خلال 48 ساعة.<br/>
<sub>Clear prices, 2-tap cancel, human appeal within 48 h</sub>
</td>
<td width="33%" valign="top">
<img src="assets/emoji/family.png" width="52" alt=""/>
<h3>العيلة والحماية</h3>
<sub><b>Family & safety</b></sub><br/>
وضع الطفل، ووضع الجد والجدة، وكاشف أرقام النصب، وحلقة الأمان، والورثة الرقمي. كله بموافقة كل فرد.<br/>
<sub>Child mode, grandparent mode, scam shield, consent-based circle</sub>
</td>
</tr>
</table>

</div>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""/></p>

<a id="gallery"></a>
<div dir="rtl">

## <img src="assets/emoji/eye.png" width="30" alt=""/> المعرض · Gallery

<table>
<tr>
<td align="center" width="25%"><img src="assets/screens/hl_01_hub_5.0.jpg" width="200" alt="الرئيسية · سَنَد النخبة"/><br/><sub><b>الرئيسية · سَنَد النخبة</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/hl_05_agent_fleet.jpg" width="200" alt="أسطول الوكلاء"/><br/><sub><b>أسطول الوكلاء</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/hl_03_avatar.jpg" width="200" alt="أفاتار سَنَد"/><br/><sub><b>أفاتار سَنَد</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/hl_07_grandparent_mode.jpg" width="200" alt="وضع الجد والجدة"/><br/><sub><b>وضع الجد والجدة</b></sub></td>
</tr>
<tr>
<td align="center" width="25%"><img src="assets/screens/hl_09_keyboard.jpg" width="200" alt="كيبورد سَنَد"/><br/><sub><b>كيبورد سَنَد</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/hl_08_health_alerts.jpg" width="200" alt="الأدوية والدكاترة"/><br/><sub><b>الأدوية والدكاترة</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/hl_06_family_map.jpg" width="200" alt="خريطة العيلة"/><br/><sub><b>خريطة العيلة</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/hl_02_hub_5.0_experience_business.jpg" width="200" alt="التجربة والأعمال"/><br/><sub><b>التجربة والأعمال</b></sub></td>
</tr>
<tr>
<td align="center" width="25%"><img src="assets/screens/hl_11_plans.jpg" width="200" alt="العضويات (مقترحة)"/><br/><sub><b>العضويات (مقترحة)</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/hl_04_black_tier_paywall.jpg" width="200" alt="سَنَد الأسود"/><br/><sub><b>سَنَد الأسود</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/hl_10_admin_dashboard.jpg" width="200" alt="لوحة الأدمن"/><br/><sub><b>لوحة الأدمن</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/hl_12_admin_plans.jpg" width="200" alt="العضويات في الأدمن"/><br/><sub><b>العضويات في الأدمن</b></sub></td>
</tr>
</table>

<br/>

**جديد في 6.0 «الأفق»** · <sub>New 6.0 screens (tap to expand)</sub>

<details>
<summary><b>🎖️ الجيش والدستور · Agent army (6.0-A)</b> · 5 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/166_v6_hub.jpg" width="150" alt="جيش سَنَد «الأفق»"/><br/><sub><b>جيش سَنَد «الأفق»</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/167_v6_room.jpg" width="150" alt="غرفة العمليات"/><br/><sub><b>غرفة العمليات</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/169_v6_battalions.jpg" width="150" alt="الكتايب الـ12"/><br/><sub><b>الكتايب الـ12</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/170_v6_free.jpg" width="150" alt="الوكلاء الأحرار"/><br/><sub><b>الوكلاء الأحرار</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/178_v6_constitution.jpg" width="150" alt="دستور الوكلاء"/><br/><sub><b>دستور الوكلاء</b></sub></td>
</tr>
</table>

</details>
<details>
<summary><b>💎 العضويات والعدل · Memberships (6.0-B)</b> · 5 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/181_v6b_plans.jpg" width="150" alt="العضويات الـ8"/><br/><sub><b>العضويات الـ8</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/182_v6b_compare.jpg" width="150" alt="مقارنة العضويات"/><br/><sub><b>مقارنة العضويات</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/184_v6b_fair.jpg" width="150" alt="نظام العدل"/><br/><sub><b>نظام العدل</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/190_v6b_diamond.jpg" width="150" alt="سَنَد الماسي «الأوائل»"/><br/><sub><b>سَنَد الماسي «الأوائل»</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/192_v6b_security.jpg" width="150" alt="أمان العضوية"/><br/><sub><b>أمان العضوية</b></sub></td>
</tr>
</table>

</details>
<details>
<summary><b>🌅 الأفق: الميزات العبقرية · Horizon features (6.0-C)</b> · 4 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/194_v6c_twin.jpg" width="150" alt="التوأم الرقمي 2.0"/><br/><sub><b>التوأم الرقمي 2.0</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/198_v6c_bills.jpg" width="150" alt="حارس الاشتراكات والفواتير"/><br/><sub><b>حارس الاشتراكات والفواتير</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/204_v6c_heir.jpg" width="150" alt="افتح أمانة"/><br/><sub><b>افتح أمانة</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/206_v6c_employee.jpg" width="150" alt="وكيل الموظف"/><br/><sub><b>وكيل الموظف</b></sub></td>
</tr>
</table>

</details>
<details>
<summary><b>🧩 السوق والمطوّرين · Market & developers (6.0-D)</b> · 4 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/210_v6d_market.jpg" width="150" alt="سوق الوكلاء 2.0"/><br/><sub><b>سوق الوكلاء 2.0</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/211_v6d_agent.jpg" width="150" alt="مساعد الوصفات (مثال SDK)"/><br/><sub><b>مساعد الوصفات (مثال SDK)</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/213_v6d_sdk.jpg" width="150" alt="SDK للوكلاء"/><br/><sub><b>SDK للوكلاء</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/225_admin_dev_market.jpg" width="150" alt="أدمن · مراجعة السوق"/><br/><sub><b>أدمن · مراجعة السوق</b></sub></td>
</tr>
</table>

</details>
<details>
<summary><b>⚖️ القانوني والخصوصية · Legal (6.0-D/E)</b> · 4 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/215_v6d_legal.jpg" width="150" alt="المستندات القانونية"/><br/><sub><b>المستندات القانونية</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/216_v6d_doc.jpg" width="150" alt="شروط الاستخدام"/><br/><sub><b>شروط الاستخدام</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/220_v6d_dpo.jpg" width="150" alt="مسؤول حماية البيانات"/><br/><sub><b>مسؤول حماية البيانات</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/222_v6e_actions.jpg" width="150" alt="أفعال الإدارة على حسابك"/><br/><sub><b>أفعال الإدارة على حسابك</b></sub></td>
</tr>
</table>

</details>
<details>
<summary><b>👑 المالك والرتب · Owner & ranks (6.0-E)</b> · 5 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/234_admin_rk_ranks.jpg" width="150" alt="الرتب والأدمنز"/><br/><sub><b>الرتب والأدمنز</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/235_admin_rk_invite.jpg" width="150" alt="دعوات الأدمن"/><br/><sub><b>دعوات الأدمن</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/238_admin_rk_sessions.jpg" width="150" alt="الجلسات والأجهزة"/><br/><sub><b>الجلسات والأجهزة</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/239_admin_rk_dash.jpg" width="150" alt="لوحة المالك"/><br/><sub><b>لوحة المالك</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/242_admin_rk_matrix.jpg" width="150" alt="مصفوفة الصلاحيات"/><br/><sub><b>مصفوفة الصلاحيات</b></sub></td>
</tr>
</table>

</details>
<details>
<summary><b>🛡️ مركز الأمن الذكي · Security center (6.0-F)</b> · 5 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/243_admin_soc.jpg" width="150" alt="مركز الأمن الذكي"/><br/><sub><b>مركز الأمن الذكي</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/244_admin_soc_alerts.jpg" width="150" alt="التنبيهات"/><br/><sub><b>التنبيهات</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/245_admin_soc_actions.jpg" width="150" alt="الأفعال المؤقتة"/><br/><sub><b>الأفعال المؤقتة</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/247_admin_soc_redteam.jpg" width="150" alt="الفريق الأحمر"/><br/><sub><b>الفريق الأحمر</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/249_admin_soc_grants.jpg" width="150" alt="المنح والإعدادات"/><br/><sub><b>المنح والإعدادات</b></sub></td>
</tr>
</table>

</details>

<br/>

**لقطات أكتر حسب القسم** · <sub>More screens by section (tap to expand)</sub>

<details>
<summary><b>🧠 عقل الوكيل والذكاء · Agent brain & AI</b> · 8 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="25%"><img src="assets/screens/003_agent.jpg" width="150" alt="عقل الوكيل"/><br/><sub><b>عقل الوكيل</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/007_memory.jpg" width="150" alt="ذاكرة سَنَد"/><br/><sub><b>ذاكرة سَنَد</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/009_skills.jpg" width="150" alt="مكتبة المهارات"/><br/><sub><b>مكتبة المهارات</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/027_v3_studio.jpg" width="150" alt="استوديو المهارات"/><br/><sub><b>استوديو المهارات</b></sub></td>
</tr>
<tr>
<td align="center" width="25%"><img src="assets/screens/028_v3_ask.jpg" width="150" alt="اسأل الشاشة"/><br/><sub><b>اسأل الشاشة</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/029_v3_translate.jpg" width="150" alt="ترجمة حية"/><br/><sub><b>ترجمة حية</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/045_a_specialists.jpg" width="150" alt="الوكلاء المتخصصين"/><br/><sub><b>الوكلاء المتخصصين</b></sub></td>
<td align="center" width="25%"><img src="assets/screens/046_a_fleet.jpg" width="150" alt="المدير والفريق"/><br/><sub><b>المدير والفريق</b></sub></td>
</tr>
</table>

</details>
<details>
<summary><b>⚙️ الأتمتة · Automations</b> · 6 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/015_auto.jpg" width="150" alt="الأتمتة"/><br/><sub><b>الأتمتة</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/057_b_modes.jpg" width="150" alt="أوضاع الحياة"/><br/><sub><b>أوضاع الحياة</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/058_b_places.jpg" width="150" alt="أماكني وقواعدها"/><br/><sub><b>أماكني وقواعدها</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/059_b_queue.jpg" width="150" alt="طابور الموافقات"/><br/><sub><b>طابور الموافقات</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/060_b_home.jpg" width="150" alt="البيت الذكي"/><br/><sub><b>البيت الذكي</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/062_b_recur.jpg" width="150" alt="التكرار بالمصري"/><br/><sub><b>التكرار بالمصري</b></sub></td>
</tr>
</table>

</details>
<details>
<summary><b>👨‍👩‍👧 العيلة والحماية · Family & safety</b> · 6 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/016_family.jpg" width="150" alt="وضع الطفل"/><br/><sub><b>وضع الطفل</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/056_b_kids.jpg" width="150" alt="الأمان والمذاكرة"/><br/><sub><b>الأمان والمذاكرة</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/086_b2_elder.jpg" width="150" alt="وضع الجد والجدة"/><br/><sub><b>وضع الجد والجدة</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/066_b_scam.jpg" width="150" alt="كاشف أرقام النصب"/><br/><sub><b>كاشف أرقام النصب</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/070_b_med.jpg" width="150" alt="بطاقتي الطبية"/><br/><sub><b>بطاقتي الطبية</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/071_b_shield.jpg" width="150" alt="درع النصب لكبار السن"/><br/><sub><b>درع النصب لكبار السن</b></sub></td>
</tr>
</table>

</details>
<details>
<summary><b>✨ التجربة والأعمال · Experience & business</b> · 6 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/091_c_avatar.jpg" width="150" alt="أفاتار سَنَد"/><br/><sub><b>أفاتار سَنَد</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/098_c_themes.jpg" width="150" alt="الثيمات الزجاجية"/><br/><sub><b>الثيمات الزجاجية</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/100_c_keyboard.jpg" width="150" alt="كيبورد سَنَد"/><br/><sub><b>كيبورد سَنَد</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/102_c_biz.jpg" width="150" alt="سَنَد للأعمال"/><br/><sub><b>سَنَد للأعمال</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/105_c_invoice.jpg" width="150" alt="فواتير بالكاميرا"/><br/><sub><b>فواتير بالكاميرا</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/110_c_compliance.jpg" width="150" alt="تقرير الامتثال"/><br/><sub><b>تقرير الامتثال</b></sub></td>
</tr>
</table>

</details>
<details>
<summary><b>🔒 الخصوصية والأمان · Privacy & safety</b> · 6 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/018_privacy.jpg" width="150" alt="مركز الخصوصية"/><br/><sub><b>مركز الخصوصية</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/025_privacy_log.jpg" width="150" alt="سجل نشاط الوكيل"/><br/><sub><b>سجل نشاط الوكيل</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/026_privacy_perms.jpg" width="150" alt="صلاحيات الوكيل"/><br/><sub><b>صلاحيات الوكيل</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/023_policy.jpg" width="150" alt="قواعد الأمان"/><br/><sub><b>قواعد الأمان</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/113_c_privacy.jpg" width="150" alt="خصوصية مطلقة"/><br/><sub><b>خصوصية مطلقة</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/114_c_undo.jpg" width="150" alt="تراجع 10 ثواني"/><br/><sub><b>تراجع 10 ثواني</b></sub></td>
</tr>
</table>

</details>
<details>
<summary><b>💎 العضويات وتطبيق الأدمن · Memberships & admin app</b> · 9 لقطات</summary>
<br/>

<table>
<tr>
<td align="center" width="33%"><img src="assets/screens/119_plans_plus.jpg" width="150" alt="العضويات · Plus"/><br/><sub><b>العضويات · Plus</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/127_plans_black.jpg" width="150" alt="العضويات · سَنَد الأسود"/><br/><sub><b>العضويات · سَنَد الأسود</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/128_themes_black.jpg" width="150" alt="الثيمات الزجاجية · سَنَد الأسود"/><br/><sub><b>الثيمات الزجاجية · سَنَد الأسود</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/129_admin_home.jpg" width="150" alt="أدمن · الرئيسية"/><br/><sub><b>أدمن · الرئيسية</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/133_admin_health.jpg" width="150" alt="أدمن · صحة السيرفر"/><br/><sub><b>أدمن · صحة السيرفر</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/136_admin_switches.jpg" width="150" alt="أدمن · المفاتيح"/><br/><sub><b>أدمن · المفاتيح</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><img src="assets/screens/155_admin_transparency.jpg" width="150" alt="أدمن · الشفافية"/><br/><sub><b>أدمن · الشفافية</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/159_admin_agents.jpg" width="150" alt="أدمن · الوكلاء السحابيين"/><br/><sub><b>أدمن · الوكلاء السحابيين</b></sub></td>
<td align="center" width="33%"><img src="assets/screens/164_admin_cannot.jpg" width="150" alt="أدمن · اللي الأدمن مايقدرش يعمله"/><br/><sub><b>أدمن · اللي الأدمن مايقدرش يعمله</b></sub></td>
</tr>
</table>

</details>

</div>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""/></p>

<a id="architecture"></a>

## <img src="assets/emoji/satellite.png" width="30" alt=""/> المعمار · Architecture

```mermaid
flowchart LR
  subgraph PHONE["📱 موبايل المستخدم · User phone"]
    APP["سَنَد App<br/>Accessibility agent + UI"]
    BRAIN["Brain · on-device first<br/>user's own AI key"]
    VAULT[("Keystore AES-GCM<br/>encrypted local stores")]
    APP --> BRAIN
    APP --> VAULT
  end
  subgraph OWNER["👑 موبايل المالك · Owner device"]
    ADMIN["Sanad Admin app<br/>owner + 5 ranks · passkey"]
  end
  subgraph CF["☁️ Cloudflare · free tier"]
    WORKER["Worker API<br/>entitlements · army · devapi · safety"]
    DO[("SQLite Durable Object")]
    WORKER --> DO
  end
  EXT["🧩 Chrome extension<br/>signed pairing"]
  APP -- "Ed25519 tickets · 24h" --> WORKER
  ADMIN -- "signed config · aggregates only" --> WORKER
  EXT -- "handoff" --> APP
  WORKER -. "no user content, ever" .-> ADMIN
```

### <img src="assets/emoji/robot.png" width="24" alt=""/> جيش الوكلاء · Agent-army flow

```mermaid
flowchart TD
  U(["🙋 المستخدم · You<br/>«عايز أسافر الإسكندرية الأسبوع الجاي»"]) --> C["🎖️ القائد العام · Commander<br/>understands the goal, splits it into tasks"]
  C --> B1["💰 المال"] & B2["✈️ السفر"] & B3["🛒 التسوق"] & B4["📚 الدراسة"] & B5["…  12 battalions"]
  C -. "مهمة مش مغطّاة" .-> F["🧪 وكيل حر · Free agent<br/>born from a description, sandboxed first"]
  B1 & B2 & B3 & B4 & B5 & F --> R["🔍 المراجع · Reviewer<br/>hunts for mistakes"]
  R --> A["🧮 المحاسب · Accountant<br/>per-task + daily budget caps"]
  A --> K{"📜 الدستور + مستوى الموافقة<br/>Constitution + approval level"}
  K -- "🟢 حر" --> DONE["✅ ينفّذ ويبلّغك"]
  K -- "🟡 بإذن عام" --> G["إذن واحد لنوع معيّن · revocable"]
  K -- "🟠 كل مرة" --> P["موافقة على النص والمستلم بالظبط"]
  K -- "🔴 مشددة" --> S["بصمة + تأكيد + 10 ثواني للتراجع + سقف مبلغ"]
  G & P & S --> U2(["🙋 القرار الأخير ليك · You decide"])
  U2 --> DONE
```

<a id="roadmap"></a>

### <img src="assets/emoji/target.png" width="24" alt=""/> موجات 6.0 «الأفق» · Waves A–G

```mermaid
flowchart LR
  A["✅ A<br/>Army + constitution<br/>5.1.0"]:::done --> B["✅ B<br/>Memberships engine<br/>+ fairness · 5.2.0"]:::done --> C["✅ C<br/>13 genius features<br/>5.3.0"]:::done --> D["✅ D<br/>Developers · self-dev<br/>legal · 5.4.0"]:::done --> E["✅ E<br/>Owner app<br/>+ 5 ranks · 5.5.0"]:::done --> F["✅ F<br/>AI security center<br/>red team 189 · 5.6.0"]:::done --> G["✅ G<br/>Full QA + emulator<br/>shots · 6.0.0"]:::done
  classDef done fill:#10b981,stroke:#065f46,color:#fff
  classDef wip fill:#f5a524,stroke:#92400e,color:#1a1446
  classDef todo fill:#334155,stroke:#64748b,color:#e2e8f0
```

<p align="center"><img src="assets/divider.svg" width="100%" alt=""/></p>

<a id="promises"></a>
<div dir="rtl">

## <img src="assets/emoji/lock.png" width="30" alt=""/> وعود الأمان والخصوصية · Safety &amp; privacy promises

<table>
<tr>
<td width="50%" valign="top">

<img src="assets/emoji/shield.png" width="36" alt=""/> **الأمان مجاني ومش بيتقفل** في أي عضوية.<br/><sub>Safety and accessibility are free in every tier, forever.</sub>

<img src="assets/emoji/eye.png" width="36" alt=""/> **محدش يشوف محتواك**، ولا المالك نفسه. الأدمن ووكلاء الأمن بيشوفوا أرقام مجمّعة بس.<br/><sub>No one reads your content, not even the owner.</sub>

<img src="assets/emoji/brain.png" width="36" alt=""/> **الذكاء على الجهاز أولًا**، وبمفتاحك إنت لو اخترت سحابة.<br/><sub>On-device AI first; cloud AI only with your own key.</sub>

<img src="assets/emoji/check.png" width="36" alt=""/> **مفيش إرسال أو دفع من غير موافقتك** على النص والمستلم والمبلغ بالظبط.<br/><sub>Nothing is sent or paid without your explicit approval.</sub>

</td>
<td width="50%" valign="top">

<img src="assets/emoji/undo.png" width="36" alt=""/> **التراجع أولًا**: أي فعل ليه إلغاء بيتعرض قبل التنفيذ، و10 ثواني تراجع في الحاجات الخطيرة.<br/><sub>Undo first, with a 10-second window on risky actions.</sub>

<img src="assets/emoji/child.png" width="36" alt=""/> **وضع الطفل ظاهر ومعلن**: مفيش تجسس، ومفيش إرسال أو شراء من الوكلاء.<br/><sub>Child mode is visible and consent-based, never spyware.</sub>

<img src="assets/emoji/trash.png" width="36" alt=""/> **صدّر بياناتك أو امسحها كلها** في ضغطة (قانون 151 لسنة 2020) · اتبنت في الموجة D.<br/><sub>One-tap export or erase (Egypt PDPL 151/2020), built in wave D.</sub>

<img src="assets/emoji/key.png" width="36" alt=""/> **مفيش مفاتيح ولا أسرار في الكود**: فحص مفاتيح على كل إصدار.<br/><sub>No keys in the binary; every release passes a key scan.</sub>

</td>
</tr>
</table>

</div>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""/></p>

<div dir="rtl">

## <img src="assets/emoji/medal.png" width="30" alt=""/> رحلة الإصدارات · Changelog

| الإصدار | الاسم | أبرز ما فيه | الحالة |
|:--:|:--|:--|:--:|
| **1.0** | الأساس | الوكيل بالمصري، ووضع الطفل، والأقسام الخمسة، وتطبيق الأدمن، وسيرفر Cloudflare، و160 ميزة | ✅ |
| **2.0** | العقل القابل للاختبار | عقل وكيل نقي بيتختبر من غير موبايل، وأمان في مكان واحد | ✅ |
| **3.0** | استوديو المهارات | مهارة من وصف بالكلام، و«اسأل الشاشة»، وترجمة حية، وذاكرة الموبايل | ✅ |
| **4.0** | الفريق والعضويات | خطة: فريق وكلاء، و«نسختك»، وطابور الموافقات، ومتجر مهارات موقّع، والبيت الذكي | ↪️ اندمجت في 5.0 |
| **5.0.0** | «النخبة» | ذكاء خارق، وأسطول وكلاء، وأتمتة، وحماية العيلة، وتجربة مهيبة، و165/165 شاشة على المحاكي، و4,426 اختبار JDK | ✅ |
| **6.0.0** | «الأفق» | جيش الوكلاء بالـ12 كتيبة، والدستور، و4 مستويات موافقة، و8 عضويات، ونظام العدل، وسوق المطوّرين، والمالك + 5 رتب، ومركز الأمن الذكي · 7 موجات (A–G) · JDK 9,799 / 0 · سيرفر 1,235 / 0 · فريق أحمر 189 / 189 · 249/249 شاشة على المحاكي | ✅ مستقر (2026-10-15) |
| **7.0** | الجاي | نشر السيرفر، ومراجعة المحامي للمستندات، وتعيين مسؤول حماية البيانات، وتشغيل الدفع بعد موافقة المالك | 🗺️ خطة |

</div>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""/></p>

<a id="en"></a>

## <img src="assets/emoji/sparkles.png" width="30" alt=""/> English

**Sanad (سَنَد, "support")** is an Android AI agent that understands Egyptian Arabic and works the phone for you. It reads the screen, carries out tasks step by step, remembers what matters to you, and protects your family. Everything runs inside clear safety rules.

**6.0.0 «الأفق» (Horizon)**, released 2026-10-15 in 7 waves (A–G), adds a free agent army that can work for you over days and weeks:

- 🎖️ **Commander + 12 battalions**: money, travel, shopping, study, health, work, home, family, legal & paperwork, content & design, coding, research. Free agents are created on demand and sandboxed first.
- 📜 **Constitution**: 10 articles checked in code before every action. Humans decide. No impersonation, nothing illegal, and budget caps can't be broken.
- 🚦 **4 approval levels**: 🟢 free · 🟡 standing grant · 🟠 per action · 🔴 strict (biometric, 10-second undo, amount cap).
- 💎 **8 membership tiers**, from Free to Sovereign. All prices are **proposed**, and payments stay **off** until the owner approves a licensed gateway.
- 👑 **Owner app + 5 admin ranks** with a two-person rule, passkeys, and an append-only audit log.
- 🛡️ **AI security center**: Guardian, Fraud Hunter, Red Team, Fixer, Incident Lead, Auditor. They see patterns, never content.
- ⚖️ **Fairness system**: a reminder 3 days before renewal, 2-tap cancel, a full refund within 7 days, and human review of any suspension within 48 h.
- 🧩 **Developer market 2.0 + SDK**, self-development, and 7 Egyptian legal documents (drafts pending a lawyer's review).

| | |
|:--|:--|
| **Platform** | Android 7.0+ (API 24), target 34 / Play build 36, separate admin app |
| **Backend** | One Cloudflare Worker + one SQLite Durable Object (free tier) |
| **AI** | On-device first; cloud models only with the user's own key, via a cost-aware router |
| **Quality** | 6.0.0: **9,799 / 0** JDK · **1,235 / 0** server · red team **189 / 189** · emulator **249 / 249** screens, 0 crashes |
| **This repo** | CI: APK builds, tests, and Android emulator screenshots |

<details>
<summary><b>Credits</b></summary>

- 3D emoji: [Microsoft Fluent Emoji](https://github.com/microsoft/fluentui-emoji) (MIT).
- Wordmark: Tajawal (SIL Open Font License 1.1), outlined to SVG paths so no web fonts load.
- Hero, typing, divider and footer art: hand-written animated SVG in this repo (`assets/`).
- Badges: [shields.io](https://shields.io).

</details>

<p align="center"><img src="assets/footer-wave.svg" width="100%" alt="سَنَد · صُنع في مصر بعناية"/></p>
