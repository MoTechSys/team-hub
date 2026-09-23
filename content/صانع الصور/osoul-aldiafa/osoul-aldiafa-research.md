osoul-aldiafa | صانع الصور | 2026-09-23 | draft

# أصول الضيافة — بحث وتحليل السوق

تاريخ البحث: 2026-09-23 (بحث ويب + قراءة صفحات المنافسين في اليوم نفسه). ادعاءات المنافسين من صفحاتهم؛ ادعاءات مشروعنا من tech.md/brief فقط.

## 1. من يشتري هذا
- المشتري: شركة ضيافة مناسبات (قهوجية/صبّابين، ضيافة أعراس ومؤتمرات) في منطقتَي مكة والمدينة، تريد الظهور في بحث «قهوجي/ضيافة + مدينة» وتحويل الزائر إلى واتساب أو اتصال بلا باقات ولا أسعار. (tech.md المشكلة)
- الفئة الأوسع لمعين: أصحاب خدمات الضيافة والمناسبات في المدن السعودية الذين لديهم موقع «جميل لكنه بطيء». (brief.ar لمن يفيد)
- حجم الفئة: يُستكمل — لا رقم موثّق في مصادر المشروع؛ مؤشر كيفي فقط: البحث عن «قهوجي جدة» يعيد صفحة أولى كاملة من مواقع مستقلة (أدناه) إضافة إلى منصات وسيطة (yojad.com) وإعلانات haraj — أي أن الفئة تتنافس فعلاً على SEO المحلي.

## 2. المنافسون والبدائل (3 مواقع في نفس الفئة والمدن)
| # | الموقع | المدن المعلَنة | ماذا يقول عن نفسه | الرابط (وصول 2026-09-23) |
|---|---|---|---|---|
| 1 | القهوة الملكية | الرياض، جدة، مكة، الدمام، الطائف، تربة | قهوجية وصبّابين رجال ونساء بزي رسمي، ماء زمزم، بوفيهات، تأجير عدة ضيافة؛ «أسعار تنافسية»؛ الأسعار غير معروضة وتختلف حسب عدد الضيوف؛ الحجز واتساب/هاتف | https://alqahwaalmalakiya.com/ |
| 2 | قهوجي جدة (qahwaji-jed) | جدة، مكة، الطائف | فرق رجالية ونسائية للقهوة العربية والمشروبات في الأعراس والاجتماعات؛ «20+ سنة خبرة»، 24/7؛ لا أسعار؛ الحجز بإرسال تفاصيل المناسبة عبر واتساب | https://qahwaji-jed.com/ |
| 3 | دلة الضيافة (noblesoiree) | جدة، مكة، الرياض | صبّابين/قهوجيات وماء زمزم للأعراس والعزاء والفعاليات؛ زي سعودي تراثي، 24/7، التزام بالمواعيد؛ «أسعار تنافسية» بلا قائمة أسعار؛ واتساب/هاتف | https://noblesoiree.com/?page=home |

ظهر أيضاً في البحث بلا فتح صفحاته: kahwgysa.com، qahawagy.com، aswlfor.com (اسم «أصول الضيافة الملكية» — تشابه اسم يستحق الانتباه)، thawq-rafeea.com، ومنصة yojad.com. ومشروع معين الشقيق keifaldiafa.com يظهر في نتائج «ضيافة مناسبات المدينة المنورة» بادعاء «+500 مناسبة ناجحة».

## 3. التموضع
| المحور | ماذا يقول المنافسون | أين يتفوّق مشروعنا (من tech.md فقط) |
|---|---|---|
| النطاق الجغرافي | قوائم مدن واسعة (حتى 6 مدن على صفحة واحدة) ووعود «نغطي كل الأحياء» | نطاق ثابت ومعلَن: 5 مدن فعلية، صفحة لكل خدمة×مدينة، GeoCircle 30 كم لكل مدينة في البيانات المهيكلة، وحُذف 15 ادعاءً جغرافياً — الصدق الجغرافي مبدأ مكتوب في README |
| الأداء | لا ينشر أي منهم أرقام أداء | LCP 956 ms (كان 2240)، CLS ≤ 0.0001، JS مشترك 87.4 KB — مقيسة محلياً وموثّقة |
| الإتاحة | غير مذكورة | axe WCAG 2.1 AA على 9 صفحات: 0 مخالفة؛ اختبارات Playwright للإتاحة وWCAG 2.2 |
| SEO التقني | صفحات مدن عامة؛ لا دليل على بيانات مهيكلة | JSON-LD ProfessionalService + GeoCircle، sitemap 48/48، فحص تشابه المحتوى (أقصى 0.259) وسكربتات check:seo داخل المستودع |
| نموذج التحويل | واتساب/هاتف بلا أسعار | نفس النموذج (واتساب/اتصال بلا باقات) — تكافؤ، لا تفوّق |
| الهندسة | مواقع قوالب/ووردبريس على الأغلب (غير مُتحقَّق) | Next.js 14 + TypeScript + Tailwind مع Vitest وPlaywright — قابلية صيانة واختبار |

