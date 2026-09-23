motech-generators-system | مخطط التسويق | 2026-09-23 | v2

# SOURCES.md — مصدر كل نص ورقم وصورة في motech-generators-system-project-pack-v2

المشروع لم يكن في portfolio-hub؛ البند 0 أنتج `project/` (brief.ar/en.md · tech.md · links.md · screenshots/ 29 لقطة) — المصدر الأساسي لكل ما يلي، مع الكود في https://github.com/moain2028/motech-generators-system (commit 6dc3791، 2026-06-18) وتشغيل محلي بتاريخ 2026-09-23.

## A. النصوص والأرقام على التصاميم
| العنصر | المصدر |
|---|---|
| الاسم «نظام MoTech للمولدات / MoTech Generators» | README السطر الأول «نظام MoTech المتكامل لإدارة المولدات» (مختصر ليتّسع) |
| slug motech-generators-system | اسم المستودع |
| العنوان «ERP عربي يستبدل ملف Excel في محطات المولدات» | README «نظرة عامة» (ERP عربي متكامل) + «المعادلات المستخرجة من نظام Excel الأصلي» |
| السطر الوصفي (متعدد الشركات والفروع، 5 قيم فوراً، رصيد ديزل متدحرج، 8 تقارير، صلاحيات ديناميكية، سجل عمليات) | README «نظرة عامة» + «الإدخال اليومي: 5 قيم محسوبة تلقائياً» |
| 39 صلاحية | `database/02_seed_permissions.sql` 39 صفاً · `SELECT COUNT(*) FROM permissions` = 39 |
| 11 وحدة | نفس الملف `COUNT(DISTINCT module)` = 11 |
| 13 جدولاً | `01_schema.sql` 13 `CREATE TABLE` · information_schema = 13 (README «14» خطأ) |
| 8 تقارير | `app/page_reports.js` 8 `case` · README |
| 4 أدوار جاهزة | `03_seed_initial_data.sql` · `COUNT(*) FROM roles` = 4 |
| 11 شاشة | `app/nav.js` PAGES · docs/SCREENS.md |
| 5 قيم محسوبة فوراً / 5 أعمدة محسوبة | `page_daily_entry.js` + `01_schema.sql` (5 `GENERATED ALWAYS`) |
| 13 حقل صيانة | `page_maintenance.js` 13 `id="m-…"` (README «14») |
| 3,361 سطراً (في explainer/copy فقط) | `wc -l app/* database/*` |
| تاجات: JavaScript · PostgreSQL · AgentDB · Chart.js · RTL | README «المتطلبات» + `index.html` سطر 10 |
| شارة الشريحة: شركات / Companies | تكليف مدير المنتج msg 4614181 + 02-brand SEGMENTS |
| الفوتر github.com/moain2028/motech-generators-system | تكليف مدير المنتج |
| wordmark «معين العباسي / Moain Al-Abbasi» (نسخ logo فقط) | project-pack-standard-v2 §A |
| «Excel» كأصل المشكلة | README «المعادلات المستخرجة من نظام Excel الأصلي» (7 معادلات) |
| نصوص الكاروسيل 1–5 والريل | brief + tech.md + README؛ copy.ar/en.md |
| بطاقة الرقم «39 صلاحية عبر 11 وحدة» | `02_seed_permissions.sql` + README «الأدوار والصلاحيات» (إنشاء أدوار بأي اسم، مصفوفة بالوحدات) |
| البانر «من ملف Excel إلى ERP: كيف تُحسب القراءات داخل قاعدة البيانات لا في الواجهة» | عنوان مقال مقترح (زاوية 1 في research) من `01_schema.sql` |

