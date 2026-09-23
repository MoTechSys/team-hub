ads-agency-platform | المصمم | 2026-09-23 | v1 — بحث ويب مؤرَّخ (تاريخ الوصول لكل رابط: 2026-09-23)

# منصة الوكالة — البحث والتحليل

## 1. تحليل السوق المختصر
**من يشتري هذا؟** وكالات التسويق الرقمي والفرق الداخلية التي تدير أكثر من حساب Google Ads، خصوصاً في السعودية والخليج حيث الواجهة العربية RTL والفواتير بضريبة 15% مطلوبتان (tech.md).

**حجم الفئة (أرقام طرف ثالث — تُذكر كسياق لا كإنجاز):**
- سوق الإعلان الرقمي في السعودية: من 2,050 مليون دولار (2025) إلى 4,156 مليون دولار متوقعة بحلول 2031، بنمو سنوي مركّب 12.5% — Ken Research: https://www.kenresearch.com/industry-reports/ksa-digital-advertising-market
- الإنفاق الإعلاني الرقمي في السعودية متوقع أن يصل 4.68 مليار دولار في 2026 بنمو 16.8% سنوياً — Yahoo Finance / ResearchAndMarkets (2026-02-10): https://finance.yahoo.com/news/saudi-arabia-digital-ad-spend-153500740.html
- سوق وكالات التسويق والإعلان في السعودية: 3.19 مليار دولار في 2026 بنمو 5.30% — Mordor Intelligence (2026-02-23): https://www.mordorintelligence.com/industry-reports/saudi-arabia-marketing-and-advertising-agency-market
- «البحث» هو أكبر قطاع في الإعلان الرقمي السعودي — Statista Market Outlook: https://www.statista.com/outlook/amo/advertising/saudi-arabia/

**الألم الذي يعالجه المشروع موثَّق في السوق:** ميزة Google «Automatically apply recommendations» تطبّق التوصيات دورياً بلا مراجعة — Google Ads Help: https://support.google.com/google-ads/answer/10279006 — ومحترفو PPC ينصحون بإيقافها لأنها تسلّم التحكم للنظام (r/adwords: https://www.reddit.com/r/adwords/comments/1isfqk8/why_you_need_to_turn_off_google_ads_autoapply/ · Blinkjar Media 2023-12-20: https://www.blinkjarmedia.com/blog/baton-rouge-digital-ad-agencies-why-you-should-avoid-google-ads-auto-apply-recommendations · HawkSEM: https://hawksem.com/blog/google-ads-auto-apply/). هذا هو بالضبط الفراغ الذي تملؤه «الموافقة البشرية الإلزامية».

## 2. المنافسون / البدائل (3) — تم تصفّح مواقعهم الرسمية 2026-09-23
| المنافس | الرابط | ماذا يقول عن نفسه (من موقعه) | تعدد الحسابات | التوصيات | التنفيذ |
|---|---|---|---|---|---|
| **Opteo** | https://opteo.com/ | «توصيات ذكية تحسّن أداء Google Ads… تُدفع إلى الحساب في ثوانٍ»، مراقبة وتقارير للوكالات | نعم (موجَّه للوكالات) | نعم — «Improvements» مبنية على أنماط ذات دلالة إحصائية | بضغطة من المستخدم؛ لا توثيق لمسار موافقة متعدد الأدوار أو evidence إلزامي |
| **Optmyzr** | https://www.optmyzr.com/ | «أتمتة يتحكّم بها المستخدم»، AI Sidekick، One-Click Optimizations، 461,000+ حساب متصل، تدقيق سريع | نعم | نعم — LLM لنصوص الإعلانات + تحسينات جاهزة | «أنت وحدك أو من تفوّضه يغيّر» — تحكّم بالصلاحيات، لكن بلا مسار PENDING→APPROVED→APPLIED موثَّق علناً |
| **Adalysis** | https://adalysis.com/ | «PPC copilot»: تدقيق 100+ فحص، مراقبة وتنبيهات، تعديل ميزانيات يومي آلي، تقارير white-label، 2,000+ وكالة | نعم | قواعد وتنبيهات + تحليل n-gram | تعديل الميزانيات **آلي**، وأدوات تعديل جماعي — أقل تركيزاً على الموافقة البشرية |

