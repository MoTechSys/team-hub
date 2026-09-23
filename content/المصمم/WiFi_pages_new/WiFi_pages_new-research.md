WiFi_pages_new | المصمم | 2026-09-23 | draft

# بوابة هوت سبوت Glassmorphism (WiFi_pages_new) — بحث وتحليل

## English summary
WiFi_pages_new is a CSS-layer redesign of MikroTik RouterOS hotspot templates (8 HTML files, 27 `$(…)` variables preserved, 0 external libraries, 19.9 KB CSS). The buyer is a small wireless ISP / rest-house / café selling hotspot cards on MikroTik. The alternatives market is a long tail of free templates (GitHub repos on Bootstrap 4, blog/YouTube template drops, forum threads since 2014) plus SaaS voucher managers (MKController) that ship their own portal. Our measured edge: no framework (Bootstrap-based templates ship jQuery + Bootstrap), modern glass aesthetic with 9 CSS animations, a documented data-integrity contract (variables, field names, CHAP untouched) and an `original/` rollback. Gaps: a real CSS bug hides the three status-page buttons' text, provider phone/prices/LAN links are hard-coded, no tests or router verification, 2 commits, no font for Arabic beyond system fonts, and README still lists a deleted index.html.

## 1. من يشتري هذا وحجم الفئة
- **المشتري:** مزوّدو إنترنت لاسلكي صغار ومشغّلو هوت سبوت في استراحات ومقاهٍ وأحياء يبيعون «كروت» وقت/بيانات على MikroTik (سياق الصفحات: كرت، سرعة، رصيد، استراحة، بث مباشر).
- **حاجة القرار:** أول ما يراه المستخدم على هاتفه هو صفحة الدخول؛ الافتراضية رمادية وغير متجاوبة، والمشغّل يخشى كسر منطق الدخول عند التعديل.
- **حجم الفئة:** لا أملك رقماً موثّقاً لعدد هوت سبوتات MikroTik في السوق المستهدف — **يُستكمل**؛ لا يُعرض رقم بلا مصدر.
- **إشارة مقاسة:** المجتمع الرسمي لـ MikroTik يتداول قوالب دخول مجانية منذ 2014 (خيط «New (and free) Hotspot Login Templates»)، وصفحة قوالب مجانية واحدة تعرض 5+ قوالب موضوعية (Terminal، Office، PUBG…) — الطلب حقيقي وطويل الذيل.

## 2. المنافسون / البدائل (فُحصت 2026-09-23 ~06:09 UTC)
| # | البديل | الرابط | ما يقوله | ما قِسته / لاحظته |
|---|---|---|---|---|
| 1 | Responsive-Mikrotik-Template (teguhrianto) | https://github.com/teguhrianto/Responsive-Mikrotik-Template | «Responsive Mikrotik Template Base on Bootstrap 4» | 41★؛ يعتمد Bootstrap 4 (+jQuery ضمنياً) = مكتبات خارجية تُرفع للراوتر |
| 2 | Free Hotspot Template for Mikrotik (Ilhamuddin Sirait) | https://ilhamuddinsirait.github.io/ | قوالب مجانية موضوعية: Terminal Style، Office، PUBG Mobile، Berkah Full Color… | صفحة تحميل مرتبطة بقناة يوتيوب؛ 5+ قوالب؛ لا توثيق تقني لسلامة المتغيرات |
| 3 | MKController | https://mkcontroller.com/give-your-mikrotik-hotspot-login-page-a-boost-a-practical-guide-to-impressing-your-users/ | «customize your Mikrotik Hotspot Voucher login page using the MKController app» | SaaS لإدارة القسائم يقدّم تخصيص الصفحة كميزة داخل التطبيق (اشتراك)؛ موقع WordPress |
| 4 | MikroTik community forum — free templates thread | https://forum.mikrotik.com/t/new-and-free-hotspot-login-templates/83952 | قوالب مجانية + تعليمات للمبتدئين (2014) | الروابط تقود إلى مدوّنة blogspot؛ عمر 12 سنة — يؤكد قِدم الفئة |

(المصدر: curl لكل صفحة + regex على العنوان/الوصف/النجوم؛ systemzone.net أعاد 406 فلم يُدرج.)

## 3. التموضع
**ما يقوله المنافسون:** «responsive»، «free»، «Bootstrap»، «theme»؛ أو تخصيص عبر تطبيق SaaS. لا أحد من المفحوصين يوثّق **عقد سلامة البيانات** (أي متغيرات وحقول ودوال يجب ألا تُمَس).

