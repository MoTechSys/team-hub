zawada-al-dukkan | مهندس | 2026-09-23 | research v1 (بحث ويب حقيقي — تاريخ الوصول لكل رابط 2026-09-23)

# زوادة الدكان — البحث والتحليل

**English summary at the end.**

## 1. تحليل السوق المختصر

**من يشتري هذا؟** صاحب بقالة أو محل صغير يريد «واجهة عرض تليق» تربطه بالزبون عبر واتساب، ولا يريد الدخول في منصة متجر كاملة باشتراك وبوابة دفع (brief.ar.md — المشكلة/لمن يفيد). الشريحة في portfolio-hub: أفراد / مشاريع صغيرة، عربي أولاً (tech.md).

**حجم الفئة (إشارات لا أرقام مخترعة):**
- الكتالوج مدمج مجاناً في تطبيق WhatsApp Business نفسه، أي أن «العرض عبر واتساب» صار سلوكاً قياسياً للمحلات الصغيرة، لا ميزة نادرة — https://faq.whatsapp.com/405903568419894 (accessed 2026-09-23).
- ظهور فئة كاملة من أدوات «WhatsApp store builder» (Take App وبدائله العشرة في مقال Jotform) يشير إلى طلب فعلي ومتكرر على هذا الحل بالتحديد — https://www.jotform.com/blog/take-app-alternatives/ (accessed 2026-09-23).
- لا يوجد رقم موثوق لحجم هذه الفئة في اليمن/الخليج في المصادر التي فُحصت — **يُستكمل**.

## 2. ثلاث بدائل / منافسون فعليون (واجهات بقالة/محل تطلب عبر واتساب)

| # | البديل | ما يقدّمه (من صفحته) | التكلفة | ما لا يقدّمه | الرابط (accessed 2026-09-23) |
|---|---|---|---|---|---|
| 1 | **WhatsApp Business Catalog** (الحل الأصلي من Meta) | كتالوج منتجات يظهر على البروفايل التجاري؛ لكل منتج عنوان وصورة وبلد المنشأ، واختيارياً سعر ووصف ورابط؛ يمكن مشاركته في المحادثة ووسائل التواصل؛ عربة تسوق داخل المحادثة | مجاني داخل تطبيق WhatsApp Business | لا صفحة ويب مستقلة بهوية المحل، لا تصميم مخصص، لا فهرسة في Google لصفحة خاصة بالمحل، إضافة الأسعار «متاحة في بلدان معيّنة فقط» | https://faq.whatsapp.com/405903568419894 · https://faq.whatsapp.com/1184376605821468 |
| 2 | **Take App** (take.app) | متجر ويب تُنشئه بلا كود؛ «Checkout turns the cart into a structured WhatsApp message with the items, options, address and total»؛ صفحة قابلة للفهرسة | Basic مجاني: 50 طلباً/شهر محفوظاً في اللوحة، منتجات غير محدودة، بلا عمولة؛ Business مدفوع (Jotform يذكر 50$/شهر) | في المجاني: لا دفع بالبطاقة، لا نطاق خاص، لا إزالة شعار Take App، لا متاجر متعددة؛ التصميم قالب المنصة | https://www.take.app/whatsapp-store · https://www.jotform.com/blog/take-app-alternatives/ |
| 3 | **Store.link** | متجر مبني فوق Google Sheets («One row = one product»)، يدعم «WhatsApp store» وتتبّع الطلبات؛ 0% عمولة | «free forever plan with basic features»؛ الخطط المدفوعة للميزات القوية (حدود المجاني غير مذكورة في الصفحة) | لا قوالب تصميم تختارها («No templates to browse. Just type and go») — الهوية محدودة؛ بوابة الدفع والنطاق الخاص إضافات | https://store.link/ |

ملاحظة: منصات المتاجر السعودية (سلة، زد) بدائل أوسع نطاقاً — متجر كامل باشتراك وبوابة دفع — أي أنها تحلّ مشكلة مختلفة عن التي يستهدفها زوادة (brief: «دون تكلفة متجر إلكتروني كامل ولا بوابة دفع»)، فلم تُدرج كمنافس مباشر. مرجع للمقارنة: https://origami.sa/en/blog/custom-store-vs-salla-zid-decision-guide/ (accessed 2026-09-23).

## 3. التموضع

**ماذا يقول المنافس؟** «بلا كود، في دقائق، مجاني للبداية» — كل البدائل الثلاثة تبيع السرعة والسهولة، والهوية البصرية فيها قالب موحّد أو غير موجود.

**أين يتفوّق زوادة الدكان (من tech.md/README فقط):**
- **هوية مخصصة بالكامل:** نظام تصميم موثّق (185 سطراً في tailwind.config.ts + 249 في globals.css) بألوان وخطوط ومؤثرات المحل نفسه — لا شعار منصة ولا قالب مشترك.
- **عربي RTL أصيل** بخطي Cairo وAmiri، لا واجهة مترجمة.
- **صفر تكلفة تشغيل شهرية:** صفحة ثابتة على GitHub Pages، لا اشتراك ولا حدّ طلبات.
- **بيانات مهيكلة GroceryStore** (JSON-LD) لفهرسة صفحة المحل نفسها في البحث.

