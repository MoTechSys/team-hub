almutahassil-site | متخصص SEO | 2026-09-23 | ready

# almutahassil-site — Technical Sheet (المتحصل — موقع نظام التحصيل والسداد الذكي)

- **Repo:** moain2028/almutahassil-site (public) — commitان بتاريخ 2026-08-11 (`docs/00-INDEX.md` يشير إلى نسخة خاصة قديمة على moain2026 — 404 اليوم)
- **Primary language / stack:** HTML5 + CSS3 (custom properties) + Vanilla JS — **بلا إطار، بلا build، بلا CDN JS، بلا تبعيات** (README «المواصفات»؛ `grep '<script src'` يعطي `app.js` و`demo.js` فقط). التبعية الخارجية الوحيدة: Google Fonts (IBM Plex Sans Arabic، preconnect + preload لوزنَي 400/700)
- **Problem:** صندوق تحصيل متعدد الفروع يحتاج موقعاً تعريفياً فاخراً عربياً بالكامل لنظام «المتحصل» (تحصيل ميداني + سداد فوري للخزنة المركزية)، مع لوحة إدارة تجريبية تُظهر شكل المنتج قبل الاشتراك (README؛ `about.html` «الواقع قبل المتحصل»)
- **Solution / core features:** 8 صفحات HTML عربية RTL (`index` رئيسية بسبعة أقسام · `demo` لوحة إدارة تجريبية بأربع بطاقات KPI ورسم أعمدة وجدولَين قابلَين للفرز والتصفية · `features` تسع وحدات مفصّلة بفهرس لاصق · `faq` 12 سؤالاً بأكورديون وبحث فوري · `about` مشكلة/حل + خط زمني بأربع محطات · `contact` نموذج طلب عرض بستة حقول وتحقق · `changelog` خمسة إصدارات · `404`) + `nav-snippet.html` (قالب داخلي) + `brand/presskit.html` (صفحة الهوية). 10 أيقونات 3D squircle 1024×1024 PNG شفافة + 20 WebP محسَّنة (512 و256) عبر `<picture>` مع width/height ضد CLS. أرقام هندية في كل العدّادات. JSON-LD (Organization + SoftwareApplication) وOG وTwitter card على الرئيسية. manifest PWA (`display: standalone`، RTL)، robots.txt، sitemap.xml
- **Architecture notes:** موقع ثابت 100%؛ التفاعلات في `app.js` (IntersectionObserver reveal · عدّادات · قائمة جوال · شريط متحرك · تحقق النموذج) و`demo.js` (بيانات ثابتة + عدّادات + رسم SVG + فرز/تصفية). نظام التصميم في `style.css` بـ14 متغيّراً (`--bg-0..3`، ذهب `#fce38a→#d4af37→#87651a`، نص `#f4f7ff/#b9c6e4/#8695b8`). نقاط استجابة أساسية 420/760/980px (+1080 و560–860 محلياً في الصفحات). `prefers-reduced-motion` في `style.css` و`demo.html`. مسار جودة الأيقونات موثّق في README (توليد بالذكاء الاصطناعي → تدقيق بصري → رفض 5 → إعادة توليد → `fix_icons.py` قصّ + قناع squircle → 10/10 PASS). النشر الأصلي: Caddy `handle_path /mut/*`
- **Status:** موقع مكتمل الصفحات، **بلا رابط حي الآن** (الرابط في README لا يستجيب 2026-09-23)؛ **بلا اختبارات آلية**؛ محتوى الـ demo والعدّادات بيانات عرض مُعلَنة في الصفحة نفسها
- **Last commit:** 2026-08-11 (`git log`)
- **Live URL:** none (انظر links.md)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source (file/line or command) |
|---|---|---|
| HTML pages (public) | 8 | `ls *.html \| grep -v nav-snippet \| wc -l` → 404 · about · changelog · contact · demo · faq · features · index |
| Framework / build / runtime deps | 0 · 0 · 0 | README «المواصفات»؛ لا `package.json`؛ `grep -h '<script[^>]*src' *.html` → app.js، demo.js فقط |
| External requests (non-font) | 0 | `grep -ho 'href="https\?://[^"]*"' *.html` → fonts.googleapis/gstatic + رابط canonical فقط |
| 3D icons | 10 (1024×1024 RGBA PNG) | `ls icons/*.png \| wc -l`؛ PIL size check |
| Optimized WebP variants | 20 (512 + @256 لكل أيقونة) | `ls icons/opt/*.webp \| wc -l` |
| Icon quality pass | 10/10 (بعد رفض 5 وإعادة توليدها) | README «مسار جودة الأيقونات» |
| Modules on features page | 9 | `grep -c '<article class="mod' features.html` |
| Modules in index grid | 9 (8 + «الحضور» بوسم «قريباً») | `app.js` مصفوفة `FEATURES` |
| Capabilities listed | 48 بنداً (features.html) | `grep -oE '<li>' features.html \| wc -l` (الصفحة تكتب «٤٥+») |
| FAQ items | 12 | `grep -oE 'class="faq-item' faq.html \| wc -l` |
| Changelog releases | 5 (١٫٠ → ١٫٤) + ١٫٥ قيد العمل | `grep -c '<article class="rel' changelog.html` |
| Timeline milestones (about) | 4 (Q3 2024 → 2026) | `grep -oE 'class="tl-item' about.html \| wc -l` |
| Contact form fields | 6 (name · phone · org · branches · agents · msg) | `grep -oE 'name="[^"]*"' contact.html` |
| Homepage sections | 7 | README «البنية»: Hero · الوحدات · آلية العمل · التطبيق · الأمان · الباقات · CTA |
| Pricing tiers | 3 (فرع واحد · متعدد الفروع · مخصّص) | `index.html` قسم `#pricing` |
| Security cards (index) | 4 | `index.html` قسم `#security` |
| style.css | 333 سطراً · 22.8 KB (غير مضغوط) | `wc -l style.css` · `wc -c style.css` |
| app.js · demo.js | 7.9 KB · 17.5 KB | `wc -c app.js demo.js` |
| Total source lines (html+css+js) | 3,836 | `wc -l *.html *.css *.js` (بدون nav-snippet) |
| Repo files · size | 61 · 7.8 MB (7.1 MB أيقونات) | `git ls-files \| wc -l` · `du -sh` |
| CSS custom properties | 14 | `grep -oE '^\s*--[a-z0-9-]+:' style.css \| sort -u \| wc -l` |
| Breakpoints (style.css) | 3 (420 · 760 · 980) | `grep -oE '@media[^{]*' style.css` |
| aria-* attributes | 180 | `grep -ohE 'aria-[a-z]+=' *.html \| wc -l` |
| Lazy-loaded images | كل أيقونة (`loading="lazy" decoding="async"`) | `app.js` دالة `pic` · `demo.js` سطر 102 |
| JSON-LD blocks | 1 (Organization + SoftwareApplication) | `index.html` `<script type="application/ld+json">` |
| Sitemap URLs | 3 | `grep -c '<loc>' sitemap.xml` |
| Commits · authors | 2 · 1 | `git log --oneline \| wc -l` |
| Tests | **0** | لا ملف اختبار، لا CI |
| Hero counters (99.9% · 4ث · 100%) | **بيانات عرض** — لا تُنقل كإنجاز | `index.html` سطر 121–123 `data-count` ثابتة في HTML |
| Demo KPIs (4,820,500 ر.ي · 148 سند …) | **بيانات عرض** — تنبيه صريح على الصفحة | `demo.js` «البيانات (تجريبية بالكامل)» + `demo.html` `.demo-note` |
| Changelog claims (4.2s→1.1s · 68% · 72h) | **نص تسويقي للمنتج**، غير قابل للتحقق من الكود | `changelog.html` — لا تُستخدم كأرقام تصميم |
| Users / clients | يُستكمل — لا عملاء موثّقون | — |

