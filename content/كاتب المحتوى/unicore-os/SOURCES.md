unicore-os | كاتب المحتوى | 2026-09-23 | project-pack v2

# UniCore-OS project pack v2 — مصادر كل نص ورقم وصورة

المشروع ليس في portfolio-hub؛ البند 0 أنتج `project/` (brief.ar/en.md · tech.md · links.md · screenshots/ + index.md) المرفق في هذه الحزمة وجاهز للإضافة إلى `01-projects/unicore-os/`. المصدر الأصلي: https://github.com/moain2028/UniCore-OS-V2 (main، commit 618d180، 2026-09-04) — README.md، CHANGELOG.md، docs/HANDOFF.md، docs/PROJECT_STATUS.md، app/package.json، app/prisma/schema.prisma، app/src/lib/auth/constants.ts، .env.example، وتشغيل محلي 2026-09-23.

## A. التصاميم (24 PNG)
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| العنوان | UniCore-OS | UniCore-OS | README H1 |
| الثانوي | نظام إدارة جامعي | نظام إدارة جامعي | README H1 «نظام إدارة جامعي ذكي متكامل» |
| السطر التعريفي | نظام إدارة جامعي عربي بصلاحيات دقيقة وميزات ذكاء اصطناعي اختيارية | An Arabic university management system with fine-grained permissions and optional AI features | brief H1 (من README «الميزات الرئيسية») |
| الشارة | عربي RTL بالكامل | Fully Arabic RTL | HANDOFF §3 «RTL عربي»؛ README |
| الميزات (X/Hero/Story) | 52 صلاحية وأدوار مخصصة · كليات → أقسام → تخصصات → مقررات → شُعب · محرك كويزات + توليد أسئلة بالذكاء الاصطناعي (اختياري) · سلة مهملات — لا حذف نهائي | (مقابلها) | README «الميزات الرئيسية» + «الأمان: Soft Delete» |
| الأرقام الثلاثة | 52 صلاحية · 26 صفحة · 22 جدولاً | 52 permissions · 26 pages · 22 database models | tech.md: constants.ts (52) · find page.tsx (26) · schema.prisma (22) |
| شارة الشريحة | طلاب | Students | تكليف مدير المنتج؛ #8B5CF6 من 02-brand |
| التقنيات (فوتر) | Next.js 16 · React 19 · Prisma 5 · Tailwind 4 | | app/package.json (next 16.1.6, react 19.2.3, prisma 5.22.0, tailwindcss ^4) |
| الرابط | github.com/moain2028/UniCore-OS-V2 | | تكليف مدير المنتج؛ links.md |
| عنوان شريط المتصفح | فارغ عمداً | | لا موقع حي (links.md) — لم يُكتب رابط وهمي |
| wordmark (logo فقط) | معين العباسي | Moain Al-Abbasi | معيار v2 |
| الخافت | #A3B1C0 | | معيار v2 |

## B. تصاميم النشر (14 PNG)
- كاروسيل 5×AR + 5×EN: 1 المشكلة (brief «المشكلة») · 2 الحل (brief «الحل») · 3 كيف يعمل: RBAC 52 من مصدر واحد (HANDOFF §3.2)، الهيكل (README)، أنواع الكويز (README «محرك الكويزات»)، AI (README «ذكاء اصطناعي») · 4 الأرقام: 52 · 26 · 22 · 0 أخطاء TypeScript (tech.md، tsc محلياً exit 0) · 5 لمن (brief «لمن يفيد» + «للتواصل»).
- بطاقة «رقم واحد»: 52 — «أدوار مخصصة + Super Admin» (README) + جملة التحقق قبل التنفيذ (HANDOFF §3.2 requirePermission/assertPermission) + soft delete (README «الأمان»).
- بانر مقال 1600×840: kicker «مشروع طلابي · نظام جامعي» (الشريحة) · العنوان صياغة تسويقية لمشكلة brief («خمسة أنظمة» تعبير مجازي لا رقم مصدري — يقرّره المحرر) · السطر من brief «الحل».

## C. الفيديو
- unicore-os-reel-ar.mp4 · -en.mp4 — 1080×1920، 30fps، H.264+AAC، 19.6 ث، 6 مشاهد، بلا شعار + غلافان.
- المشهد 01 من HANDOFF §3.2 وREADME «52 صلاحية»؛ 02 من README «محرك الكويزات» و«ذكاء اصطناعي» وحالات Quiz (HANDOFF §3.1 بند 6)؛ 03 من README «الهيكل الأكاديمي» و«الأمان»؛ الأرقام من tech.md.
- الموسيقى: 02-brand/scripts/reels/bgm-tech-minimal.mp3 (مولّدة آلياً بلا حقوق). لا مشاهد خطأ: كل اللقطات من تشغيل ناجح (200).

