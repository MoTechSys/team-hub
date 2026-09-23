grocery-ledger | كاتب المحتوى | 2026-09-23 | v1

# دفتر البقالة — بحث وتحليل (Research & positioning)

تاريخ البحث: 2026-09-23 (بحث ويب + قراءة صفحات Play Store بـ hl=en والتحقق من استجابتها 200). كل ادعاء عن مشروعنا من tech.md/brief؛ كل ادعاء عن منافس من صفحته.

## 1. من يشتري هذا؟
- المستخدم النهائي: صاحب بقالة أو محل صغير بجهاز واحد ومستخدم واحد، يسجّل الديون ورقياً والإنترنت عنده غير مضمون (brief «المشكلة»، «لمن يفيد»).
- المشتري في المحفظة: من يريد من معين تطبيقاً محلياً (offline-first) لمحل/نشاط صغير — نفس النمط قابل للتكرار لأنواع محلات أخرى.
- حجم الفئة: لا رقم موثّق لدينا لعدد البقالات الصغيرة في اليمن/المنطقة — «يُستكمل». مؤشر غير مباشر: فئة «دفتر ديون/محاسبة محل بلا إنترنت» العربية على Play Store مزدحمة بتطبيقات صغيرة (1K–5K تنزيل لكل منها) — طلب موجود ومجزّأ.

## 2. المنافسون والبدائل على Google Play (وصول 2026-09-23)
| # | التطبيق | التنزيلات | التقييم | آخر تحديث | إعلانات / مشتريات | ماذا يقدّم (من صفحته) | الرابط |
|---|---|---|---|---|---|---|---|
| 1 | Cashier App: Offline POS (Softwex) | 1K+ | 4.3 | 2026-09-22 | لا / لا | «dead simple and powerful POS… Works offline» — باركود بالكاميرا أو قارئ HID، بيع بالوحدة أو الوزن، بيع نقدي أو بالدين مع دفتر لكل عميل، ضرائب، خصومات، طباعة إيصالات | https://play.google.com/store/apps/details?id=com.softwex.apps.deadsimple_pos |
| 2 | سريع — محاسبة وفواتير وديون | 5K+ | — | 2026-08-28 | لا / نعم | «يعمل بالكامل دون إنترنت (Offline-First)» — فواتير، ديون، مخزون، نقاط بيع؛ عربي/تركي/إنجليزي؛ ميزات مدفوعة | https://play.google.com/store/apps/details?id=com.accounting_book.quick_accounting_pro |
| 3 | Accounting — Sales POS (Offline) | 1K+ | 4.2 | 2026-08-24 | نعم / نعم | «offline accounting and POS app designed for small shop owners, grocery stores, mini markets» — منتجات، مبيعات، فواتير، ديون، مخزون، أرباح | https://play.google.com/store/apps/details?id=com.shmool.salesmanager |
| + | دفتري — دفتر الحسابات والديون | 1K+ | — | 2026-08-09 | لا / نعم | دفتر ديون وعملاء، أقساط، كشوف PDF، مشاركة واتساب؛ «Works offline with secure cloud backup»؛ PDF ونسخ Drive بالاشتراك | https://play.google.com/store/apps/details?id=com.madasuite.daftari |
| + | UBee: Offline POS & Inventory | 10+ | — | 2026-07-14 | نعم / نعم | «offline-first POS and inventory tracker»؛ إنجليزي/فرنسي/عربي RTL؛ فواتير PDF | https://play.google.com/store/apps/details?id=com.raystate.ubee |
| + | دفتر — محاسبة وديون وعملاء | 10+ | — | 2026-05-09 | لا / لا | للتجار الصغار في الأردن والعالم العربي؛ دخل/مصروف/ديون؛ يعمل بدون إنترنت؛ مزامنة سحابية للمشتركين | https://play.google.com/store/apps/details?id=net.dafter.app |

الأرقام (تنزيلات/تقييم/تاريخ) كما ظهرت في صفحات Play Store بتاريخ 2026-09-23 وتتغيّر مع الوقت. لم يظهر تقييم لبعض التطبيقات (عدد مراجعات غير كافٍ).

## 3. التموضع
ماذا يقول المنافس: الفئة تنقسم إلى «دفاتر ديون» بسيطة (دفتري، دفتر) تسجّل الدين والدفع وتصدّر كشفاً، و«نقاط بيع أوفلاين» (Cashier App، Sales POS، سريع، UBee) تجمع البيع والمخزون والديون. أغلبها يموّل نفسه بالإعلانات أو الاشتراك، ويضع النسخ الاحتياطي أو PDF خلف الدفع، والعربية فيه ترجمة واجهة لا أساساً محاسبياً.

