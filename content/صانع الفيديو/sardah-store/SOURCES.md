sardah-store | صانع الفيديو | 2026-09-23 | project-pack v2

# مصادر كل نص ورقم وصورة

## النصوص على التصاميم والريل
| النص | المصدر |
|---|---|
| «عبايات سردة» / «Sardah Abayas» | brief.ar/en.md — H1 |
| «بوتيك رقمي فاخر يبيع عبر واتساب لا عبر سلّة» / «A luxury digital boutique that sells through WhatsApp, not a cart» | brief — H1 |
| «موقع ترويجي عربي RTL بالكامل بهوية «شامبين نيود» دافئة — لا سلّة ولا دفع؛ كل دعوة تقود إلى واتساب» / EN equivalent | brief — الحل / Solution |
| «20 قطعة بصفحة لكل قطعة» / «20 pieces, a page each» | brief — الحل؛ tech.md — products.ts (20 SKUs) |
| «33 صفحة ثابتة» / «33 static pages» | brief — النتيجة / Result (README) |
| «دليل مقاسات ومعرض» / «Size guide + gallery» | brief — الحل |
| «دعم تقليل الحركة» / «Reduced-motion support» | brief — النتيجة؛ tech.md — Framer Motion + prefers-reduced-motion |
| «6 آراء عملاء حرفية» / «6 verbatim customer reviews» | brief — النتيجة |
| «0 سلّة أو دفع — واتساب فقط» | brief — الحل (لا سلّة ولا دفع)؛ tech.md — buildWhatsAppUrl |
| «سلّة ودفع لا تحتاجهما…» (مشهد المشكلة) | brief — المشكلة |
| «صفحة سينمائية وهوية دافئة» | brief — الحل (صفحة سينمائية، هوية شامبين نيود) |
| «القصّة والمقاس في صفحة القطعة، والطلب عبر واتساب مباشرة» | لقطة mobile-product.png الحقيقية (خيارات القصّة والمقاس) + tech.md (CTA → واتساب) |
| «تريدين بوتيكاً رقمياً بهذا المستوى؟ راسلني» / «Want a digital boutique at this level? DM me» | brief — تواصل / Contact |
| تاجات Next.js · React 19 · Tailwind · Framer Motion | tech.md — جدول التقنيات (package.json) |
| github.com/moain2026/sardah.com (تذييل + دعوة) | tech.md / links.md — المستودع عام (200) |
| شارة «مشاريع صغيرة» / «Small business» | تكليف مدير المنتج؛ tech.md — الشريحة أفراد/مشاريع صغيرة |

## ما لم يُستخدم عمداً
- «6 تصنيفات» (brief) مقابل 5 في الكود (tech.md) — متضارب، لم يُعرض.
- «75 صورة» (brief/README) مقابل 68 في public/ (tech.md) — متضارب، لم يُعرض.
- «Next.js 15» (brief) مقابل 16.2 (package.json) — كُتب «Next.js» بلا رقم.
- رقم واتساب — عنصر نائب في الكود، لم يُذكر.
- رابط حي — sardah.com يعمل على منصة سلة لا على هذا الكود (فحص 2026-09-23)، فلم يُعرض كرابط حي.
- تقييم 4.9 الظاهر في لقطة الصفحة الرئيسية — بيانات عرض من products.ts غير متحقّقة من عميل فعلي (tech.md)، لم يُكتب في أي نص.

## الصور واللقطات
- كل اللقطات **حقيقية** من تشغيل المستودع moain2026/sardah.com محلياً (`next build` + `next start`) وتصويرها بـ Playwright/Chromium بدقة 2x يوم 2026-09-23: ديسكتوب 1440×900 وجوال 390×844. الملفات في `screenshots/` داخل الحزمة (20 لقطة).
- المستخدمة: desktop-home (البطل في 24 تصميماً والبانر والكاروسيل 2 والريل)، desktop-product (ريل)، mobile-home، mobile-product، mobile-product-2، mobile-category-abayas.
- **تنبيه:** صور العبايات داخل الموقع نفسه مولّدة بالذكاء الاصطناعي بحسب README المرحلة 7 (tech.md) — اللقطات حقيقية للموقع، لكن ما تعرضه من عبايات ليس تصويراً لمنتجات فعلية؛ يُذكر عند النشر إن لزم.
- الأسماء الظاهرة في آراء العملاء داخل اللقطات: لم تُستخدم أي لقطة تُظهر آراء بأسماء.

## البحث (research.md)
كل ادعاء خارجي برابطه وتاريخ الوصول 2026-09-23 داخل الملف نفسه (سلة، زد، كتالوج واتساب، Shopify Starter، Origami، Store Leads، مدوّنة سلة).

## قاعدة الشعار والألوان
- الأساس nologo بلا أي شعار أو أيقونة؛ مساحة الأمان (أعلى-يمين AR / أعلى-يسار EN) فارغة ≥12%. نسخة logo = wordmark نصّي فقط. الريلان والكاروسيل والبطاقة والبانر كلها nologo.
- النص الصغير الخافت بلون #A3B1C0 (قاعدة v2) في الكاروسيل والبانر.

## الملفات
- A: 24 PNG `sardah-store-<piece>-<WxH>-<ar|en>-<nologo|logo>.png`
- B: 10 كاروسيل `sardah-store-carousel-0N-1080x1080-<ar|en>-nologo.png` + 2 بطاقة رقم واحد + 2 بانر 1600×840
- C: `sardah-store-reel-<ar|en>-nologo.mp4` (1080×1920 · 30fps · H.264+AAC · 20.6ث · موسيقى bgm-tech-minimal بلا حقوق طرف ثالث) + غلافان
- D: `sardah-store-explainer.<ar|en>.md` · E: `sardah-store-research.md` · F: `sardah-store-copy.<ar|en>.md` · G: هذا الملف
- screenshots/: 20 لقطة حقيقية خام (للمنصة ولإعادة الاستخدام)
