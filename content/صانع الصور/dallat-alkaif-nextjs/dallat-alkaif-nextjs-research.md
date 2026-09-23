dallat-alkaif-nextjs | صانع الصور | 2026-09-23 | draft

# دلة الكيف — بحث وتحليل السوق

تاريخ البحث: 2026-09-23 (بحث ويب + قراءة صفحات المنافسين في اليوم نفسه). ادعاءات المنافسين من صفحاتهم؛ ادعاءات مشروعنا من README/tech.md فقط.

## 1. من يشتري هذا
- المشتري النهائي للخدمة: أسر وجهات في جنوب المملكة (أبها، خميس مشيط، جازان، نجران، الباحة، الطائف…) تحجز قهوجية وصبّابين وضيافة للأعراس والمجالس والمؤتمرات. (README نطاق الخدمة، lib/site.ts CITIES)
- مشتري «المنتج» (الموقع نفسه) لمحفظة معين: أصحاب شركات ضيافة صغيرة يريدون موقعاً عربياً فاخراً يحوّل إلى واتساب بلا وعود مضخّمة. (brief.ar لمن يفيد)
- حجم الفئة: يُستكمل — لا رقم موثّق. مؤشر كيفي: البحث عن «قهوجي أبها خميس مشيط» يعيد إعلانات حراج وحسابات تيك توك/إنستغرام أكثر من مواقع مستقلة — أي أن المنافسة الجنوبية على المواقع ضعيفة نسبياً مقارنة بجدة/الرياض.

## 2. المنافسون والبدائل (3)
| # | الموقع | المدن/النطاق المعلَن | ماذا يقول عن نفسه | الرابط (وصول 2026-09-23) |
|---|---|---|---|---|
| 1 | هيف الضيافة (hevaldiafa) | جدة، الرياض، الدمام «ومناطق أخرى» | «أول مؤسسة إلكترونية متخصصة» في ضيافة المناسبات؛ صبّابين وصبّابات، معجنات وشوكولاتة وتمور؛ نموذج طلب عرض سعر من 5 خطوات؛ لا أسعار معروضة | https://hevaldiafa.com/ |
| 2 | قهوجيين الطائف (qahwajie) | الطائف أساساً + مكة والرياض وجدة | قهوجيين وصبّابين للأعراس والعزاء والفعاليات؛ «سنوات من العمل الدؤوب» و«سجل كامل من المناسبات الناجحة» بلا أرقام؛ «أسعار رخيصة» و«باقات متكاملة» بلا قائمة | https://qahwajie.com/قهوجيين-الطائف/ |
| 3 | سهلها (sahelha.app) — منصة وسيطة | أبها (صفحة مدينة مخصصة) | منصة تجمع مقدمي خدمة «صبّاب قهوة» بملفات وتقييمات؛ لا أسعار ثابتة؛ التواصل المباشر والاتفاق على نطاق مكتوب | https://sahelha.app/services/saudi/abha/coffee-server/ |

ظهرت أيضاً بلا فتح صفحاتها: aswlfor.com «أصول الضيافة الملكية» (الطائف/مكة/جدة)، frhsa.com «فرحة» (منصة ضيافة جازان)، customer.jad.services (منصة)، إعلانات حراج لضيافة أبها/خميس مشيط، وحساب keifaldiafa.com — المشروع الشقيق بالاسم القديم الذي يمنع README استخدامه هنا (يدّعي «+500 مناسبة» و«كل مناطق المملكة»، وهو بالضبط ما تمنعه قواعد دلة الكيف).

## 3. التموضع
| المحور | ماذا يقول المنافسون | أين يتفوّق مشروعنا (من README/tech.md فقط) |
|---|---|---|
| النطاق الجغرافي | قوائم مدن كبرى (جدة/الرياض/الدمام) + «مناطق أخرى»؛ الجنوب يظهر عبر منصات وإعلانات لا مواقع | نطاق جنوبي حصري ومحمي بأمر grep: 13 مدينة في 5 مناطق، وأي مدينة خارجه تُفشِل بوابة الجودة |
| الادعاءات | «سنوات خبرة»، «سجل كامل»، «+500 مناسبة»، «أول مؤسسة» — بلا مصدر | قاعدة إلزامية: لا إحصائية على الإطلاق حتى يوفّرها المالك؛ لا شعارات شركاء؛ لا أسعار رقمية (`PRICE_TEXT`) |
| العربية RTL | غير مُتحقَّق تقنياً من صفحاتهم | خصائص CSS منطقية حصراً، صفر tracking سالب، عزل bidi للأرقام اللاتينية، خطوط عربية محلية بـ unicode-range |
| الأداء والتشغيل | مواقع ديناميكية/قوالب على الأغلب (غير مُتحقَّق) | HTML ثابت بالكامل: صفر خادم، صفر تكلفة شهرية، قابل للتخزين على CDN؛ JS 636 KB لكل الموقع |
| الوصولية | غير مذكورة | 48px أهداف لمس، لا قفل تكبير، skip link، aria-expanded/aria-live، reduced-motion — موثّقة في README |
| نموذج التحويل | واتساب/نموذج طلب سعر | نفس النموذج (واتساب + نموذج حجز مُتحقَّق منه) — تكافؤ |

