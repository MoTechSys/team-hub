motech-attendance | صانع العروض | 2026-09-23 | project-pack-v2

# مصادر كل نص ورقم وصورة — motech-attendance project-pack-v2

المصدر الحي: https://github.com/moain2028/portfolio-hub → 01-projects/motech-attendance/ (brief.ar.md · brief.en.md · tech.md · tech-planner.md · links.md · screenshots/ · video/reel-script.en.md) · الهوية 02-brand/README.md · المعيار project-pack-standard-v2.md.
المستودع الأصلي moain2026/motech-attendance خاص 🔒 → لا رابط كود على أي تصميم. لا اسم عميل. اسم المورّد (ZKTeco) محجوب من العناوين كما فعل المحرر في reel-script.

## A. التصاميم (24 PNG) + B. النشر (14 PNG)
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| العنوان H1 | بديل مركزي لبرنامج البصمة المكتبي | Replace the desktop attendance tool with a central web system | brief.ar/en — H1 |
| السطر فوق العنوان | Motech Attendance — نظام حضور وانصراف مؤسسي | Motech Attendance | brief H1 + tech.md عنوان |
| اسم المستودع (Mono/Amber) | motech-attendance | motech-attendance | اسم مجلد المشروع في portfolio-hub |
| السطر التعريفي | بصمات كل الفروع في نظام ويب واحد | Every branch's fingerprints in one system | video/reel-script.en.md عنوان (مختوم) — ترجمة مباشرة |
| الوصف | جامع خفيف يسحب من أجهزة البصمة كل 10 دقائق موقّعاً بـ HMAC، ولوحة عربية RTL للتقارير اليومية والشهرية والورديات والإجازات وتصدير CSV/Excel | A thin collector pulls from fingerprint devices every 10 minutes, HMAC-signed; an RTL dashboard covers daily & monthly reports, shifts, leave and CSV/Excel export | brief «الحل» / «Solution» |
| تاجات | Go · PostgreSQL · Python · pyzk · HMAC · bcrypt · systemd | نفسها | brief «الحل» + tech.md «التقنيات» |
| 3,118 | بصمة من جهاز حقيقي | punches from a live device | brief «النتيجة» · tech.md «الأرقام» ← README |
| 2,277 | صفاً يومياً كتبها المحرك | daily rows by the engine | brief «النتيجة» · tech.md ← README سطر 97 |
| 11 | موظفاً في الاختبار الحي | employees in the live test | brief «النتيجة» · tech.md ← README |
| 19 | ملف اختبار Go | Go test files | tech.md «الأرقام» ← git ls-tree (يوافق tech-planner: 19 ملفاً) |
| السطر السفلي | دراسة حالة · نظام داخلي — مُختبَر على جهاز بصمة حقيقي | Case study · internal system — tested on a live fingerprint device | brief «النتيجة» + links.md (Live: يُستكمل) |
| CTA | أُقدّم دراسة لنظام الحضور لديك — راسلني | Let's scope your attendance setup — DM or email | brief «تواصل» / «Contact» |
| شارة الشريحة | شركات | Companies | tech.md «الشريحة: شركات» · لون #3B82F6 |
| wordmark (نسخة logo) | معين العباسي | Moain Al-Abbasi | project-pack-standard-v2 §A |
| كاروسيل 1 المشكلة | أجهزة البصمة في الفروع تصبّ في برنامج سطح مكتب واحد… | Branch fingerprint devices feed one desktop program… | brief «المشكلة» / «Problem» |
| كاروسيل 2 الحل | خادم Go مركزي + جامع خفيف بـ Python… كل 10 دقائق عبر systemd | A central Go backend + a thin Python collector… | brief «الحل» |
| كاروسيل 3 كيف يعمل | محرك يومي يحسب التأخير والإضافي والناقص حسب الوردية… | A shift-aware daily engine computes late, overtime and short hours… | brief «الحل» + tech.md «الحل» (محرك معالجة يومي تأخير/إضافي/ناقص) |
| كاروسيل 4 الأرقام | 3,118 · 2,277 · 11 · 19 + «المصدر: README المستودع — iFace950، محرك يومي idempotent» | same | tech.md «الأرقام» |
| كاروسيل 5 الدعوة | للشركات متعددة الفروع التي تعتمد أجهزة بصمة… | For multi-branch companies with biometric attendance devices… | brief «لمن يفيد» + «تواصل» |
| بطاقة «رقم واحد» | 3,118 بصمة سُحبت من جهاز بصمة حقيقي · 11 موظفاً · المحرك كتب 2,277 صفاً يومياً · إعادة التشغيل لا تكرّر صفاً | 3,118 punches pulled from a live fingerprint device · 11 employees · the engine wrote 2,277 daily rows · idempotent on every rerun | brief «النتيجة» |
| بانر المقال 1600×840 | العنوان + السطر التعريفي + التاجات | same | كما أعلاه |

