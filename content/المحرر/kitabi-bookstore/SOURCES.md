kitabi-bookstore | المحرر | 2026-09-23 | final

# kitabi-bookstore-project-pack-v2 — مصدر كل نص ورقم وصورة

## النصوص على التصاميم (A + B + C)
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| الاسم | كِتابي | Kitabi | brief.ar/en.md (العنوان) |
| السطر التعريفي | متجر كتب كامل بـ Flutter يعمل بلا خادم | A complete Flutter bookstore with no server | brief (العنوان)، مختصر بحذف «مشروع مقرر» وهي في التاج |
| التاج | مشروع مقرر · Android | Course project · Android | brief (العنوان) + tech.md «Flutter/Android» |
| الوصف | 24 كتاباً في 6 تصنيفات، بحث وتصفية، سلة مع كوبونات، مفضلة، تقييمات، وتتبّع الطلبات. كل البيانات في SQLite محلية تُبذر عند أول تشغيل. | (المقابل) | brief §الحل / Solution |
| 24 كتاباً / books | ✓ | ✓ | tech.md §الأرقام — lib/data/seed.dart |
| 17 شاشة / screens | ✓ | ✓ | tech.md §الأرقام — docs/ARCHITECTURE.md §2 |
| 31 اختباراً ناجحاً / passing tests | ✓ | ✓ | tech.md §الأرقام — docs/RELEASE_NOTES.md v1.1.0 · test/ (31/31) |
| v1.1.0 | ✓ | ✓ | tech.md — pubspec.yaml 1.1.0+2 |
| تاجات التقنيات | Flutter 3.35 · Dart 3.9 · Material 3 · Provider · SQLite · RTL | نفسها | tech.md §التقنيات (Flutter 3.35.4 / Dart 3.9.2 / Material 3 / Provider / sqflite / RTL) |
| الدعوة | المستودع مفتوح — اسألني | The repository is open — ask me | brief §تواصل / Contact |
| شارة الشريحة | طلاب | Students | تكليف المهمة + 02-brand/README.md (#8B5CF6) |
| الرابط في الفوتر | github.com/moain2028/Flutter-Native-App-033 | نفسه | تكليف المهمة؛ HTTP 200 بتاريخ 2026-09-23 |
| النسخة بشعار | «معين العباسي» نص فقط | "Moain Al-Abbasi" wordmark only | project-pack-standard-v2.md §A |
| بطاقة «رقم واحد»: 0 خادم / servers | ✓ | ✓ | brief «يعمل بلا خادم» + tech.md §الحالة «لا رابط حي (تطبيق Android)» |
| الكاروسيل: «Provider لأربع حالات: الجلسة، الكتالوج، السلة، المفضلة» و«زر الرجوع خطوة بخطوة داخل كل تبويب» | ✓ | ✓ | tech.md §التقنيات (Provider: Session/Catalog/Cart/Favorites · IndexedStack + Navigator + PopScope) + brief |
| الكاروسيل 4: «APK جاهز في المستودع، دليل بناء، توثيق معمارية وسجل تطوير» | ✓ | ✓ | brief §النتيجة / Result |
| الريل: 6 لقطات نصية | ✓ | ✓ | كلها من الصفوف أعلاه؛ لا رقم جديد |

## الصور
- اللقطات حقيقية من `01-projects/kitabi-bookstore/screenshots/` (390×844 بدقة 2x، من بناء الويب المحلي، حساب تجريبي للتصوير فقط):
  - mobile-04-book-detail.png — تفاصيل كتاب
  - mobile-06-book-list.png — قائمة كتب مع تصفية السعر
  - mobile-07-cart.png — السلة مع حقل الكوبون
- **أغلفة الكتب داخل اللقطات (وعناوينها وأسعارها) هي بيانات seed من التطبيق نفسه (lib/data/seed.dart)، لا صور حقيقية لكتب منشورة ولا بيانات مبيعات.** (بطلب مدير المنتج 2026-09-23)
- لا اسم شخص على أي لقطة مستخدمة؛ استُبعدت لقطات الحساب/الملف الشخصي/الإدارة التي تُظهر اسماً وبريداً تجريبيَّين.
- لا لقطة مولّدة. لا صورة مخزون.
- الريلان (AR/EN) مبنيان من إطارات مولّدة على خلفية الهوية + اللقطات الثلاث أعلاه فقط؛ 21 ث، 1080×1920، 30fps، بلا شعار، **بلا موسيقى** (تُضاف مقطوعة بلا حقوق عند النشر — لم أُرفق مقطوعة حتى لا أُدخل ملفاً بلا ترخيص موثّق).

## الشروحات والبحث والنصوص (D–F)
- explainer.ar/en: كل جملة من brief.ar/en.md أو tech.md أو README المستودع (كما نقله tech.md). 396 / 499 كلمة.
- research.md: المنافسون الثلاثة من صفحات Google Play بتاريخ الوصول 2026-09-23 (الروابط داخل الملف). حجم الفئة: «يُستكمل» — لا مصدر.
- copy.ar/en: من brief + tech؛ الأطوال داخل الحدود (مقيسة)؛ مختومة.
- **يُستكمل قبل النشر (من brief وtech):** نسب المشروع — README ينسبه للطالب علي عبده يحيى ودور معين غير معلن؛ حُذف الاسمان من كل النصوص التسويقية حتى يقرّ معين.

## الهوية
`02-brand/README.md` عبر `02-brand/scripts/brand.py`؛ النص الخافت الصغير #A3B1C0 (تحديث 2026-09-23). المساحة الآمنة 12% من العرض خالية في نسخة nologo.

## إعادة التوليد
`python3 kit.py` (التصاميم والإطارات) ثم `./reel.sh ar|en <out.mp4>`. يعتمد على ~/repos/portfolio-hub + Pillow (raqm) + ffmpeg.