**أين يتفوّق المنافس (صريحاً):** الثلاثة يوفّرون تدفّق طلب مكتمل اليوم؛ زوادة ما زال في المرحلة الأولى بلا سلة ولا إتمام طلب (tech.md — الحالة). Take App يقدّم لوحة طلبات وتحديثات آلية؛ زوادة لا يقدّم إدارة طلبات على الإطلاق.

## 4. الكلمات المفتاحية

**عربي (10):** متجر واتساب للبقالة · واجهة متجر بقالة · طلب عبر واتساب بدون بوابة دفع · تصميم موقع بقالة · متجر إلكتروني بسيط للمحلات الصغيرة · كتالوج منتجات واتساب · موقع بقالة عربي RTL · واجهة تسوق فاخرة · متجر بدون اشتراك شهري · Next.js متجر عربي

**English (10):** WhatsApp grocery storefront · WhatsApp order website · storefront without payment gateway · small grocery website design · Next.js Tailwind storefront · RTL Arabic e-commerce UI · static grocery store GitHub Pages · WhatsApp catalog alternative · premium grocery UI design · no-server storefront

## 5. ثلاث زوايا محتوى مقترحة

1. **«بقالة بلا بوابة دفع ولا خادم»:** كيف تصل من قائمة واتساب نصية إلى واجهة تليق — بصفر تكلفة تشغيل (مقال + كاروسيل المشكلة/الحل).
2. **«أسلوب الضيافة الراقية على بقالة»:** تشريح نظام التصميم (تركوازي/ذهبي، Cairo/Amiri، Glassmorphism) — لجمهور المصممين والمطوّرين العرب (ثريد X + بانر مقال).
3. **«لماذا صفحة ثابتة تكفي؟»:** مقارنة صريحة مع WhatsApp Catalog وTake App وStore.link — متى تكفي واجهة عرض ومتى تحتاج منصة (منشور LinkedIn للمالكين).

## 6. الفجوات (صريحة)

**تقنياً:**
- لا سلة ولا إتمام طلب عبر واتساب حتى الآن — الوعد الأساسي في العنوان غير مُنفَّذ (Phase 3).
- الصفحة الحية HTML ثابت بـ Tailwind CDN لا تطبيق Next.js المبني في المستودع — نسختان غير متطابقتين.
- لا اختبارات ولا CI؛ لا نشاط منذ 2026-04-28.
- تعارض إصدار Next.js (README 15 / package.json 14.2)؛ نطاق JSON-LD غير مفعّل.
- صور المنتجات خارجية (Unsplash/Pexels) — لا تصلح لعرض بضاعة عميل حقيقي.

**تسويقياً:**
- لا عميل حقيقي ولا أرقام استخدام؛ كل ما يمكن تسويقه هو النموذج والهوية.
- README ينسب البناء إلى «Zawada Team» — دور معين يُستكمل قبل النص التسويقي (tech.md).
- الأرقام داخل الواجهة (4.8 تقييم، 12 بلد، +20 منتج) محتوى تجريبي قد يُقرأ كادّعاء — لا تُنقل إلى أي منشور.

## 7. المصادر

- brief.ar.md / brief.en.md / tech.md / links.md — portfolio-hub 01-projects/zawada-al-dukkan/
- README: https://github.com/moain2026/zawada-al-dukkan (accessed 2026-09-23)
- الصفحة الحية: https://moain2026.github.io/zawada-al-dukkan/ (HTTP 200، accessed 2026-09-23)
- WhatsApp Business Catalog: https://faq.whatsapp.com/405903568419894 · عربة التسوق: https://faq.whatsapp.com/1184376605821468 (accessed 2026-09-23)
- Take App: https://www.take.app/whatsapp-store (accessed 2026-09-23)
- Take App alternatives / pricing note: https://www.jotform.com/blog/take-app-alternatives/ (accessed 2026-09-23)
- Store.link: https://store.link/ (accessed 2026-09-23)
- Salla/Zid context: https://origami.sa/en/blog/custom-store-vs-salla-zid-decision-guide/ (accessed 2026-09-23)

---

## English summary

**Who buys:** small grocery/shop owners who want a brand-worthy showcase that connects to customers over WhatsApp without a full store platform, subscription, or payment gateway (brief). **Category signal:** Meta ships a free catalog inside WhatsApp Business, and a whole class of "WhatsApp store builders" exists (Take App and ten alternatives) — demand is real; no reliable market-size figure for Yemen/Gulf was found (to be confirmed).

**Three real alternatives (all accessed 2026-09-23):** (1) WhatsApp Business Catalog — free, in-app, no standalone branded page, prices only in some countries; (2) Take App — no-code web store whose checkout becomes a structured WhatsApp message; free plan 50 orders/month, paid for card payments/custom domain/logo removal; (3) Store.link — Google-Sheets-driven store with WhatsApp ordering, free-forever basic plan, no design templates.

**Positioning:** competitors sell speed and no-code; Zawada wins on a fully custom documented design system, native Arabic RTL, zero monthly running cost (static GitHub Pages), and GroceryStore structured data. Competitors win today on a complete order flow and order management — Zawada is Phase 1 without cart/checkout.

**Gaps:** cart/WhatsApp checkout unbuilt; live page is static HTML, not the Next app; no tests/CI, dormant since 2026-04-28; Next.js version mismatch; stock images; no real client or usage numbers; UI demo figures (4.8/12/20+) must not be quoted as metrics.
