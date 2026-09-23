zawada-al-dukkan | مهندس | 2026-09-23 | project-pack v2

# مصادر كل نص ورقم وصورة في الحزمة (المعيار v2 §G)

المرجع: github.com/moain2028/portfolio-hub → 01-projects/zawada-al-dukkan/ (brief.ar/en.md · tech.md · links.md) + README المستودع + الصفحة الحية (قراءة وتصوير 2026-09-23).

## A) التصاميم الـ24 + B) الكاروسيل/البطاقة/البانر — النصوص
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| السطر التمهيدي | ماركت زوادة الدكان | Zawada Al-Dukkan Market | brief H1 |
| العنوان | واجهة بقالة فاخرة تطلب عبر واتساب | A premium grocery storefront that orders through WhatsApp | brief H1 |
| اسم المستودع | zawada-al-dukkan | — | tech.md |
| الوصف | أسلوب مستوحى من الضيافة الراقية: لون تركوازي وتدرّج ذهبي، خلفية متدرّجة متحركة وتأثيرات زجاجية، وتخطيط عربي RTL مع بيانات SEO مهيكلة — والطلب يُرسل رسالة واتساب جاهزة. | A look borrowed from fine hospitality … ordering sends a ready WhatsApp message. | brief «الحل / Solution» |
| رقم 1: 20 منتجاً — بيانات عرض تجريبية | ✓ | ✓ | brief الحل · tech.md الأرقام (lib/mockData.ts) · README |
| رقم 2: 10 فئات | ✓ | ✓ | brief الحل · README |
| رقم 3: 0 بوابة دفع، 0 خادم | ✓ | ✓ | brief المشكلة («دون … بوابة دفع») · tech.md الحل («بلا بوابة دفع ولا خادم») |
| التاجات | Next.js · TypeScript · Tailwind CSS · Framer Motion · JSON-LD · RTL · GitHub Pages | — | tech.md «التقنيات». **بلا رقم إصدار Next.js** لأن README (15) وpackage.json (14.2) متعارضان — المعيار v2: لا يُعرض |
| الجمهور | لأصحاب البقالات والمحلات الصغيرة … | For grocery and small-shop owners … | brief «لمن يفيد / Who it's for» |
| CTA | تريد واجهة مثلها لدكانك؟ راسلني | Want one like it for your shop? DM me | brief «تواصل / Contact» |
| الشارة | أفراد | Individuals | tech.md الشريحة · لونها #22B08A من 02-brand |
| الرابط (تذييل) | github.com/moain2028/zawada-al-dukkan | نفسه | توجيه مدير المنتج 2026-09-23 (حساب موحّد للدفعة؛ تحقّقت HTTP 200) |
| عنوان شريط المتصفح | moain2026.github.io/zawada-al-dukkan — الصفحة الرئيسية — الموقع الحي | … Home — live site | links.md (الموقع الحي 200) |
| الكاروسيل 1–5 | المشكلة · الحل · كيف يعمل · بالأرقام · الدعوة | The problem · The solution · How it works · By the numbers · The ask | brief (المشكلة/الحل/لمن يفيد/تواصل) · tech.md (الحل، SEO GroceryStore) — النص الكامل في render.py CAROUSEL مع مصدر كل شريحة |
| بطاقة الرقم الواحد | 0 — بوابة دفع · 0 خادم | 0 — payment gateway · 0 server | brief المشكلة/الحل · tech.md |
| بانر المقال | كيف تبني واجهة بقالة فاخرة تطلب عبر واتساب — بلا بوابة دفع ولا خادم | How to build a premium grocery storefront … | عنوان مقترح مركّب من brief H1 + المشكلة (زاوية محتوى 1 في research) |
| الشعار النصي (نسخة logo فقط) | معين العباسي | Moain Al-Abbasi | المعيار §A |

