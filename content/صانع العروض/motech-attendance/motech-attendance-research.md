motech-attendance | صانع العروض | 2026-09-23 | draft

# Motech Attendance — بحث وتحليل (AR + EN summary)
تاريخ الوصول لكل الروابط: 2026-09-23. كل ادعاء عن منافس مأخوذ من صفحته المذكورة؛ كل ادعاء عن مشروعنا من tech.md / brief فقط.

## 1. تحليل سوق مختصر
- من يشتري: شركات ومؤسسات متعددة الفروع (كهرباء، تجزئة، مصانع) تملك أجهزة بصمة ZKTeco وتريد تقارير مركزية ورواتب WPS بلا ترخيص برنامج مغلق. (tech-planner.md «لمن يفيد»)
- الفئة: برمجيات الحضور والانصراف (Time & Attendance) في الخليج واليمن حيث أجهزة ZKTeco شائعة والبرنامج المرافق مكتبي لكل جهاز. حجم الفئة بالأرقام: «يُستكمل» — لم أجد رقماً موثوقاً خاصاً بالمنطقة في بحث اليوم، ولا أضع رقماً عالمياً عاماً بديلاً.

## 2. المنافسون / البدائل (3) — بروابط حقيقية
| البديل | ماذا هو | ماذا يقول عن نفسه (من صفحته) | الرابط | تاريخ الوصول |
|---|---|---|---|---|
| ZKBio Time.Net (ZKTeco) | برنامج سطح مكتب Windows «lite» للمنشآت الصغيرة والمتوسطة — هو الوضع الراهن الذي يستبدله مشروعنا | «lite windows-based desktop time and attendance software for small and medium enterprises… stable communication for ZKTeco devices» | https://www.zkteco.com/en/ZKBioTime_Net/ZKBio_Time_Net | 2026-09-23 |
| BioTime Cloud (ZKTeco) | سحابة ZKTeco الرسمية على AWS: geofencing، تطبيق جوال، إجازات، وصول متعدد المدراء عبر المتصفح؛ تجربة مجانية 90 يوماً | «geofencing, time and attendance performance tracking, leave applications… Multiple administrators can access BioTimeCloud anywhere using a web browser» | https://www.zkteco.me/cloud-based-time-attendance-solution | 2026-09-23 |
| Bayzat (الإمارات/الخليج) | منصة HR/رواتب شاملة للخليج مع حضور بـ geofencing وتكامل بيومتري ومزامنة رواتب مع WPS | «one-tap check-ins via our mobile app and seamless biometric integration… AI validates attendance through facial recognition» | https://www.bayzat.com/attendance | 2026-09-23 |
| (بديل رابع للمرجع) Jibble | حضور «مجاني للأبد» بالوجه/GPS على الجوال والتابلت؛ البصمة عبر تطبيقاتهم وأجهزتهم لا عبر أجهزة ZKTeco الموجودة | «Free forever for unlimited users… facial recognition and fingerprint scanning in one… Coming soon!» | https://www.jibble.io/biometric-attendance | 2026-09-23 |
| (مرجع إضافي) Keka | HRMS هندي يعلن تكامل مع «1000+ biometric device» | «1000+ biometric device integration» | https://www.keka.com/attendance-management-system | 2026-09-23 |

## 3. التموضع — أين يتفوّق مشروعنا (من tech.md فقط)
- ضد Time.Net: مركزي متعدد الفروع عبر الويب بدل برنامج لكل جهاز؛ RTL أصلاً؛ الجامع يسحب من الأجهزة الموجودة نفسها (iFace950 وغيرها) فلا استبدال عتاد. (tech.md «الحل»)
- ضد BioTime Cloud: البيانات على خادم العميل (self-hosted: Go + PostgreSQL + systemd + Caddy) لا في سحابة المورّد؛ عزل مستأجرين fail-closed؛ تشفير PII at-rest؛ بلا اشتراك لكل مستخدم. (tech.md «التقنيات» · tech-planner.md «الأمان»/«النشر») — ملاحظة: BioTime يقدّم geofencing وتطبيق جوال للموظف، ومشروعنا لا يعلن geofencing.
- ضد Bayzat: Bayzat منصة HR كاملة؛ مشروعنا أخفّ وأضيق (حضور + ورديات + إجازات + WPS) ويعمل داخل شبكة العميل؛ الأنسب لمن يريد ملكية البيانات وتكاملاً مباشراً مع أجهزة البصمة القائمة. (tech-planner.md «الحل»)
- مشترك مع الجميع: تصدير WPS بصيغتَي السعودية والإمارات (tech-planner.md «الأرقام»)، محرك يومي idempotent مُثبت على 2,277 صف (brief «النتيجة»).

