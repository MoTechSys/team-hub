keif-aldiafa-ads-platform | مخطط التسويق | 2026-09-23 | final

# keif-aldiafa-ads-platform — منصة Google Ads Intelligence لعميل ضيافة — Technical Sheet

- **Repo:** moain2028/keif-aldiafa-ads-platform (public) · commit واحد `e21bd98` · 25 ملفاً متعقَّباً · آخر commit 2026-08-31
- **Primary language / stack:** TypeScript · Hono 4.13 (JSX SSR للوحة) · Vite 8 + @hono/vite-build · Cloudflare Pages + D1 (SQLite) · Wrangler 4 · Google Ads API v24 (GAQL) · Search Console API v3 · OAuth 2.0 refresh-token · Tailwind (CDN) + Font Awesome (CDN) في اللوحة
- **Problem:** حساب Google Ads لعميل ضيافة تُجرى عليه تغييرات مجهولة المصدر (Auto-Apply من Google، تعديلات ميزانية متكررة، صلاحية إدارية ثانية غير معروفة، تحويلات بقيمة صفر) — والمالك لا يعرف «من غيّر إيش ومتى» (README «المشاكل التي تحلّها»؛ توصف نوعياً فقط)
- **Solution / core features:** طبقة اتصال دائمة بـ Google: تجديد access_token تلقائياً من refresh_token مع ذاكرة في D1 (لا يُضرب Google كل طلب)؛ 13 نقطة API (11 GET + 2 POST) منها استعلام GAQL حر `POST /api/ads/query` وفحص صحة رباعي؛ قراءة الحملات والأداء وSearch Console؛ لقطات دورية في D1؛ سجل اتصالات؛ لوحة عربية RTL بتحديث كل 5 دقائق؛ 10 وثائق تشغيلية منها دليل GAQL بـ 19 وصفة مُختبرة و5 استعلامات فاشلة موثَّقة، ووثيقة جنائية تشرح قراءة `change_event`
- **Architecture notes:** `src/google.ts` (طبقة Google: توكن/كاش/GAQL/GSC/health/log) → `src/index.tsx` (Hono، 13 مساراً + وسيط `DASH_KEY` اختياري + CORS) → `src/ui.tsx` (لوحة HTML واحدة تستدعي الـAPI بـ fetch). D1: 3 جداول (token_cache، connection_log، snapshots) + 3 فهارس. الأسرار من `.dev.vars`/Pages secrets. قواعد ميدانية مثبّتة في الكود: لا `login-customer-id`، v17–v21 ملغاة، Basic Auth بعميل الويب
- **Status:** المرحلة 0 (الاتصال الدائم) مكتملة ومُتحقَّقة ميدانياً 2026-08-31 (docs/00-HANDOVER)؛ المرحلة 1 (حرس التغييرات + 7 محرّكات تحليل + mutate بحارس) والمرحلة 2 (مصنع صفحات SEO) والمرحلة 3 (النشر) **لم تُبنَ** — «التحليل الجنائي» موجود كمنهجية موثَّقة واستعلامات GAQL في docs/04، لا كمحرّك في الكود
- **Last commit:** 2026-08-31
- **Live URL:** none (README: لم يُنشر — يحتاج توكن Cloudflare)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| نقاط API | 13 (11 GET + 2 POST) | `grep -o "app\.(get\|post)(" src/index.tsx` · docs/09 يعدّد 12 عنواناً (يضم `/` ولا يفصل `/api/ads/query`) |
| جداول D1 | 3 (+3 فهارس) | `migrations/0001_init.sql` |
| الوثائق | 10 ملفات · 1,553 سطراً | `ls docs` · `wc -l docs/*.md` (README يقول «11 وثيقة» بعدّ README نفسه) |
| وصفات GAQL مُختبرة | 19 | `docs/07-GAQL-COOKBOOK.md` عناوين `###` تحت «استعلامات مُختبرة وتعمل» (19 من 26 `###`؛ الباقي أدوات مساعدة) |
| استعلامات فاشلة موثَّقة | 5 | نفس الملف، جدول «استعلامات تفشل» |
| محرّكات التحليل المخطَّطة | 7 (غير مبنية) | `docs/08-ROADMAP.md` §ب |
| فحوص الصحة | 4 (الأسرار، التوكن، Ads، GSC) | `src/google.ts healthCheck()` |
| حجم الـWorker | 38.57 kB · gzip 14.52 kB | `npm run build` 2026-09-23 |
| كود TypeScript | 758 سطراً (google 318 · index 254 · ui 174 · renderer 12) | `wc -l src/*` |
| الاعتماديات وقت التشغيل | 1 (hono) | `package.json` dependencies |
| إصدار Ads API | v24 (v17–v21 موثَّقة كملغاة) | `src/google.ts ADS_API_VERSION` + `/api/catalog` |
| عمر access_token / هامش الكاش | 3599 ث / −120 ث | `src/google.ts writeCache()` + `/api/token` |
| تحديث اللوحة | كل 5 دقائق (300000 ms) | `src/ui.tsx setInterval` |
| عدد الملفات | 25 | `git ls-files` |
| تجاوز أفقي | 0 على 16 لقطة | فحص Playwright 2026-09-23 (`_meta.json`) |
| Tests | لا اختبارات؛ لا CI | فحص المستودع |
| Users / clients | عميل واحد: كيف الضيافة (جهة معروفة على المنصة) | README |