أين يتفوّق دفتر البقالة (من tech.md/brief فقط):
- محاسبة كاملة لا دفتر ديون: نقطة بيع + عملاء + موردون + سندات مرقّمة + ورديات بتقرير Z + تقرير ربح شهري — في تطبيق واحد بلا خادم.
- عربي في العمق: تفقيط عربي للمبلغ على السندات، إيصال 80 مم وفاتورة A4 وسند A5 — لا مجرد ترجمة.
- نزاهة الدفاتر: append-only، لا تُحذف حركة، تُعكس بقيد مقابل — ميزة لم يذكرها أي منافس في صفحته.
- النسخ الاحتياطي اليومي التلقائي (آخر 7) وتصدير PDF/Excel من كل شاشة مجاناً — بينما دفتري/دفتر يضعانها خلف اشتراك.
- بلا إعلانات، بلا حساب، بلا اشتراك؛ 157 اختباراً وصفر تحذيرات؛ مفتوح المصدر.

أين يتأخر (صريح): غير منشور على Play Store (APK من GitHub فقط) مقابل 1K–5K تنزيل للمنافسين · جهاز واحد ومستخدم واحد بلا مزامنة ولا سحابة (Cashier App وسريع يدعمان أكثر) · لا ضرائب/VAT ولا بيع بالوزن (Cashier App يدعمهما) · لا واتساب لكشوف العملاء (دفتري يدعمه) · لقطات التسويق ببيانات فارغة.

## 4. الكلمات المفتاحية
AR (10): تطبيق محاسبة بقالة · دفتر ديون البقالة · نقطة بيع بدون إنترنت · برنامج كاشير للمحلات الصغيرة · سندات قبض وصرف · تقرير الوردية Z · نسخة احتياطية يومية · تطبيق محاسبة أندرويد عربي · باركود بالكاميرا · تطبيق Flutter محاسبة
EN (10): offline POS app · grocery store accounting app · debt ledger app Arabic · small shop cashier app · barcode POS Android · cash shift Z report · append-only ledger · offline-first Flutter app · Hive Flutter accounting · receipt payment voucher app

## 5. ثلاث زوايا محتوى
1. «الدفتر الذي لا يُمحى»: لماذا تُعكس الحركة بقيد مقابل بدل حذفها — زاوية ثقة/محاسبة لأصحاب المحلات والمحاسبين.
2. «بلا إنترنت، بلا حساب، بلا اشتراك»: مقارنة صريحة مع تطبيقات الفئة التي تضع النسخ الاحتياطي خلف الدفع — زاوية تسويقية مباشرة.
3. «157 اختباراً لبقالة»: كيف تُبنى أداة صغيرة بجودة منتج (محرك محاسبة مختبَر، Z report، تفقيط) — زاوية للمهندسين والعملاء المحتملين.

## 6. الفجوات (بلا تجميل)
تقنياً: مستخدم واحد وجهاز واحد بلا مزامنة · لا ضرائب ولا بيع بالوزن · اسم المستودع (mohanad-web-app-2) لا يطابق المنتج وله نسخة أقدم (mohanad-web-app) تحتاج أرشفة · README ينشر رقم هاتف المطوّر · اللقطات من نسخة ويب فارغة لا من جهاز حقيقي.
تسويقياً: غير موجود على Play Store · لا أرقام مستخدمين · لا فيديو تشغيل حقيقي · «الشريحة أفراد» بينما المنتج للمحلات الصغيرة (يُراجَع التصنيف مع مدير المنتج).

## 7. المصادر
- المشروع: https://github.com/MoTechSys/mohanad-web-app-2 (200) · https://github.com/MoTechSys/mohanad-web-app-2/releases/tag/v2.2.1 · portfolio-hub/01-projects/grocery-ledger/{brief.ar.md, brief.en.md, tech.md, links.md}
- المنافسون: روابط الجدول، صفحات Play Store بـ hl=en بتاريخ 2026-09-23.

## EN summary
Grocery Ledger targets single-device small grocers with unreliable internet. Play Store competitors (accessed 2026-09-23): Softwex's Cashier App: Offline POS (1K+, 4.3★, barcode + debt ledger + tax/weight), Saree (5K+, offline-first, Arabic/Turkish/English, IAP), Accounting — Sales POS (1K+, 4.2★, ads + IAP), plus debt-notebook apps Daftari (1K+, PDF/backup behind subscription), UBee (10+) and Daftar (10+). Grocery Ledger's edge: full accounting not just a debt notebook, Arabic amount-in-words and print formats, append-only ledgers, free daily backups and PDF/Excel export, no ads/account/subscription, 157 tests. Gaps: not on Play Store, single user/device, no tax or weight-based sales, repo naming, empty-data screenshots.
