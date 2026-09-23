almutahassil-site | متخصص SEO | 2026-09-23 | v2 · بحث وتحليل (بحث ويب مؤرَّخ: 2026-09-23)

# almutahassil-site — بحث وتحليل السوق والتموضع
English summary at the end.

## 1. من يشتري هذا؟
المشروع ذو وجهَين، ولكل وجه مشترٍ:
- **الموقع كواجهة لنظام «المتحصل»:** جمهوره صناديق التحصيل، مؤسسات التمويل الأصغر، شركات التوزيع ذات المندوبين، والجمعيات ذات الاشتراكات الدورية — كما يسمّيها `faq.html` (السؤال 1) و`about.html` («لمن هذا النظام؟»)، في اليمن أولاً (العملة ر.ي، رقم يمني في نموذج التواصل، صنعاء في العنوان).
- **النمط كخدمة قابلة للبيع (شريحة شركات):** أي شركة منتجات/خدمات تريد موقعاً تعريفياً عربياً فاخراً + لوحة تجريبية تُظهر منتجها، بهوية بصرية كاملة، يُستضاف على أي خادم ملفات بلا إطار ولا تبعيات (brief «لمن يفيد»، README «المواصفات»).
- حجم الفئة: لا رقم مؤرّخ موثوق لعدد صناديق/شركات التحصيل الميداني في اليمن أو المنطقة — **يُستكمل**.

