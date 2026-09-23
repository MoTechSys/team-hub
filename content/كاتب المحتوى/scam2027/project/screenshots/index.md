scam2027 | كاتب المحتوى | 2026-09-23 | ready

# scam2027 — فهرس اللقطات (31 لقطة حقيقية، 2x)

تشغيل محلي 2026-09-23 من main (c761778): PostgreSQL 16 محلي + `prisma migrate deploy` + `prisma/seed.ts` (مستأجر «جامعة النموذج» demo بحسابات وهمية — لا جامعة ولا شخص حقيقي) + `pnpm build && pnpm start -p 3300`. التقاط Playwright/Chromium بـ deviceScaleFactor=2: ديسكتوب 1440×900 → 2880×1800؛ جوال 390×844 → 780×1688. لغة الواجهة عربية. لا اتصال بأي خدمة خارجية. سكربت: `_portfolio-shoot.mjs`. لم تُلتقط صفحة `/developer` (تحمل هاتف المطوّر).

| الملف | المحتوى | استخدام مقترح |
|---|---|---|
| desktop/mobile-00-login | /login — صفحة الدخول | |
| desktop/mobile-01-dashboard | /dashboard — لوحة مدير المستأجر بإحصائيات حقيقية من seed (33 مستخدماً، 30 طالباً، 4 أدوار) | **اللقطة الرئيسية** ديسكتوب |
| desktop/mobile-02-users | /users — المستخدمون | |
| desktop/mobile-03-roles | /roles — الأدوار (5 نظام) | |
| desktop/mobile-04-role-detail | /roles/[id] — مصفوفة صلاحيات دور «طالب» (20 من 114) | الكاروسيل «كيف يعمل» |
| desktop/mobile-05-academic-colleges | /academic/colleges — البنية الأكاديمية | |
| desktop/mobile-06-academic-years | /academic/years — الأعوام والفصول | |
| desktop/mobile-07-courses | /courses — 6 مقررات | |
| desktop/mobile-08-offerings | /offerings — 4 شُعب بحالاتها والسعة | الكاروسيل «الحل» |
| desktop/mobile-09-offering-detail | /offerings/[id] — شعبة CS101 بالتسجيلات | **اللقطة الرئيسية** جوال |
| desktop/mobile-10-files | /files — الملفات (2 عيّنة) | |
| desktop/mobile-11-notifications | /notifications — الإشعارات | |
| desktop/mobile-12-trash | /trash — سلة المحذوفات الموحّدة | |
| mobile-13-nav-open | قائمة التنقل مفتوحة على الجوال | |
| desktop/mobile-14-student-dashboard | /dashboard — لوحة الطالب | |
| desktop/mobile-15-student-courses | /courses — مقررات الطالب | |

أسماء المستخدمين الظاهرة (عبدالله المدير، محمد الطالب، د. أحمد الحسني…) وهمية من prisma/seed.ts. لا صورة مولّدة بالذكاء الاصطناعي؛ الأيقونات lucide من المنتج نفسه.
