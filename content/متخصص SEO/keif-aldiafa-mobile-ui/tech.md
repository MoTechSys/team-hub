keif-aldiafa-mobile-ui | متخصص SEO | 2026-09-23 | ready

# keif-aldiafa-mobile-ui — Technical Sheet (كيف الضيافة — واجهة جوال فاخرة)

- **Repo:** moain2028/keif-aldiafa-mobile-ui (public) — commitان 2026-08-08
- **Primary language / stack:** HTML + CSS + Vanilla JS — صفحة واحدة، بلا إطار، بلا build، بلا تبعيات (README «التبعيات: لا شيء»؛ `grep '<script src'` → `app.js` فقط). التبعية الخارجية الوحيدة: Google Fonts (Almarai + Amiri)
- **Problem:** عرض تجربة جوال فاخرة لخدمات ضيافة عربية (قهوة مختصة، حلويات، تنسيق موائد وفعاليات) بواجهة RTL بتباين مقيس لا تقديري، وزر واتساب عائم لا يحجب النص ولا يتداخل مع الشريط السفلي (README؛ تعليقات `app.js`)
- **Solution / core features:** شاشة جوال واحدة: ترويسة بقائمة جانبية (drawer + scrim + Escape)، بطل بصورة وعنوان Amiri بتدرّج ذهبي، زر «احجز الآن» بلمعة متحركة، 4 مربعات تصنيف بصور، بطاقة «توقيعنا»، 6 بطاقات خدمات بأيقونات SVG مضمّنة، شريط ثقة بثلاثة أرقام (بيانات عرض)، تذييل، زر واتساب عائم يختفي أثناء التمرير ويعود بعد 420 ms، شريط تبويب سفلي بأربعة تبويبات بأيقونات SVG. على الشاشات > 520px تُعرض داخل إطار جهاز بنسبة 617/1376؛ تحتها ملء الشاشة
- **Architecture notes:** 21 متغيّر CSS (`:root`)؛ لوحة ألوان «مقيسة بكسل-بكسل من مرجع 617×1376» (تعليق `styles.css`)؛ 5 نقاط تدرّج ذهب؛ الزر العائم `position:fixed` مرسى على `--tabbar-h: 58px` مع `--fab-safe: 70px` محجوزة؛ RTL بـ`right/left` الفيزيائي للعائم (README «RTL»)؛ `prefers-reduced-motion` عبر `*{transition:none;animation:none}`؛ الصور بـ`width/height` و`loading="lazy"`
- **Status:** واجهة مكتملة (prototype/عرض) — **بلا رابط حي** (لا رابط في README؛ لا canonical/OG/sitemap/robots)؛ **بلا اختبارات آلية**؛ الصور السبع **مولّدة بالذكاء الاصطناعي** (README: `nano-banana-pro`؛ commit «الأصول المستخدمة كلها مولّدة»)
- **Last commit:** 2026-08-08 (`git log`)
- **Live URL:** none (انظر links.md)

