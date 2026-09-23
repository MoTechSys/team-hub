s-acm | مخطط التسويق | 2026-09-23 | v1 (بحث ويب مؤرَّخ — تاريخ الوصول لكل رابط 2026-09-23)

# S-ACM — بحث وتحليل السوق والتموضع

## 1. من يشتري هذا وما حجم الفئة؟
- المشترون الفعليون لأنظمة إدارة المحتوى/التعلم الأكاديمي هم الجامعات والكليات (أقسام تقنية المعلومات وعمادات التعلم الإلكتروني)، لا الطلاب. الطلاب هم المستخدم النهائي والجمهور الثاني للمشروع كمرجع تقني (مشاريع التخرج).
- حجم الفئة في السعودية: 1.57 مليون طالب وطالبة في التعليم العالي عام 2024 بنسبة التحاق 83.88% في التعليم ما بعد الثانوي (وكالة الأنباء السعودية نقلاً عن اليونسكو، https://www.spa.gov.sa/en/N2550420). تقدير آخر يذكر 2.2 مليون طالب في 2024، 94% منهم في مؤسسات عامة/شبه عامة عددها 29 (University World News, 2026-01-19, https://www.universityworldnews.com/post.php?story=20260119163608138). نعرض الرقمَين معاً ولا نختار بينهما — المنهجيات مختلفة.
- عالمياً: Moodle وحده يسجّل 146,737 موقعاً و527 مليون مستخدم و59 مليون مقرر (https://stats.moodle.org/ — أرقام حية تتغير يومياً).
- في التعليم العالي بأمريكا الشمالية (حسب الالتحاق): Canvas ~50%، D2L Brightspace ~20%، Blackboard ~12%، Moodle ~9% (Cubite نقلاً عن Edutechnica Spring 2025 وOnEdTech، https://cubite.io/blogs/lms-market-share-2026؛ المصدر الأصلي https://edutechnica.com/2025/05/26/lms-data-spring-2025-updates/).
- في السياق السعودي، Blackboard هو النظام الأكثر انتشاراً في الجامعات الحكومية حسب أدبيات بحثية متعددة (مثال: الجامعة السعودية الإلكترونية، https://files.eric.ed.gov/fulltext/EJ1472168.pdf؛ دراسة التحديات والآفاق https://www.researchgate.net/publication/352840371).

الخلاصة: S-ACM لا ينافس Canvas أو Blackboard على عقود الجامعات الكبيرة اليوم — حالته 40–95% وبلا نشر حي. سوقه الواقعي هو (أ) مرجع تقني لطلاب التخرج وأقسام الحاسوب، و(ب) نقطة بداية لكلية أو قسم واحد يريد أداة عربية خفيفة، و(ج) بطاقة إثبات كفاءة لمعين في بناء أنظمة Monorepo كاملة.

## 2. ثلاثة منافسين/بدائل (بروابط حقيقية)

| البديل | ما هو | ما يقوله عن نفسه | الرابط | تاريخ الوصول |
|---|---|---|---|---|
| Moodle | LMS مفتوح المصدر (PHP، GPL-3.0)، الأوسع انتشاراً عالمياً | 146,737 موقعاً · 527M مستخدم · 236+ دولة؛ واجهة عربية متوفرة | https://moodle.org/ · https://stats.moodle.org/ · https://github.com/moodle/moodle (7,425 نجمة · 7,642 fork) | 2026-09-23 |
| Canvas LMS (Instructure) | LMS مفتوح المصدر (Ruby on Rails، AGPL-3.0) بنسخة سحابية تجارية | «مبني في السحابة على تقنية مفتوحة، يتكامل مع 1000+ أداة خارجية»؛ ~50% من التحاق التعليم العالي بأمريكا الشمالية | https://www.instructure.com/canvas · https://github.com/instructure/canvas-lms (6,832 نجمة · 3,028 fork) | 2026-09-23 |
| Open edX | منصة مقررات مفتوحة المصدر (Python/Django + JS، AGPL-3.0) موجّهة للتعليم العالي والمقررات الضخمة | «modular monolith لتأليف وتقديم التعلم عبر الإنترنت»؛ تخصيص عميق في كل طبقة | https://openedx.org/ · https://github.com/openedx/edx-platform | 2026-09-23 |

بدائل إضافية يُسأل عنها عادة: Blackboard Learn (Anthology، تجاري، الأكثر استخداماً في الجامعات السعودية — https://www.blackboard.com/)، وGoogle Classroom (مجاني، 150M+ مستخدم، يغلب في التعليم العام — https://edu.google.com/).

## 3. التموضع: ماذا يقولون، وأين يتفوّق S-ACM (من tech.md وREADME فقط)

| المحور | المنافسون | S-ACM |
|---|---|---|
| اللغة | العربية ترجمة/حزمة لغوية فوق واجهة إنجليزية الأصل | عربي RTL من الأساس، وضع داكن (اللقطات) |
| الصلاحيات | أدوار محددة مسبقاً (Moodle: 8 أدوار افتراضية قابلة للتعديل؛ Canvas: أدوار حساب/مقرر) | 70+ صلاحية على 12 قسماً في 3 مستويات، الأدمن ينشئ الأدوار من الواجهة (README «نظام الصلاحيات») |
| الحزمة التقنية | PHP (Moodle) · Ruby on Rails (Canvas) · Python/Django (Open edX) — أعمار 10–20 سنة | React 19 · TypeScript · Tailwind 4 · Hono · Drizzle · Turborepo — حزمة 2025 (tech.md) |
| الحجم والتشغيل | أنظمة ضخمة تحتاج فريق تشغيل | 13 جدولاً · 14 وحدة API · 19 صفحة — يقرأه طالب في أسبوع (tech.md) |
| النضج | مستقرة، منتشرة، موثّقة، مجتمعات ضخمة | 40–95% حسب المكوّن، بلا نشر حي (README) — **هنا يتفوّق المنافسون بوضوح** |

ادعاء التموضع الآمن: «مرجع عربي حديث ومفتوح لبنية Monorepo بصلاحيات ديناميكية» — لا «بديل Moodle».

## 4. الكلمات المفتاحية
AR (10): نظام إدارة المحتوى الأكاديمي · نظام إدارة التعلم مفتوح المصدر · مشروع تخرج نظام جامعي · نظام صلاحيات ديناميكي · إدارة المقررات الجامعية · رفع ملفات المحاضرات · منصة تعليمية عربية · React مشروع تخرج · Monorepo مشروع تخرج · بديل عربي لأنظمة إدارة التعلم
EN (10): academic content management system · open source LMS alternative · graduation project React 19 · Turborepo monorepo example · dynamic RBAC permissions system · Hono Drizzle PostgreSQL starter · Arabic RTL admin dashboard · university course file management · shadcn/ui dashboard open source · full-stack TypeScript graduation project

## 5. ثلاث زوايا محتوى
1. «70 صلاحية بلا سطر كود إضافي»: كيف تصمّم نظام صلاحيات ديناميكياً (12 قسماً × 3 مستويات) — مقال تقني + كاروسيل. الجمهور: طلاب ومطوّرون.
2. «مشروع تخرج على حزمة 2025»: لماذا React 19 + Hono + Drizzle بدل PHP/Laravel المعتاد في مشاريع التخرج — منشور LinkedIn + ريل. الجمهور: طلاب حاسوب وأساتذة مشرفون.
3. «من مجموعة واتساب إلى نظام»: قصة المشكلة (محتوى متناثر) والحل بلغة غير تقنية — منشور فيسبوك/إنستغرام لأقسام الجامعات. الجمهور: عمادات التعلم الإلكتروني.

## 6. الفجوات (صريحة)
تقنياً:
- لا نشر حي: Vercel يعطي DEPLOYMENT_NOT_FOUND وRailway 404 (tech.md، فحص 2026-09-11). أي منشور بلا رابط تجربة يخسر معظم أثره.
- الخادم 60% والصلاحيات 40%: الميزة المحورية للتسويق (الصلاحيات الديناميكية) غير مكتملة في الخادم.
- ميزات الذكاء الاصطناعي 0% رغم أن الاسم «ذكي» — فجوة بين الاسم والواقع؛ لا نسوّقها كميزة موجودة.
- لا اختبارات مذكورة في README؛ لا CI. المنافسون الثلاثة كلهم بـ CI واختبارات ضخمة.
- ثلاثة مستودعات (s-acm، s-acm-backend، s-acm-frontend) بتداخل — يحتاج توضيحاً أيّها المصدر الحقيقي.
تسويقياً:
- لا اسم عميل/جامعة ولا شهادة استخدام؛ اللقطات على بيانات تجريبية (مُعلَن).
- لا دراسة حالة ولا فيديو تعريفي (links.md: يُستكمل).
- اسم «S-ACM» غير قابل للبحث ويتشابه مع مصطلحات أخرى؛ يُفضّل دائماً إرفاق الوصف الكامل.

## 7. المصادر
- المشروع: https://github.com/moain2028/s-acm (README، تحقق 2026-09-23) · 01-projects/s-acm/tech.md · brief.ar.md · brief.en.md · links.md
- Moodle: https://stats.moodle.org/ · https://moodle.org/ · https://github.com/moodle/moodle · https://docs.moodle.org/en/Standard_roles
- Canvas: https://www.instructure.com/canvas · https://github.com/instructure/canvas-lms
- Open edX: https://openedx.org/ · https://github.com/openedx/edx-platform
- حصص السوق: https://cubite.io/blogs/lms-market-share-2026 · https://edutechnica.com/2025/05/26/lms-data-spring-2025-updates/
- السعودية: https://www.spa.gov.sa/en/N2550420 · https://www.universityworldnews.com/post.php?story=20260119163608138 · https://files.eric.ed.gov/fulltext/EJ1472168.pdf
- Blackboard / Google Classroom: https://www.blackboard.com/ · https://edu.google.com/ · https://blog.google/products-and-platforms/products/education/google-for-education-year-in-review-2025/

---
## EN summary
S-ACM's realistic market is not enterprise LMS contracts (Canvas ~50%, D2L ~20%, Blackboard ~12%, Moodle ~9% of North-American higher-ed enrollment; Blackboard dominant in Saudi public universities). It is (a) a technical reference for graduation-project students, (b) a lightweight Arabic starting point for a single faculty, and (c) proof of Moain's ability to ship a full monorepo. Three named alternatives with links: Moodle (PHP, GPL-3.0, 146,737 sites / 527M users), Canvas LMS (Ruby, AGPL-3.0, ~50% NA higher-ed enrollment), Open edX (Python/Django, AGPL-3.0). S-ACM's defensible edges (from tech.md/README only): Arabic-RTL by design, admin-built dynamic permissions (70+ across 12 sections, 3 levels), and a 2025 stack (React 19, Hono, Drizzle, Turborepo) small enough to read in a week. Honest gaps: no live deployment, backend 60% / permissions 40% / AI 0%, no tests or CI, three overlapping repos, no customer or case study. Positioning claim to use: "a modern, open Arabic reference for a monorepo with dynamic permissions" — never "a Moodle alternative".
