motech-generators-system | مخطط التسويق | 2026-09-23 | final

# motech-generators-system — نظام MoTech المتكامل لإدارة المولدات — Technical Sheet

- **Repo:** moain2028/motech-generators-system (public) · commit واحد `6dc3791` «Initial release» · 20 ملفاً متعقَّباً · 181.6 KB بلا `.git` · آخر commit 2026-06-18
- **Primary language / stack:** JavaScript خالص (بلا إطار عمل ولا bundler) + HTML/CSS في ملف واحد · PostgreSQL 12+ (أعمدة `GENERATED ALWAYS AS … STORED`) · منصة AgentDB (Interactive View + استعلامات مسجَّلة عبر `window.agentdb.executeQuery`) · Chart.js 4.4.0 من CDN · خط Cairo من Google Fonts · RTL بالكامل
- **Problem:** محطات مولدات كهربائية تُدار بملف Excel: قراءات عدادات يومية، حركات ديزل، صيانة، بلا صلاحيات ولا سجل عمليات ولا تقارير موحّدة عبر الفروع (README «المعادلات المستخرجة من نظام Excel الأصلي»)
- **Solution / core features:** ERP عربي متعدد الشركات والفروع: إدخال يومي يجلب القراءات السابقة تلقائياً ويحسب 5 قيم فورياً (ساعات التشغيل، مبيع المحولات/الشاشات، الإنتاج لكل لتر ×2) وتُخزَّن كأعمدة محسوبة في Postgres؛ حركات ديزل برصيد متدحرج؛ سجل صيانة 13 حقلاً؛ 8 تقارير قابلة للتصدير CSV/الطباعة؛ لوحة تحليل بـ 4 رسوم Chart.js؛ RBAC ديناميكي بـ 39 صلاحية × 11 وحدة و4 أدوار جاهزة؛ SHA-256 + Salt، قفل بعد 5 محاولات، جلسات 8 ساعات، إجبار تغيير كلمة المرور، Audit log
- **Architecture notes:** الواجهة SPA بسيطة: `index.html` (القشرة + CSS) → `auth.js` (دخول/جلسة/صلاحيات) → `nav.js` (11 شاشة بصلاحية لكل شاشة) → `page_*.js` (8 ملفات) → `utils.js` (`q(name, params)` = `window.agentdb.executeQuery`). قاعدة البيانات: 13 جدولاً + 12 فهرساً؛ الحسابات في الـ schema لا في الواجهة. الحماية تطبيقية (README «ملاحظة على الحماية»: لا RLS)
- **Status:** «Initial release» — كود كامل وقابل للتشغيل على AgentDB؛ الاستعلامات الـ52 المسجَّلة **غير مضمَّنة في المستودع** (الملف المرجعي يوثّق 10 منها كتعليقات)
- **Last commit:** 2026-06-18
- **Live URL:** none (يعمل داخل AgentDB workspace خاص)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| الصلاحيات | 39 | `database/02_seed_permissions.sql` (عدّ الصفوف `^\('`) · `SELECT COUNT(*) FROM permissions` بعد التحميل محلياً = 39 |
| الوحدات | 11 | نفس الملف، `COUNT(DISTINCT module)` = 11: generators, readings, diesel, maintenance, reports, analytics, users, roles, branches, company, audit |
| الأدوار الجاهزة | 4 (Super Admin، مشغّل بيانات، مشاهد، فني صيانة) | `03_seed_initial_data.sql` · `COUNT(*) FROM roles` = 4 |
| الجداول | 13 | `grep -c 'CREATE TABLE' 01_schema.sql` = 13 · `information_schema.tables` = 13 — **README يقول 14 وجدوله يعدّد 13** |
| الفهارس | 12 | `grep -c 'CREATE INDEX' 01_schema.sql` |
| الأعمدة المحسوبة في DB | 5 (`GENERATED ALWAYS … STORED`) | `01_schema.sql` جدول generator_readings |
| الشاشات | 11 | `app/nav.js` PAGES (11 `{ id:`) · docs/SCREENS.md |
| التقارير | 8 | `app/page_reports.js` (8 `case`) · README |
| الرسوم البيانية | 4 (Chart.js) | `app/page_analytics.js` (4 `new Chart`) |
| بطاقات KPI في اللوحة | 8 | `app/page_dashboard.js` kpi-grid (8 بطاقات + بطاقتان في شاشة الصيانة) |
| حقول سجل الصيانة | 13 حقل إدخال (+ التاريخ) | `app/page_maintenance.js` (13 `id="m-…"`) · جدول `maintenance_log` 13 عمود بيانات — README يقول 14 |
| الاستعلامات المسمّاة التي تستدعيها الواجهة | 52 | `grep -oh "q('…'" app/*.js \| sort -u` = 52 — الملف `04_app_queries.sql` يقول 35 ويوثّق 10 |
| القيم المحسوبة فورياً في الإدخال اليومي | 5 | README + `page_daily_entry.js` (ساعات، مبيع محولات، إنتاج/لتر، مبيع شاشات، إنتاج/لتر) |
| فحوص الصلاحيات في الواجهة | 27 كوداً مختلفاً عبر `hasPerm()` | `grep -o "hasPerm('…')" app/*.js \| sort -u` |
| استدعاءات سجل العمليات | 23 موضعاً `audit(…)` + login/logout/password | `grep -c "audit(" app/*.js` |
| حجم الكود | 3,361 سطراً (2,560 JS · 292 HTML · 509 SQL) · 181.6 KB | `wc -l` · `du -sb --exclude=.git` |
| عدد الملفات | 20 | `git ls-files \| wc -l` |
| الاعتماديات وقت التشغيل | 1 (Chart.js 4.4.0 CDN) + خط Cairo | `app/index.html` السطر 9–10؛ لا package.json |
| أمان | SHA-256 + Salt 32 حرفاً · جلسة 8 ساعات · قفل 15 دقيقة بعد 5 محاولات | README «الأمان» · `04_app_queries.sql` (`INTERVAL '8 hours'`) · `utils.js randomSalt()` (16 بايت = 32 hex) — منطق القفل في استعلام مسجَّل غير موجود بالمستودع |
| تجاوز أفقي | 0 على 29 لقطة (12 شاشة × 390/1440) | فحص Playwright 2026-09-23 (`_meta.json` overflowX=0) |
| Tests | لا اختبارات؛ لا CI | فحص المستودع |
| Users / clients | مصمَّم لمتطلبات شركة العباسي للطاقة (MoTech) — جهة، لا شخص | README «الدعم» + `03_seed_initial_data.sql` (companies) |

