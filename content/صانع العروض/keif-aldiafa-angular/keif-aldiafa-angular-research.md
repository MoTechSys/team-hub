keif-aldiafa-angular | صانع العروض | 2026-09-23 | draft

# keif-aldiafa-angular — بحث وتحليل (AR + EN summary)
تاريخ الوصول لكل الروابط: 2026-09-23. ادعاءات المنافسين من صفحاتهم؛ ادعاءات مشروعنا من README/tech.md فقط.

## 1. تحليل سوق مختصر
- من يشتري: مؤسسات ضيافة وتنظيم فعاليات صغيرة (6–50 موظفاً) في السعودية والخليج تحجز مضيفين بالساعة/الفعالية وتسلّم عُهداً وتتابع ذمماً، وغالباً تديرها بدفتر أو جداول. (README «ما هذا؟» · brief «لمن يفيد»)
- الفئة: برمجيات إدارة الفعاليات + جدولة الطاقم + تأجير/تتبّع المعدات + فوترة صغيرة. الحلول العالمية سحابية بالاشتراك لكل مستخدم وبالإنجليزية أولاً؛ الفجوة: عربي RTL أصلاً، بلا اشتراك، ويعمل أوفلاين في مواقع الفعاليات. حجم الفئة بالأرقام: «يُستكمل».

## 2. المنافسون / البدائل (3) — بروابط حقيقية
| البديل | ماذا هو | ماذا يقول عن نفسه (من صفحته) | الرابط | تاريخ الوصول |
|---|---|---|---|---|
| Odoo Event Management (+ Rental) | ERP سحابي/مفتوح المصدر بوحدات فعاليات وتأجير معدات وجدولة طاقم وفوترة آلية — للأعمال الصغيرة 6–50 موظفاً | «From tracking equipment rental and maintenance to streamlined purchasing to scheduling shifts for your staff… Manage equipment such as sound systems, lighting, and party tents with Odoo's rental feature» | https://www.odoo.com/industries/event-management · https://www.odoo.com/app/rental | 2026-09-23 |
| Ubeya | منصة جدولة طاقم الفعاليات المؤقت للمنشآت الكبيرة (تطبيق جوال، تأكيد ورديات، رواتب) | «for large scale events, venues, and organizations managing complex temporary workforces… real-time updates, mobile accessibility, automated shift confirmations» | https://www.ubeya.com/blog/top-event-staff-scheduling-software-large-events-venues | 2026-09-23 |
| Zoho Bookings | حجز مواعيد وطاقم سحابي مع منع الحجز المزدوج عبر مزامنة التقويم | «Eliminate double-bookings. Every confirmed appointment is immediately synced to your connected calendar» (ومنتدى دعمهم يذكر حجوزات مزدوجة عشوائية) | https://www.zoho.com/bookings/explore/simplify-team-scheduling.html · https://help.zoho.com/portal/zh/community/topic/double-booking-consultants | 2026-09-23 |
| (مرجع) Connecteam / When I Work / Skedda | أدوات جدولة ورديات عامة تُذكر في قوائم «أفضل أدوات جدولة طاقم الفعاليات» | — | https://www.eventstaffapp.com/articles/best-event-staff-scheduling-software-tools/ | 2026-09-23 |
| (الوضع الراهن) الدفتر الورقي + واتساب | ما تستبدله المؤسسة فعلاً | — | README «المشاكل السبع» | — |

## 3. التموضع — أين يتفوّق مشروعنا (من README/tech.md فقط)
- ضد Odoo: لا خادم ولا اشتراك ولا تهيئة ERP؛ يعمل أوفلاين كاملاً على الجوال؛ عربي RTL أصلاً؛ نموذج مبني حرفياً على متطلبات مؤسسة ضيافة (مضيفون، عُهد، ذمم «له/عليه»). (ADR-002 · README «الميزات الجوهرية») — Odoo أوسع بكثير (محاسبة كاملة، متجر، CRM) وهذا ليس هدفنا.
- ضد Ubeya: Ubeya للمنشآت الكبيرة والطواقم المعقّدة؛ مشروعنا لمؤسسة صغيرة بمضيفين معدودين، مع مطابقة إرجاع العُهد ودفتر الذمم التي لا تقدّمها أدوات الجدولة. (README «المشاكل 5 و7»)
- ضد Zoho Bookings: منع التعارض عندنا في المنطق بالدقيقة ومغطّى بـ 13 اختباراً، لا اعتماداً على مزامنة تقويم خارجي. (README «منع التعارض» · conflict.service.spec.ts)
- ما لا نعلنه: لا تطبيق متجر (App Store/Play) بل PWA؛ لا تعدد مستأجرين؛ لا مزامنة بين الأجهزة إلا بالنسخ الاحتياطي. (ADR-002 · docs/ARCHITECTURE.md §8)