حيث يتفوّق المنافسون (صراحة): لديهم مواقع منشورة على نطاقات حية وحضور على منصات الوساطة، وبعضهم يعرض صوراً حقيقية لمناسباته؛ دلة الكيف بلا نطاق حي مُتحقَّق، وكل صوره مولّدة بالذكاء الاصطناعي (README نفسه)، ولا رقم واحد عن حجم العمل.

## 4. الكلمات المفتاحية
AR (10): قهوجي أبها · قهوجيين خميس مشيط · ضيافة مناسبات جازان · صبابين قهوة نجران · ضيافة أعراس الباحة · قهوجي الطائف · ضيافة جنوب السعودية · سقاء زمزم للمناسبات · تأجير معدات ضيافة · خطاط مناسبات
EN (10): Arabic coffee servers Abha · hospitality services Khamis Mushait · southern Saudi events hospitality · qahwaji Jazan · Next.js 16 static export Arabic site · RTL CSS logical properties · self-hosted Arabic fonts · WCAG 2.2 touch targets Arabic · single source of truth Next.js · CSS Modules vs Tailwind RTL

## 5. ثلاث زوايا محتوى
1. «لماذا لا يوجد رقم واحد على هذا الموقع» — قصة قاعدة «لا إحصائية بلا مصدر» وبوابة grep التي تمنع المدن خارج النطاق (الصدق كقاعدة هندسية).
2. «CSS Modules لا Tailwind: كيف تبني عربياً RTL لا ينكسر» — ADR-002 والخصائص المنطقية وقواعد الاحتياط خارج @layer لأندرويد القديم.
3. «موقع بلا خادم: صفر تكلفة شهرية» — ADR-001 التصدير الثابت، الخطوط المحلية، والصور بمُحمِّل مخصص.

## 6. الفجوات (صريحة)
تقنياً: لا اختبارات آلية (لا Vitest/Playwright)؛ sections.module.css 691 سطراً يخالف معيار «≤ 400»؛ commitان فقط (2026-08-06/07) — تاريخ قصير؛ بقايا create-next-app في public/؛ رقم الواتساب في README نفسه وفي lib/site.ts (مقبول تصميمياً لكن يظهر في أي استنساخ عام). (tech.md)
تسويقياً: لا نطاق حي مُتحقَّق؛ كل الصور مولّدة بالذكاء الاصطناعي (يمنع ترويج «معرض أعمال» كحقيقي)؛ لا أسعار ولا سنة تأسيس ولا عدد مناسبات؛ ازدواج اسم المستودع moain2026/moain2028؛ الاسم القديم «كيف الضيافة» ممنوع فيتعذّر الاستفادة من حضوره الحالي في البحث.

## English summary
Dallat Al-Kaif is a static Next.js 16 brochure site for a luxury hospitality company in southern Saudi Arabia. Three verified alternatives (accessed 2026-09-23) — Hev Al-Diafa (Jeddah/Riyadh/Dammam, 5-step quote form), Qahwajie Taif (Taif/Makkah/Riyadh/Jeddah, "years of experience" without numbers) and the Sahelha marketplace (an Abha coffee-server category page) — all sell via WhatsApp or quote forms with no prices and broad, unsourced claims. The project's defensible edge, from README/tech.md: an enforced southern-only footprint (13 cities, grep-gated), a hard rule of no invented statistics or partner logos, RTL-correct CSS with logical properties only, self-hosted fonts, fully static hosting, and documented accessibility (48 px targets, no zoom lock, aria semantics). Gaps: no verified live domain, all imagery AI-generated, no automated tests, only two commits, and a competitor sibling brand (keifaldiafa.com) whose old name this project forbids.

## المصادر
- README.md، package.json، next.config.ts، lib/site.ts — moain2028/dallat-alkaif-nextjs (commit 3257571، 2026-08-07) + قياسات محلية 2026-09-23 (tech.md في هذه الحزمة)
- https://hevaldiafa.com/ — 2026-09-23
- https://qahwajie.com/قهوجيين-الطائف/ — 2026-09-23
- https://sahelha.app/services/saudi/abha/coffee-server/ — 2026-09-23
- ذُكرت بلا تحقق (نتائج بحث 2026-09-23): https://aswlfor.com/ · https://frhsa.com/c/catering/jazan/ · https://customer.jad.services/ · https://keifaldiafa.com/qahwajiin-abha · إعلانات haraj.com.sa لضيافة أبها/خميس مشيط