## التشغيل والتصوير (2026-09-23 — مخطط التسويق)
- `npm install` → `npm run build` ناجح (41 ms). التشغيل الكامل يحتاج مفاتيح Google حقيقية (OAuth + developer token + refresh token) — **لم يُتصل بأي حساب حقيقي**.
- **المحاكاة:** غلاف خارج المستودع (`make/mock/mock-worker.js`) يستورد `dist/_worker.js` كما هو ويعترض `fetch` الخارج إلى `oauth2.googleapis.com` و`googleads.googleapis.com` و`googleapis.com/webmasters` فيردّ ببيانات وهمية معلَّمة «(عرض)»: حساب `0000000000`، 3 حملات بأسماء عامة، 6 كلمات بحث عامة، موقع `example.com`. D1 محلي عبر `wrangler dev --local` مع migration المستودع + 5 صفوف سجل معلَّمة. **الكود الأصلي لم يُغيَّر.**
- **ما جرى تصويره (16 لقطة، 8 × ديسكتوب 1440×900 / جوال 390×844، DPR 2):** اللوحة (3 مواضع تمرير) + 5 استجابات API حقيقية من التشغيل المحلي (`/api/health`، `/api/ads/performance`، `/api/ads/campaigns`، `/api/gsc/queries`، `/api/log`) مقدَّمة كبطاقات طرفية (نفس البايتات، تنسيق فقط).
- **مستبعَد عمداً:** لقطة `/api/catalog` — الاستجابة تحمل بريد المالك مكتوباً في الكود (`src/index.tsx` سطر 219) → لا تُعرض؛ بند تنظيف.
- **كل رقم داخل اللقطات (80,060 ظهور، 3,244 نقرة، 10,490.75 SAR، 71 تحويل، الكلمات…) وهمي من الغلاف ولا يُقتبس على أي تصميم.**

## ملاحظات التنظيف / Cleanup notes
- **بيانات حقيقية في المستودع العام:** معرّف حساب Google Ads في README و`.dev.vars.example` و4 وثائق؛ بريد المالك مكتوب في `src/index.tsx` (catalog)؛ معرّفات حملات حقيقية وأرقام أداء (55 كلمة محذوفة، 8 تغييرات ميزانية، ROAS 0.00) في docs/03–06. لا شيء منها على أي تصميم أو نص في هذه الحزمة. يُنصح بنقل docs/03–06 إلى مستودع خاص أو تعميتها.
- README يصف «محرك تحليل جنائي» و«حرس حساب» — الكود الحالي طبقة اتصال + لوحة قراءة؛ المرحلة 1 لم تُبنَ (docs/08). الادعاء الآمن: «اتصال دائم + GAQL حر + منهجية جنائية موثَّقة».
- README «11 وثيقة» = 10 في docs + README. docs/09 يعدّد 12 نقطة والكود 13 (`/api/ads/query` غير مُعنوَن).
- اللوحة تعتمد Tailwind وFont Awesome من CDN (طلبان خارجيان)؛ `public/static/style.css` فارغ (0 سطر).
- لا اختبارات ولا CI؛ commit واحد؛ لم يُنشر؛ `DASH_KEY` اختياري محلياً (اللوحة و`/api/token` مكشوفان إن نُشر بلا مفتاح — README يقرّ «إلزامي عند النشر»).
