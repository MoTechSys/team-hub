keif-diafa | صانع العروض | 2026-09-23 | draft

# keif-diafa — بحث وتحليل / Research & analysis

> كل رقم عن المشروع من tech.md؛ كل رقم خارجي برابط وتاريخ وصول 2026-09-23. ما لم أقسه قلته صراحة.

## 1) تحليل سوق مختصر / Market snapshot
- **من يشتري هذا:** مقدّمو خدمات الضيافة والمناسبات (قهوجيين وصبابين، تجهيز مجالس) في مدن المناطق — أبها وخميس مشيط وجازان وبيشة ونحوها — الذين يعلنون على Google Ads أو يريدون الظهور في بحث «قهوجي في أبها» ويحتاجون موقعاً يمرّ من التوثيق ويحوّل إلى واتساب.
- **حجم الفئة (خارجي):** سوق خدمات الأعراس العالمي قُدّر بـ **185.22 مليار دولار في 2023** ويُتوقَّع **284.64 مليار بحلول 2032** بمعدل **4.89٪** — Introspective Market Research: https://introspectivemarketresearch.com/reports/wedding-service-market/ (وصول 2026-09-23). لا أعرف حجم فئة ضيافة المناسبات في جنوب السعودية تحديداً — «يُستكمل».
- **قيد تنظيمي حقيقي:** Google Ads قد يقيّد بعض الإعلانات أو يوقف الحساب حتى استكمال «توثيق المُعلِن» — https://support.google.com/adspolicy/answer/9703665 (وصول 2026-09-23). المشروع يضمّن صفحتي الخصوصية والشروط لهذا السبب (README «مطلوبة لتوثيق Google Ads»).

## 2) ثلاث بدائل / منافسون حقيقيون
| البديل | ما يقدّمه | التكلفة المنشورة (وصول 2026-09-23) | المصدر |
|---|---|---|---|
| **Wix** | بناء موقع بلا كود مع نطاق ودعم | Light 21 · Core 33 · Business 44 · Business Elite 165 (CAD/شهر، اشتراك سنوي كما عُرض لأداتي؛ مصادر أخرى تذكر $17/$29/$39.77/$159.77) | https://www.wix.com/plans · https://litextension.com/blog/wix-pricing/ |
| **Squarespace** | قوالب موقع أعمال مع استضافة | Basic $19 · Core $29 · Plus $49 · Advanced $99 /شهر (سنوي) | https://www.squarespace.com/pricing |
| **Google Business Profile** (بديل «بلا موقع») | ملف نشاط مجاني بخدمة مناطق (Service-area business) يظهر في الخرائط والبحث | مجاني | https://business.google.com/us/business-profile/ · https://support.google.com/business/answer/9157481 |

## 3) التموضع / Positioning
- **ماذا يقول المنافس:** «موقعك في دقائق بلا كود» (Wix/Squarespace) — اشتراك شهري دائم، وقالب لاتيني يُعرَّب لاحقاً. Google Business Profile مجاني لكنه لا يعطي صفحة خصوصية/شروط ولا صفحات مدن ولا FAQPage.
- **أين يتفوّق المشروع (من tech.md فقط):**
  - **20 صفحة ساكنة بلا خادم وبلا اشتراك** — تُستضاف على أي مضيف ثابت (`output: export`، 4.6 MB).
  - **بوابة جودة ثلاثية:** tsc 0 · eslint 0 تحذيرات · next build 21/21.
  - **SEO منظّم:** 8 أنواع JSON-LD (ProfessionalService بلا تقييمات ذاتية، FAQPage من نفس نص الأسئلة الـ8)، sitemap بـ17 رابطاً، robots، 7 صفحات مدن من مصدر بيانات واحد.
  - **عربي أصيل لا مُعرَّب:** خطوط Tajawal/Amiri مضمّنة (0 طلبات خارجية)، `adjustFontFallback:false`، `letter-spacing:normal`، خصائص منطقية RTL — قرارات موثَّقة في README.
  - **أمانة البيانات:** 4 حقائق غير مؤكَّدة محجوبة بـ `unverified`؛ لا شارات «24/7» أو «+500» بلا مصدر.
  - **سرعة:** FCP 184 ms محلياً، CLS 0.
- **أين يتفوّق المنافس (صريح):** محرّر بصري للعميل، نماذج تخزّن الطلبات، تحليلات مدمجة، ودعم — المشروع يحتاج مطوّراً لأي تعديل، و«الحجز» زرّا واتساب/اتصال فقط.