## 4. الكلمات المفتاحية
AR (10): نظام إدارة الضيافة · برنامج حجز مضيفين · إدارة فعاليات للمؤسسات الصغيرة · تطبيق يعمل بدون إنترنت · بديل الدفتر الورقي · إدارة العُهد والمخزون · دفتر ذمم المضيفين · عرض سعر وفاتورة آلية · منع تعارض الحجوزات · تطبيق ويب تقدّمي عربي
EN (10): hospitality management PWA · event staffing app offline · host booking conflict prevention · equipment check-out return tracking · small business receivables ledger · Arabic RTL business app · serverless Angular PWA · IndexedDB offline-first app · quote to invoice generator · paper ledger replacement

## 5. ثلاث زوايا محتوى مقترحة
1. «لماذا بلا خادم؟ تطبيق أعمال كامل يعمل على جوال المدير في موقع الفعالية» — زاوية الملكية والتكلفة الصفرية. (ADR-002)
2. «التلاصق ليس تعارضاً: منع حجز المضيف مرتين بالدقيقة و13 اختباراً» — زاوية تقنية. (README «منع التعارض»)
3. «كاسات ودلات وثلاجات: كيف تُطابق العُهد المسلَّمة بالمرتجَعة وتحمّل التالف على من يستحق» — زاوية تشغيلية للمؤسسات الصغيرة. (README «المشكلة 7» · AUDIT-GAPS «أفضل جزء في النظام»)

## 6. فجوات صريحة (تقنياً وتسويقياً)
- لا رابط حي ولا نسخة تجريبية عامة. (links.md)
- إشعار المضيف عند الحجز مبني وغير موصول؛ التذكير ليس SMS؛ ربط العُهدة بالمضيف عند التسليم غير إلزامي. (AUDIT-GAPS.md)
- بيانات حقيقية في مستودع عام: سجل تجاري، IBAN، رقم حساب، جوال المؤسسة، وكلمة مرور مبدئية — تستحق النقل إلى إعدادات وقت التشغيل. (tech.md «ملاحظات التنظيف»)
- لا مزامنة بين الأجهزة: بيانات جهاز واحد، والنسخ الاحتياطي يدوي/Google Drive. (ADR-002)
- تعارض أعداد في الوثائق (نماذج 14/17/18، مكوّنات 18/24). (tech.md)
- نشاط تطوير 5 أيام فقط ثم توقف منذ 2026-08-05؛ الشارة «قيد التطوير». (git)
- لوحة التحكم تُظهر أصفاراً مع بيانات البذر (0 فعاليات قادمة) — لقطات ببيانات أغنى ستقوّي التصاميم.

## EN summary
keif-aldiafa-angular is a serverless, offline-first, fully Arabic PWA (Angular 22 / Signals / IndexedDB) that replaces a paper ledger for a small Jeddah hospitality staffing company. Versus Odoo (broad subscription ERP with rental and staff scheduling), Ubeya (enterprise event workforce) and Zoho Bookings (calendar-synced double-booking prevention), its edge is zero running cost, true offline use at venues, Arabic RTL by design, and domain-specific pieces general tools lack: minute-level conflict logic under 13 tests, an append-only "owed to/by" ledger, and equipment return matching with damage/loss. Gaps: no live demo, unwired host notifications, real identifiers committed to a public repo, single-device data, documentation count mismatches, and no commits since 2026-08-05.

## المصادر
- moain2028/keif-aldiafa-angular: README.md · CONTRACT.md · AUDIT-GAPS.md · docs/ARCHITECTURE.md · docs/DECISIONS.md · git log
- https://www.odoo.com/industries/event-management · https://www.odoo.com/app/rental (2026-09-23)
- https://www.ubeya.com/blog/top-event-staff-scheduling-software-large-events-venues (2026-09-23)
- https://www.zoho.com/bookings/explore/simplify-team-scheduling.html · https://help.zoho.com/portal/zh/community/topic/double-booking-consultants (2026-09-23)
- https://www.eventstaffapp.com/articles/best-event-staff-scheduling-software-tools/ (2026-09-23)