## اللقطات (كلها حقيقية من screenshots/ — لا لقطة مولّدة)
- البطلة في A والبانر: `desktop-02-daily.png` (2880×1800) + `mobile-02-daily.png` (780×1688)؛ Story تضيف `mobile-03-monthly.png`.
- كاروسيل: `desktop-01-home.png` (1) · `mobile-02-daily.png` (2) · `desktop-03-monthly.png` (3) · `desktop-07-shifts.png` (5).
- الريل: `desktop-01-home.png` · `mobile-02-daily.png` · `desktop-02-daily.png` · `desktop-07-shifts.png`.
- بيانات اللقطات: seed محلي التقطه مخطط التسويق 2026-09-11 (12 موظفاً بأسماء عربية تجريبية، 494 بصمة/30 يوماً) — tech-planner.md «التشغيل والتصوير». الأسماء الظاهرة تجريبية لا حقيقية (مُعلَن هنا بحسب معيار v2).

## C. الريل
- `motech-attendance-reel-1080x1920-{ar,en}-nologo.mp4`: 21 ث · 1080×1920 · 30fps · H.264/AAC · 6 مشاهد × 4 ث بتلاشٍ 0.6 ث وزوم بطيء · بلا شعار · لا مشاهد خطأ. نصوص المشاهد في copy.{ar,en}.md «نص الريل» ومصدرها brief + tech.md «الأرقام». غلافان `reel-cover-1080x1920-{ar,en}-nologo.png` = المشهد 1.
- الموسيقى: `reel/music.mp3` مولَّدة بالذكاء الاصطناعي (CassetteAI عبر أدوات Genspark، 30 ث، instrumental) — بلا حقوق طرف ثالث.
- ملاحظة: في المستودع ريل سابق `video/motech-attendance-reel-en.mp4` بشعار M ورابط GitHub — لم يُستخدم لأنه يخالف قاعدة «بلا شعار / بلا رابط كود».

## D. الشروحات
- `motech-attendance-explainer.{ar,en}.md`: كل جملة مذيَّلة بمصدرها داخل الملف (brief · tech.md · tech-planner.md · links.md). ~430/420 كلمة + خلاصة 5 نقاط.

## E. البحث
- `motech-attendance-research.md`: 5 روابط خارجية بتاريخ وصول 2026-09-23 (ZKTeco Time.Net · ZKTeco BioTime Cloud · Bayzat · Jibble · Keka). التموضع من tech.md/tech-planner.md فقط. حجم الفئة: «يُستكمل».

## F. النصوص
- `motech-attendance-copy.{ar,en}.md`: LinkedIn ≤120 كلمة · X ≤280 حرف · IG ≤150 كلمة · نص الريل — كلها draft بانتظار ختم المحرر.

## الهوية والتباين
- 02-brand/README.md: Navy #0E2A47 · Ink #08172B · Amber #F4A62A · Sand #F7F5F0 · Mist #DCE3EA · شركات #3B82F6؛ النص الخافت #A3B1C0 (تحديث v2 بدل Slate). Plex Sans Arabic / Inter / JetBrains Mono، أرقام غربية.
- Sand على Navy ≈ 13:1 · Amber على Navy ≈ 7.5:1 · Sand على #3B82F6 ≈ 4.6:1 · #A3B1C0 على Navy ≈ 7:1 — كلها AA فأعلى.

## تناقضات لم تُعرض (قاعدة v2)
- عدد الهجرات: tech.md يقول 7، tech-planner.md يقول 10 → لم يُعرض.
- عدد الجداول (19) وأسطر Go (~7,500) من tech-planner فقط → لم يُعرض على التصاميم.
- الحالة: tech.md «لا نشاط منذ 2026-06-24» مقابل tech-planner «Phase 3–4 وESS مكتملة» → ذُكر الاثنان في الشرح وسُجّل كفجوة في البحث.

## إعادة التوليد
- `build.py all` → 24 تصميم · `build.py b` → 14 قطعة نشر · `build.py reel` ثم `make_reel.sh ar|en` → الريل. (Python 3 + Playwright/Chromium + ffmpeg)
