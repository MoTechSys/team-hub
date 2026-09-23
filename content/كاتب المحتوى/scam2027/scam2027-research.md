scam2027 | كاتب المحتوى | 2026-09-23 | v1

# scam2027 — بحث وتحليل (Research & positioning)

تاريخ البحث: 2026-09-23 (فتح صفحات الأسعار + GitHub API + بحث ويب). كل ادعاء عن مشروعنا من tech.md؛ كل ادعاء عن بديل من رابطه بتاريخ الوصول. التموضع «عزل المستأجرين في قاعدة البيانات» — لا «بديل كامل لنظام LMS» لأن التقييم والواجبات لم تُبنَ (P2/P3 لم تبدأ). المشروع «قيد البناء، الأساس مكتمل» (24/65). الرخصة «جميع الحقوق محفوظة» — لا كلمة open source لمشروعنا.

## 1. من يشتري هذا؟
- المستخدم: جامعة أو كلية تريد منصة مقررات وتقييم تُدار لعدة مؤسسات من نشر واحد (SaaS متعدد المستأجرين) أو نشراً خاصاً بها، بواجهة عربية RTL جوال-أولاً (README H1 + docs/10-research/00-LMS-BENCHMARK «SaaS متعدد المستأجرين + خيار استضافة خاصة»).
- المشتري في المحفظة: الشريحة «شركات» — إدارات تقنية المعلومات الجامعية ومزوّدو حلول التعليم العالي في المنطقة العربية (docs/10-research/03-PDPL-NCA-COMPLIANCE: امتثال PDPL/NCA السعودي مستهدَف).
- حجم الفئة: لا رقم موثّق لدينا. مؤشر غير مباشر: Moodle 7,425 نجمة على GitHub وOpen edX 8,193 وCanvas 6,834 (2026-09-23) — فئة LMS ناضجة ومزدحمة، والتمايز في العزل والتوطين لا في الميزات.

## 2. البدائل الحقيقية (وصول 2026-09-23)
| # | البديل | ماذا هو | السعر المعلن | الرابط | ملاحظة |
|---|---|---|---|---|---|
| 1 | Moodle / MoodleCloud | أشهر LMS مفتوح المصدر، ذاتي الاستضافة مجاناً أو مستضاف عبر MoodleCloud | MoodleCloud سنوي: Starter $170 USD (50 مستخدماً، 1 GB) · Mini $270 (100) · Small $500 (200) · Medium $1,210 (500) · Standard $2,140 (750) — تُحاسَب بالدولار الأسترالي | https://moodlecloud.com/app/en/ · https://www.moodlecloud.com/standard-plans/ | 7,425★ · GPL-3.0 · آخر push 2026-09-16 · تعددية المستأجرين عبر Moodle Workplace أو استضافات منفصلة |
| 2 | Canvas LMS (Instructure) | LMS سحابي رائد للجامعات مع نسخة مفتوحة المصدر | لا أسعار منشورة — عرض سعر مخصّص بحسب المؤسسة وعدد المستخدمين (vendr.com: «does not publish fixed per-user rates»)؛ Free-for-Teacher وCanvas Lite (2026) بلا كلفة للمعلّم الفرد | https://www.instructure.com/canvas · https://github.com/instructure/canvas-lms | 6,834★ · AGPL-3.0 · آخر push للمستودع العام 2026-04-30 · صفحة /canvas/pricing تعيد 404 |
| 3 | Open edX | منصة تعلّم مفتوحة المصدر (Python/Django) للجامعات والمنصات الضخمة؛ توزيعة Tutor بـ Docker | مجاني ذاتي الاستضافة؛ مزوّدون مُدارون (edly وغيرهم) بأسعار غير منشورة على openedx.org | https://openedx.org/get-started/self-managed/ · https://openedx.org/trademark-licensing-details/ · https://github.com/openedx/openedx-platform | 8,193★ · AGPL-3.0 (+ Apache 2.0 لأجزاء) · آخر push 2026-09-22 |

ملاحظات: Canvas لا ينشر أسعاراً مؤسسية (النطاقات في مدوّنات طرف ثالث لم تُعتمد)؛ Open edX مزوّدوه بأسعار غير منشورة؛ الأسعار تتغيّر — كلها بتاريخ 2026-09-23. المستودع نفسه يقارن بـ Moodle/Canvas/Blackboard في docs/10-research/00-LMS-BENCHMARK.md.

## 3. التموضع
ماذا يقول المنافسون: أنظمة LMS كاملة وناضجة — مقررات، تقييم، واجبات، تفاعل، تكاملات LTI، تطبيقات جوال — كلٌّ منها يخدم مؤسسة لكل نشر (Moodle/Canvas) أو يعمل كمنصة ضخمة لجهة واحدة (Open edX)؛ تعددية المستأجرين إما منتج منفصل (Moodle Workplace) أو استضافة منفصلة لكل عميل.

أين يتميّز scam2027 (من tech.md فقط):
- **عزل المستأجرين في قاعدة البيانات نفسها**: مخطط مشترك + tenantId + Row Level Security على 30 جدولاً؛ مستخدم التطبيق بلا BYPASSRLS والمستأجر يُضبط بـ GUC لكل طلب — عدة جامعات على نشر واحد بلا ثقة في كود التطبيق (ADR-0002).
- **RBAC منقّط بـ 114 صلاحية في 14 فئة** و5 أدوار نظام + أدوار مخصّصة لكل مستأجر، مولَّدة من مصفوفة موثَّقة (permissions.ts).
- **عربي RTL جوال-أولاً من اليوم الأول** بقشرة تطبيق (viewport ثابت، شريط سفلي، ADR-0007/0008) — لا ترجمة لاحقة لواجهة إنجليزية.
- **توثيق يتحدّث مع الكود**: STATUS.json وCHANGELOG في نفس الالتزام؛ 33 وثيقة و9 ADR؛ 181 اختبار Vitest تمرّ وtypecheck صفر.

