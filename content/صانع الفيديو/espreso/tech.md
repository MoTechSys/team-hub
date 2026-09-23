espreso | صانع الفيديو | 2026-09-23 | draft

# espreso — Technical Sheet

- **Repo:** moain2028/espreso (public) · الفرع الافتراضي `genspark_ai_developer` (لا `main` على origin) · 3 commits كلها بتاريخ 2026-09-18 · لا README.md
- **Primary language / stack:** HTML/CSS/JS خام (ES modules) · Vite 8.3 (بناء متعدد الصفحات + إضافة partials مخصّصة) · Sharp 0.35 لخط أنابيب الصور · لا إطار واجهة ولا تبعيات تشغيل
- **Problem:** مقهى قهوة مختصة (3 فروع في الحديدة) حضوره الرقمي حساب إنستغرام فقط؛ لا قائمة ولا صفحات فروع ولا تواصل ثابت.
- **Solution / core features:** 6 صفحات (index · menu · gallery · story · branches · contact) + 404؛ ثنائي اللغة AR/EN عبر `?lang=` + localStorage مع RTL/LTR؛ قائمة 15 مشروباً في 4 فئات مع فلترة؛ معرض 18 عنصراً مع Lightbox؛ طبقة حركة (reveal/parallax) تحترم prefers-reduced-motion؛ PWA (manifest + أيقونات + اختصارات)؛ SEO (JSON-LD، sitemap، hreflang، OG)؛ رؤوس أمان `_headers`؛ خطوط مستضافة محلياً (Amiri · Cormorant Garamond · IBM Plex Sans Arabic · Manrope)؛ أداة QA بصرية `tools/screenshot.py` وأداة مزامنة إنستغرام.
- **Architecture notes:** partials تُدمج وقت البناء عبر `<!-- @include -->` (صفر تكلفة وقت التشغيل)؛ الصور من `assets/source/**` → Sharp يولّد AVIF/WebP/JPG بأحجام 400–1024 + LQIP base64 في `src/data/images.json` (52 مدخلاً)؛ CSS ملف واحد (cssCodeSplit=false)؛ الهدف es2020.
- **Status:** prototype/ready-to-deploy — يبنى ويعمل محلياً بلا أخطاء؛ لا رابط حي مؤكَّد
- **Last commit:** 2026-09-18 (744acbb)
- **Live URL:** none — sitemap يشير إلى espresso-coffee.pages.dev ولا يستجيب (2026-09-23)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source (file/line or command) |
|---|---|---|
| الصفحات | 6 (+404) | `ls *.html` = 7 ملفات؛ vite.config.js يبني كل .html في الجذر |
| اللغات | 2 (AR/EN) | src/js/i18n.js (KEY espresso_lang، `?lang=`) · `data-ar/data-en` |
| مشروبات القائمة | 15 | src/js/content.js: `grep -c "{ id: '.*', cat:"` = 15 |
| فئات القائمة | 4 (espresso · signature · cold · tea) | content.js `cat:` values |
| عناصر المعرض | 18 | content.js `cap: {` = 18 |
| الفروع | 3 | content.js branches · brand-pack.json branches (3) |
| مدخلات الصور المعالَجة | 52 (ig 24 · derived 12 · kiosk 8 · stock 8) | src/data/images.json |
| ملفات الصور المولَّدة | 419 (139 AVIF · 139 WebP · 141 JPG/SVG) | `find public/img -type f` |
| ملفات الخطوط المستضافة | 24 woff2 | `ls public/fonts` |
| حزمة البناء | JS 69.50 KB (gzip 25.08) · CSS 62.10 KB (gzip 11.11) · index 64.37 KB | ناتج `npm run build` 2026-09-23 |
| ملفات dist | 461 · 20 MB | `find dist -type f`, `du -sh dist` |
| أسطر JS / CSS المصدر | 823 / 695 | `cat src/js/*.js \| wc -l` · `cat src/styles/*.css \| wc -l` |
| ملفات المستودع | 542 | `git ls-files \| wc -l` |
| الالتزامات | 3 | `git log --oneline \| wc -l` |
| التبعيات (تشغيل / تطوير) | 0 / 2 (vite, sharp) | package.json |
| أخطاء الكونسول عند التشغيل | 0 على 18 صفحة×لغة | Playwright run 2026-09-23 |
| متابعو إنستغرام / منشورات (كما يعرضها الموقع) | 1,408 / 102 | index.html س58–59 · brand-pack.json (بيانات ثابتة بتاريخ 2026-09-18 — **لا تُعرض** كرقم مُنجَز لأنها بيانات العميل لا المشروع) |
| الاختبارات | 0 آلية (أداة QA بصرية فقط) | لا test في package.json · tools/screenshot.py |

## ملاحظات التنظيف / Cleanup notes
- **لا README.md** في المستودع ولا فرع main — بند لمحمد؛ الأرقام أعلاه كلها من الكود والبناء.
- **لا رابط حي**: sitemap/robots يشيران إلى espresso-coffee.pages.dev (لا يستجيب).
- **صور تحوي أشخاصاً**: صفحة الحكاية وبعض صور المعرض تُظهر المؤسس وباريستا (ig/mazen-*، ig/barista، interview-*) — لقطات story وgallery المحتوية على وجوه **لا تُستخدم في التصاميم ولا الريل**؛ تبقى في screenshots/ للتوثيق فقط.
- **اسم المؤسس** في content.js وJSON-LD وصفحة الحكاية — لا يُنقل إلى أي نص أو تصميم.
- **أصل الصور**: 24 صورة من حساب إنستغرام العلامة (brand-pack.json: «محفوظة بحقوق الحساب الأصلي»)، 8 صور kiosk (تصوير كشك حديدة لاند بحسب commit 744acbb)، و**8 صور stock** (beans-macro، cappuccino-heart، espresso-crema، espresso-flatlay، hero-beans، latte-leaf، latte-swan، portafilter) بلا ملف ترخيص/مصدر في المستودع — تُفصَح كـ«صور مخزون من طرف ثالث، المصدر غير موثّق» في SOURCES والشرح وتذييل شرائح اللقطات.
- **الحساب @espre__sso وروابط instagram.com** في التذييل والمعرض — جهة العلامة، مسموح داخل اللقطات فقط.
- **لا رقم هاتف** في الكود (زر «راسلنا» يقود إلى إنستغرام).
- أداة sync-instagram تقرأ من عارض عام (Imginn) — اعتبار حقوقي يُذكر.

## اللقطات (screenshots/) — 24 لقطة حقيقية 2x من التشغيل المحلي (vite preview، Chromium، 2026-09-23)
ديسكتوب 1440×900 (12) وجوال 390×844 (12): home AR/EN (+2)، menu AR/EN (+2)، gallery AR/EN (+2)، story AR، branches AR، contact AR. الصفحات صُوِّرت بعد تمرير كامل لتفعيل الحركة والصور الكسولة. لقطات story وgallery-2 تحوي وجوهاً → توثيق فقط.