## 2. المنافسون/البدائل الحقيقية (تاريخ الوصول 2026-09-23)
### أ) أنظمة تحصيل/أقساط ميدانية تعرض نفسها بموقع تسويقي (منافسو «المنتج» الذي يعرضه الموقع)
| البديل | ماذا يقول عن نفسه | السعر المعلن | الرابط |
|---|---|---|---|
| **CobrApp** (كولومبيا/عالمي، AR/EN/ES) | تطبيق محصّلين ميداني: مسار يومي، سند مطبوع Bluetooth 58/80 مم، يعمل offline بالكامل، نسخ سحابي | مجاني حتى 20 عميلاً · Individual 10.99$/شهر · Team 5 19.99$/شهر · Team 10 34.99$/شهر · Enterprise 49.99$/شهر (خصم 26–47% سنوياً) | https://cobrapp.co/en/debt-collection-app · https://cobrapp.co/en/pricing |
| **أقساط (aksat-ms)** (عربي، أندرويد/iOS/ويندوز) | إدارة أقساط وديون وخزنة ومخزن؛ 22 جدولاً يعمل بلا إنترنت؛ طباعة حرارية؛ مساعد ذكي؛ تنبيهات واتساب؛ تجربة 14 يوماً | غير معلن على الصفحة الرئيسية (تجربة مجانية 14 يوماً؛ اشتراك شهري/سنوي) | https://aksat-ms.com/ |
| **سَنَد SANAD** (مصر، سحابي) | إدارة أقساط وتحصيل: عقود، متأخرات، خزينة، إشعارات واتساب | 250 جنيهاً مصرياً/شهر يشمل كل الموديولات | https://sanadims.site/ |
| (أيضاً: **Credgenics CG Collect** — تطبيق تحصيل ميداني مؤسسي بتتبّع جغرافي وoffline، بلا سعر معلن — https://www.credgenics.com/cg-collect-field-debt-collections · **نظام حصِّل / ECOLOR** السعودية — https://ecolor.com.sa/hassel/ · **ضمان dhman.io**) |

### ب) بدائل «الأداة» — بناء موقع تعريفي بلوحة تجريبية بغير كتابة الكود يداً
| البديل | ماذا يقول | ملاحظة |
|---|---|---|
| قالب SaaS جاهز (Webflow/Framer/WordPress theme) | صفحة هبوط في دقائق | اشتراك شهري بالدولار، LTR أصلاً ويُعرَّب، الأيقونات من مكتبات عامة لا هوية خاصة، اللوحة التجريبية غالباً صورة ثابتة لا تفاعل |
| موقع بإطار (Next.js/Nuxt) | مكوّنات وSEO مدمج | يحتاج build وNode وتبعيات وصيانة؛ زائد عن الحاجة لثماني صفحات ثابتة |

## 3. التموضع: ماذا يقول البديل، وأين يتفوّق مشروعنا (من README/tech.md فقط)
| ما يقوله البديل | ما عندنا (المصدر) |
|---|---|
| CobrApp/أقساط/سند: تطبيق بالاشتراك، موقعه التسويقي عام الطابع | موقع بهوية بصرية كاملة موثّقة في `brand/BRAND.md` (ألوان، خطوط، شعار، أيقونات، نبرة) — و10 أيقونات 3D بأسلوب واحد بدل مكتبة عامة (README «الأيقونات») |
| مواقع المنافسين: صور ثابتة للمنتج | لوحة إدارة **تفاعلية** تجريبية: عدّادات، رسم أعمدة SVG، فرز وتصفية — كلها كود محلي بلا مكتبة رسوم (`demo.js`) |
| قوالب LTR مُعرَّبة | RTL من الجذر (`dir="rtl" lang="ar"`)، أرقام هندية في كل عدّاد، خط عربي مضبوط بأوزان محددة (README، BRAND.md §2) |
| اعتماد على إطار وbuild | 0 إطار · 0 build · 0 تبعيات · سكربتان محليان؛ يُستضاف على أي خادم ملفات (tech.md) |
| — | إمكانية وصول: 180 سمة aria، `prefers-reduced-motion`، مانيفست PWA، JSON-LD (Organization + SoftwareApplication) (tech.md) |

**نقطة صدق:** البدائل في (أ) منتجات حقيقية تعمل وتُباع وبأسعار معلنة؛ موقعنا يعرض نظاماً لا نملك دليلاً عاماً على تشغيله (تطبيق «المتحصل» نفسه ليس في الحساب العام). البدائل في (ب) أسرع للإطلاق ولها CMS. مشروعنا **بلا رابط حي اليوم**، وبلا اختبارات، وعدّاداته وأرقام لوحته بيانات عرض (tech.md «Cleanup notes»).

## 4. الكلمات المفتاحية
**عربي (10):** موقع تعريفي لنظام تحصيل · تصميم موقع عربي RTL فاخر · لوحة إدارة تجريبية للموقع · موقع HTML بلا إطار · نظام تحصيل ميداني · سداد فوري للخزنة المركزية · سند إلكتروني بترقيم متسلسل · أيقونات 3D لتطبيق مالي · دليل هوية بصرية عربي · موقع بلا تبعيات سريع
**English (10):** static marketing site no framework · Arabic RTL landing page design · demo dashboard on marketing site · field collection system website · collection and settlement software · vanilla JS dashboard sortable tables · 3D squircle icon set · brand guidelines Arabic fintech · zero-dependency HTML site · PWA manifest static site
(بلا أحجام بحث — لا أداة بيانات هنا؛ الاختيار من صياغات ظهرت في نتائج البحث المؤرّخة ومن محتوى الموقع الفعلي.)

## 5. ثلاث زوايا محتوى مقترحة
1. **«8 صفحات، صفر تبعيات»** — لماذا لا يحتاج الموقع التعريفي إطاراً، وكيف يعطي HTML/CSS/JS خام أداءً وملكية كاملة (README «المواصفات»، tech.md).
2. **«لوحة تشرح المنتج بنفسها»** — كيف تُبنى لوحة تجريبية تفاعلية ببيانات عرض مُعلَنة بلا مكتبة رسوم، ولماذا الإفصاح عن «بيانات افتراضية» يزيد الثقة (`demo.js`، `demo.html` التنبيه).
3. **«تدقيق SEO تقني لموقع ثابت جميل»** — خمس فجوات يكشفها فحص عشر دقائق: `og:image` يشير لملف غير موجود (`assets/og.png` مقابل `brand/og.png`)، sitemap يغطي 3 من 8 صفحات، canonical/robots/OG على رابط معطّل، JSON-LD على الرئيسية فقط، تعارض «عشر وحدات»/9 — مع قائمة إصلاح قبل النشر على دومين دائم (tech.md «Cleanup notes»). (بديل احتياطي: مسار جودة الأيقونات المولّدة — README «مسار جودة الأيقونات»، `fix_icons.py`.)

## 6. الفجوات (صريحة)
- **تقنية:** لا رابط حي (الرابط في README/canonical/sitemap/robots/OG معطّل) · لا اختبارات آلية ولا CI · commitان بتاريخ واحد (2026-08-11) · `og:image` → `assets/og.png` غير موجود (الفعلي `brand/og.png`) · sitemap يغطي 3 من 8 صفحات · JSON-LD على الرئيسية فقط · `docs/00-INDEX.md` يحوي مساراً محلياً ومستودعاً خاصاً 404.
- **محتوى:** تعارض «عشر وحدات» (نص index.html) مع 9 في الكود (`app.js` FEATURES و`features.html` «تسع») — المعتمد 9 بقرار مدير المنتج 2026-09-23 · «٤٥+ قدرة» مقابل 48 بنداً · عدّادات الرئيسية وأرقام changelog (4.2→1.1 ث، 68%، 72 ساعة) ادعاءات منتج غير قابلة للتحقق من الكود.
- **تسويقية/خصوصية:** اسم شخص كامل كاسم الجهة في README/BRAND/عناوين الصفحات/JSON-LD — لا يُنقل · هاتف وبريد نموذجيان في contact · الأيقونات مولّدة بالذكاء الاصطناعي (يُفصَح) · لا عملاء موثّقون · لا نسخة إنجليزية من الموقع.

## 7. المصادر
- README.md · brand/BRAND.md · docs/00-INDEX.md · index/demo/features/faq/about/contact/changelog.html · app.js · demo.js — https://github.com/moain2028/almutahassil-site (commitان 2026-08-11)
- tech.md الخاص بهذا التسليم (أوامر التحقق المحلي 2026-09-23)
- CobrApp: https://cobrapp.co/en/debt-collection-app · https://cobrapp.co/en/pricing (2026-09-23)
- أقساط: https://aksat-ms.com/ (2026-09-23)
- سَنَد: https://sanadims.site/ (2026-09-23)
- Credgenics: https://www.credgenics.com/cg-collect-field-debt-collections · ECOLOR حصِّل: https://ecolor.com.sa/hassel/ · ضمان: https://dhman.io/ (2026-09-23)

---
## English summary
Two audiences: collection funds, microfinance, distributors with field agents and subscription associations (the site's own FAQ/about pages, Yemen first), and — as a sellable pattern — any company wanting a premium Arabic marketing site with an interactive demo dashboard and a full brand system, hosted anywhere. Market size: no dated figure — "to be completed".
Alternatives (accessed 2026-09-23): products — CobrApp (free ≤20 customers; $10.99–49.99/month), Aksat (Arabic, offline, 14-day trial, price not listed), SANAD (EGP 250/month), plus Credgenics CG Collect, ECOLOR Hassel, Dhman; tools — SaaS templates (Webflow/Framer/WordPress) and framework sites (Next/Nuxt).
Positioning (from README/tech.md only): fully documented brand system and a consistent 10-icon 3D set; an interactive demo dashboard rather than static product shots; RTL from the root with Eastern numerals; 0 framework / 0 build / 0 dependencies; 180 aria attributes, reduced-motion support, PWA manifest, JSON-LD. Honest gaps: no live URL, no tests, two same-day commits, broken og:image, sitemap covers 3 of 8 pages, module-count inconsistency, demo counters and changelog claims unverifiable, personal name used as the entity name, AI-generated icons (disclosed), Arabic-only.
