unicore-os | كاتب المحتوى | 2026-09-23 | v1

# UniCore-OS — بحث وتحليل (Research & positioning)

تاريخ البحث: 2026-09-23 (بحث ويب + GitHub API + فتح الصفحات). كل ادعاء عن مشروعنا من tech.md؛ كل ادعاء عن بديل من رابطه.

## 1. من يشتري هذا؟
- المستخدم: إدارة كلية أو قسم جامعي يحتاج نظاماً واحداً للمستخدمين والهيكل الأكاديمي والكويزات والدرجات بالعربية (README «الميزات»، MASTER_BLUEPRINT).
- المشتري في المحفظة: طالب مشروع تخرج أو قسم حاسب يريد قاعدة جاهزة حديثة (Next.js/Prisma) يبني عليها — الشريحة «طلاب»؛ وثانوياً جهة تعليمية صغيرة تريد نظاماً عربياً مفتوح المصدر.
- حجم الفئة: لا رقم موثّق لدينا — «يُستكمل». مؤشر غير مباشر: Moodle وحده 7,425 نجمة على GitHub وآخر push 2026-09-16، أي أن فئة الأنظمة الأكاديمية المفتوحة نشطة وكبيرة.

## 2. البدائل الحقيقية — أنظمة جامعية وتعليمية (وصول 2026-09-23)
| # | البديل | ماذا هو | GitHub (نجوم · لغة · ترخيص · آخر push) أو النموذج | الرابط | ماذا يقول عن نفسه |
|---|---|---|---|---|---|
| 1 | Moodle | أشهر منصة تعلّم مفتوحة المصدر: مقررات، كويزات وبنك أسئلة، أدوار وصلاحيات، ترجمات كثيرة | 7,425 · PHP · GPL-3.0 · 2026-09-16 | https://github.com/moodle/moodle · https://moodle.org/ | «the world's open source learning platform» |
| 2 | Open edX | منصة MOOC/تعلّم مفتوحة المصدر (edX/Harvard-MIT الأصل)، مقررات وتقييمات على نطاق واسع | 8,193 · Python · AGPL-3.0 · 2026-09-22 | https://github.com/openedx/edx-platform · https://openedx.org/ | منصة التعلّم المفتوحة خلف edX |
| 3 | Gibbon | منصة إدارة مدرسية مفتوحة المصدر: طلاب، معلمون، أولياء أمور، جداول، تقييم | 633 · PHP · GPL-3.0 · 2026-09-21 | https://github.com/GibbonEdu/core · https://gibbonedu.org/ | «flexible, open source school management platform designed to make life better for teachers, students, parents and leaders» |
| 4 | Classter | نظام إدارة تعليمي سحابي تجاري (SaaS) لـ K12 والجامعات ومراكز التدريب؛ تكاملات Office 365/Zoom | تجاري SaaS | https://www.classter.com/ | «all-in-one cloud-based… ecosystem» للمدارس والتعليم العالي |
| 5 | Fedena | ERP مدرسي/جامعي سحابي (SaaS) بخطط مدفوعة وإضافات (SMS، تطبيق جوال)؛ صفحة الموقع لا تذكر نسخة مفتوحة المصدر | تجاري SaaS | https://fedena.com/ | «web-based, multipurpose school and college management ERP» |
| 6 | openSIS Classic | نظام معلومات طلابي مفتوح المصدر بنسخة تجارية | 340 · PHP · (بلا ترخيص معلن في API) · 2026-06-08 | https://github.com/OS4ED/openSIS-Classic · https://www.opensis.com/ | «commercial grade, secure, scalable & intuitive Student Information System» |

ملاحظات: moodle.org ردّ 403 على الفحص الآلي (المستودع 200)؛ openedx.org ردّ 202؛ أرقام GitHub من API بتاريخ 2026-09-23 وتتغيّر. Classter وFedena لا يعلنان دعم العربية/RTL في صفحاتهما الرئيسية (لم أتحقق من صفحات داخلية).

## 3. التموضع
ماذا يقول المنافس: المفتوحة (Moodle، Open edX، Gibbon، openSIS) ناضجة ومجرّبة في آلاف المؤسسات لكنها PHP/Python وLMS/SIS عامة تُعرَّب بحزم ترجمة لاحقة، وصلاحياتها على مستوى الوحدة/السياق لا الإجراء الواحد، والذكاء الاصطناعي فيها إضافات لا نواة. التجارية (Classter، Fedena) SaaS مدفوعة مغلقة المصدر — لا يبني عليها طالب.