**أين يتفوّق مشروعنا (من tech.md فقط):**
- **صفر مكتبة خارجية** مقابل Bootstrap 4 + jQuery: أخف على ذاكرة الراوتر (الحمولة 133 KB منها 68 KB الشعار).
- **جمالية حديثة موثّقة:** Glassmorphism، `backdrop-filter` ×16، 9 حركات CSS، خلفية متدرجة متحركة، أيقونات SVG مضمّنة (6).
- **عقد سلامة صريح في README:** 27 متغير قالب، أسماء الحقول الستة، form action، CHAP-MD5، الكوكيز — كلها محفوظة؛ ونسخة `original/` للرجوع.
- **تجاوب حتى 380px** (7 media queries) + عربي RTL أصلي.

**أين يتفوّقون علينا (صراحة):** لديهم توزيع ومجتمع ونجوم وفيديوهات تعليمية؛ MKController يقدّم إدارة قسائم كاملة لا صفحة فقط. مشروعنا مخصّص لعميل واحد (اسم، هاتف، أسعار، روابط LAN مضمّنة) وليس قالباً عاماً قابلاً للتوزيع بعد.

## 4. الكلمات المفتاحية
**AR (10):** صفحة دخول هوت سبوت · قالب مايكروتك هوت سبوت · تصميم صفحة كروت الواي فاي · بوابة captive portal عربية · تصميم Glassmorphism · صفحة تسجيل دخول متجاوبة · قالب login مايكروتك بدون Bootstrap · تخصيص hotspot RouterOS · واجهة كروت إنترنت · صفحة حالة الرصيد هوت سبوت
**EN (10):** mikrotik hotspot login template · captive portal design · glassmorphism login page · mikrotik hotspot custom page · routeros hotspot html templates · responsive hotspot login no bootstrap · CHAP md5 hotspot login · wifi voucher login page design · pure css animated gradient login · mikrotik status page template

## 5. ثلاث زوايا محتوى
1. **«كيف تعيد تصميم بوابة MikroTik دون أن تلمس سطر JavaScript واحداً»** — عقد سلامة البيانات كقصة: ما الذي يجب ألا يُمَس ولماذا، وكيف تتحقق منه بـ grep.
2. **«Glassmorphism بلا مكتبات»** — 19.9 KB CSS تصنع خلفية متحركة وبطاقات زجاجية و9 حركات؛ مقارنة وزن مع قالب Bootstrap 4.
3. **«عطل وجدته وأنا أصوّر»** — قاعدة `h1:first-of-type` التي أخفت نص الأزرار: درس في نطاقات CSS العامة على قوالب متعددة الصفحات.

## 6. الفجوات (صريحة)
- **عطل CSS حقيقي:** `.wrap h1:first-of-type` (style.css:682) تجعل نص أزرار status.html الثلاثة شفافاً → أزرار بلا نص على الجهاز. إصلاحه سطر واحد (تقييد بـ `.brand-glow`).
- **بيانات العميل مضمّنة في القوالب:** اسم الشبكة، رقم الهاتف، جدول أسعار الكروت، روابط LAN وبث خارجي، UUID سرعة افتراضي — يمنع إعادة استخدامه كقالب عام.
- **لا اختبار على راوتر فعلي** موثّق؛ لا اختبارات آلية؛ 2 commits فقط.
- **خط النظام (Segoe UI/Tahoma)** للعربية — لا خط عربي مخصص؛ 21 إيموجي في الواجهة تختلف بين الأجهزة.
- README يذكر `index.html` رغم حذفه؛ ولا يذكر عطل الأزرار.
- الشعار 1.png أصله غير موثّق (68 KB — نصف الحمولة).
- `original/style.css` 4.7 KB مقابل 19.9 KB الجديد — الوزن ×4 مقبول لكن يُذكر.
- لا نسخة إنجليزية من الواجهة؛ لا وضع فاتح.

## المصادر
- المستودع: https://github.com/moain2028/WiFi_pages_new (README، CLEANUP_LOG، style/style.css، *.html، original/) — الأرقام في tech.md بأوامرها.
- البدائل: الروابط الأربعة أعلاه — curl 2026-09-23 ~06:09 UTC.
- بحث ويب: «mikrotik hotspot login page template modern responsive» 2026-09-23.
