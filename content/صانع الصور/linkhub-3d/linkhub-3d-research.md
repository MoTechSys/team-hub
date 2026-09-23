linkhub-3d | صانع الصور | 2026-09-23 | draft

# LinkHub 3D — بحث وتحليل السوق

تاريخ البحث: 2026-09-23 (بحث ويب + قراءة صفحات البدائل في اليوم نفسه). ادعاءات البدائل من صفحاتها؛ ادعاءات مشروعنا من README/tech.md/linkhub-audit.json فقط.

## 1. من يشتري هذا
- المستخدم النهائي: متابع على إنستقرام/تيك توك يضغط رابط البايو لعلامة ضيافة ويريد الوصول إلى واتساب أو الحساب أو الخريطة في ضغطة. (docs/00-INDEX «الطلب»)
- مشتري «المنتج» (النمط نفسه) لمحفظة معين: أصحاب علامات صغيرة فاخرة — ضيافة، مطاعم، استوديوهات — يريدون صفحة روابط تُشعر بالمنتج لا بقالب مستأجر، بلا اشتراك شهري ولا سكربت طرف ثالث. (brief.ar لمن يفيد)
- حجم الفئة: يُستكمل — لا رقم موثّق لدينا. مؤشر من السوق: Linktree يعلن على صفحته الرئيسية «70M+ people» — الفئة ضخمة، والتمايز فيها شكلي في الغالب.

## 2. البدائل والمنافسون (3)
| # | البديل | ماذا يقول عن نفسه (من صفحته) | حدّه أمام مشروعنا | الرابط (وصول 2026-09-23) |
|---|---|---|---|---|
| 1 | Linktree | «70M+ people»، «one link to help you share everything»، «Customize every detail or let Linktree automatically enhance it»، QR، تحليلات؛ خطط Free/Starter/Pro/Premium بحسب صفحة الأسعار | صفحة مستضافة لدى طرف ثالث بقالب موحّد؛ التخصيص ضمن حدود الخطة؛ لا تحكّم بالكود ولا بالطلبات الخارجية | https://linktr.ee/ (200) · https://linktr.ee/s/pricing (406 لعميل curl — تُفتح في المتصفح) |
| 2 | Beacons | «the most powerful, AI-packed, fully-stacked Link in Bio»، «Get all your creator tools, for free, forever»، بلوكات روابط/فيديو/موسيقى/تسجيل بريد، نطاق مخصص مجاني، بيع منتجات رقمية | موجّه للمبدعين والتحقيق النقدي (متجر/بريد) لا للعلامات الفاخرة؛ صفحة ثقيلة الوظائف تُستضاف لديهم | https://beacons.ai/i/app-pages/link-in-bio (200) |
| 3 | Later — Link in Bio | «link in bio tool for free»، «add up to five links on each Instagram, TikTok, or Snap post»، أزرار وخلفيات وثيمات، Mailchimp، عنوان/وصف SEO | امتداد لأداة جدولة سوشيال؛ التصميم ضمن ثيمات الأداة؛ لا انقلاب 3D ولا تحوّل صفحة | https://later.com/link-in-bio/ (200) · https://linkin.bio/latermedia/ (200) |

ظهرت أيضاً بلا فتح صفحاتها: Lnk.Bio (403 لعميل curl)، ومقالات مقارنة Beacons vs Linktree 2026، ومقالات أسعار Linktree 2026 (Free/$8/$15/$35–40) — لم تُعتمد الأسعار لأنها من طرف ثالث.

## 3. التموضع
| المحور | ماذا تقول البدائل | أين يتفوّق مشروعنا (من README/tech.md فقط) |
|---|---|---|
| الملكية والاستضافة | صفحة على نطاق المزوّد (أو نطاق مخصص ضمن الخطة)، اشتراك للميزات | ملف HTML واحد لكل علامة يُنشر على أي خادم ثابت؛ صفر اشتراك؛ 76 ملفاً بالكامل في المستودع |
| الطلبات الخارجية والخصوصية | سكربتات المزوّد وتحليلاته (لم تُقَس هنا) | **0 طلبات خارجية** مقيسة في المتصفح؛ خطوط woff2 وأيقونات SVG وصور محلية |
| الوزن | غير مقيس هنا | **8.4 KB** مضغوطة لصفحة كيف كاملة (8.0 لأصول) |
| التجربة البصرية | قوالب وثيمات ألوان؛ «Customize every detail» ضمن القالب | بطاقة مادية: انقلاب `rotateY(180°)` حقيقي مقيس بـ matrix3d، سُمك `translateZ`، لمعة specular، 15 طبقة خامة، وتحوّل الصفحة كاملة لهوية المنصة قبل الانتقال |
| العربية | واجهات إنجليزية أولاً؛ RTL بحسب القالب (غير مُتحقَّق تفصيلياً) | عربية RTL من الجذر بخطوط Amiri/Kufi محلية، تسميات عربية للمنصات، aria-label عربي |
| الوصولية | غير مذكورة على الصفحات المقروءة | كل بطاقة `<a href>` تعمل بلا JS، `:focus-visible`، `aria-live`، `prefers-reduced-motion`، تباين مقيس ALL PASS |
| التحليلات | Linktree وLater يعِدان بتحليلات وتتبّع | **فجوة**: لا تحليلات ولا تتبّع نقرات في مشروعنا |
| الإدارة | لوحة تحكم لتعديل الروابط | **فجوة**: التعديل يدوي في HTML وdata.json |

