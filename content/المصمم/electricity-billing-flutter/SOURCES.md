electricity-billing-flutter | المصمم | 2026-09-23 | draft

# SOURCES — electricity-billing-flutter project pack v2

المستودع: https://github.com/moain2028/electricity-billing-flutter · commit 9170b0e (2026-09-01) · استُنسخ 2026-09-23. كل الأرقام أُعيد قياسها بأوامر مذكورة في tech.md.

## الأرقام
| الرقم | أين يظهر | المصدر |
|---|---|---|
| 14/14 اختبار ناجح | كل التصاميم، بطاقة الرقم، الريل، الشرح، النصوص | `flutter test` هنا 2026-09-23 → `All tests passed!` (14 test) |
| 10 شاشات | التصاميم، الريل، الشرح، النصوص | `ls lib/features/*/*_screen.dart \| wc -l` = 10 |
| 0 خدمة سحابية | التصاميم، الريل، الشرح، النصوص | pubspec.yaml بلا http/dio/firebase؛ README «الخدمات السحابية: لا يوجد» |
| 3 جداول Drift | كاروسيل 4، الشرح | `grep "extends Table" lib/core/database/tables.dart` = 3 |
| 36 ثابتاً مشتقاً (19 `_X` + 17 `_Y`) | كاروسيل 3، الريل، الشرح، النصوص | python regex على `class _X`/`class _Y` في invoice_pdf.dart |
| 1024px شبكة مرجعية | كاروسيل 3، الريل، الشرح | invoice_pdf.dart `_kRefW = 1024`؛ INVOICE_FORENSICS.md §1 |
| 0000FF ورد 31 مرة · FCD5B4 | كاروسيل 3، الريل، الشرح، النصوص | INVOICE_FORENSICS.md §2؛ invoice_pdf.dart:189,197 |
| 297 mm · 841.89×444.54 pt | tech.md | `_kPageWmm = 297`؛ `pdfinfo invoice-demo.pdf` |
| 7,379 سطر Dart | brief، الشرح | `find lib -name '*.dart' -not -name '*.g.dart' \| xargs cat \| wc -l` |
| v1.1.0 · 8 commits · 2026-09-01 | الشرح، البحث | pubspec · `git log` |
| 62 حزمة قديمة | البحث، الشرح | مخرجات `flutter pub get` |
| 50K+ تنزيل (Smart Meter Reading & Billing) · 10,104★ Invoice Ninja · 7,646★ Dolibarr | البحث | curl على الصفحات 2026-09-23 ~05:27 UTC |
| **غير معروض عمداً:** 65→~10 MB APK | — | ادعاء README لم يُقَس (لا Android SDK هنا) |
| **غير معروض عمداً:** أي عدد مشتركين/محطات/فواتير حقيقية | — | غير موثّق؛ اللقطات ببيانات وهمية |

## النصوص
- «القاعدة الحاكمة»، «كل قياس مشتق ولا يُكتب رقماً سحرياً»، «الألوان لا تُقارَب بالعين»، «لا تشخّص من صورة»: README §الفاتورة + docs/INVOICE_FORENSICS.md §1–4.
- معادلات الفاتورة (استهلاك/قيمة/إجمالي/صافي): `lib/core/utils/invoice_calculator.dart` تعليق الرأس.
- MediaStore/مجلد عام/لا صلاحية على API 29+: README §حفظ الملفات + docs/STORAGE_AND_PERMISSIONS.md.
- اسم الملف = اسم المشترك + التاريخ + رقم الفاتورة: README + CHANGELOG 1.1.0.
- «نسخة أندرويد أصلية من نفس المنتج» (سلسلة فواتير الكهرباء): links.md فقط؛ الشرح لا يقارن بـ #5.
- الدعوة «راسلني / DM me» في nologo (ريل + كاروسيل 5) — draft للمحرر.
- الفجوات (ثلاثة أسماء، .bak، 62 حزمة، لا CI/اختبار واجهة، بيانات اتصال في الكود): tech.md «ملاحظات التنظيف» → research §6.

## الصور
- **18 لقطة** في screenshots/: Playwright Chromium على `flutter build web --release` مخدومة بـ `python3 -m http.server 8766`، جوال 390×844 @2x وديسكتوب 1440×900 @2x، locale ar-SA (`shoot.py`).
- **البيانات وهمية بالكامل:** `demo-backup.json` (8 مشتركين بأسماء مختلقة بلا هواتف، 13 فاتورة، إعدادات الشركة «شركة النموذج — لتوليد الطاقة الكهربائية — بيانات تجريبية») استُورد عبر زر «استيراد نسخة» في التطبيق؛ التفقيط حُسب بدالة التطبيق `numberToArabicWords` نفسها.
- **RUN-NOTES:** بوابة الترخيص تُجاوزت للتصوير بوضع `flutter.app_licensed=true` في localStorage (SharedPreferences على الويب) — للمعاينة فقط.
- **مستبعد عمداً:** لقطات صفحة «المطوّر والتواصل» (/about) والدرج الجانبي — تحوي اسم شخص ورقم واتساب ودومين.
- `invoice-demo.pdf` / `invoice-demo-1.png` (220 dpi): مولَّدة بمِسبار المستودع `test/pdf_render_probe.dart` بعد استبدال بياناته ببيانات وهمية مؤقتاً (أُعيد الملف لأصله، `git status` نظيف). `shot-invoice.png` = نفس الصورة بهامش أبيض 60px.
- `shot-mobile-quad*.png`, `reel-mobile-stack.png`: تركيب 3–4 لقطات جوال حقيقية جنباً إلى جنب/فوق بعض على خلفية Navy — بلا تعديل على المحتوى.
- **الشعار (الدرع الأصفر/الكحلي) داخل لقطات الفاتورة والترويسة:** أصل `assets/images/logo.png` غير موثّق في المستودع؛ يظهر كجزء من الواجهة فقط ولا يُستخدم عنصراً مستقلاً في أي تصميم.
- لا صورة مولّدة بالذكاء الاصطناعي أضفتها أنا؛ أيقونات الواجهة Material Icons.
- الموسيقى: `reel/music.mp3` مولّدة بـ CassetteAI/music-generator 2026-09-23 (30 ث) — بلا حقوق طرف ثالث.

## الهوية
- 02-brand/README.md (portfolio-hub): Navy/Ink/Amber/Sand/Mist + شريحة «شركات» #3B82F6؛ النص الخافت #A3B1C0؛ IBM Plex Sans Arabic / Inter / JetBrains Mono. الأساس بلا شعار؛ نسخة logo = wordmark نصّي «معين العباسي / Moain Al-Abbasi».
- التذييل: github.com/moain2028/electricity-billing-flutter. لا رابط حي (links.md).