أين يتأخر (صريح): **37٪ من الخطة فقط** — لا تقييم ولا اختبارات إلكترونية ولا واجبات ولا درجات (P2/P3 لم تبدأ)؛ لا AI ولا استيراد SIS ولا PDPL كامل ولا MFA ولا SSO ولا LTI/QTI/OneRoster (P2–P5)؛ CI غير مفعَّل على GitHub (قالب فقط)؛ لا رابط حيّ ولا جامعة مستخدمة؛ 23 commits في 4 أيام؛ الرخصة النهائية غير محدَّدة؛ README يوجّه إلى MoTechSys لا moain2028.

## 4. الكلمات المفتاحية
AR (10): نظام إدارة مقررات جامعي · منصة تعليم عالٍ متعددة المستأجرين · Row Level Security للمستأجرين · صلاحيات منقّطة RBAC · واجهة عربية RTL جوال أولاً · Next.js 16 Prisma PostgreSQL · تسجيل الطلاب في الشُعب · بنية أكاديمية كليات أقسام تخصصات · امتثال PDPL للجامعات · LMS عربي قيد البناء
EN (10): multi-tenant LMS PostgreSQL RLS · university course management platform Next.js · dotted permissions RBAC 114 · Arabic RTL mobile-first LMS · Prisma Row Level Security tenant isolation · Auth.js revocable sessions · academic structure colleges departments majors · section enrolment management · Saudi PDPL compliant education platform · higher-education SaaS foundation

## 5. ثلاث زوايا محتوى
1. «تسعة مستودعات تراثية — أساس واحد متعدد المستأجرين» — زاوية المنتج: لماذا يُبنى من جديد وما الذي وُحِّد (GAP-01..27).
2. «العزل في Postgres لا في الكود» — زاوية هندسية: RLS على 30 جدولاً، مستخدم بلا BYPASSRLS، GUC لكل طلب، اختبارات تكامل للعزل.
3. «24 من 65 — بصراحة» — زاوية الصدق: STATUS.json يُحدَّث مع كل PR، P0 مكتمل، P1 8/15، وما لم يبدأ مسمّى.

## 6. الفجوات (بلا تجميل)
تقنياً: P2–P5 لم تبدأ (تقييم، AI، SIS، PDPL كامل، MFA، SSO، PWA، LTI/QTI/OneRoster) · CI قالب غير مفعَّل (`.github/ci.yml.template`) · «68 نموذجاً» في خريطة التوثيق مقابل 34 في schema.prisma · «Playwright 80 ✅» في README لم يُعَد هنا · 23 commits في 4 أيام (2026-09-04 → 09-07) · لا CHANGELOG لإصدار منشور · الرخصة النهائية غير محدَّدة.
تسويقياً: لا رابط حيّ ولا جامعة مستخدمة موثَّقة · هاتف المطوّر في README وصفحة `/developer` داخل المنتج · README يوجّه clone إلى MoTechSys/scam2027 لا moain2028 · اسم المشروع scam2027 (Smart Course & Assessment Manager) يُقرأ بالإنجليزية كـ «scam» — يُعاد النظر في الاسم التجاري.

## 7. المصادر
- المشروع: https://github.com/moain2028/scam2027 (200، main c761778) · README.md · AGENTS.md · docs/90-handoff/STATUS.json · docs/40-plan/01-ROADMAP.md · docs/10-research/00-LMS-BENCHMARK.md · docs/60-adr/0002, 0004, 0007, 0008 · app/prisma/schema.prisma · app/src/lib/auth/permissions.ts · تشغيل محلي 2026-09-23 (PostgreSQL 16، pnpm test 181/181، typecheck 0، build 28 مساراً).
- البدائل: الروابط أعلاه (MoodleCloud 200 · Instructure /canvas 200 و/canvas/pricing 404 · openedx.org 202) + GitHub API لـ moodle/moodle، instructure/canvas-lms، openedx/openedx-platform — كلها بتاريخ 2026-09-23.

## EN summary
scam2027 targets universities and colleges that want a course and assessment platform serving several institutions from one deployment, in Arabic RTL and mobile-first. Real alternatives (accessed 2026-09-23): Moodle / MoodleCloud (GPL-3, hosted plans $170–$2,140 USD per year for 50–750 users), Canvas LMS (AGPL-3, institutional pricing by quote only, free tiers for individual teachers) and Open edX (AGPL-3, free self-hosted via Tutor, managed providers unpriced). Its positioning is database-level tenant isolation — PostgreSQL Row Level Security on 30 tables with an app user that cannot bypass it — plus 114 dotted permissions, an Arabic mobile-first shell and documentation that updates with every PR (181 tests passing, 0 type errors). Gaps, stated plainly: 24 of 65 roadmap tasks (37%) — no assessment, assignments, grading, AI, SIS import, full PDPL, MFA, SSO or LTI yet; CI is a template only; no live URL or documented university; license undecided; README points to another account; the product name reads as "scam" in English.
