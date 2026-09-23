almham-electricity-erp | صانع العروض | 2026-09-23 | project-pack-v2-addendum (B–F) — يُكمل design-pack-v1 المعتمد

# مصادر كل نص ورقم وصورة — ملحق almham-electricity-erp (B–F)

المصدر الحي: https://github.com/moain2028/portfolio-hub → 01-projects/almham-electricity-erp/ (brief.ar.md · brief.en.md · tech.md · links.md · screenshots/) · الهوية 02-brand/README.md · المعيار project-pack-standard-v2.md. المستودع الأصلي MoTechSys/almham خاص 🔒 → لا رابط كود. لا اسم عميل.

## B. النشر (14 PNG)
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| كاروسيل 1 المشكلة | محطات الكهرباء الصغيرة تدير التوليد والمشتركين والفوترة بين جداول متفرقة / وبرنامج فوترة قديم على SQL Server، بلا صورة مالية واحدة | Small utilities run generation, subscribers and billing across spreadsheets / and a legacy SQL Server tool, with no single financial picture | brief «المشكلة» / «Problem» |
| كاروسيل 2 الحل | ERP واحد متعدد الشركات والفروع والمحطات / Angular 22 على NestJS 11 مع PostgreSQL… جسر آمن الفشل لبيانات ECAS | One multi-company, multi-branch, multi-station ERP / Angular 22 on NestJS 11… fail-safe bridge to legacy ECAS data | brief «الحل» / «Solution» |
| كاروسيل 3 كيف يعمل | من قراءة العداد إلى القيد / قراءات → سدادات → أثر على دفتر الأستاذ بقيد مزدوج ومسار اعتماد draft → ready → approved → posted، وترحيل كامل من ECAS | From meter reading to ledger / Readings → payments → direct ledger impact… | brief «لمن يفيد» + tech.md «الحل» |
| كاروسيل 4 الأرقام | 687 · 9 · 515 · 48 + «المصدر: README المستودع §4 و§6 · git ls-tree 2026-09-11» | same | tech.md «الأرقام» |
| كاروسيل 5 الدعوة | نظام واحد لشركة الكهرباء / لشركات الكهرباء والمشغّلين الصناعيين… أُقدّم دراسة لنظام محطتك — راسلني | One system for the utility / For utilities and industrial operators… Let's scope your utility's system | brief «لمن يفيد» + «تواصل» |
| بطاقة «رقم واحد» | 687 فترة فوترة مطابَقة في استيراد ECAS الكامل · ترحيل كامل للبيانات التاريخية · idempotent وقابلة للاستئناف | 687 billing periods reconciled in the full ECAS import · full historical migration · idempotent, resumable reruns | tech.md «الأرقام» (README §6) + «التقنيات» (ETL) |
| بانر المقال 1600×840 | العنوان + «أنظمة العباسي المتخصصة» + «نظام واحد من قراءة العداد إلى القيد» + التاجات | same | brief H1 + «لمن يفيد» + «الحل» |

اللقطات: `desktop-02-dashboard.png` (1، بانر) · `mobile-02-dashboard.png` (2، بانر) · `desktop-06-subscribers-map.png` (3) · `desktop-11-treasury.png` (5) — كلها حقيقية من screenshots/؛ لا لقطة مولّدة.

## C. الريل
- `almham-electricity-erp-reel-1080x1920-{ar,en}-nologo.mp4`: 21 ث · 1080×1920 · 30fps · H.264/AAC · 6 مشاهد × 4 ث، تلاشٍ 0.6 ث، زوم بطيء · بلا شعار · لا مشاهد خطأ. نصوص المشاهد في copy «نص الريل»؛ مصدرها brief + tech.md. غلافان `reel-cover-1080x1920-{ar,en}-nologo.png` = المشهد 1.
- لقطات الريل: desktop-02-dashboard · mobile-02-dashboard · desktop-06-subscribers-map · desktop-11-treasury.
- الموسيقى: `reel/music.mp3` مولَّدة بالذكاء الاصطناعي (CassetteAI عبر أدوات Genspark، 30 ث، instrumental) — بلا حقوق طرف ثالث.
- ريل المستودع السابق `video/almham-electricity-erp-reel-*.mp4` لم يُستخدم (شعار + رابط GitHub على الأرجح كنظيره في motech).

## D. الشروحات
- `explainer.{ar,en}.md` ~470/460 كلمة + خلاصة 5 نقاط؛ كل جملة مذيَّلة بمصدرها (brief · tech.md · links.md).

## E. البحث
- `research.md`: 3 منافسين بروابط مؤرَّخة 2026-09-23 (Oracle CC&B · SAP FI-CA · Springbrook Cirrus) + مرجع Kill Bill + الوضع الراهن ECAS. التموضع من tech.md فقط. حجم الفئة «يُستكمل».

## F. النصوص
- `copy.{ar,en}.md`: LinkedIn ≤120 كلمة · X ≤280 حرف · IG ≤150 كلمة · نص الريل — draft للمحرر؛ تستبدل copy.ar/en.md في design-pack-v1 (نفس نص LinkedIn مع إضافة X وIG والريل).

## تناقضات لم تُعرض (قاعدة v2)
- 170 جدولاً (schema.ts) مقابل 204 (قاعدة التشغيل) — tech.md نفسه؛ لم يُعرض.
- brief «عدد الاختبارات والصفحات: يُستكمل» مقابل tech.md «515 ملف اختبار» (git ls-tree) — استُخدم رقم tech.md لأنه بمصدر قابل للتحقق؛ يلزم تحديث brief.
- أعداد المشتركين/العدّادات/المستخدمين: يُستكمل — لم تُعرض.

## الهوية والتباين
كما SOURCES.md في design-pack-v1؛ النص الخافت #A3B1C0 (تحديث v2).

## إعادة التوليد
`build.py b` → 14 قطعة نشر · `build.py reel` ثم `make_reel.sh ar|en` → الريل. (Python 3 + Playwright/Chromium + ffmpeg)