## 4. الكلمات المفتاحية
AR (10): صفحة روابط بايو عربية · link in bio بالعربي · بديل Linktree عربي · صفحة روابط فاخرة · بطاقات ثلاثية الأبعاد CSS · صفحة روابط بلا اشتراك · صفحة روابط تعمل بلا جافاسكربت · رابط QR لصفحة الروابط · تصميم صفحة روابط للمطاعم · صفحة روابط RTL
EN (10): custom link in bio page · Linktree alternative self-hosted · CSS 3D card flip rotateY · preserve-3d link cards · zero-dependency link page · link in bio no third-party scripts · RTL Arabic link in bio · single-file HTML landing · WCAG contrast link buttons · platform-themed link page

## 5. ثلاث زوايا محتوى
1. «صفحة روابط بـ 8.4 كيلوبايت وصفر طلبات خارجية — لماذا تدفع اشتراكاً؟» — مقارنة الملكية والوزن مع Linktree/Beacons/Later.
2. «كيف تجعل بطاقة CSS جسماً مادياً» — تشريح 15 طبقة backgroundImage، translateZ، specular بلا rAF، وحادثة تصحيح التباين (phone 1.09:1 → 14.3).
3. «الثيم الذي يتبع المنصة» — قياس تحوّل الصفحة بالبكسل والـ computed style، ولماذا `data-theme` وحدها لا تكفي (درس docs/02).

## 6. الفجوات (صريحة)
تقنياً: commit واحد فقط (2026-08-21) — لا تاريخ تطوير في git؛ لا تحليلات/تتبّع نقرات؛ تعديل الروابط يدوي في ملفَين (HTML + data.json)؛ README يقول «15 طبقة» ولم يذكر أصول (17)؛ docs/00 يشير إلى مجلد src/ غير موجود؛ Lighthouse غير موثّق. (tech.md)
تسويقياً: الرابطان الحيّان ميتان والنطاق «مؤقت (VM)» بحسب README نفسه؛ canonical/og/JSON-LD تشير إليهما؛ الحسابات الناقصة (سناب/يوتيوب/ثريدز لكيف، X/تيليجرام لأصول) معلّقة على المالك؛ أرقام الهاتف صريحة في HTML وdata.json (طُمست هنا)؛ docs/03 يحوي إشارات إلى توكنات مكشوفة سابقاً ومستودعات خاصة — يُنظَّف قبل أي عرض عام للمستودع.

## English summary
LinkHub 3D is a single-file, framework-free link-in-bio pattern applied to two hospitality brands: every card is a real `<a href>` that performs a true 3D flip (measured `matrix3d` at 180°), fills a 900 ms progress ring and recolours the whole page to the platform's identity before navigating. Measured on a local run: 8.4 KB gzipped, 0 external requests, one screen (844 = 844), 15 material layers per card face, all WCAG contrast pairs passing. Three alternatives accessed 2026-09-23 — Linktree ("70M+ people", customization within plan tiers), Beacons ("AI-packed", free-forever creator tools with monetization blocks) and Later's Link in Bio (free, up to five links per post, theme customization) — are all hosted, template-driven and analytics-oriented; none offers a physical 3D card or a page-wide platform theme. Gaps: no analytics, manual link editing, a single commit, dead live URLs on a self-declared temporary VM domain, and repo docs that need cleaning.

## المصادر
- README.md، docs/00-INDEX.md، docs/02-TECH-FACTS.md، docs/03-NEXT-TASK.md، docs/data.json، keif/index.html، asoul/index.html — moain2028/linkhub-3d (commit abd0989، 2026-08-21) + قياسات محلية وفحص Playwright 2026-09-23 (tech.md، linkhub-audit.json في هذه الحزمة)
- https://linktr.ee/ — 2026-09-23 (200؛ اقتباسات من الصفحة الرئيسية)
- https://beacons.ai/i/app-pages/link-in-bio — 2026-09-23 (200)
- https://later.com/link-in-bio/ — 2026-09-23 (200) · https://linkin.bio/latermedia/ (200)
- ذُكرت بلا اعتماد أرقامها: https://linktr.ee/s/pricing (406 لعميل curl) · https://lnk.bio/ (403) · مقالات مقارنة/أسعار 2026 (talkspresso، saasworthy، qr-verse، stackinfluence) — نتائج بحث 2026-09-23
