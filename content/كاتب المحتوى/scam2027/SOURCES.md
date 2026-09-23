scam2027 | كاتب المحتوى | 2026-09-23 | project-pack v2

# scam2027 project pack v2 — مصادر كل نص ورقم وصورة

المشروع ليس في portfolio-hub؛ البند 0 أنتج `project/` (brief.ar/en.md · tech.md · links.md · screenshots/ + index.md) المرفق في هذه الحزمة وجاهز للإضافة إلى `01-projects/scam2027/`. المصدر الأصلي: https://github.com/moain2028/scam2027 (main، commit c761778، 2026-09-07) — README.md، AGENTS.md، docs/** (33 وثيقة، STATUS.json، ROADMAP، 9 ADR)، app/prisma/schema.prisma + migrations + seed.ts، app/src/**، app/e2e/**، app/tests/** — وتشغيل محلي كامل 2026-09-23 (PostgreSQL 16 محلي، migrate deploy، seed، pnpm build/start، pnpm test، pnpm typecheck). لا اتصال بأي خدمة خارجية.

## إفصاحات صدق (تسري على كل الحزمة)
- **الحالة تُعرض كما هي:** «قيد البناء · 24 / 65 مهمة» شارة على كل تصميم من الـ 24، وعلى غلاف الريل ومشهده الأول، وفي كل نص. لا صياغة توحي بمنتج جاهز؛ ما لم يبدأ (تقييم، AI، SIS، PDPL، MFA، LTI) مسمّى في الشرح والبحث.
- **كل اللقطات من seed وهمي**: مستأجر «جامعة النموذج» (demo) وحسابات من prisma/seed.ts (عبدالله المدير، محمد الطالب، د. أحمد الحسني…) — لا جامعة ولا شخص حقيقي. وُسمت «بيانات عرض» في تذييل شرائح الكاروسيل 2/5 و3/5 و5/5 وغلاف الريل ومشاهده الثلاثة.
- **صفحة `/developer` مستبعدة** من اللقطات (تحمل هاتف المطوّر)؛ الهاتف لا يظهر في أي مادة.
- **الأرقام المسموحة على التصاميم:** 114 · 34 · 181 · 30 · 24/65 — لا غير. «68 نموذجاً» (خريطة التوثيق = المخطَّط) و«Playwright 80 ✅» (README) لم يُعادا فلا يُعرضان. CI قالب غير مفعَّل — لا ادعاء CI.
- **الرخصة** «جميع الحقوق محفوظة © 2026 MoTechSys (تُحدَّد لاحقاً)» — لا كلمة open source لمشروعنا في أي نص (تظهر فقط في وصف Moodle/Canvas/Open edX في research).
- التذييل github.com/moain2028/scam2027 على كل شيء؛ README يوجّه إلى MoTechSys — فجوة معلَنة وبند لمحمد.
- الدعوة في nologo «راسلني / DM me» بلا اسم؛ الاسم النصّي «معين العباسي / Moain Al-Abbasi» في نسخة logo فقط. لا صورة ولا أيقونة مولّدة بالذكاء الاصطناعي؛ الأيقونات lucide من المنتج نفسه.

## A. التصاميم (24 PNG)
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| العنوان | scam2027 | scam2027 | README H1 |
| الثانوي | منصة مقررات وتقييم متعددة المستأجرين | Multi-tenant course & assessment | README H1 «Smart Course & Assessment Manager … متعدّدة المستأجرين» |
| السطر التعريفي | عدة جامعات على نشر واحد — عزل بـ Row Level Security و114 صلاحية منقّطة | Several universities on one deployment — isolated by Row Level Security and 114 dotted permissions | README المقدمة؛ ADR-0002؛ permissions.ts |
| الشارة | قيد البناء · 24 / 65 مهمة | Under construction · 24 / 65 tasks | docs/90-handoff/STATUS.json progress (قرار مدير المنتج) |
| الميزات (X/Hero/Story) | RLS على 30 جدولاً · RBAC 114 و5 أدوار · مستخدمون/بنية/مقررات/شُعب/ملفات/إشعارات · عربية RTL جوال-أولاً | (مقابلها) | pg_class.relrowsecurity محلياً؛ seed.ts ROLE_META؛ STATUS.json doneTaskIds P1-01..08؛ ADR-0007/0008 |
| الأرقام الثلاثة | 114 صلاحية · 34 نموذج بيانات · 181 اختباراً تمرّ | 114 permissions · 34 data models · 181 tests passing | `SELECT count(*) FROM "Permission"`؛ `grep -c "^model " schema.prisma`؛ `pnpm test` 2026-09-23 |
| شارة الشريحة | شركات | Companies | تكليف مدير المنتج؛ #3B82F6 من 02-brand |
| التقنيات (فوتر) | Next.js 16 · Prisma · PostgreSQL RLS · Auth.js | | app/package.json؛ README «الحزمة التقنية» |
| الرابط | github.com/moain2028/scam2027 | | تكليف مدير المنتج؛ links.md |
| عنوان شريط المتصفح | فارغ عمداً | | لا موقع حي (links.md) |
| wordmark (logo فقط) | معين العباسي | Moain Al-Abbasi | معيار v2 |
| الخافت | #A3B1C0 | | معيار v2 |
| اللقطات | DESK = desktop-01-dashboard (لوحة مدير المستأجر) · MOB = mobile-09-offering-detail (شعبة CS101) · FAN = mobile-09, 01, 04 | | project/screenshots/index.md؛ البطل معتمد من مدير المنتج 2026-09-23 |

