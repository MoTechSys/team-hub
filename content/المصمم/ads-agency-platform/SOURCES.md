ads-agency-platform | المصمم | 2026-09-23 | v2

# مصادر كل نص ورقم وصورة — ads-agency-platform project pack v2

المصدر الحي: https://github.com/moain2028/portfolio-hub → 01-projects/ads-agency-platform/ (brief.ar.md · brief.en.md · tech.md · links.md · screenshots/ · video/reel-script.en.md). المستودع الأصلي moain2026/ads-agency-platform خاص 🔒 → **لا رابط كود على أي تصميم**؛ التذييل «مستودع خاص — يُعرض كدراسة حالة» بدل رابط GitHub.

## A. التصاميم (24 PNG) — النصوص
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| العنوان | منصة الوكالة | Ads Agency Platform | brief.ar/en.md (العنوان) |
| السطر التعريفي | حملات Google Ads لعدة عملاء من لوحة واحدة | Many clients' Google Ads, one dashboard, human approval | brief.ar/en.md (العنوان) |
| الوصف | SaaS متعدد المستأجرين: لقطات مقاييس يومية، توصيات ذكية مسنودة بأرقام، وموافقة بشرية إلزامية قبل تنفيذ أي تغيير | Multi-tenant SaaS: daily metric snapshots, evidence-backed AI recommendations, human approval before any change runs | brief فقرة «الحل / Solution» |
| 12 | جدولاً في Prisma | Prisma tables | tech.md «الأرقام»: 12 جدولاً — schema.prisma + README |
| 17/17 | اختبار عزل | isolation tests | tech.md: عزل المستأجرين 17/17 — README (المرحلة 2) |
| 20/20 | اختبار تشفير | encryption tests | tech.md: تشفير 20/20 — README |
| التاجات | Next.js · TypeScript · Prisma 6 · PostgreSQL 16 · Google Ads API · BullMQ | — | tech.md «التقنيات» (Next.js بلا رقم إصدار لأن brief يقول 15 وtech.md يقول 16.3 — الأرقام المتضاربة لا تُعرض، حسب المعيار) |
| الشارة | شركات | Companies | تصنيف المهمة · 02-brand/README.md |
| نسخة logo | معين العباسي | Moain Al-Abbasi | project-pack-standard-v2 (wordmark نصّي فقط) |

## B. الكاروسيل (5+5) · بطاقة الرقم · بانر المقال
- شريحة 1 (المشكلة): brief فقرة «المشكلة». شريحة 2 (الحل): brief «الحل» + tech.md (Google Ads API، MetricSnapshot). شريحة 3 (كيف يعمل): tech.md — ChangeRequest PENDING→APPROVED→APPLIED، evidence JSON، AuditLog. شريحة 4 (الأرقام): tech.md — 12 جدولاً، 17/17، 20/20، 5 مزوّدي AI. شريحة 5 (الدعوة): brief «لمن يفيد» + «تواصل» + tech.md (AES-256-GCM، الأسرار خارج قاعدة البيانات).
- بطاقة الرقم 17/17: tech.md (عزل المستأجرين) + brief («عزل مستأجرين 17/17»).
- بانر المقال: عنوان تحريري مشتق من brief «القرار الأخير للإنسان / a human in the loop»؛ الوصف من brief «الحل».

## C. الريل (AR + EN، 28 ث، 1080×1920، 30fps، بلا شعار)
- النص على الشاشة: brief (المشكلة/الحل/لمن) + tech.md (الحالات الثلاث، الأرقام). بنية المشاهد بتصرّف من video/reel-script.en.md (كاتب المحتوى، مختوم).
- اللقطات: screenshots/mobile-03-dashboard-full.png (تمرير داخل إطار جوال) · desktop-03-dashboard.png (تحريك أفقي داخل إطار متصفح). لا مشهد خطأ/404.
- الموسيقى: مولّدة بلا حقوق عبر CassetteAI/music-generator (instrumental، 30 ث)، بلا تعليق صوتي.
- الغلاف: إطار من مشهد 2 (APPROVE).
- أرقام الحملة الحقيقية (6,632/353/45) **مستبعدة** بانتظار موافقة معين (تعليق brief + reel-script).

## D/E/F. الملفات النصية
- explainer.ar/en: كل جملة من brief + tech.md + links.md.
- research.md: روابط خارجية مؤرَّخة 2026-09-23 (مواقع Opteo/Optmyzr/Adalysis الرسمية وصفحات تسعيرها، Google Ads Help، تقارير Ken Research/Mordor/ResearchAndMarkets/Statista، منشورات PPC). التموضع «أين يتفوّق» من tech.md فقط.
- copy.ar/en: brief (المختوم) + tech.md؛ حالة draft حتى ختم المحرر.

## الصور
- كل اللقطات حقيقية من screenshots/ في المستودع (التقاط 2026-09-11، تشغيل محلي Next.js dev **ببيانات تجريبية مطابقة لأرقام README** لأن Google Ads API يحتاج بيانات اعتماد معين — حسب links.md). لذلك **لا يُكتب «بيانات حية»** في أي مادة. اللقطات تُظهر اسم النطاق keifaldiafa.com والحساب 3412658939 لأنهما جزء من واجهة المنتج المُصوَّرة (مشروع معين نفسه، لا عميل خارجي).
- لا صورة مولّدة بالذكاء الاصطناعي في الحزمة.

## الهوية
02-brand/README.md: Navy #0E2A47 · Ink #08172B · Amber #F4A62A · Sand #F7F5F0 · Mist #DCE3EA · شريحة «شركات» #3B82F6. النص الصغير الخافت #A3B1C0 (تحديث AA معتمد 2026-09-23). خطوط IBM Plex Sans Arabic / Inter / JetBrains Mono. منطقة أمان الشعار 12% من العرض خالية في كل نسخة nologo.