حيث يتفوّق المنافسون (صراحة): تغطية مدن أكثر (الرياض/الدمام) وحضور أطول في السوق («20+ سنة»)، وأرقام واتساب ظاهرة على الصفحة الأولى؛ بينما صفحة أصول الضيافة لم تُقَس حياً بعد، وأرقام التواصل «يُستكمل» في links.md.

## 4. الكلمات المفتاحية
AR (10): قهوجي جدة · صبابين قهوة مكة · ضيافة مناسبات المدينة المنورة · قهوجيين وصبابين · ضيافة أعراس جدة · قهوة عربية للمناسبات · مباشرين ضيافة · ضيافة فعاليات رسمية · قهوجي ينبع · ضيافة مناسبات بدر
EN (10): Arabic coffee servers Jeddah · hospitality services Makkah events · Saudi wedding hospitality · qahwaji service · Next.js hospitality website · local SEO service-by-city pages · ProfessionalService schema GeoCircle · Core Web Vitals LCP hospitality site · WCAG 2.1 AA Arabic RTL site · luxury hospitality web design Saudi

## 5. ثلاث زوايا محتوى
1. «حذفت 15 ادعاءً جغرافياً من موقع عميلي — وهذا ما حدث» — منشور عن الصدق الجغرافي وGeoCircle مقابل «كل المملكة».
2. «من 2240 إلى 956 مللي ثانية: ماذا غيّرت؟» — قصة أداء: keyframes بدل motion، WebP، سقف JS 90 KB (مع تحفّظ القياس المحلي).
3. «موقع ضيافة فاخر بلا صورة مخزون واحدة» — الهوية الذهبية على أسود ولقطات الموقع الحقيقية كمرجع للفئة.

## 6. الفجوات (صريحة)
تقنياً: أرقام الأداء قياس محلي لا حي؛ الموقع الحي V2 بينما الأرقام V3؛ 4 مستودعات متكررة بلا كانوني؛ V2 على Vercel يعيد 404 حسب selected-20. (tech.md، links.md)
تسويقياً: أرقام الواتساب/الاتصال غير موثّقة في المحفظة («يُستكمل»)، لا دراسة حالة ولا فيديو ديمو، ولا اسم عميل يمكن ذكره (قاعدة الفريق). وجود موقع باسم «أصول الضيافة الملكية» (aswlfor.com) يزاحم الاسم في البحث.

## English summary
Osoul Al-Diafa competes in Saudi events-hospitality (Arabic coffee servers for weddings, conferences, funerals) around Jeddah/Makkah/Madinah. Three verified competitors (accessed 2026-09-23) — Al-Qahwa Al-Malakiya, Qahwaji-Jed and Dallah Al-Diyafa — all sell through WhatsApp/phone with no prices, list broad city coverage and "competitive prices," and publish no performance or accessibility data. The project's defensible edge, from tech.md: geographic honesty (5 real cities, service-by-city pages, GeoCircle schema, 15 false claims removed), measured performance (LCP 956 ms, CLS ≤ 0.0001), zero WCAG 2.1 AA violations on 9 pages, and repo-level SEO/similarity checks. Gaps: numbers are local not live, the live site is V2, contact details and a case study are still "to be completed," and a similarly named competitor (aswlfor.com) exists.

## المصادر
- brief.ar/en.md، tech.md، links.md — portfolio-hub/01-projects/osoul-aldiafa (2026-09-11)
- https://alqahwaalmalakiya.com/ — 2026-09-23
- https://qahwaji-jed.com/ — 2026-09-23
- https://noblesoiree.com/?page=home — 2026-09-23
- ذُكرت بلا تحقق (نتائج بحث 2026-09-23): https://www.kahwgysa.com/ · https://qahawagy.com/ · https://aswlfor.com/qaheji-jeddah · https://thawq-rafeea.com/ · https://www.yojad.com/ · https://keifaldiafa.com/diyafa-munasabat-madinah