## الصور (22 لقطة، كلها حقيقية من تشغيل محلي 2x)
| المستخدمة في التصاميم | الصفحة | الدور | أين |
|---|---|---|---|
| desktop-07-quizzes | /quizzes (لوحة المدرّس — قائمة الكويزات) | مدرس | **البطل** في A (LinkedIn/X/IG/Story/Hero) — بديلاً عن لوحة المدير بطلب مدير المنتج (عدّادات seed شبه فارغة وبريد seed) |
| desktop-01-admin-dashboard | /dashboard | مدير | كاروسيل 2 فقط (بيانات seed مُعلَنة) |
| desktop-02-users | /users | مدير | كاروسيل 1 |
| desktop-03-roles | /roles (52 صلاحية) | مدير | البانر |
| mobile-02-quizzes | /quizzes | مدرس | الجوال المتداخل في A، ريل 00/02 |
| mobile-01-admin-dashboard | /dashboard | مدير | كاروسيل 1، ريل 03 |
| mobile-07-roles | /roles | مدير | كاروسيل 3، البانر، ريل 00/01 |
| mobile-03-student-dashboard | /dashboard | طالب | كاروسيل 5، ريل 02 |
| mobile-06-login | /login | — | ريل 99 |
- الالتقاط: Playwright/Chromium، deviceScaleFactor 2، 1440×900 و390×844، locale ar، ثلاثة حسابات seed. السكربت `project/screenshots/_portfolio-shoot.mjs`.
- البيانات: كلها seed تجريبي (`prisma/seed.ts`) — العدّادات صغيرة (3 مستخدمين، كويز واحد، شعبة واحدة) لأن لا بيانات إنتاج؛ لا توجد لقطة «أغنى» فعلياً، فاختيرت قائمة الكويزات بطلاً (بلا بريد) وأُبقيت لوحة المدير في الكاروسيل — الأسماء الظاهرة (مدير النظام، أحمد العلي، سارة محمد) وهمية من seed؛ لا شخص حقيقي، لا رقم هاتف، لا بريد حقيقي. لم يُطمس شيء لأن لا بيانات حقيقية.
- لم تُستخدم صفحة /developer (تحمل اسم معين ورقم هاتفه) ولا /logs (404).

## D/E/F. النصوص
- explainer AR/EN (~520/540 كلمة + خلاصة 5 نقاط): README، HANDOFF §0/§3، .env.example، tech.md.
- research.md: Moodle · Open edX · Gibbon · openSIS Classic (GitHub API) + Classter · Fedena (SaaS تجاري، صفحاتهما) بأرقام GitHub API (نجوم/لغة/ترخيص/آخر push) بتاريخ 2026-09-23 + روابط الصفحات؛ ادعاءات مشروعنا من tech.md فقط.
- copy AR/EN: LinkedIn 112/116 كلمة · X 228/234 حرفاً · IG 118/112 كلمة · نص الريل — من brief/tech؛ draft-for-editor.

## ما لم يُذكر عمداً / تضاربات
- «362 ملفاً» (تكليف) لم يُتحقَّق — git يعدّ 258 متعقّباً؛ لم يُعرض أيّ منهما على التصاميم.
- «20 جدول» و«Next.js 15» و«100%» في README متأخرة عن الكود — اعتُمد الكود (22، 16.1.6، rc.4).
- «زحف 102 صفحة» رقم قياس المؤلف في HANDOFF — ذُكر في brief/explainer منسوباً لمصدره، ولم يُعرض على التصاميم.
- أرقام مستخدمين/مؤسسات: يُستكمل. بيانات الدخول التجريبية ورقم الهاتف: لا تُنقل.
- التصنيف «طلاب» بحسب التكليف؛ المنتج بطبيعته لجهات تعليمية — يُراجَع عند الحاجة.
- «الذكاء الاصطناعي» على كل التصاميم والنصوص بصيغة «اختياري/بمفتاح API» لا كمنجز مُشغَّل — مركز AI ظهر «غير مفعّل» في التشغيل المحلي (ملاحظة مدير المنتج 2026-09-23).

## الأدوات
tools/: packgen.py (KIND=web: إطار متصفح + جوال) · reelgen.py · project.py · _portfolio-shoot.mjs — إعادة التوليد بأمر واحد.
