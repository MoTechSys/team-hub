espreso | صانع الفيديو | 2026-09-23 | v2

# SOURCES — كل نص ورقم وصورة في الحزمة

## المستودع (قراءة 2026-09-23، commit 744acbb بتاريخ 2026-09-18، الفرع genspark_ai_developer)
- github.com/moain2028/espreso (عام) — لا README؛ المصادر: package.json · vite.config.js · src/js/{content,i18n,images,motion}.js · src/data/{images,brand-pack}.json · src/styles/ · public/ · tools/ · ناتج `npm run build`.

## الأرقام
| الرقم | أين يظهر | المصدر |
|---|---|---|
| 6 صفحات (+404) | كل التصاميم، الريل، النصوص | `ls *.html` = 7؛ vite.config.js يبني كل .html |
| لغتان AR/EN | كل التصاميم | src/js/i18n.js · data-ar/data-en |
| 15 مشروباً · 4 فئات | التصاميم، الكاروسيل 4، الريل، النصوص | src/js/content.js (`{ id:…, cat:` × 15؛ cat ∈ espresso/signature/cold/tea) |
| 18 صورة في المعرض | brief، explainer، IG copy | content.js `cap: {` = 18 |
| 3 فروع | الريل (مشهد الفروع)، explainer | content.js branches · brand-pack.json |
| 139 AVIF + 139 WebP | التصاميم، الكاروسيل 3–4، بطاقة… | `find public/img -name '*.avif' \| wc -l` = 139؛ webp = 139 |
| 52 مدخل صور معالَجة | tech.md | src/data/images.json |
| 24 ملف خط | brief، explainer | `ls public/fonts \| wc -l` |
| JS 69.50 KB · CSS 62.10 KB · index 64.37 KB | brief، explainer، LinkedIn copy | ناتج `npm run build` 2026-09-23 |
| 0 تبعيات تشغيل | التصاميم، بطاقة الرقم «0»، الكاروسيل 4 | package.json (dependencies غير موجودة؛ devDependencies: vite, sharp) |
| 0 أخطاء كونسول | brief، tech.md | Playwright run على 18 صفحة×لغة، 2026-09-23 |
| 3 commits · 542 ملفاً | tech.md | `git log --oneline \| wc -l` · `git ls-files \| wc -l` |
| Squarespace $19/$29/$49/$99 شهرياً (سنوي) | research | https://www.squarespace.com/pricing (2026-09-23) |
| Linktree خطة مجانية | research | https://linktr.ee/s/pricing (2026-09-23) |

## النصوص
- brief.ar/en، explainer، copy: كل جملة من الكود (content.js نصوص الواجهة، package.json الوصف، vite.config.js البنية) وtech.md. لا README في المستودع. لا اسم شخص (اسم المؤسس الموجود في content.js وstory.html **لم يُنقل**) ولا هاتف (لا يوجد في الكود).
- اسم العلامة «إسبرسو كوفي / Espresso Coffee» يظهر كجهة داخل اللقطات وفي العنوان (كما في مشاريع المنصة السابقة)؛ المدينة «الحديدة» من package.json.
- research: كل ادعاء عن منافس برابطه وتاريخ الوصول.

## الصور (24 لقطة حقيقية في screenshots/)
- المصدر: تشغيل محلي `npm run build` ثم `vite preview` (Chromium/Playwright، deviceScaleFactor 2) بتاريخ 2026-09-23. ديسكتوب 1440×900 وجوال 390×844، AR وEN.
- **لقطات تحوي وجوهاً (للتوثيق فقط، غير مستخدمة في A/B/C):** desktop-story-ar، mobile-story-ar، desktop-menu-ar/en، mobile-menu-ar/en، desktop-gallery-ar، mobile-gallery-ar-2 (صورة المؤسس/باريستا في hero القائمة والحكاية وشبكة المعرض). المستخدمة في التصاميم والريل: home AR/EN (+2)، menu-ar-2، gallery-ar/en، branches-ar، contact-ar — بلا وجوه واضحة.
- **أصل صور الموقع نفسه (إفصاح):** 24 صورة من حساب إنستغرام العلامة عبر عارض عام (brand-pack.json: «محفوظة بحقوق الحساب الأصلي»)؛ 8 صور كشك «حديدة لاند» (commit 744acbb: kiosk photography)؛ **8 صور مخزون من طرف ثالث بلا ملف ترخيص/مصدر في المستودع** (beans-macro، cappuccino-heart، espresso-crema، espresso-flatlay، hero-beans، latte-leaf، latte-swan، portafilter — تظهر في القائمة والرئيسية). لا صور مولّدة بالـAI معروفة. هذا الإفصاح مذكور في explainer وresearch وهنا.

## الهوية
- 02-brand/README.md (portfolio-hub): Navy/Ink/Amber/Sand/Mist + لون شريحة «مشاريع صغيرة»؛ الخافت #A3B1C0؛ IBM Plex Arabic / Inter / JetBrains Mono. الأساس بلا شعار؛ «بشعار» = wordmark نصّي؛ زر الدعوة في nologo «راسلني / DM me».
- الموسيقى: 02-brand/scripts/reels/bgm-tech-minimal.mp3 (أصل الفريق).