## 4. الكلمات المفتاحية
AR (10): نظام حضور وانصراف · برنامج بصمة مركزي · بديل ZKTeco · حضور متعدد الفروع · تقارير حضور عربية · نظام ورديات وإجازات · تصدير WPS · حضور self-hosted · جهاز بصمة iFace950 · إدارة الحضور للشركات
EN (10): attendance management system · ZKTeco alternative · central attendance software · multi-branch time attendance · biometric attendance Go PostgreSQL · WPS payroll export · self-hosted attendance · pyzk collector · shift and leave management · RTL HR dashboard

## 5. ثلاث زوايا محتوى مقترحة
1. «لماذا لا يكفي برنامج البصمة المكتبي لشركة بأربعة فروع» — المشكلة → الجامع النحيف → لوحة واحدة. (brief «المشكلة/الحل»)
2. «كيف يُوقَّع كل إرسال بصمة: HMAC ومنع إعادة التشغيل بلغة بسيطة» — زاوية أمان تقنية للمهندسين. (tech.md «التقنيات»)
3. «3,118 بصمة و2,277 صفاً بلا تكرار: ماذا يعني idempotent لقسم الرواتب» — زاوية الثقة بالأرقام. (brief «النتيجة»)

## 6. فجوات صريحة (تقنياً وتسويقياً)
- لا رابط حي ولا عرض تجريبي عام؛ النظام داخلي. (links.md)
- لا geofencing ولا تطبيق جوال أصلي للموظف (المنافسون يعلنونها)؛ الواجهة ويب متجاوبة فقط. (tech.md «التقنيات» — لا ذكر لتطبيق)
- عدد الفروع/الأجهزة في الإنتاج والمستخدمين الفعليين غير معلوم. (tech.md «يُستكمل»)
- الاختبار الحي على جهاز واحد و11 موظفاً؛ لا برهان على نطاق مئات الأجهزة. (brief «النتيجة»)
- لا نشاط تطوير منذ 2026-06-24 بحسب tech.md، بينما tech-planner.md يذكر Phase 3–4 وESS مكتملة — يلزم توحيد الحالة بين الملفَين قبل النشر. (tech.md «الحالة» · tech-planner.md «الحالة»)
- لا اسم علامة تجارية مستقلة ولا صفحة منتج؛ التسويق يعتمد على دراسة الحالة فقط.
- ملاحظة تشغيلية من التصوير: هجرة 003 تفشل إذا كانت pgcrypto خارج schema public وseed المدير الأول يفشل — تحتاج إصلاحاً في المستودع. (tech-planner.md «التشغيل والتصوير»)

## EN summary
Motech Attendance targets multi-branch companies already running ZKTeco fingerprint devices whose attendance lives in a per-device desktop program (ZKBio Time.Net). It competes with ZKTeco's own BioTime Cloud (AWS, geofencing, mobile app, 90-day trial), GCC HR platforms such as Bayzat (biometric integration + WPS payroll), and free mobile-first tools like Jibble. Its edge, per tech.md: self-hosted Go/PostgreSQL, a thin HMAC-signed collector on existing devices, RTL-first dashboard, idempotent daily engine (2,277 rows proven), fail-closed tenant isolation, and KSA/UAE WPS export. Gaps: no live demo, no geofencing or native mobile app, unknown production scale, single-device live test, and an inconsistent status between tech.md and tech-planner.md that must be reconciled before publishing.

## المصادر
- portfolio-hub: 01-projects/motech-attendance/{brief.ar.md, brief.en.md, tech.md, tech-planner.md, links.md}
- https://www.zkteco.com/en/ZKBioTime_Net/ZKBio_Time_Net (2026-09-23)
- https://www.zkteco.me/cloud-based-time-attendance-solution (2026-09-23)
- https://www.bayzat.com/attendance (2026-09-23)
- https://www.jibble.io/biometric-attendance (2026-09-23)
- https://www.keka.com/attendance-management-system (2026-09-23)