## B. الصور (كلها لقطات حقيقية من تشغيل محلي 2026-09-23، Playwright Chromium، DPR 2)
| الاستخدام | الملف | ملاحظة |
|---|---|---|
| القطع الست، كاروسيل 2، غلاف الريل، الريل 2 | desktop-01-dashboard / mobile-01-dashboard | لوحة المعلومات |
| كاروسيل 1، 3، البانر، الريل 3 | mobile-02-daily_entry / desktop-02-daily_entry | الإدخال اليومي |
| كاروسيل 4 | desktop-09b-roles-permissions-matrix | مصفوفة الصلاحيات (نافذة دور «مشغّل بيانات») |
| كاروسيل 5 | mobile-06b-reports-efficiency | تقرير كفاءة المولدات |
| الريل 4، 5 | mobile-09-roles / mobile-03-diesel | الأدوار · حركات الديزل |
| **بيانات داخل اللقطات** | كل الأرقام (30 يوماً، 23,500 لتر، 1,283 رصيد، G-01/G-02/G-03، Perkins/Cummins، أرقام سندات D-1041…) | **تجريبية** من `make/seed_demo.sql` حُمِّلت للتصوير لأن قاعدة البيانات تبدأ فارغة — لا يُقتبس منها رقم نصاً على أي تصميم |
| «شركة العباسي للطاقة (MoTech)» و«محطة غليل» في الشريط العلوي | من بذور المستودع `03_seed_initial_data.sql` | جهة لا شخص (مسموح — تكليف مدير المنتج)؛ «غليل» موقع في البذور الأصلية |
| «المدير العام» / admin | `03_seed_initial_data.sql` (full_name المستخدم الافتراضي) | ليس اسم شخص حقيقي |
| «فريق الصيانة / مشرف المحطة» في سجل الصيانة | seed_demo.sql | أوصاف عامة عمداً، لا أسماء |
| الخلفيات/الشبكة/التوهج | مولّدة برمجياً (02-brand/scripts/brand.py) | لا صور مخزون، لا لقطة مولّدة بالذكاء الاصطناعي |

## C. الصوت
- الريلان: نفس المقطع الموسيقي الآلي المولّد (CassetteAI/music-generator، 24 ث، 2026-09-23) المستخدم في s-acm وhafawa وroyal-coffee لتوحيد صوت المحفظة؛ بلا حقوق طرف ثالث.

## D. ملفات البحث والنص
- `research.md`: كل ادعاء خارجي برابط وتاريخ وصول 2026-09-23؛ يوضّح أن المنتج ليس IoT.
- `explainer.ar/en.md`، `copy.ar/en.md`: كل جملة من brief/tech/README؛ draft حتى ختم المحرر.

## E. طريقة التشغيل (make/)
- `bridge/server.js` + `bridge/queries.js`: جسر محلي يعوّض `window.agentdb` وينفّذ الـ52 استعلاماً على PostgreSQL 16 — مكتوب من أسماء الاستدعاءات والأعمدة التي تقرأها الواجهة (10 منها نصاً من `04_app_queries.sql`). **خارج المستودع؛ الكود الأصلي لم يُغيَّر.**
- `seed_demo.sql`: البيانات التجريبية الموسومة. `shoot.py`: التصوير. `build.py` + `packlib.py`: التصاميم. `make_reel.sh`: الريل.

## F. ما لم يُستخدم عمداً
- أي رقم من بيانات اللقطات التجريبية.
- «14 جدول» و«14 حقل» و«35 استعلام» من README/الملف المرجعي — مصحَّحة من الكود (13 · 13 · 52).
- أرقام الأمان (8 ساعات، 5 محاولات، 15 دقيقة) على التصاميم — منطق القفل في استعلام مسجَّل غير موجود في المستودع، فذُكرت في brief/tech منسوبة لـ README فقط.
- كلمة مرور admin الافتراضية — لم تظهر في أي لقطة (حقل كلمة المرور فارغ في لقطة الدخول).
- أي رقم هاتف أو بريد أو اسم شخص.
- منصات IoT كمنافسين مباشرين.

## G. التباين
- النصوص على الخلفية الداكنة: White/#F2F2F2 و#A3B1C0 (الخافت المعتمد) على Navy — AA فأعلى؛ الشارة الصفراء الوسطى للشريحة بنص Navy؛ لا نص مقطوع (فحص بصري لكل قطعة من الـ40).
