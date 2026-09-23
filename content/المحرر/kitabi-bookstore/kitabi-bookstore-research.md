kitabi-bookstore | المحرر | 2026-09-23 | final

# كِتابي — بحث وتحليل (Research & analysis)

## 1. من يشتري هذا وحجم الفئة
كِتابي ليس منتجاً يُباع؛ هو مشروع مقرر مفتوح المصدر يخاطب شريحة «طلاب». المستفيد المباشر: طالب تطوير تطبيقات الهاتف يبحث عن مثال Flutter كامل (متجر، سلة، مصادقة، بيانات محلية) يعمل من أول تشغيل. المستفيد غير المباشر: مدرّس المقرر أو المشرف الذي يريد مرجعاً للمستوى المتوقّع. حجم الفئة بالأرقام: يُستكمل — لا مصدر موثوق لعدد طلاب Flutter العرب، ولا نقدّره.

الفئة التجارية المقابلة (متاجر الكتب العربية على Android) كبيرة وواضحة، وهي التي نقارن بها بصرياً ووظيفياً أدناه لا تنافسياً.

## 2. ثلاثة بدائل حقيقية (Google Play — تاريخ الوصول 2026-09-23)
| التطبيق | المطوّر | ما يفعله | مؤشرات Play | الرابط |
|---|---|---|---|---|
| Abjjad: Audiobooks & Ebooks (أبجد) | Abjjad US | 30,000+ كتاب إلكتروني وصوتي عربي، قراءة واستماع دون اتصال، اشتراك | 1M+ تنزيل · 4.6 (27.5K مراجعة) · آخر تحديث 2026-09-22 | https://play.google.com/store/apps/details?id=com.abjjad.app |
| Rufoof: eBooks & Audiobooks (رفوف) | Yaqut | «أكبر مجموعة كتب عربية إلكترونية وصوتية، 30,000+ عنوان»، اشتراك | 1M+ تنزيل · 4.3 (30.9K مراجعة) · آخر تحديث 2026-08-16 | https://play.google.com/store/apps/details?id=co.yaqut.app |
| nwf.com (نيل وفرات) | neelwafurat | متجر كتب ورقية عبر الإنترنت («Biggest Online Book store») مع شحن | 10K+ تنزيل · آخر تحديث 2022-12-09 | https://play.google.com/store/apps/details?id=com.neelwafurat.nwf |

ملاحظة منهجية: الأرقام كما تعرضها صفحات Play Store يوم الوصول؛ التقييم غير ظاهر في صفحة nwf.com فلم يُدرج.

## 3. التموضع
ما يقوله المنافس: «آلاف الكتب»، «اقرأ واستمع بلا حدود»، «الأكبر». كلها منتجات تجارية بخوادم واشتراكات وكتالوجات ضخمة.

أين يقف كِتابي (من tech.md فقط):
- لا خادم: كل البيانات في SQLite محلية تُبذر عند أول تشغيل — المنافسون الثلاثة يعتمدون على خوادم وحسابات سحابية.
- كود مفتوح قابل للقراءة والبناء: APK جاهز + BUILD_GUIDE + ARCHITECTURE — لا شيء من ذلك متاح في التطبيقات التجارية بطبيعتها.
- دورة متجر كاملة في ≈6,900 سطر Dart و17 شاشة: حجم يستطيع طالب أن يقرأه كله.
- قابل للتحقق: 31/31 اختباراً + فحص بصري آلي لـ 23 شاشة/حالة.
- ما لا نقوله: لا نقارن بالكتالوج (24 كتاباً مقابل 30,000+) ولا بالتنزيلات؛ الغرض مختلف.

الجملة التموضعية: «ما تحصل عليه من متجر كتب عربي تجاري، مفتوحاً وقابلاً للتشغيل على جهازك، لتتعلّم كيف يُبنى».

## 4. الكلمات المفتاحية
AR (10): مشروع Flutter كامل · تطبيق متجر كتب Flutter · مشروع مقرر تطوير تطبيقات الهاتف · SQLite في Flutter · sqflite مثال · Provider Flutter مثال · تطبيق عربي RTL Flutter · سلة تسوق Flutter · مشروع تخرج Flutter · تطبيق أندرويد بلا خادم
EN (10): Flutter bookstore app · Flutter e-commerce example · Flutter SQLite offline app · sqflite CRUD example · Provider state management example · Flutter RTL Arabic app · Flutter cart and coupons · Flutter student project · Flutter course project source code · offline-first Flutter app

## 5. ثلاث زوايا محتوى
1. «متجر كامل بلا خادم»: كيف تبني تصفحاً وسلة وطلبات ومصادقة على SQLite محلية فقط — للطلاب الذين يخافون تكلفة الـ backend.
2. «زر الرجوع الذي لا يخرج من التطبيق»: IndexedStack + Navigator لكل تبويب + PopScope؛ درس صغير من مشكلة يعرفها كل مبتدئ Flutter.
3. «كيف تعرف أن مشروعك مكتمل؟»: 31 اختباراً في 4 ملفات وفحص بصري لـ 23 حالة — قائمة تحقق لمشروع مقرر.

## 6. الفجوات (صريحة)
تقنياً:
- لا رابط حي ولا نسخة ويب منشورة؛ المعاينة تتطلّب بناء APK أو `flutter build web` محلياً.
- بوابة الترخيص تقرأ license.json من GitHub — نقطة اعتماد خارجية في تطبيق يُسوَّق بأنه «بلا خادم»؛ تحتاج توضيحاً أو إزالة.
- 9 commits فقط؛ التاريخ التطويري قصير مقارنة بالتوثيق.
- الكتالوج ثابت (seed) ولا يُحدَّث؛ لا مزامنة ولا دفع حقيقي (محاكاة متجر).
تسويقياً:
- نسب المشروع غير محسوم (README ينسبه للطالب علي عبده يحيى؛ دور معين غير معلن) — يمنع النشر باسم معين حتى يقرّر.
- اسم المستودع Flutter-Native-App-033 غير دالّ ويضعف الاكتشاف في البحث.
- لا فيديو ديمو منشور ولا صفحة تعريفية؛ الحزمة الحالية تسدّ هذا جزئياً.

## Summary (EN)
Kitabi is an open-source Flutter course project, not a commercial product. We compared it with three real Arabic bookstore apps on Google Play (Abjjad 1M+, Rufoof 1M+, nwf.com 10K+; accessed 2026-09-23). Positioning: everything a commercial Arabic bookstore does, open and runnable on your own device with no server, so students can learn how it is built. Strengths come only from tech.md: local SQLite seeded on first launch, 17 screens, 31/31 tests, ready APK, build and architecture docs. Gaps: no live demo, a remote license gate that contradicts the "no server" story, a short commit history, unresolved attribution (student vs. developer), and a non-descriptive repository name.

## المصادر
- brief.ar/en.md، tech.md، links.md — `01-projects/kitabi-bookstore/` في moain2028/portfolio-hub.
- README — https://github.com/moain2028/Flutter-Native-App-033 (HTTP 200، 2026-09-23).
- Abjjad — https://play.google.com/store/apps/details?id=com.abjjad.app (2026-09-23).
- Rufoof — https://play.google.com/store/apps/details?id=co.yaqut.app (2026-09-23).
- nwf.com — https://play.google.com/store/apps/details?id=com.neelwafurat.nwf (2026-09-23).