## C) الريل (AR + EN، 18 ث، 1080×1920، بلا شعار)
- كل نص على الشاشة من brief/tech.md — الجدول الكامل في copy.ar/.en «نص الريل».
- الأرقام: 20 (بيانات عرض تجريبية) · 10 · 0 · 0 · 1 — نفس مصادر A.
- الموسيقى: `02-brand/scripts/reels/bgm-tech-minimal.mp3` — مولَّدة آلياً بلا حقوق طرف ثالث (02-brand/scripts/reels/README.md).
- الأداة: `reel/reel_nologo.py` = نسخة من خط إنتاج الفريق `02-brand/scripts/reels/reel.py` بإزالة الـlockup (المعيار v2 §C) وتحديث اللون الخافت إلى #A3B1C0. المواصفات في `reel/zawada-ar.json` و`reel/zawada-en.json`.
- لا مشهد خطأ/404؛ كل اللقطات من `screenshots/`.

## اللقطات — حقيقية 100%، مصوّرة 2026-09-23 من الموقع الحي
`screenshots/` في الحزمة (12 + 2 صفحة كاملة)، Playwright Chromium بـ device_scale_factor=2:
- desktop-01-hero … desktop-06-phase-status (1440×900 @2x = 2880×1800) + desktop-full
- mobile-01-hero … mobile-06-phase-status (390×844 @2x = 780×1688، iPhone UA) + mobile-full
- الأقسام: الهيرو · الفئات · عروض اليوم · شبكة العروض · المنتجات المميزة · حالة المرحلة 1. سكربت الالتقاط: `shoot.py`.
- **تنبيه محتوى الواجهة:** الصفحة الحية تُظهر «4.8 تقييم العملاء» و«12 بلد منشأ» و«+20 منتج فاخر» وأسماء منتجات/موردين وأسعاراً — كلها **محتوى واجهة تجريبي (mock) لا مقاييس**، ولم تُنقل إلى أي نص أو شريحة أرقام (توجيه مدير المنتج 2026-09-23 + tech.md «تنبيهات»).
- صور المنتجات داخل اللقطات من Unsplash/Pexels (tech.md · README) — ليست تصوير عميل.
- الصفحة الحية HTML ثابت بـ Tailwind CDN، لا تطبيق Next (tech.md) — اللقطات تمثّل هذه النسخة.

## D) الشرح · E) البحث · F) النصوص
- explainer.ar/.en: ذيل مصادر في كل ملف (brief · tech.md · README · الصفحة الحية).
- research.md: كل ادعاء برابط + تاريخ وصول 2026-09-23 (WhatsApp FAQ ×2 · take.app · jotform · store.link · origami.sa)؛ التموضع من tech.md فقط.
- copy.ar/.en: LinkedIn ≤120 كلمة (AR 106 / EN 117) · X ≤280 حرف (AR 242 / EN 270) · IG ≤150 كلمة (AR 88 / EN 111) · نص الريل — كلها draft للمحرر.

## ما لم يُستخدم عمداً
- «متجر إلكتروني» / «سلة» / «إتمام طلب» كمنجز — السلة والطلب في Phase 3 غير المنجزة (tech.md تنبيهات).
- رقم إصدار Next.js (تعارض) · النطاق zawada-aldukkan.com (غير مفعّل) · رقم واتساب الطلب (رقم هاتف شخصي في README) · أرقام الواجهة التجريبية 4.8/12/+20.
- أيقونة M / lockup — ممنوعة في الأساس والريل (المعيار).

## الهوية (02-brand/README.md)
Navy #0E2A47 · Ink #08172B · Amber #F4A62A · Sand #F7F5F0 · Mist #DCE3EA · شريحة أفراد #22B08A · النص الخافت #A3B1C0 (تحديث معتمد 2026-09-23). خطوط IBM Plex Sans Arabic / Inter / JetBrains Mono. تباين: Sand/Navy 13.4 · Amber/Navy 7.2 · Mist/Navy 11.3 · #A3B1C0/Navy 6.7 · نص الشارة #D3F5EA على خلفيتها ≥ 7.

## التحقق الآلي
38 PNG بالمقاسات الدقيقة (Pillow) + فحص DOM لكل قطعة (لا عنصر خارج اللوحة، لا تداخل نص/أجهزة، لا نص مقطوع في الشارات/التاجات/الأرقام). الريلان: h264 1080×1920 + aac، 18.0 ث (ffprobe).
