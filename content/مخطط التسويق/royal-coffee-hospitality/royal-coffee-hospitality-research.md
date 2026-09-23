royal-coffee-hospitality | مخطط التسويق | 2026-09-23 | v1 (بحث ويب مؤرَّخ — تاريخ الوصول لكل رابط 2026-09-23)

# القهوة الملكية — بحث وتحليل السوق والتموضع

## 0. تصحيح تموضع (مهم)
`DIAFA_ANALYSIS.md` داخل المستودع يحلّل موقعَي keifaldiafa.com وasoulaldiafa.com مقارنةً. **كلاهما من مشاريع معين العباسي نفسه** (keif-aldiafa-web وosoul-aldiafa في portfolio-hub) — فالوثيقة تحليل داخلي لأعمال سابقة يُبنى عليه، لا تحليل منافسين. لا يُقدَّم أيٌّ منهما كمنافس في أي نص، وتُقرأ الوثيقة كـ«تعلّم من مشروعَين سابقَين في نفس الفئة». (ظهر الخلط في بحث osoul سابقاً — مصحَّح هنا.)

## 1. من يشتري هذا وما حجم الفئة؟
- المشتري: صاحب مؤسسة قهوجيين/صبابين وضيافة مناسبات في السعودية — نشاط صغير يعتمد على واتساب والحجز الهاتفي، وعميله النهائي يبحث «قهوجيين + مدينة» قبل مناسبة (عرس، عزاء، مؤتمر) بأيام، ويتصفح من الجوال.
- حجم الفئة: 1.7 مليون سجل تجاري نشط في السعودية بنهاية الربع الثالث 2025 (منشآت عبر Arab News، https://www.arabnews.com/startups/biban-2025-monshaat-report-highlights-surge-in-sme-growth-funding-2621496). سوق القهوة السعودي: 36 مليون كوب يومياً و8,900+ مقهى ذي علامة (CoffeeZone / The Hotel Show Saudi Arabia 2026، https://www.thehotelshowsaudiarabia.com/coffeezone/ ومنشوراتها؛ رقم ترويجي للمعرض — يُستخدم كمؤشر لا كإحصاء رسمي).
- ما يستخدمه هذا المشتري فعلاً: مواقع WordPress بقوالب عامة، أو حسابات إنستغرام بلا موقع. عينة حقيقية من نتائج «قهوجيين وصبابين الرياض» (2026-09-23): qahwajie.com — WordPress، 134 KB HTML، 27 صورة، 11 سكربت؛ al-mostakbl.com — WordPress، 237 KB HTML، 16 سكربت، زمن استجابة 2.2 ث؛ qahwadirn.com — خلف تحدّي Cloudflare (403 للزاحف). وثلاث نتائج من السبع حسابات/ريلز إنستغرام برقم هاتف في العنوان.

## 2. ثلاثة بدائل/منافسون حقيقيون (بروابط)
| البديل | ما هو | ما قِيس/ما يقوله | الرابط | تاريخ الوصول |
|---|---|---|---|---|
| qahwajie.com («قهوجيين الرياض») | موقع مؤسسة قهوجيين وصبابين بالرياض | WordPress (generator 7.0.5) · 27 صورة و11 سكربت في الرئيسية · «خدمة 24 ساعة» | https://qahwajie.com/ | 2026-09-23 |
| al-mostakbl.com (المستقبل) | موقع خدمات ضيافة ومناسبات بالرياض | WordPress (7.1.2) · 237 KB HTML · 16 سكربت · TTFB+تحميل 2.17 ث من الخادم | https://al-mostakbl.com/ | 2026-09-23 |
| WordPress كفئة | الخيار الافتراضي لمواقع هذه الفئة | 43.5% من كل المواقع · 61.7% من المواقع ذات CMS (W3Techs عبر Kinsta) | https://kinsta.com/wordpress-market-share/ · https://w3techs.com/technologies/overview/content_management | 2026-09-23 |

الموقع الأصلي المُستبدَل: alqahwaalmalakiya.com (يعمل، عنوان «القهوة الملكية | قهوجي وصبابين قهوة في جدة والرياض والدمام ومكة والطائف»، 73 KB HTML) — هو النسخة القديمة لنفس النشاط لا منافس.

## 3. التموضع: ماذا يقولون، وأين يتفوّق المشروع (من tech.md/README فقط)
| المحور | مواقع الفئة (WordPress) | القهوة الملكية |
|---|---|---|
| الحمولة | HTML 134–237 KB + 11–16 سكربت + إضافات | Worker مضغوط 52.6 KB · CSS 17.7 · JS 4.8 · صفر مكتبات |
| الهوية | قالب عام + شعار | نظام تصميم Onyx + Gold خاص، 49 أيقونة SVG يدوية، حركة سينمائية على transform/opacity |
| RTL | ترجمة فوق قالب LTR | RTL أصيل: inset-inline، أرقام عربية-هندية، عزل اتجاه الهاتف |
| البحث المحلي | صفحات مدن مكرّرة النص | 10 مدن بنصوص محلية + صفحات خدمة×مدينة، 13 بانياً JSON-LD، 73/73 عنواناً ≤70 حرفاً |
| الحجز | نموذج بريدي/إضافة | نموذج → رسالة واتساب منسّقة بلا خادم |
| الصيانة | تحديثات ووردبريس وإضافات، قاعدة بيانات | لا خادم ولا قاعدة بيانات؛ التحديث من data.ts |
| التحرير لغير المطوّر | **يتفوّق المنافس**: لوحة تحكم | يحتاج تعديل TypeScript ونشراً |
| النشر | حي ومفهرس | **غير منشور** (README) |
| المحتوى الحقيقي | أرقام هواتف وصور فعلية | placeholders وصور مولّدة |

ادعاء التموضع الآمن: «موقع ضيافة فاخر بحمولة 52 كيلوبايت — يُصيَّر على الحافة ويُدار من ملف واحد». لا «أسرع موقع قهوجيين» (لا قياس Core Web Vitals منشور بعد).

## 4. الكلمات المفتاحية
AR (10): قهوجيين وصبابين · موقع خدمات ضيافة · تصميم موقع قهوجي · ضيافة مناسبات السعودية · موقع فاخر للمناسبات · حجز عبر واتساب · صفحة لكل مدينة · موقع سريع على الجوال · موقع بدون ووردبريس · Cloudflare Workers عربي
EN (10): Saudi hospitality website · qahwaji coffee service site · Hono Cloudflare Workers SSR · edge-rendered marketing site · luxury RTL web design · no-framework TypeScript website · per-city local SEO pages · WhatsApp booking form · JSON-LD LocalBusiness Arabic · lightweight luxury website

## 5. ثلاث زوايا محتوى
1. «الفخامة بـ 52 كيلوبايت»: كيف يبدو الموقع سينمائياً بلا مكتبة واحدة — Hono على الحافة، حركة على transform/opacity فقط. الجمهور: مطوّرون وأصحاب أنشطة فاخرة. (مقال + كاروسيل)
2. «RTL أصيل لا ترجمة»: تشابك الخطوط العربية وline-height، letter-spacing الذي يفكّ الوصلات، أرقام الهاتف — دروس من الجولة الخامسة في README. الجمهور: مصمّمون ومطوّرون عرب. (منشور LinkedIn/X)
3. «73 صفحة من ملف واحد»: لماذا يحتاج نشاط القهوجيين صفحة لكل مدينة ولكل خدمة×مدينة، وكيف تُدار بلا CMS. الجمهور: أصحاب أنشطة ضيافة متعددة المدن. (ريل + بانر)

## 6. الفجوات (صريحة)
تقنياً:
- غير منشور: لا نطاق، لا Core Web Vitals حقيقية، لا فهرسة. الأرقام كلها أحجام بناء لا قياسات ميدانية.
- README متضارب عبر 5 جولات (7→73 صفحة، 21→204 صورة، 11→13 بانياً)؛ سكربتات QA المذكورة غير موجودة في المستودع فلا يُعاد تشغيلها.
- 12.8 MB صور في المستودع؛ لا اختبارات وحدات ولا CI.
- خط Amiri من Google Fonts هو الطلب الخارجي الوحيد لكنه ثقيل نسبياً (DIAFA_ANALYSIS §5 يشير إلى 318 KB خطوط في موقع سابق بنفس الخط) — لم يُقَس هنا.
- التحرير يحتاج مطوّراً.
تسويقياً:
- بيانات تواصل placeholders وصور مولّدة: لا يمكن نشر أي تصميم يُظهر رقماً أو يزعم «صوراً حقيقية من مناسباتنا» (عنوان المعرض داخل الموقع).
- أرقام الهيرو (+6500 مناسبة، 24/7) ومراجعات REVIEWS محتوى عرض.
- لا اسم عميل مسموح؛ العميل الفعلي (القهوة الملكية) هو النشاط نفسه — يُذكر اسم الموقع كمنتج لا كشهادة.
- الاسم «Royal Coffee» عام جداً في البحث الإنجليزي؛ يُرفق دائماً بـ hospitality/Saudi.

## 7. المصادر
- المشروع: https://github.com/moain2028/royal-coffee-hospitality (README + الكود، تحقق 2026-09-23) · tech.md · brief.ar/en.md · DIAFA_ANALYSIS.md (داخلي)
- المنافسون: https://qahwajie.com/ · https://al-mostakbl.com/ · https://qahwadirn.com/ (403) · https://alqahwaalmalakiya.com/ (الأصل)
- حصص السوق: https://kinsta.com/wordpress-market-share/ · https://w3techs.com/technologies/overview/content_management
- السعودية: https://www.arabnews.com/startups/biban-2025-monshaat-report-highlights-surge-in-sme-growth-funding-2621496 · https://www.thehotelshowsaudiarabia.com/coffeezone/
- Hono: https://hono.dev/docs/ («small, simple, and ultrafast web framework built on Web Standards»؛ hono/tiny < 14KB) · https://blog.cloudflare.com/the-story-of-web-framework-hono-from-the-creator-of-hono/

---
## EN summary
Positioning correction first: DIAFA_ANALYSIS.md compares keifaldiafa.com and asoulaldiafa.com — both are Moain's own earlier projects, so the document is an internal benchmark, not competitor analysis. The real buyer is a small Saudi coffee-service/hospitality business; real alternatives found in live search (2026-09-23) are WordPress sites such as qahwajie.com (WP 7.0.5, 27 images, 11 scripts) and al-mostakbl.com (WP 7.1.2, 237 KB HTML, 16 scripts, 2.2 s), plus Instagram accounts with a phone number in the title; WordPress runs 43.5% of all websites. Royal Coffee's defensible edges (from tech.md/README only): a 52.6 KB gzipped Hono worker with zero runtime libraries, a bespoke Onyx + Gold system with 49 hand-drawn icons, native RTL, 73 pages from one data file with 13 JSON-LD builders, and a serverless WhatsApp booking flow. Honest gaps: not deployed (no real Core Web Vitals), placeholder contacts and generated imagery, a README with contradictory rounds and missing QA scripts, 12.8 MB of images in the repo, no tests, and no non-developer editing. Safe claim: "a luxury hospitality site in 52 KB, rendered at the edge and managed from one file" — never "the fastest qahwaji site".
