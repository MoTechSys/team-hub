sijilati | صانع الصور | 2026-09-23 | draft

# سِجِل (Sijil) — بحث وتحليل السوق

تاريخ البحث: 2026-09-23 (بحث ويب + قراءة صفحات المنافسين في اليوم نفسه). كل ادعاء عن منافس مأخوذ من صفحته المذكورة؛ كل ادعاء عن سِجِل من tech.md/brief في portfolio-hub.

## 1. من يشتري هذا
- المشتري: صاحب محل صغير في اليمن (بقالة، مطعم، صيدلية) يبيع بالدَّين ويريد «رقماً صحيحاً كل مساء». المستخدم اليومي: العامل، وقد لا يقرأ ولا يكتب. (tech.md المشكلة والشريحة)
- القيد البنيوي للفئة: الإنترنت متاح لـ17.7% فقط من السكان، وAdMob لا يدفع في اليمن، فالنموذج المجاني بالإعلانات غير قابل للتطبيق — لذلك اختار المشروع الترخيص بكود تفعيل دون إنترنت مع تجربة 30 يوماً ومجاني حتى 15 زبوناً. (tech.md المشكلة، الحل)
- حجم الفئة: يُستكمل — لا يوجد رقم موثّق لعدد المحلات المستهدفة في مصادر المشروع، ولا نعرض تقديراً بلا مصدر.

## 2. المنافسون والبدائل (3)
| # | المنافس | السوق واللغة | ماذا يقول عن نفسه | الرابط (وصول 2026-09-23) |
|---|---|---|---|---|
| 1 | Khatabook | الهند؛ لغات هندية | «Digital Ledger, Invoice Creation, Inventory Management, Loans» و«5 Cr+ Businesses»؛ على Google Play: 50M+ تنزيل، 591K تقييم، يحوي إعلانات | https://khatabook.com/ · https://play.google.com/store/apps/details?id=com.vaibhavkalpe.android.khatabook |
| 2 | OkCredit | الهند؛ 11 لغة هندية | «free digital bahi khata»، «works even when you are offline»، تذكيرات آلية، دفع UPI؛ Basic Plan مجاني | https://okcredit.in/ · https://play.google.com/store/apps/details?id=in.okcredit.merchant |
| 3 | دفتر ديوني (Daftar Duyouni) | عربي/إنجليزي/كردي؛ متاجر وورش ومطاعم | «إدارة الديون والفواتير»، «تعمل ميزات أساسية دون اتصال»، فواتير PDF، تقارير، نسخة احتياطية، إدارة عملاء؛ يدعم معظم العملات | https://daftarduyouni.site/ · https://play.google.com/store/apps/details?id=com.sofealtai.daftar_dyoni |

بدائل أخرى ظهرت في البحث بلا تحقق من صفحاتها (تُذكر للاكتمال فقط): DueNox (duenox.com — دفتر ديون إلكتروني للمتاجر)، تيجار/teajar (تطبيق ديون العملاء مع واتساب)، «دفتر الديون» (com.aidayn.app)، «Debt Book سجل الديون» (com.mustafa.debtbook). والبديل الأكبر فعلياً هو الدفتر الورقي نفسه.

## 3. التموضع
| المحور | ماذا يقول المنافس | أين يتفوّق سِجِل (من tech.md فقط) |
|---|---|---|
| الأوفلاين | OkCredit ودفتر ديوني: «يعمل دون اتصال / ميزات أساسية دون اتصال» — والمزامنة لاحقاً | يعمل دون إنترنت **بالكامل** بما فيه التفعيل (كود HMAC مرتبط بالجهاز) والنسخ الاحتياطي المحلي؛ Drive اختياري |
| المستخدم الأمي | لا يذكر أي من الثلاثة تصميماً لعامل لا يقرأ | زرّان عملاقان أخذ/دفع، المبلغ بصور الأوراق النقدية، تأكيد بقراءة صوتية، مساعدة صوتية 11 موضوعاً، أهداف لمس ≥56dp |
| سلامة الدفتر | تذكيرات وتقارير؛ لا ذكر لمنع الحذف | جدول حركات إلحاقي فقط بـ SQLite triggers؛ التصحيح قيد عكسي بسبب؛ المال أعداد صحيحة؛ 10 قواعد لكل منها اختبار |
| العملات المحلية | دفتر ديوني: «معظم العملات» | دفتر مستقل لكل عملة مع الريال اليمني جديد/قديم — تفصيل محلي لا يقدّمه المنافس الهندي |
| نموذج الربح | Khatabook: إعلانات + خدمات؛ OkCredit: Basic مجاني | ترخيص بكود تفعيل (لأن الإعلانات لا تدفع في اليمن): تجربة 30 يوماً، مجاني حتى 15 زبوناً |
| المستندات | دفتر ديوني: فواتير PDF | 6 أنواع PDF عربية A4/A5/حراري 80mm × 3 قوالب + محرر ترويسة |