## 4) الكلمات المفتاحية
**AR (10):** قهوجي أبها · قهوجيين وصبابين خميس مشيط · ضيافة مناسبات الجنوب · قهوجيات جازان · تجهيز ضيافة زواج أبها · معاميل ودلال للتأجير · صبابين مؤتمرات · موقع يمر من توثيق Google Ads · موقع ساكن بالعربية · ضيافة الكيف
**EN (10):** Arabic coffee service Abha · qahwaji Saudi south · event hospitality Asir · Next.js static export Arabic · RTL Next.js site · Google Ads advertiser verification site · FAQPage schema Arabic · service-area business website · static site no server · Saudi wedding hospitality

## 5) ثلاث زوايا محتوى
1. **«ما نعرفه لا نعرضه»:** كيف يحجب `unverified` أربع حقائق حتى يؤكّدها العميل — درس في موقع لا يكذب على Google ولا على الزبون.
2. **«20 صفحة بلا خادم مقابل اشتراك شهري»:** مقارنة تكلفة 3 سنوات: ملفات ساكنة مقابل Wix/Squarespace.
3. **«الطباعة العربية ليست CSS لاتينياً»:** 6 قرارات موثَّقة (fallback الخط، تباعد الحروف، ارتفاع السطر 1.38/1.85، الخصائص المنطقية، قلب الأسهم، `aspect-ratio` للبطل).

## 6) فجوات صريحة / Gaps
- **لا رابط حي مؤكَّد؛** canonical/sitemap/JSON-LD تشير إلى VM مؤقت لا يستجيب.
- **معرض الأعمال 100٪ أماكن محجوزة (12)** — لا يمكن ترويج الموقع بصرياً حتى يسلّم العميل صوراً حقيقية (HANDOFF يمنع AI/stock).
- **رقم الهاتف في الكود** (`site.ts`) ويظهر في 4 مواضع + JSON-LD — يُنقل إلى env.
- **18 عنصر نص تحت 12px على الجوال** (أصغرها 8.8px) — يخالف أرضية 12px المتَّبعة في مشاريع الفريق.
- **صورة البطل (دلّة 604×760 PNG بلا ضغط)** بلا مصدر موثَّق ولا ترخيص — أُفصح عنها «أصل غير موثَّق».
- **4 حقائق و7 مناطق تنتظر تأكيد العميل؛** Ads/Analytics غير مركَّبة (صحيح، لكن يعني أن الموقع لم يُطلق).
- **لا اختبارات، لا CI، لا LICENSE؛** 5 commits في يوم واحد ثم توقّف منذ 2026-08-01.
- README «10 أقسام» مقابل 9 `<section>` مقيسة على الرئيسية.

## 7) المصادر
- tech.md (هذه الحزمة) — كل أرقام المشروع.
- Google Ads Help, Advertiser verification — https://support.google.com/adspolicy/answer/9703665 — 2026-09-23
- Wix plans — https://www.wix.com/plans — 2026-09-23 · LitExtension Wix pricing — https://litextension.com/blog/wix-pricing/ — 2026-09-23
- Squarespace pricing — https://www.squarespace.com/pricing — 2026-09-23
- Google Business Profile — https://business.google.com/us/business-profile/ · service areas https://support.google.com/business/answer/9157481 — 2026-09-23
- Introspective Market Research, Wedding Service Market — https://introspectivemarketresearch.com/reports/wedding-service-market/ — 2026-09-23

---
### English summary
Target buyer: regional Saudi hospitality/event providers who advertise on Google Ads and need a verifiable, SEO-ready, WhatsApp-converting site. Google may restrict ads or pause accounts until advertiser verification is complete (Google Ads Help, accessed 2026-09-23) — the project ships privacy/terms pages for that reason. Global wedding-service market: USD 185.22B (2023) → 284.64B (2032), 4.89% CAGR (Introspective Market Research). Alternatives: Wix (Light→Business Elite, ~21–165 CAD/mo annual), Squarespace ($19–99/mo), free Google Business Profile. Project edge (tech.md): 20 static pages with no server or subscription, tsc/eslint 0, build 21/21, 8 JSON-LD types, 7 city pages from one data source, self-hosted Arabic fonts with 0 external requests, FCP 184 ms local, CLS 0, and 4 unverified facts deliberately hidden. Gaps: no live URL, 12 empty gallery slots, phone in code, 18 sub-12px text nodes, undocumented hero image origin, no tests/CI/license, no commits since 2026-08-01.
