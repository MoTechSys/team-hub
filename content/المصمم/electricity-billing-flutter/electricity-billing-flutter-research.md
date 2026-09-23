electricity-billing-flutter | المصمم | 2026-09-23 | draft

# فواتير الكهرباء (Flutter) — بحث وتحليل السوق

## English summary
electricity-billing-flutter is the native Android member of a three-project billing series (PWA #5, PWA v2, and this Flutter app). Target buyer: small private power stations and landlords/utilities that bill metered consumption and need an official-looking Arabic PDF invoice from a phone, offline. Alternatives fall in three groups — meter-reading apps on Google Play (Smart Meter Reading & Billing, 50K+ downloads), SaaS utility billing (Kimans, MyRead Pro) and open-source invoicing suites (Invoice Ninja 10.1K★, Dolibarr 7.6K★). None of the checked alternatives advertises an offline-only, on-device model with a pixel-verified invoice template; ours does (measured: 14/14 tests, 0 cloud services, 36 derived layout constants). Gaps: no automated UI tests, no CI, unverified APK size claim, personal contact data baked into the app, a single-tenant licence gate, and no public download confirmed.

## 1. من يشتري هذا وحجم الفئة
- **المشتري:** محطات توليد كهرباء أهلية (مولدات تجارية تبيع الطاقة لمشتركين بعدّادات) وملّاك عقارات/مرافق صغيرة يوزّعون فواتير استهلاك؛ السياق العربي RTL بعملة «ريال» (المصدر: `SettingKeys.defaults`، brief سلسلة electricity-billing-pwa).
- **حاجة القرار:** إنترنت غير مضمون في موقع العمل، فاتورة ورقية/PDF رسمية بصيغة ثابتة، ومبلغ مكتوب بالعربية (README «القاعدة الحاكمة»، tech.md).
- **حجم الفئة:** لا أملك رقماً موثّقاً لعدد المحطات الأهلية أو حجم سوق برمجيات فوترتها في السوق المستهدف — **يُستكمل**؛ لا يُعرض رقم بلا مصدر.
- **إشارة سوقية مقاسة:** تطبيق Smart Meter Reading & Billing على Google Play يعلن **50K+** تنزيلاً (فُحص 2026-09-23 05:27 UTC) — دليل على وجود طلب فردي/صغير على قراءة العدّادات والفوترة من الهاتف.

## 2. المنافسون / البدائل (فُحصت مباشرة 2026-09-23 ~05:27 UTC)
| # | البديل | الرابط | ما يقوله | ما قِسته / لاحظته |
|---|---|---|---|---|
| 1 | Smart Meter Reading & Billing (Android) | https://play.google.com/store/apps/details?id=io.github.ttyniwa.kenshin | «Read tenant water, electric & gas meters. Auto-calculate bills, send invoices.» | 50K+ تنزيل؛ الصفحة تذكر PDF واشتراكاً مدفوعاً؛ لا ذكر لـ offline في وصف المتجر؛ لا عربي/RTL معلن |
| 2 | Kimans Utility Billing Software | https://kimans.com/product/billing-software/ | «per-unit calculation, branded PDF invoices, email and SMS delivery, multi-tariff» | SaaS ويب؛ يعتمد إرسال بريد/SMS (أي اتصال)؛ لا ذكر لـ offline؛ تسعير بالدولار |
| 3 | MyRead Pro (Utilivisor) | https://www.utilivisor.com/myread-pro.html | «accurate manual meter readings … accurate tenant invoices – without any new hardware» | تطبيق قراءة عدّادات + فوترة مستأجرين؛ لا ذكر لـ PDF أو offline في الصفحة |
| 4 | Invoice Ninja (مفتوح المصدر) | https://github.com/invoiceninja/invoiceninja | «source-available invoice, quote, project and time-tracking app built with Laravel» | 10,104★؛ يحتاج خادماً (Laravel) — بديل عام لا يعرف العدّادات |
| 5 | Dolibarr ERP/CRM (مفتوح المصدر) | https://github.com/Dolibarr/dolibarr | «modern software package to manage your company … invoices, orders, stocks» | 7,646★؛ تطبيق ويب PHP يحتاج خادماً — بديل ERP عام |

(المصدر: `curl` لكل صفحة + regex على العنوان/الوصف/النجوم؛ ملاحظة: البديلان 4 و5 بدائل «فوترة عامة» لا «فوترة عدّادات»، أُدرجا لأن مشترياً صغيراً قد يقارن بهما.)

## 3. التموضع
**ما يقوله المنافسون:** «حساب تلقائي»، «فواتير PDF بعلامتك»، «إرسال بريد/SMS»، «متعدد التعرفة» — كلها سحابية أو تعتمد الاتصال، والفاتورة قالب عام قابل للتخصيص لا نسخة مطابقة لمستند رسمي محدد.

**أين يتفوّق مشروعنا (من tech.md فقط):**
- **بلا إنترنت وبلا سحابة:** 0 خدمة سحابية (pubspec لا يحوي http/dio/firebase)؛ SQLite محلي عبر Drift؛ النسخ الاحتياطي ملف JSON يملكه المستخدم.
- **الفاتورة مطابقة لمستند رسمي محدد لا قالباً عاماً:** شبكة مرجعية 1024px، 36 ثابتاً مشتقاً، ارتفاع صفحة مشتق، ألوان مستخرجة من bill.docx، وفحص من داخل PDF لا من صورة (INVOICE_FORENSICS.md).
- **عربي أصيل:** تفقيط عربي مُختبر، خط Amiri يغطي Presentation Forms-B، RTL كامل.
- **حفظ في مجلد عام يبقى بعد إزالة التطبيق** عبر طبقة Kotlin/MediaStore بلا طلب صلاحية على Android 10+.
- **مُختبر:** 14/14 اختبار وحدوي ناجح هنا.

**أين يتفوّقون علينا (صراحة):** لديهم توزيع عام (متجر/SaaS) وتسعير ودعم؛ لدينا لا رابط تحميل مؤكَّد. لديهم إرسال الفاتورة بالبريد/SMS وتعرفات متعددة؛ لدينا مشاركة يدوية وسعر وحدة واحد افتراضي. لديهم تعدّد مستخدمين/مستأجرين؛ تطبيقنا جهاز واحد بترخيص واحد.

## 4. الكلمات المفتاحية
**AR (10):** تطبيق فواتير كهرباء · نظام فواتير مولدات أهلية · فاتورة استهلاك كهرباء PDF · قراءة العداد وحساب الفاتورة · تطبيق أندرويد يعمل بلا إنترنت · تفقيط المبلغ بالعربية · فوترة مشتركين عدّادات · نسخة احتياطية محلية للفواتير · تطبيق Flutter عربي · فاتورة مطابقة للأصل
**EN (10):** offline electricity billing app · meter reading invoice app Android · Flutter Drift offline app · private power station billing · Arabic PDF invoice generator · amount in words Arabic · utility billing without server · pixel-perfect PDF invoice Flutter · MediaStore public folder Flutter · local-first billing app

## 5. ثلاث زوايا محتوى
1. **«لماذا الفاتورة لا يجوز أن تكون "تقريباً" مثل الأصل»** — قصة القياسات المشتقة: كيف تُحوَّل شبكة 1024px إلى نقاط، ولماذا استُخرج اللون من ملف docx بدل تقديره بالعين، ودرس «لا تشخّص من صورة».
2. **«تطبيق بلا سحابة في 2026»** — ماذا تكسب المحطة الصغيرة من بيانات لا تخرج من الجهاز (خصوصية، لا اشتراك، يعمل في الموقع بلا شبكة) وماذا تخسر (لا مزامنة، جهاز واحد).
3. **«ثلاث نسخ لمنتج واحد»** — PWA ← PWA v2 ← Flutter: متى تنتقل من الويب إلى أندرويد أصلي (الحفظ في مجلد عام، الطباعة، الأداء)، بأرقام مقاسة من المستودعات الثلاثة (تُستكمل عند اكتمال حزم الشقيقين).

## 6. الفجوات (صريحة)
- **لا رابط تحميل عام مؤكَّد** (CHANGELOG يحيل على روابط لم أفحصها؛ README لا يذكر متجراً).
- **بيانات اتصال شخصية مضمّنة في الكود** (`app_info.dart`: اسم، واتساب، دومين) وتظهر في الدرج وصفحة about — تُفصل إلى إعدادات أو تُزال قبل أي نشر.
- **ادعاء حجم APK (65→~10 MB) غير مقاس هنا** — لا Android SDK في بيئة الفحص؛ يبقى ادعاء README.
- **الاختبارات وحدوية فقط** (14): لا اختبار واجهة، لا اختبار لطبقة Kotlin، لا CI.
- **62 حزمة قديمة** بحسب `pub get` (إصدارات أحدث غير متوافقة مع القيود).
- **ترخيص جهاز واحد بـ SHA-256 ثابت** في الكود — يمنع الاستخدام العرضي لكنه ليس نظام ترخيص.
- **ثلاثة أسماء** للمشروع (`motech_billing` · «فواتير الكهرباء» · `com.abbasisoft.billing`) + ملف `.bak` في الشجرة.
- **سعر وحدة واحد** — لا شرائح تعرفة؛ لا إرسال فاتورة بالبريد/SMS (المنافسون يفعلون).
- **الشعار داخل التطبيق** أصله غير موثّق في المستودع.
- الوثائق ممتازة في الفاتورة والتخزين، لكن لا وثيقة معمارية عامة ولا دليل مستخدم.

## المصادر
- المستودع: https://github.com/moain2028/electricity-billing-flutter (README، CHANGELOG، docs/INVOICE_FORENSICS.md، docs/STORAGE_AND_PERMISSIONS.md، pubspec.yaml، lib/) — الأرقام في tech.md بأوامرها.
- البدائل: الروابط الخمسة في الجدول — فُحصت بـ curl 2026-09-23 ~05:27 UTC.
- بحث ويب: «electricity billing app offline android small utility subscribers meter reading invoice PDF» 2026-09-23.
- المشروع الشقيق: portfolio-hub/01-projects/electricity-billing-pwa/tech.md (للسياق فقط).
