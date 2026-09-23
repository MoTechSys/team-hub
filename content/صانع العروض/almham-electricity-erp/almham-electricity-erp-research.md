almham-electricity-erp | صانع العروض | 2026-09-23 | draft

# almham-electricity-erp — بحث وتحليل (AR + EN summary)
تاريخ الوصول لكل الروابط: 2026-09-23. ادعاءات المنافسين من صفحاتهم؛ ادعاءات مشروعنا من tech.md / brief فقط.

## 1. تحليل سوق مختصر
- من يشتري: شركات توليد وتوزيع الكهرباء الصغيرة والمتوسطة والمشغّلون الصناعيون (محطات ديزل/شمسية بمشتركين) الذين يديرون التوليد والفوترة والخزينة على أنظمة منفصلة وقديمة. (brief «لمن يفيد» · tech.md «المشكلة»)
- الفئة: أنظمة Customer Care & Billing / meter-to-cash للمرافق، مع طبقة ERP (خزينة، موظفون، وقود). المنتجات العالمية موجّهة للمرافق الكبيرة؛ الفجوة عند المرافق الصغيرة في أسواق مثل اليمن التي تعمل على أدوات محلية قديمة (ECAS على SQL Server). حجم الفئة بالأرقام: «يُستكمل» — لا رقم موثوق خاص بالمنطقة في بحث اليوم.

## 2. المنافسون / البدائل (3) — بروابط حقيقية
| البديل | ماذا هو | ماذا يقول عن نفسه (من صفحته) | الرابط | تاريخ الوصول |
|---|---|---|---|---|
| Oracle Utilities Customer Care and Billing (CC&B) | منصة عناية بالعملاء وفوترة للمرافق الكبيرة (سحابي وon-prem) | «a customer care and billing system for traditional scalar devices and billing processes» · «from the meter to billing, service orders, and outages» | https://docs.oracle.com/en/industries/energy-water/ccb/ · https://www.oracle.com/utilities/customer-service/ | 2026-09-23 |
| SAP S/4HANA Utilities مع FI-CA | حسابات عقود (Contract Accounts) للفوترة عالية الحجم في الطاقة والمياه والغاز، مع ترحيل تلقائي إلى المحاسبة | «Invoices and credit memos from contract billing and invoicing are posted in FI-CA automatically» | https://help.sap.com/docs/SUPPORT_CONTENT/uindustry/3362183821.html | 2026-09-23 |
| Springbrook Cirrus Utility Billing | فوترة meter-to-cash سحابية للمرافق الحكومية (مياه، كهرباء، صرف) مع مدفوعات متعددة القنوات | «Complete "meter-to-cash" solution for utilities of water, electric, sewage… Accept payments Online, Over the counter, lockbox, or via mail» | https://springbrooksoftware.com/solutions/utility-billing/ | 2026-09-23 |
| (الوضع الراهن) ECAS على SQL Server | برنامج الفوترة المكتبي القديم الذي يرحّل منه مشروعنا | — (نظام محلي بلا صفحة عامة وُجدت في بحث اليوم) | — | tech.md «المشكلة» |
| (مرجع) Kill Bill | فوترة اشتراكات مفتوحة المصدر self-hosted — ليست للمرافق لكنها البديل «ابنِ بنفسك» | «Open-source billing and payments infrastructure you run yourself» | https://killbill.io/ | 2026-09-23 |

## 3. التموضع — أين يتفوّق مشروعنا (من tech.md فقط)
- ضد Oracle CC&B وSAP FI-CA: نفس النمط المحاسبي (قيد مزدوج، idempotency، مسار اعتماد — tech.md يذكر صراحة «بنمط SAP FI-CA / Oracle CC&B») لكن بحجم وتكلفة مرفق صغير، self-hosted على PostgreSQL، وبواجهة عربية RTL وخرائط Leaflet للمشتركين والمحطات. (tech.md «الحل» و«التقنيات»)
- ضد Springbrook: مشروعنا يغطي التوليد نفسه (محطات، مولدات، ديزل، طاقة شمسية) لا الفوترة فقط، ويضيف خزينة وموظفين ومهام وتطبيقات ميدانية أوفلاين. (tech.md «التقنيات»: 9 نطاقات وظيفية)
- ضد ECAS: ترحيل كامل بلا قطيعة — 687 فترة فوترة مطابَقة، جسر آمن الفشل للقراءة من SQL Server أثناء الانتقال. (tech.md «الأرقام» و«الحل»)
- ما لا نعلنه: لا شهادات امتثال ولا SLA ولا دعم متعدد العملات مذكور في tech.md.