## ملاحظات التنظيف / Cleanup notes
- **لا رابط حي**: `suppdizl.gensparkclaw.com/mut/` (README، canonical، sitemap، robots، OG) لا يستجيب 2026-09-23 → canonical/sitemap/OG تحتاج تحديثاً عند النشر على دومين دائم.
- README و`BRAND.md` و`docs/00-INDEX.md` وعنوان الصفحات وJSON-LD `alternateName` تذكر **اسم شخص كاملاً** كاسم الجهة → طُمس في كل اللقطات؛ لا يظهر على أي تصميم أو نص؛ يُوصَف بـ«صندوق تحصيل متعدد الفروع».
- الأيقونات العشر **مولّدة بالذكاء الاصطناعي** (إقرار README) → يُفصَح عنها في SOURCES والشرح، ولا تُقدَّم كتصوير حقيقي.
- `contact.html` يعرض هاتفاً/واتساب نموذجياً (+967 77 000 0000) وبريداً (info@almutahassil.ye) وعنواناً → طُمست في اللقطات.
- `demo.js` يحوي أسماء محصّلين وعملاء **افتراضية**؛ الصفحة تعلن ذلك؛ الاسم الأول في جدول الإنتاجية طُمس لأنه يطابق اسم الجهة.
- `index.html` يقول «عشر وحدات» والشبكة تعرض 9، و`features.html` تقول «تسع وحدات» و«٤٥+ قدرة» بينما البنود 48 → المعتمد على التصاميم: **9 وحدات** (الكود).
- `docs/00-INDEX.md` يذكر مساراً محلياً `/home/work/almutahassil` ومستودعاً خاصاً على moain2026 (404) → يُنقّى.
- `og:image` يشير إلى `assets/og.png` وهو غير موجود (الملف الفعلي `brand/og.png`) → رابط OG مكسور.
- `sitemap.xml` يغطي 3 صفحات من 8 (about · features · contact · changelog غير مضمّنة).
- لا اختبارات، لا CI، commitان فقط بتاريخ واحد — تُذكر في الفجوات.
