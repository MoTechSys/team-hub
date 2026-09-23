electricity-billing-flutter | المصمم | 2026-09-23 | draft

# electricity-billing-flutter — Technical Sheet

- **Repo:** moain2028/electricity-billing-flutter (public — استُنسخ بلا مصادقة 2026-09-23). pubspec name `motech_billing` v1.1.0+2. معرّف الحزمة `com.abbasisoft.billing`.
- **Primary language / stack:** Dart 3.9 / Flutter 3.35.4 · Riverpod 2.6 · Drift 2.31 (SQLite محلي؛ على الويب عبر sqlite3.wasm + drift_worker.js) · go_router 17 · pdf 3.12 + printing 5.14 · fl_chart · Kotlin (طبقة MediaStore أصلية) (المصدر: pubspec.yaml، android/app/src/main/kotlin).
- **Problem:** محطة توليد كهرباء أهلية تُصدر فواتير استهلاك للمشتركين يدوياً؛ تحتاج تطبيق جوال يعمل بلا إنترنت، يحفظ البيانات في الجهاز فقط، ويُخرج فاتورة PDF **مطابقة للمستند الرسمي الأصلي** (README «القاعدة الحاكمة»، docs/INVOICE_FORENSICS.md §1).
- **Solution / core features:** تطبيق أندرويد أصلي (وواجهة ويب للمعاينة): مشتركون، فاتورة جديدة بحساب تلقائي (استهلاك = الحالية − السابقة؛ القيمة = الاستهلاك × سعر الوحدة؛ الإجمالي = القيمة + خدمات + متأخرات؛ الصافي = الإجمالي − المدفوع) وتفقيط عربي، أرشيف مع فلاتر (الكل/صادرة/مسودة/ملغاة)، معاينة/طباعة/مشاركة PDF، إعدادات الشركة، نسخ احتياطي JSON تصدير/استيراد، شاشة ترخيص بـ SHA-256، حفظ في مجلد عام `Documents/فواتير الكهرباء/` عبر MediaStore. الفاتورة: كل قياس مشتق من شبكة مرجعية 1024px وارتفاع الصفحة مشتق من آخر عنصر؛ الألوان مستخرجة من bill.docx (0000FF ورد 31 مرة).
- **Architecture notes:** `lib/app` (theme, router) · `lib/core` (app_info مصدر واحد للحقيقة، database/tables 3 جداول، providers، services/public_storage، utils، widgets) · `lib/features/{about,dashboard,invoices,onboarding,settings,subscribers}` 10 شاشات · `android/.../PublicStoragePlugin.kt` + `MainActivity.kt` (MethodChannel). `test/pdf_render_probe.dart` مِسبار يُخرج فاتورة حقيقية إلى PDF للفحص بكسلياً؛ `tools/verify_invoice.py` أداة تحقق.
- **Status:** beta/داخلي — v1.1.0 (2026-09-01)، بلا رابط تحميل عام مؤكَّد (CHANGELOG يحيل على روابط تحميل لكل إصدار — لم أفحص روابط خارجية).
- **Last commit:** 2026-09-01 (`git log -1`) · 8 commits كلها 2026-09-01.
- **Live URL:** none (تطبيق أندرويد؛ واجهة الويب للمعاينة تُبنى محلياً — بُنيت هنا بنجاح).

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| Tests | **14/14 passed** | `flutter test` هنا 2026-09-23 (`All tests passed!`) — يطابق README |
| flutter build web --release | **نجح** (34.8 s) | سجل البناء المحلي |
| Screens | **10** | `ls lib/features/*/*_screen.dart \| wc -l` (splash, license, dashboard, subscribers, subscriber_form, invoice_form, invoice_archive, invoice_preview, settings, about) |
| Routes | 10 GoRoute | `grep -c "GoRoute(" lib/app/router.dart` |
| Drift tables | **3** (Subscribers · Invoices · Settings) | `grep -n "extends Table" lib/core/database/tables.dart` |
| Invoice columns | 23 | tables.dart سطر 39–66 |
| Dart files / LOC | 31 ملفاً · **7,379** سطراً (بلا `.g.dart` المولَّد) | `find lib -name '*.dart' -not -name '*.g.dart' \| xargs cat \| wc -l` |
| Kotlin LOC | 183 (ملفان) | `find android -name '*.kt' \| xargs wc -l` |
| invoice_pdf.dart | 894 سطراً · 19 ثابت `_X` + 17 ثابت `_Y` مشتقة · 52 استدعاء `_r()` | wc -l · grep |
| Page size | A4 أفقي 297 mm × ارتفاع مشتق (**841.89 × 444.54 pt** في الفاتورة المولَّدة) | `pdfinfo` على PDF المِسبار |
| Invoice colors | `0000FF` عنوان ومبلغ (ورد 31 مرة في bill.docx) · `FCD5B4` ترويسة الجدول | docs/INVOICE_FORENSICS.md §2 · invoice_pdf.dart:189,197 |
| Font boost | ×1.16 | invoice_pdf.dart:205 |
| Dependencies | 19 runtime + 4 dev | pubspec.yaml |
| minSdk | 24 (افتراضي Flutter 3.35) | build.gradle.kts يستخدم `flutter.minSdkVersion` → FlutterExtension.kt = 24 |
| Version | 1.1.0 (versionCode 2) · CHANGELOG: 1.0.0 → 1.1.0 | pubspec · CHANGELOG.md |
| APK size | 65 MB → ~10 MB لكل معمارية | README «تقليص حجم الحزمة» — **ادعاء README، لم أبنِ APK هنا (لا Android SDK)**؛ لا يُعرض كرقم مقاس |
| Fonts bundled | 6 ملفات: AmiriInvoice 291/296 KB · Plex Arabic 236/247 KB · TinosLatin 20/21 KB | `du -b assets/fonts/*` |
| Web build | 35 MB (main.dart.js 4.5 MB) | `du -sh build/web` |
| Docs | README + CHANGELOG + 2 في docs/ | `ls docs` |
| Repo size | 3.5 MB (بلا .git/build) | `du -sh` |
| Cloud services | 0 | README «الخدمات السحابية: لا يوجد»؛ pubspec لا يحوي http/dio/firebase |
| Users / stations | يُستكمل | غير موثّق |

## ملاحظات التنظيف / Cleanup notes
- **README وapp_info.dart يحويان اسم شخص كاملاً ورقم واتساب ودومين** (صفحة «المطوّر والتواصل» وتذييل الدرج) → لا يظهر أي منها على تصميم أو نص؛ لقطات about/الدرج استُبعدت من الحزمة.
- CHANGELOG يذكر اسم مشترك كمثال لاسم ملف — لا يُستخدم.
- الشعار `assets/images/logo.png` (درع أصفر/كحلي بعامل) — أصله غير موثّق في المستودع؛ يظهر داخل اللقطات كجزء من الواجهة، ولا يُقدَّم كأصل صمّمته.
- `android/app/build.gradle.kts.bak` ملف احتياطي في الشجرة — يُحذف.
- الاختبارات وحدوية فقط (حسابات، تفقيط، أسماء ملفات)؛ لا اختبار واجهة ولا CI.
- pub outdated: 62 حزمة لها إصدارات أحدث غير متوافقة مع القيود.
- اسم pubspec `motech_billing` مقابل اسم التطبيق «فواتير الكهرباء» وبادج الباكج `abbasisoft` — ثلاثة أسماء لمشروع واحد.
- بوابة الترخيص: bypass للمعاينة عبر localStorage `flutter.app_licensed=true` — للتصوير فقط، ليس ثغرة (SharedPreferences على الويب = localStorage بحكم التصميم).