## 4. الكلمات المفتاحية
AR (10): نظام ERP كهرباء · فوترة كهرباء · نظام فوترة مشتركين · إدارة محطات توليد · نظام محاسبي للمرافق · ترحيل بيانات فوترة قديمة · خرائط المشتركين · نظام تحصيل ميداني · Angular NestJS PostgreSQL · نظام إدارة الديزل والطاقة الشمسية
EN (10): utility ERP · electricity billing system · meter-to-cash software · customer care and billing alternative · multi-station generation management · billing to general ledger · legacy billing migration · offline collection point · Angular NestJS PostgreSQL ERP · subscriber GIS map

## 5. ثلاث زوايا محتوى مقترحة
1. «من قراءة العداد إلى القيد: لماذا يجب أن تلمس الفاتورة دفتر الأستاذ مباشرة» — زاوية مالية/محاسبية. (tech.md «الحل»)
2. «687 فترة فوترة بلا قطيعة: كيف ترحّل 20 سنة من ECAS إلى PostgreSQL بشكل idempotent» — زاوية تقنية للمهندسين. (tech.md «الأرقام» و«التقنيات»: ETL)
3. «نظام واحد لشركة كهرباء صغيرة: محطات وديزل وشمسي ومشتركون وخزينة» — زاوية المالك/المدير. (brief «الحل» · tech.md 9 نطاقات)

## 6. فجوات صريحة (تقنياً وتسويقياً)
- لا رابط حي ولا عرض عام؛ المستودع خاص؛ يُعرض كدراسة حالة بلقطات فقط. (links.md · tech.md)
- تشغيل فعلي لدى شركة واحدة فقط؛ لا برهان على تعدد الشركات في الإنتاج رغم أن النموذج يدعمه. (tech.md «الحالة»)
- عدد المشتركين/العدّادات والمستخدمين الفعليين غير معلوم. (tech.md «يُستكمل»)
- brief يقول «عدد الاختبارات والصفحات: يُستكمل» بينما tech.md يذكر 515 ملف اختبار — التصاميم استخدمت رقم tech.md (مصدره git ls-tree)؛ يلزم تحديث brief. (brief «النتيجة» · tech.md)
- تعارض داخل tech.md: 170 جدولاً في schema.ts مقابل 204 في قاعدة التشغيل — لم يُعرض أيّ منهما على التصاميم. (tech.md «الأرقام»)
- اللقطات من بيئة تظهر فيها أصفار في عدة بطاقات (0 موظفين، 0 مهام) — تُوحي ببيانات تجريبية؛ يفضَّل لقطات من بيئة ببيانات أغنى (بلا أسماء مشتركين).
- لا ذكر للامتثال (تدقيق خارجي، نسخ احتياطي، تشفير PII) في tech.md — نقطة يسأل عنها كل مرفق.

## EN summary
almham is a self-hosted utility ERP (Angular 22 / NestJS 11 / PostgreSQL) for small electricity generators and distributors. It borrows the accounting pattern of Oracle CC&B and SAP FI-CA (double-entry, idempotent posting, approval path) at small-utility scale, and — unlike billing-only tools such as Springbrook Cirrus — also covers generation (stations, generators, fuel, solar), treasury, HR and offline field collection. Its migration story (687 billing periods reconciled from the legacy ECAS SQL Server tool, fail-safe bridge) is the strongest differentiator. Gaps: no live demo, one production company, unknown production volumes, a brief/tech.md mismatch on test counts, an internal 170-vs-204 table discrepancy, and screenshots that show zero-value cards.

## المصادر
- portfolio-hub: 01-projects/almham-electricity-erp/{brief.ar.md, brief.en.md, tech.md, links.md}
- https://docs.oracle.com/en/industries/energy-water/ccb/ · https://www.oracle.com/utilities/customer-service/ (2026-09-23)
- https://help.sap.com/docs/SUPPORT_CONTENT/uindustry/3362183821.html (2026-09-23)
- https://springbrooksoftware.com/solutions/utility-billing/ (2026-09-23)
- https://killbill.io/ (2026-09-23)