**الأسعار:** صفحات التسعير الثلاث لا تعرض أرقاماً ثابتة في النص العام (Optmyzr يذكر Campaign Automator من 249$/شهر كأداة مستقلة؛ Adalysis بسلّم حسب الإنفاق) — تُذكر «حسب الطلب» ولا يُخترع رقم. (تاريخ الوصول 2026-09-23: https://opteo.com/pricing · https://www.optmyzr.com/pricing/ · https://adalysis.com/pricing/)

**البديل الصفري:** Google Ads Manager Account (MCC) — يجمع الحسابات والفوترة والصلاحيات، لكن بلا طبقة توصيات مسنودة بدليل ولا سجل تدقيق مستقل ولا فواتير محلية: https://business.google.com/en-all/ad-tools/manage-accounts/

## 3. التموضع
المنافسون الثلاثة يبيعون **السرعة والأتمتة** («push live in seconds»، «one-click»، «automated daily budget adjustments»). مشروعنا يبيع **الضبط**: لا يُنفَّذ شيء بلا دليل رقمي وبلا موافقة إنسان، وكل خطوة في سجل تدقيق — وهذا مبنيّ في نموذج البيانات نفسه (ChangeRequest + AuditLog + evidence JSON، من tech.md) لا كخيار إعدادات.
أين يتفوّق (من tech.md فقط): واجهة عربية RTL أصلية · فواتير بضريبة 15% · إقرار تفويض قانوني (consentAt/consentIp) · اختبارات عزل مستأجرين موثّقة 17/17 · تشفير AES-256-GCM موثّق 20/20 · طبقة AI بخمسة مزوّدين (لا ارتباط بمزوّد واحد).
أين يتأخّر (صريح): لا تقارير white-label، لا Microsoft Ads، لا تدقيق بـ100+ فحص، لا قاعدة عملاء معلنة، ولا رابط حي عام.

## 4. الكلمات المفتاحية
**عربي (10):** إدارة حملات Google Ads للوكالات · لوحة موحدة لحسابات إعلانية متعددة · منصة إدارة إعلانات جوجل متعددة العملاء · موافقة بشرية على توصيات الذكاء الاصطناعي · سجل تدقيق حملات إعلانية · SaaS متعدد المستأجرين للوكالات · تقارير Google Ads للعملاء بالعربية · أتمتة إعلانات جوجل بدون مخاطرة · إيقاف التطبيق التلقائي للتوصيات · فواتير وكالة إعلانية بضريبة 15%
**English (10):** Google Ads agency dashboard · multi-client Google Ads management · multi-tenant PPC platform · human-in-the-loop ad optimization · AI recommendations with approval workflow · Google Ads audit log · alternative to auto-apply recommendations · agency PPC reporting Arabic RTL · Google Ads API integration SaaS · secure multi-tenant SaaS Prisma PostgreSQL

## 5. ثلاث زوايا محتوى
1. **«من غيّر هذا؟»** — قصة العرض الذي تغيّر ليلاً بلا موافقة، مقابل مسار PENDING→APPROVED→APPLIED. (ريل + كاروسيل، جمهور: أصحاب الوكالات)
2. **«الذكاء الاصطناعي الذي يُمنع من الكلام بلا دليل»** — كيف يُجبَر الوكيل على إرفاق evidence JSON، ولماذا هذا أهم من ذكاء النموذج نفسه. (مقال تقني + LinkedIn، جمهور: مطوّرون ومديرو منتجات)
3. **«SaaS عربي من الداخل»** — RTL أصلي، ضريبة 15%، تفويض قانوني، عزل مستأجرين 17/17: ما الذي يعنيه بناء SaaS للسوق السعودي فعلاً. (سلسلة X + مقال، جمهور: رواد أعمال ووكالات سعودية)

## 6. الفجوات (صريحة)
**تقنية:** لا رابط حي عام (نشر محلي pm2/Caddy) · لا نشاط منذ 2026-08-11 · Next.js 16.3 وReact 19.2 إصدارات حديثة جداً قد تحمل مخاطر توافق · اللقطات مبنية على بيانات تجريبية لأن الـAPI يحتاج بيانات اعتماد معين · لا اختبارات E2E معلنة للوحة نفسها · لا دعم Microsoft Ads/Meta.
**تسويقية:** عدد العملاء المدارين فعلياً «يُستكمل» · أرقام الحملة الحقيقية (6,632 / 353 / 45) تعود لحساب كيف الضيافة ولا تُنشر إلا بموافقة معين · لا فيديو تعريفي معتمد · لا تسعير · المستودع خاص فلا يمكن للمهتمين فحص الكود · لا دراسة حالة بعميل مسمّى.

## 7. المصادر
- المشروع: `01-projects/ads-agency-platform/brief.ar.md` · `brief.en.md` · `tech.md` · `links.md` (portfolio-hub، 2026-09-11).
- كل رابط خارجي أعلاه، تاريخ الوصول 2026-09-23، عبر بحث ويب وتصفّح الصفحات الرسمية. أرقام السوق من تقارير طرف ثالث وتُقرأ كتقديرات متفاوتة بين المصادر.

---
## English summary
Buyers: agencies and in-house teams running several Google Ads accounts, especially in KSA (Arabic RTL, 15% VAT). Market context (third-party): KSA digital advertising USD 2.05B (2025) → 4.16B (2031), CAGR 12.5% (Ken Research); digital ad spend USD 4.68B in 2026 (ResearchAndMarkets via Yahoo Finance). Documented pain: Google's auto-apply recommendations run without review and PPC professionals advise switching them off. Competitors reviewed 2026-09-23: Opteo (recommendations pushed live in seconds), Optmyzr (user-controlled automation, one-click optimizations, 461k+ accounts), Adalysis (automated audits, automatic daily budget adjustments, 2,000+ agencies) — all sell speed; none publicly documents an evidence-mandatory, multi-state human-approval flow with an independent audit log, which this project builds into its data model (ChangeRequest, AuditLog, evidence JSON). Where it lags: no white-label reporting, no Microsoft Ads, no public live URL, no disclosed customer base, no pricing. Keywords, content angles and gaps as above.
