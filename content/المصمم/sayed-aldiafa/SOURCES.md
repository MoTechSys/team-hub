sayed-aldiafa | المصمم | 2026-09-23 | draft

# SOURCES — sayed-aldiafa project pack v2

المستودع: https://github.com/moain2028/sayed-aldiafa · commit bd2d003 (2026-08-09) · استُنسخ 2026-09-23. كل الأرقام أُعيد قياسها بأوامر مذكورة في tech.md.

## الأرقام
| الرقم | أين يظهر | المصدر |
|---|---|---|
| 15 صفحة | كل التصاميم، الريل، الشرح، النصوص | `ls *.html \| wc -l` = 15 · sitemap.xml 15 `<loc>` |
| 0 اعتمادية / بلا build | كل التصاميم، بطاقة الرقم، الريل | لا package.json في الشجرة؛ README «نظرة عامة» |
| 30 رابط واتساب | التصاميم الأساسية (إحصائية ثالثة) | `grep -oh 'wa.me/966' *.html \| wc -l` = 30 |
| ≈280 KB HTML+CSS | كاروسيل 4 | 286,403 B مجموع *.html + sv.css (python) |
| 56/56 صورة بنص بديل | كاروسيل 4، الريل، الشرح، النصوص | regex على كل `<img>`: 56 وسماً، 56 بـ alt غير فارغ |
| 9 صفحات خدمة | كاروسيل 2، الريل، الشرح | الملفات art/zamzam/sweets/hospitality/equipment/climate/av/coffee/events + services.html «تسع خدمات» |
| 8 حقول نموذج | كاروسيل 3، الريل، الشرح | `grep -E '<(input\|select\|textarea)' booking.html` = 8 |
| 27 كتلة JSON-LD (1 LocalBusiness · 1 WebSite · 1 OfferCatalog · 18 Service · 18 Offer · 14 BreadcrumbList) | الشرح، البحث، النصوص | `grep -c 'application/ld+json' *.html` مجموع 27؛ `grep '"@type"'` للأنواع |
| 7 وسوم OG + canonical لكل صفحة | الشرح، البحث | `grep -c 'property="og:' *.html` = 7 لكل صفحة؛ `rel="canonical"` = 1 |
| ≈24 KB CSS مضمّن في index | الشرح | python: مجموع `<style>` = 24,210 B |
| ≈10 KB sv.css | الشرح | `wc -c sv.css` = 10,091 |
| 480px عرض أقصى | الشرح، tech.md | `sv.css:10` و`index.html:50` `.app{max-width:480px}` |
| 13 مدينة | brief | coverage.html قسم CITIES (13 اسماً) |
| آخر commit 2026-08-09 · 5 commits | الشرح، البحث | `git log` |
| 152 ذكراً لـ«الرياض» | tech.md، البحث | `grep -rnoE 'الرياض' *.html \| wc -l` |
| 68–83 وسم script عند المنافسين، 0–1 JSON-LD، 6–10 OG، 1–14 واتساب | البحث | curl لكل رئيسية 2026-09-23 ~05:00 UTC + regex (الروابط في research.md) |
| 2–3 وسوم script في صفحاتنا | البحث | `grep -c '<script' *.html` = 2 أو 3 لكل صفحة |

## النصوص
- عنوان/وصف المشروع، الخدمات التسع، «السعر حسب المناسبة»، «الرياض ومحافظاتها»: index.html · services.html · packages.html · coverage.html.
- «الملف الذي تحرّره هو الملف الذي يُخدَم» و«يعمل في أي مكان — استضافة مشتركة، S3، GitHub Pages، USB»: README «لماذا بلا إطار».
- آلية النموذج → واتساب: `index.html` سطر 971–975 و`booking.html` سطر 147–148 (`#send`, `aria-live`).
- الوصولية (لا maximum-scale، ≥44px، aria-live، 16px، prefers-reduced-motion): README «الوصولية» + grep تأكيدي (`maximum-scale` = 0 ظهور؛ `prefers-reduced-motion` في index.html).
- «كل الصور مولّدة بالذكاء الاصطناعي»: README «ما زال مطلوباً» — مُفصَح في تذييل كاروسيل 2 AR/EN، الشرح، IG copy، وهذا الملف.
- تعارض README (جنوب المملكة/13 صفحة/8 خدمات/~32KB/≈1.1MB): README مقابل الكود — موثّق في tech.md «ملاحظات التنظيف»؛ لا يُعرض أي رقم من README المتعارض.
- عطل `.chips` في الرئيسية: `sv.css:76` يعرّفها، `index.html` لا يعرّفها (grep = 0) — لُوحظ في اللقطة.
- نصوص CTA («أبني لمشروعك موقعاً بلا تعقيد — راسلني») من قالب brief §للتواصل لشريحة المشاريع الصغيرة — draft للمحرر.

## الصور
- كل اللقطات (30 في screenshots/ + 3 مركّبات shot-*.png + reel-mobile-home-full.png): Playwright Chromium على `python3 -m http.server 8765` محلي، 1440×900 و390×844 بـ scale 2، locale ar-SA، networkidle + 1.5 ث (`shoot.py`).
- **طمس برمجي قبل الالتقاط:** أرقام الجوال → `+966 5• ••• ••••`؛ أسماء الشهادات `<cite><b>` → «عميل — تجربة موثّقة». لا رقم ولا اسم شخص في أي لقطة أو تصميم.
- `shot-desktop-*-crop.png`: قصّ 60% من وسط لقطة الديسكتوب (الموقع عمود 480px متمركز على الحاسوب) — لا تعديل على المحتوى.
- `shot-mobile-trio/quad*.png`: 3–4 لقطات جوال حقيقية جنباً إلى جنب على خلفية #050506 (لون الموقع) — بلا تعديل على المحتوى.
- `reel-mobile-home-full.png`: لقطة تمرير للرئيسية مع إخفاء العناصر الثابتة (tabs/wa/drawer) لأن README يحذّر أن full-page تشوّهها؛ **وحُذف قسم «لماذا نحن» المعطوب (.chips)** من لقطة التمرير — موثّق هنا وفي research.md.
- صور الموقع نفسها (داخل اللقطات) مولّدة بالذكاء الاصطناعي بإقرار README؛ لا صورة مولّدة أضفتها أنا.
- الموسيقى: `reel/music.mp3` مولّدة بـ CassetteAI/music-generator 2026-09-23 (30 ث) — بلا حقوق طرف ثالث.

## الهوية
- 02-brand/README.md (portfolio-hub): Navy/Ink/Amber/Sand/Mist + شريحة «مشاريع صغيرة» #F4A62A؛ النص الخافت #A3B1C0؛ IBM Plex Sans Arabic / Inter / JetBrains Mono. الأساس بلا شعار؛ نسخة logo = wordmark نصّي «معين العباسي / Moain Al-Abbasi».
- التذييل: github.com/moain2028/sayed-aldiafa (مستودع عام). لا رابط حي (links.md).