## الأرقام ومصادرها / Numbers & sources — كلها من قياسي 2026-09-23
| Metric | Value | Source (file/line or command) |
|---|---|---|
| Source files | 3 (index.html · styles.css · app.js) | `git ls-files` |
| index.html · styles.css · app.js (raw) | 11,820 · 17,479 · 1,913 B = **31.2 KB** | `wc -c` (README يقول 11.8/17.5/1.9 KB — مطابق) |
| Same, gzip | 3,398 · 5,514 · 820 B = **9.7 KB** | `gzip -c f \| wc -c` |
| Images | 7 JPG · **603,565 B (590 KB)** | `du -b assets/opt/*` (README «589KB» — مطابق بالتقريب) |
| Image dimensions | 4 × 700² (تصنيفات) · 560² (دلّة) · 1600×893 (بطل) · 1400×781 (نسيج) | PIL |
| Total local page weight | **≈ 635 KB** (31.2 KB كود + 590 KB صور + favicon لا شيء) | مجموع أعلاه؛ سجل الشبكة: 9 طلبات محلية بـ content-length 513,270 B (texture لا يُحمَّل في اللقطة الأولى) |
| Requests on first load | **20** = 9 محلية + 11 Google Fonts (CSS + 10 woff2) | Playwright `response` log (mobile 390×844) |
| External runtime deps | 0 (خطوط فقط) | README؛ `grep -h '<script[^>]*src' index.html` → app.js |
| LCP (local server, Chromium headless) | **232 ms** mobile · 236 ms desktop | PerformanceObserver `largest-contentful-paint` (`shoot.py`) — خادم محلي؛ ليس مقياس إنتاج |
| DOMContentLoaded · load | 189 · 289 ms (mobile) | `performance.getEntriesByType('navigation')` |
| WCAG contrast — elements measured | **15** نصّاً · **15/15 ≥ 4.5:1** (AA) | `getComputedStyle` + صيغة WCAG relative luminance في `shoot.py` (`measure.json`) |
| Lowest / highest ratio | foot_tag **5.00:1** (8 px) · sec_head/trust/foot_brand **15.89:1** | `measure.json` contrast_mobile |
| README's 11 values re-measured | 8/8 المُسمّاة مطابقة (card_title 14.84 · hero_sub 14.54 · cta_note 12.27 · sig_kicker 11.81 · tile_label 11.79 · card_desc 10.65 · trust_span 7.05 · foot_tag 5.00) · tab_txt **7.45** لا 5.00 (README يجمعه مع foot_tag) | مقارنة `measure.json` بجدول README |
| Hero title contrast | غير قابل للقياس — نص بتدرّج (`background-clip:text`، اللون شفاف) | `measure.json` hero_title.skipped |
| FAB size · FAB↔tabbar overlap | 46×46 px · **0 px** تداخل (فجوة 6–7 px) | `getBoundingClientRect` desktop وmobile (scrolled) |
| FAB hides on scroll | yes (`is-hidden` بعد حدث التمرير، يعود بعد 420 ms) | `app.js` سطر 36–47؛ تحقق Playwright |
| Card texts under FAB at rest | 1–2 نصوص في الإطار | `getBoundingClientRect` — لذلك يختفي أثناء التمرير (تصميم مقصود، تعليق `app.js`) |
| CSS custom properties | 21 | `grep -oE '^\s*--[a-z0-9-]+:' styles.css \| sort -u \| wc -l` |
| Breakpoints | 1 (`max-width:520px`) + `prefers-reduced-motion` | `grep -oE '@media[^{]*' styles.css` |
| aria-* attributes | 19 | `grep -c 'aria-' index.html` |
| Inline SVG icons | 10 (6 بطاقات + 4 تبويبات) + واتساب | `grep -c '<svg' index.html` = 11 |
| Sections | 6 (hero · tiles · signature · services · trust · foot) + header + tabbar + drawer | `index.html` |
| Service cards · tiles · tabs · drawer links | 6 · 4 · 4 · 6 | `index.html` |
| Commits · authors | 2 · 1 | `git log` |
| Tests | **0** | لا ملف اختبار |
| Trust numbers (+500 مناسبة · 4.9 · 3 مدن) | **بيانات عرض** — لا تُنقل | `index.html` سطر 155–161 نص ثابت |
| Lighthouse | غير مقاس (لا Chrome كامل/Lighthouse في البيئة) — البدائل أعلاه (الحجم، الطلبات، LCP محلي) | — |

## ملاحظات التنظيف / Cleanup notes
- **لا رابط حي**: لا نشر ولا دومين؛ لا `<meta description>`/OG/canonical/manifest/robots/sitemap في الصفحة — تُضاف قبل أي نشر.
- **الصور السبع مولّدة بالذكاء الاصطناعي** (README + commit b039e58) → إفصاح إلزامي في تذييل شرائح اللقطات + SOURCES + الشرح.
- **زر واتساب** `wa.me/966500000000` — رقم نائب في `href` فقط (لا يظهر نصاً على الشاشة)؛ لا يُنقل لأي تصميم أو نص.
- **عيب على الديسكتوب:** القائمة الجانبية `.drawer` تُموضَع نسبةً إلى `.device-stage` لا إلى `.phone` (`position:absolute; inset-block:0; right:0`) فتفتح خارج إطار الجهاز على الشاشات > 520px (لقطة `desktop-05-frame-drawer.png` — أرشيف فقط). على الجوال (< 520px) تعمل صحيحاً.
- **reduced-motion جزئي:** `*{animation:none!important}` لا يطابق `::after`، فلمعة زر «احجز الآن» (`.btn-gold::after` sheen) تستمر رغم تفضيل تقليل الحركة (قياس `getComputedStyle(el,'::after').animationName` = sheen).
- **أحجام خط صغيرة:** foot_tag 8 px، trust_span 8.2 px، tile_label 8.6 px على عرض 390 — تباين AA محقَّق لكن الحجم دون 12 px.
- `shots/v8-*.png` لقطات المؤلف — لا تُستخدم؛ لقطاتنا في `screenshots/`.
- اسم العلامة «كيف الضيافة» له 4 مشاريع أخرى على المنصة — يُقدَّم هذا كنمط تقني، لا كعلامة.
