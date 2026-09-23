hafawa-riyadh-events | مخطط التسويق | 2026-09-23 | v1 (بحث ويب مؤرَّخ — تاريخ الوصول لكل رابط 2026-09-23)

# حَفاوة — بحث وتحليل السوق والتموضع

## 1. من يشتري هذا وما حجم الفئة؟
- المشتري: صاحب نشاط محلي صغير (ضيافة، حفلات، مناسبات، خدمات منزلية) يريد موقعاً يظهر في البحث المحلي ويفتح بسرعة على الجوال — لا شركة تقنية. يقرر بالسعر والسرعة وسهولة التحديث، ونادراً بالتقنية.
- حجم الفئة في السعودية: 1.7 مليون سجل تجاري نشط بنهاية الربع الثالث 2025، والمنشآت الصغيرة والمتوسطة توظّف أكثر من 8.4 مليون شخص (منشآت عبر Arab News، 2025-11-05، https://www.arabnews.com/startups/biban-2025-monshaat-report-highlights-surge-in-sme-growth-funding-2621496).
- ما يستخدمه هذا المشتري اليوم عالمياً: WordPress في 43.5% من كل المواقع (61.7% من المواقع ذات CMS معروف)، Shopify 4.6%، Wix 3.2%، Squarespace 2.2% (Kinsta نقلاً عن W3Techs، https://kinsta.com/wordpress-market-share/؛ المصدر الأصلي https://w3techs.com/technologies/overview/content_management). أي أن البديل الفعلي لموقع حَفاوة ليس «موقعاً آخر مخصصاً» بل قالب WordPress أو منشئ مواقع.
- المعيار الذي نقيس به: Google تعتبر FCP «جيداً» عند 1.8 ثانية أو أقل عند المئين 75 (web.dev، https://web.dev/articles/fcp)، وLCP جيداً عند 2.5 ث (https://web.dev/articles/lcp). حَفاوة: FCP 324 مللي ثانية — أقل من خُمس الحد.

## 2. ثلاثة بدائل (بروابط حقيقية)
| البديل | ما هو | ما يقوله عن نفسه | الرابط | تاريخ الوصول |
|---|---|---|---|---|
| WordPress + قالب حفلات | CMS مفتوح المصدر (PHP) مع قوالب وإضافات؛ الخيار الافتراضي لأغلب مواقع الأنشطة الصغيرة | يشغّل 43.5% من المواقع؛ مرونة وإضافات لا حدود لها | https://wordpress.org/ · https://kinsta.com/wordpress-market-share/ | 2026-09-23 |
| Wix | منشئ مواقع مستضاف (drag-and-drop) بواجهة عربية | «أنشئ موقعاً بلا كود»؛ 3.2% من كل المواقع | https://www.wix.com/ | 2026-09-23 |
| Squarespace | منشئ مواقع مستضاف يركّز على القوالب الجمالية للأنشطة الخدمية | قوالب مصممة للمطاعم والمناسبات؛ 2.2% من كل المواقع | https://www.squarespace.com/ | 2026-09-23 |

بديل رابع في نفس فئة حَفاوة التقنية: مولّدات المواقع الثابتة (Astro، Hugo، Eleventy) — CloudCannon: «أسرع وأأمن وأسهل صيانة من WordPress» (https://cloudcannon.com/blog/the-top-five-static-site-generators-for-2025-and-when-to-use-them/). حَفاوة يذهب أبعد: مولّد مخصص بلا أي اعتمادية.

## 3. التموضع: ماذا يقولون، وأين يتفوّق حَفاوة (من tech.md/README فقط)
| المحور | WordPress / Wix / Squarespace | حَفاوة |
|---|---|---|
| السرعة | تعتمد على القالب والإضافات والاستضافة؛ صفحات بمئات الكيلوبايت وعشرات الطلبات شائعة | الرئيسية 201 كيلوبايت في 13 طلباً، FCP 324 ms، CLS 0.003 (README، مقيسة) |
| الصور | تحسين عبر إضافات أو خدمة الاستضافة | خط صور مدمج: AVIF → WebP → JPEG بأحجام متعددة + LQIP، وفر 86% |
| التحديث | لوحة تحكم لكل صفحة؛ إضافة حي = صفحة جديدة يدوياً | سطر في data.py يعيد بناء 32 صفحة + sitemap بأمر واحد |
| البحث المحلي | إضافات SEO عامة | JSON-LD LocalBusiness بـ 24 حياً في areaServed + كتالوج عروض + 24 صفحة حي |
| الجودة | فحص يدوي أو أداة خارجية | audit.py مدمج: تباين 15/15 AA، صفر روابط مكسورة، لا تجاوز أفقي |
| الصيانة والأمن | تحديثات إطار وإضافات مستمرة؛ قاعدة بيانات | لا خادم تطبيقات، لا قاعدة بيانات، 4.17 MB / 127 ملفاً |
| سهولة التحرير لغير المطوّر | **يتفوّق المنافسون بوضوح**: واجهة تحرير بصرية | يحتاج تعديل ملف Python وتشغيل أمر — لا لوحة تحكم |
| النشر | مستضاف وحي فوراً | **غير منشور على نطاق عام** (README/tech.md) |

ادعاء التموضع الآمن: «موقع محلي يُقاس بالمللي ثانية — يُحدَّث من ملف واحد» — لا «بديل WordPress».

## 4. الكلمات المفتاحية
AR (10): تصميم موقع شركة ضيافة · موقع تعهّد حفلات الرياض · موقع سريع للجوال · تحسين سرعة الموقع · موقع بدون ووردبريس · موقع ثابت HTML · SEO محلي الرياض · صفحة لكل حي · ضغط الصور AVIF · تصميم مواقع للمشاريع الصغيرة
EN (10): static site for small business · event catering website Riyadh · fast mobile website · Core Web Vitals FCP under 1 second · no-framework HTML website · Python static site generator · local SEO district pages · AVIF WebP image pipeline · WCAG AA small business site · WordPress alternative for local business

## 5. ثلاث زوايا محتوى
1. «حذفتُ الإطار فصار الموقع أسرع خمس مرات من حد Google»: قصة القرار المعماري بالأرقام — مقال + كاروسيل. الجمهور: مطوّرون وأصحاب أنشطة يتابعون التقنية.
2. «صورك تكلّفك عملاء»: من 24.4 إلى 3.37 ميجابايت — كيف يعمل خط AVIF/WebP وماذا يعني للعميل على شبكة 4G — ريل + منشور IG. الجمهور: أصحاب مطاعم وضيافة وحفلات.
3. «صفحة لكل حي»: لماذا يحتاج النشاط المحلي 24 صفحة لا صفحة واحدة، وكيف تُدار من ملف واحد — منشور LinkedIn + بانر. الجمهور: أصحاب أنشطة متعددة المناطق ومسوّقون محليون.

## 6. الفجوات (صريحة)
تقنياً:
- غير منشور على نطاق عام: كل أرقام الأداء من تشغيل محلي، ولا يمكن لعميل أو Google قياسها بنفسه. هذه الفجوة الأولى.
- لا لوحة تحكم: التحديث يحتاج تعديل ملف Python وتشغيل أمر — ميزة للمطوّر، عائق لصاحب النشاط.
- لا اختبارات وحدات؛ التدقيق عبر audit.py فقط (tech.md).
- المستودع الأصلي خاص؛ النسخة العامة على moain2028 تحتاج توضيح أيّهما المرجع.
تسويقياً:
- لا اسم عميل ولا شهادة ولا أرقام أعمال (الزيارات، الحجوزات) — أرقام الهيرو (520+ مناسبة، 4.9) محتوى عرض لا يُستخدم.
- الأسعار في الباقات بيانات عرض؛ لا تُذكر إلا بتأكيد معين.
- لا فيديو تعريفي ولا رابط حي (links.md: يُستكمل) — الريل في هذه الحزمة يعوّض جزئياً.

## 7. المصادر
- المشروع: https://github.com/moain2028/hafawa-riyadh-events (README، تحقق 2026-09-23) · 01-projects/hafawa-riyadh-events/tech.md · brief.ar/en.md · case-study.ar/en.md · links.md
- حصص السوق: https://w3techs.com/technologies/overview/content_management · https://kinsta.com/wordpress-market-share/
- المعايير: https://web.dev/articles/fcp · https://web.dev/articles/lcp
- السعودية: https://www.arabnews.com/startups/biban-2025-monshaat-report-highlights-surge-in-sme-growth-funding-2621496 · http://www.monshaat.gov.sa/en/monshaat-reports
- البدائل: https://wordpress.org/ · https://www.wix.com/ · https://www.squarespace.com/ · https://cloudcannon.com/blog/the-top-five-static-site-generators-for-2025-and-when-to-use-them/

---
## EN summary
Hafawa's buyer is a small local business owner (hospitality, events), not a tech company; the real alternative is a WordPress template or a hosted builder — WordPress runs 43.5% of all websites, Wix 3.2%, Squarespace 2.2% (W3Techs via Kinsta). Saudi Arabia had 1.7 million active commercial registrations by Q3 2025 (Monsha'at via Arab News). Against Google's "good" FCP threshold of 1.8 s, Hafawa's measured 324 ms is more than 5× faster; its defensible edges (from README/tech.md only) are the integrated AVIF/WebP pipeline (86% lighter), one-file updates rebuilding 32 pages, LocalBusiness JSON-LD with 24 districts, and a built-in audit (15/15 AA, zero broken links). Honest gaps: not published on a public domain, no visual editor for non-developers, no unit tests, no client name or business metrics, prices are display data. Positioning to use: "a local site measured in milliseconds, updated from one file" — never "a WordPress alternative".