## B. تصاميم النشر (14 PNG)
- كاروسيل 5×AR + 5×EN: 1 المشكلة (README «لماذا هذا المستودع؟»، docs/00-analysis GAP-01..27؛ لقطة login + قائمة الجوال) · 2 الحل (README؛ ADR-0002/0004/0007؛ لقطة الشُعب + شعبة — **تذييل «بيانات عرض»**) · 3 كيف يعمل: RLS بمستخدم بلا BYPASSRLS (migrations rls_p0، ADR-0002)، 114 صلاحية resource.action (permissions.ts، 02-PERMISSIONS-MATRIX)، بنية → مقررات → شُعب → تسجيل بـ Server Actions (ADR-0004، features/*)، STATUS.json + CHANGELOG في نفس الالتزام (README «سير العمل الإلزامي»)؛ لقطة مصفوفة صلاحيات دور «طالب» — تذييل «بيانات عرض» · 4 الأرقام: 114 · 34 · 181 · 24/65 (tech.md) · 5 لمن (brief «لمن يفيد» + «للتواصل»؛ لقطة لوحة الجوال — تذييل «بيانات عرض»).
- بطاقة «رقم واحد»: **30** — «جدولاً مستأجرياً محمياً بـ Row Level Security — العزل في Postgres لا في الكود» (`SELECT count(*) FROM pg_policies` = 30؛ `relrowsecurity` على 30 من 34 جدولاً؛ migration rls_p0 ينشئ `app_user … NOBYPASSRLS`؛ tests/integration/tenant-isolation*) — معتمدة من مدير المنتج.
- بانر 1600×840 AR/EN: العنوان من زاوية «تسعة مستودعات — أساس واحد» (research §5)؛ الأرقام من tech.md؛ اللقطات desktop-01 + mobile-09.

## C. الريلان (1080×1920، 19.6 ث، بلا شعار)
- المشاهد: غلاف (brief H1 + شارة «قيد البناء · 24 / 65» + تذييل «بيانات عرض») → المستأجرون (ADR-0002، pg_policies؛ لقطات لوحة + قائمة؛ pill «قيد البناء · 24 / 65 — RLS على 30 جدولاً») → الصلاحيات (permissions.ts، seed ROLE_META، Auth.js؛ لقطة مصفوفة الدور) → المنجَز (STATUS.json P1-01..08؛ لقطات شعبة + مقررات؛ pill «P0 مكتمل · P1 8/15») → الأرقام (tech.md) → CTA «راسلني / DM me» (brief «للتواصل»؛ لقطة لوحة الطالب). تذييل «بيانات عرض» على المشاهد الثلاثة والغلاف. المدد: 3.2 + 3.6×3 + 3.8 + 3.8 − انتقالات 0.4×5 = 19.6 ث.
- الموسيقى: 02-brand/scripts/reels/bgm-tech-minimal.mp3 (أصل الفريق). الغلاف = الإطار 00.

## D. الشرح (explainer AR/EN)
يفتح بالحالة الصادقة (STATUS.json) ويسمّي ما لم يبدأ (ROADMAP P2–P5)؛ كل جملة من brief/tech/research؛ الأرقام من جدول tech.md (22 صفاً)؛ «ما لم يُنجَز» من tech.md «ملاحظات التنظيف» + research §6.

## E. البحث (research.md)
MoodleCloud https://moodlecloud.com/app/en/ + https://www.moodlecloud.com/standard-plans/ ($170–$2,140 USD/سنة) · Canvas https://www.instructure.com/canvas (عرض سعر؛ /canvas/pricing يعيد 404) + vendr.com · Open edX https://openedx.org/get-started/self-managed/ + /trademark-licensing-details/ (AGPL-3 + Apache 2.0) + GitHub API لـ moodle/moodle (7,425★ GPL-3.0)، instructure/canvas-lms (6,834★ AGPL-3.0)، openedx/openedx-platform (8,193★ AGPL-3.0) — كلها بتاريخ 2026-09-23. التموضع «عزل المستأجرين في قاعدة البيانات» لا «بديل كامل» (قرار مدير المنتج).

## F. نصوص النشر (copy AR/EN + نص الريل)
من brief + tech + research؛ الأطوال داخل الحدود (LinkedIn ≤120 · X ≤280 · IG ≤150)؛ الحالة في كل نص. draft للمحرر.

## project/ (البند 0)
brief.ar/en.md · tech.md (22 صفاً، كل رقم بأمر/ملف) · links.md · screenshots/ (31 لقطة 2x + index.md + _portfolio-shoot.mjs + _shots.log).

## tools/
packgen.py · reelgen.py · project.py · _portfolio-shoot.mjs — لإعادة التوليد.