## التشغيل والتصوير (2026-09-23 — مخطط التسويق)
- **لماذا لا يعمل مباشرة:** الواجهة تستدعي `window.agentdb.executeQuery(name, params)` — جسر منصة AgentDB غير متاح خارجها، والاستعلامات الـ52 مسجَّلة داخل المنصة وليست في المستودع.
- **ما فعلته:** PostgreSQL 16 محلياً → تحميل `01_schema` + `02_seed_permissions` + `03_seed_initial_data` بلا خطأ (39 صلاحية / 11 وحدة / 4 أدوار / 13 جدول). ثم جسر محلي صغير خارج المستودع (`make/bridge/server.js` + `queries.js`) يقدّم `app/` كما هو ويحقن `window.agentdb` بسيطاً يمرّر الاستعلامات إلى Postgres؛ كتبت الـ52 استعلاماً من أسماء الاستدعاءات والأعمدة التي تقرأها الواجهة (10 منها من `04_app_queries.sql` نصاً). **لم يُغيَّر أي ملف في المستودع.**
- **بيانات العرض:** لأن قاعدة البيانات تبدأ فارغة (مولدات 0، قراءات 0)، حُمِّلت بيانات تجريبية موسومة (`make/seed_demo.sql`: 3 مولدات، 60 قراءة لـ 30 يوماً، 4 حملات ديزل، 3 سجلات صيانة، حالة شاذة واحدة). **كل رقم داخل اللقطات (30 يوماً، 23,500 لتر، 1,283…) تجريبي ولا يُقتبس على أي تصميم.** الأرقام على التصاميم من الكود فقط.
- **الدخول:** admin / Admin@2026 من البذور → شاشة إجبار تغيير كلمة المرور (مصوَّرة كمسار حقيقي) → اللوحة.
- **التصوير:** Playwright Chromium، DPR 2، locale ar-SA: 12 شاشة (دخول، لوحة، إدخال يومي، ديزل، صيانة، تحليل، تقارير ×3، مولدات، مستخدمون، أدوار، فروع، سجل) × (1440×900 + 390×844) = 28 لقطة + لقطة مصفوفة الصلاحيات (ديسكتوب) = 29 لقطة في `screenshots/`.
- **ملاحظة جوال:** لا توجد قاعدة `@media` للشريط الجانبي؛ على 390px يبقى الشريط 220px ثابتاً وتضيق المنطقة الرئيسية (لا تجاوز أفقي لكن التجربة مضغوطة) — انظر التنظيف.

## ملاحظات التنظيف / Cleanup notes
- README: «14 جدول» والجدول يعدّد 13 — الصحيح 13. «14 حقل» صيانة — الواجهة 13 حقلاً + التاريخ.
- `04_app_queries.sql` يقول «35 استعلام» ويوثّق 10؛ الواجهة تستدعي 52 اسماً. الاستعلامات الفعلية محبوسة في AgentDB — إضافتها كاملة إلى المستودع تجعل المشروع قابلاً للتشغيل خارج المنصة (الجسر المحلي هنا يثبت أنها ~270 سطراً فقط).
- لا تجاوب للجوال (sidebar ثابت 220px)؛ لا اختبارات؛ الحماية تطبيقية فقط (README يقرّ بذلك ويقترح Node.js + RLS).
- كلمة مرور admin الافتراضية مكتوبة في README وفي SQL؛ يُغيَّر إجبارياً أول دخول لكنها منشورة.
- المستودع commit واحد بلا تاريخ تطوير؛ لا LICENSE ملف (README: ملكية خاصة).