أين يتفوّق UniCore-OS (من tech.md فقط):
- عربي RTL من الأساس لا حزمة ترجمة؛ واجهة واحدة للإدارة والتدريس والطالب.
- 52 صلاحية على مستوى الإجراء (Server Action) من مصدر واحد في الكود؛ soft delete شامل مع سلة مهملات وسجل تدقيق.
- توليد أسئلة وتصحيح المقالي بالذكاء الاصطناعي (OpenAI/Gemini) مدمج في النواة — اختياري ويحتاج مفتاح API.
- مكدّس حديث (Next.js 16، React 19، TypeScript strict، Prisma) مناسب لطالب حاسب اليوم أكثر من PHP.

أين يتأخر (صريح): ناضج مقابل rc.4 — لا اختبارات وحدة ولا E2E ولا CI · مركز الذكاء الاصطناعي غير مفعّل بلا مفتاح API (ميزة اختيارية لا منجز مُشغَّل) · /logs يعيد 404 للمدير في التشغيل المحلي · لا مجتمع ولا إضافات ولا تنزيلات · لا نشر حي · 3 أنواع أسئلة مقابل عشرات في Moodle · لا جداول دراسية ولا حضور ولا رسوم (Gibbon/openSIS/Fedena تغطيها) · README متأخر عن الكود.

## 4. الكلمات المفتاحية
AR (10): نظام إدارة جامعي · نظام معلومات أكاديمي مفتوح المصدر · نظام جامعي عربي · صلاحيات وأدوار RBAC · محرك كويزات · توليد أسئلة بالذكاء الاصطناعي · Next.js عربي RTL · مشروع تخرج نظام جامعي · إدارة الكليات والأقسام · كشف درجات إلكتروني
EN (10): university management system · open source student information system · Arabic RTL Next.js app · RBAC permissions Next.js · quiz engine with AI question generation · Prisma university schema · capstone project university system · academic hierarchy management · gradebook CSV export · soft delete audit log

## 5. ثلاث زوايا محتوى
1. «52 صلاحية على مستوى الإجراء، لا الصفحة» — زاوية هندسية عن RBAC في Server Actions للمطوّرين.
2. «كويز يولّد أسئلته» — زاوية الذكاء الاصطناعي للمدرّسين: من موضوع إلى أسئلة إلى تصحيح مقترح.
3. «لماذا PHP ليس قدر الأنظمة الجامعية؟» — زاوية مقارنة صريحة مع Moodle/Gibbon لطلاب الحاسب.

## 6. الفجوات (بلا تجميل)
تقنياً: 0 اختبارات وحدة، 0 E2E، لا CI (HANDOFF §0) · مركز الذكاء الاصطناعي «غير مفعّل» بلا مفتاح API — الميزة اختيارية وغير مُشغَّلة افتراضياً · /logs أعاد 404 للمدير محلياً · README يذكر Next 15/20 جدول/100% بينما الكود 16.1.6/22/rc.4 · لا LICENSE ولا CONTRIBUTING رغم الإشارة إليهما · بيانات دخول تجريبية ورقم هاتف في الوثائق والصفحة /developer · لا نشر حي.
تسويقياً: لا أرقام مستخدمين ولا مؤسسة تستخدمه · لا لقطات في المستودع (أُخذت هنا محلياً) · اسم المنتج «OS» قد يُفهم كنظام تشغيل.

## 7. المصادر
- المشروع: https://github.com/moain2028/UniCore-OS-V2 (200) · README.md · docs/HANDOFF.md · docs/PROJECT_STATUS.md · CHANGELOG.md · app/package.json · app/prisma/schema.prisma · app/src/lib/auth/constants.ts · تشغيل محلي 2026-09-23.
- البدائل: GitHub API (نجوم/لغة/ترخيص/آخر push) + صفحاتها، 2026-09-23.

## EN summary
UniCore-OS targets capstone students and CS departments wanting an Arabic-first, open-source university system on a modern stack. Real alternatives (accessed 2026-09-23): Moodle (7.4K★, PHP, GPL-3), Open edX (8.2K★, Python, AGPL-3), Gibbon (633★, PHP, GPL-3), openSIS Classic (340★, PHP), plus commercial SaaS Classter and Fedena. UniCore-OS's edge: Arabic RTL from the ground up, 52 action-level permissions, universal soft delete with audit log, built-in (optional, key-required) AI question generation/grading, Next.js 16 + Prisma. Gaps: rc-stage with no tests/CI, AI center disabled without an API key, no community or live deployment, 3 question types, no timetable/attendance/fees, README lags the code, /logs 404 locally.