حيث يتفوّق المنافسون (صراحة): حجم القاعدة (Khatabook 50M+ تنزيل)، الدفع الرقمي المدمج (OkCredit UPI)، دعم iOS (دفتر ديوني على App Store)، ووجود منتج منشور في المتاجر بينما سِجِل pre-release.

## 4. الكلمات المفتاحية
AR (10): دفتر ديون · تسجيل ديون الزبائن · تطبيق ديون بدون إنترنت · دفتر ديون للبقالة · إدارة ديون المحل · كشف حساب زبون PDF · سند قبض · المتأخرون في السداد · دفتر ديون بالريال اليمني · تطبيق ديون أندرويد
EN (10): debt ledger app · offline debt book · udhar khata alternative Arabic · shop credit tracker · customer debt tracking app · offline-first Android ledger · Yemeni rial debt app · PDF statement receipt app · overdue aging app · illiterate-friendly UI app

## 5. ثلاث زوايا محتوى
1. «عامل لا يقرأ سجّل 550 ريالاً في 4 ضغطات» — فيديو/كاروسيل يتتبّع العملية بلقطات الأوراق النقدية والتأكيد الصوتي (اللقطات 06–10).
2. «لماذا لا يوجد زر حذف في دفتر الديون» — منشور تقني عن الدفتر الإلحاقي وSQLite triggers والقيد العكسي، للشريحة التقنية ولأصحاب المحلات الذين يخافون العبث.
3. «الإعلانات لا تدفع في اليمن، فماذا تفعل؟» — قصة قرار نموذج الترخيص أوفلاين (HMAC، تجربة 30 يوماً، 15 زبوناً مجاناً).

## 6. الفجوات (صريحة)
تقنياً: لا اختبار ميداني على هاتف حقيقي بعد (كاميرا/صوت/واتساب/PDF/Drive)؛ سرّ التفعيل يجب تغييره قبل البيع؛ ملفات التوقيع داخل المستودع بشرط خصوصيته ويجب حسم المستودع الكانوني؛ أندرويد فقط (المنافس العربي على iOS أيضاً). (tech.md الحالة)
تسويقياً: لا رابط حي ولا فيديو ديمو ولا دراسة حالة (links.md كلها «يُستكمل»)؛ عدد المستخدمين غير موثّق؛ ازدواج الاسم Sijil/Sijilati لم يُحسم؛ لا صفحة متجر Play بعد؛ اللقطات كلها من بيانات تجريبية «بقالة الأمل» لا من محل حقيقي.

## English summary
Sijil targets Yemeni small shops that sell on credit, where the worker may be illiterate and only 17.7% of people have internet. Three verified alternatives (accessed 2026-09-23): Khatabook (India, 50M+ installs, ads) and OkCredit (India, free basic plan, offline usage, 11 languages) dominate the "udhar khata" category but are India-only; Daftar Duyouni is an Arabic/English/Kurdish debt-and-invoice app with essential offline features and PDF invoices. Sijil's defensible edge, from tech.md: fully offline including activation, an interface built for a non-reading worker (giant buttons, pictured banknotes, spoken confirmation), a tamper-proof append-only ledger enforced by SQLite triggers, and Yemeni-rial new/old ledgers. Gaps: still pre-release with no field test, no store listing, no live link or case study, undocumented user count, Android only.

## المصادر
- tech.md, brief.ar.md, brief.en.md, links.md — portfolio-hub/01-projects/sijilati (2026-09-11)
- Khatabook: https://khatabook.com/ ; Play: https://play.google.com/store/apps/details?id=com.vaibhavkalpe.android.khatabook (50M+, 591K reviews, contains ads) — 2026-09-23
- OkCredit: https://okcredit.in/ (free basic plan, offline, 11 languages) ; Play: https://play.google.com/store/apps/details?id=in.okcredit.merchant — 2026-09-23
- دفتر ديوني: https://daftarduyouni.site/ (عربي/إنجليزي/كردي، ميزات أساسية دون اتصال، PDF) ; Play: https://play.google.com/store/apps/details?id=com.sofealtai.daftar_dyoni — 2026-09-23
- Unverified mentions (search results only, 2026-09-23): https://duenox.com/ · https://teajar.io/ar/our-products/customer-debt-app · https://play.google.com/store/apps/details?id=com.aidayn.app · https://play.google.com/store/apps/details?id=com.mustafa.debtbook
