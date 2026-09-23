dallat-alkaif-static | المحرر | 2026-09-23 | draft

# dallat-alkaif-static — Technical Sheet

- **Repo:** moain2028/dallat-alkaif-static (public) — التوأم الثابت لـ dallat-alkaif-nextjs (#24 على المنصة)
- **Primary language / stack:** HTML5 · CSS3 · JavaScript (ES2020) — بلا إطار، بلا build، 0 تبعية (لا package.json)
- **Problem:** موقع ضيافة فاخر لجنوب السعودية يُرفع على أي استضافة ثابتة ويعمل بلا Node.js إطلاقاً (README §ملاحظة).
- **Solution / core features:** 13 صفحة عربية RTL بالأسود والذهبي: رئيسية + خدمات + باقات + حجز + معرض + 8 صفحات خدمة. تنقّل بشريط تبويب سفلي ثابت، نموذج حجز 8 حقول يحوّل إلى رسالة واتساب، أكورديون أسئلة، Open Graph في الصفحات الـ13، بلا قفل تكبير (WCAG 1.4.4). تنسيق الرئيسية مضمَّن في `<style>`؛ بقية الصفحات تشترك `sv.css`.
- **Architecture notes:** ملفات مسطّحة في الجذر + `assets/`. JS في صفحتين فقط (index: 38 سطراً · booking: 44). الخطوط من Google Fonts (نسخة Next.js تستضيفها محلياً). مبني للجوال أساساً بعرض أقصى 480px (README §الاستجابة) — على الديسكتوب يظهر كعمود متوسّط.
- **Status:** production-ready static (README: «الجميع أخضر») — لكن بلا رابط حي مؤكَّد
- **Last commit:** 2026-08-07 (commit واحد)
- **Live URL:** none — og:url يشير إلى toalgzwc.gensparkclaw.com/keif/ ولا يستجيب (curl 2026-09-23: 000)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source (file/line or command) |
|---|---|---|
| Pages | 13 HTML | `ls *.html \| wc -l` (يطابق شارة README) |
| Dependencies | 0 (لا package.json ولا node_modules) | `ls`; README شارة dependencies-0 |
| Build step | none | README §التشغيل: `python3 -m http.server` يكفي |
| Commits | 1 · 2026-08-07 | `git log` |
| HTML+CSS source | 201,970 B ≈ 197 KB · 2,798 سطراً | `du -cb *.html sv.css` · `wc -l` |
| index.html | 36,977 B (تنسيق مضمَّن) | `wc -c index.html` — README يقول «~32KB» للتنسيق؛ الملف كله 36 KB |
| sv.css | 10,091 B | `wc -c sv.css` |
| JavaScript | 82 سطراً في صفحتين (index 38 · booking 44)، 0 KB خارجي | `sed -n '/<script>/,/<\/script>/p' \| wc -l` |
| Images | 14 JPEG · 2,241,049 B ≈ 2.1 MB في المستودع؛ **المستخدَم منها 12 صورة = 963,862 B ≈ 941 KB** (يطابق README)؛ hero.jpg وs1.jpg (1.22 MB) غير مُشار إليهما من أي صفحة | `du -cb assets/*` · grep لكل اسم في *.html |
| img tags | 23 · 0 منها بخاصية height | `grep -o '<img' *.html \| wc -l` · بوابة README |
| Open Graph | 7 وسوم × 13 صفحة | `grep -oh "og:[a-z:]*" *.html \| sort \| uniq -c` |
| maximum-scale | 0 | grep |
| Out-of-scope cities / old brand | 0 | بوابة README (grep الرياض|جدة|كيف الضيافة…) |
| Cities in coverage | 13 | `grep -o <13 أسماء> coverage.html \| sort -u \| wc -l` |
| WhatsApp/tel links | 25 wa.me + tel: في كل صفحة، رقم واحد موحّد | grep — **مطموس في اللقطات** |
| Console errors (local run) | 0 (فقط 404 favicon.ico — لا ملف favicon في المستودع) | shoot.js على 20 صفحة/مقاس |
| Horizontal scroll @390 | 0 صفحات من 10 | shoot.js `scrollWidth > innerWidth` |

## المقارنة المقاسة مع التوأم dallat-alkaif-nextjs (نفس الجهاز، خادم محلي، كاش معطَّل، جوال 390×844، Google Fonts محجوبة للثابت)
| المؤشر | static | nextjs (out/ بعد `next build`) | المصدر |
|---|---|---|---|
| الصفحة الرئيسية — طلبات | 8 | 47 | measure3.js |
| الصفحة الرئيسية — نقل كلي | 558 KB (صور 522 · HTML 36 · JS 0) | 1,525 KB (JS 494 · RSC prefetch 524 · صور 341 · HTML 122 · CSS 43) | measure3.js |
| صفحة القهوة — طلبات / نقل | 3 / 70 KB | 30 / 907 KB | measure3.js |
| صفحة الحجز — طلبات / نقل | 4 / 87 KB | 27 / 799 KB | measure3.js |
| JavaScript للإطار | 0 KB | ≈494 KB (7 chunks) | measure3.js · `du -cb out/_next/static/chunks/*.js` = 636 KB على القرص |
| ملفات HTML الناتجة | 13 | 16 | `find out -name "*.html" \| wc -l` |
| تبعيات التطوير | 0 | 280 مجلداً في node_modules (3 runtime + 6 dev في package.json) | `ls node_modules \| wc -l` · package.json |
| كود المصدر | 2,798 سطر HTML/CSS | 3,816 سطر TS/TSX | `wc -l` |
| حجم المستودع بلا .git | 2.5 MB | 2.1 MB (+ out/ 5.4 MB بعد البناء) | `du -sh` |
| الخطوط | Google Fonts (طلب خارجي) | 12 ملف woff2 محلي (452 KB) | README · `du -sh public/fonts` |
| التخطيط | جوال أولاً، أقصى 480px | متجاوب كامل | README الثابت §الاستجابة |
ملاحظة صدق: نسخة Next.js تحمّل مسبقاً (prefetch) كل الصفحات المرتبطة عند فتح الرئيسية (RSC 524 KB) — هذا يجعل التنقّل اللاحق فورياً؛ المقارنة أعلاه لأول تحميل فقط. الخطوط المحلية في Next لم تُحمَّل في القياس (مسار /fonts بلا basePath → 404 على خادم بسيط؛ 7–8 طلبات 404 في كل صفحة) — تُصلح بوضع `assetPrefix` أو خدمة الجذر.

## اللقطات (screenshots/ — 2x، حقيقية من الخادم المحلي، 2026-09-23)
desktop-01..10 (1440×900) وmobile-01..10 (390×844): home · services · packages · booking · gallery · coffee · coverage · events · sweets · zamzam.
**تطميس مُعلَن:** رقم واتساب/الجوال في الأزرار وروابط wa.me وtel: (40 موضعاً) استُبدل بـ 9665XXXXXXXX / +966 5X XXX XXXX في نسخة عمل منفصلة. **الصور مولَّدة بالذكاء الاصطناعي** (README §ما زال مطلوباً: «كل الصور الحالية مولَّدة بالذكاء الاصطناعي») — يُفصَح في تذييل شرائح اللقطات وSOURCES والشرح.

## ملاحظات التنظيف / Cleanup notes
- hero.jpg وs1.jpg (1.22 MB) غير مستخدمَين — تُحذفان فينزل المستودع إلى ≈1.2 MB.
- لا favicon.ico → 404 في كل صفحة.
- og:url يشير إلى نطاق ميت (toalgzwc.gensparkclaw.com/keif/) — يُحدَّث عند النشر (README يشرح الأمر).
- README يربط النسخة الأحدث بـ moain2026/… بينما المستودع العام moain2028/…
- الخطوط من Google Fonts (طلب خارجي + خصوصية) — README نفسه يقترح الاستضافة المحلية.
- رقم الجوال الحقيقي في README وفي 13 صفحة (مقصود للعميل، لكنه يمنع أي لقطة بلا تطميس).
