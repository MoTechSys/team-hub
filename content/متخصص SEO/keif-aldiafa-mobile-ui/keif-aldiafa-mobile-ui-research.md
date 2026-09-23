keif-aldiafa-mobile-ui | متخصص SEO | 2026-09-23 | v2 · بحث وتحليل (بحث ويب مؤرَّخ: 2026-09-23)

# keif-aldiafa-mobile-ui — بحث وتحليل السوق والتموضع
English summary at the end.

## 1. من يشتري هذا؟
- **المشاريع الصغيرة في الضيافة والخدمات** (قهوة مختصة، حلويات، تنسيق موائد وفعاليات — أقسام الواجهة نفسها) التي تريد واجهة جوال فاخرة تُقرأ في إضاءة منخفضة، بلا اشتراك منصة ولا فاتورة إطار (brief «لمن يفيد»؛ README «بلا أي إطار»).
- **كنمط تقني قابل للبيع:** أي مشروع صغير يريد «واجهة جوال بلا إطار بتباين مقيس» — ثلاثة ملفات يملكها ويستضيفها على أي خادم ثابت (tech.md).
- حجم الفئة: لا رقم مؤرّخ موثوق لعدد مشاريع الضيافة الصغيرة الباحثة عن واجهة جوال في السعودية/اليمن — **يُستكمل**.
- ملاحظة: العلامة نفسها لها 4 مشاريع أخرى على المنصة؛ هذا التسليم يعرض **النمط التقني** لا العلامة، ولا يقارن بمشاريع معين الأخرى.

## 2. البدائل الحقيقية (تاريخ الوصول 2026-09-23)
| البديل | ماذا يقول عن نفسه | السعر المعلن | الرابط |
|---|---|---|---|
| **Framer** (بناء مواقع/صفحات هبوط بصرياً) | تصميم ونشر بلا كود، CMS، استضافة | Free · Basic 10$/شهر · Pro 30$/شهر · Scale من 100$/شهر (سنوياً)؛ مقعد محرّر 20$/شهر منذ مايو 2026 | https://www.framer.com/pricing · https://goodspeed.studio/blog/framer-pricing-explained (2026-05-28) |
| **Tailwind Plus** (مكوّنات وقوالب UI جاهزة، Tailwind UI سابقاً) | 500+ مكوّن وقالب | دفعة واحدة 249$ (شخصي) · 849$ (فريق حتى 25) | https://tailwindcss.com/plus · https://toolradar.com/tools/tailwindcss/pricing (verified Sep 2026) |
| **قوالب Figma للمطاعم/الضيافة** (مجتمع Figma · Envato Elements · Etsy) | UI kits بـ160 شاشة، فاتحة/داكنة | مجانية على مجتمع Figma؛ Envato باشتراك؛ Etsy من ≈7$ | https://www.figma.com/community/file/1408307829185709558 · https://elements.envato.com/graphic-templates/ux-and-ui-kits/restaurant+app/compatible-with-figma |
| (أيضاً: **Anima** تصميم→كود، من 500$/شهر للمؤسسات — https://www.animaapp.com/pricing) |

## 3. التموضع: ماذا يقول البديل، وأين يتفوّق مشروعنا (من README/tech.md/measure.json فقط)
| ما يقوله البديل | ما عندنا (المصدر) |
|---|---|
| Framer: اشتراك شهري بالدولار + مقعد محرّر؛ البيانات والنشر على منصتهم | ثلاثة ملفات تملكها، 31.2 KB، تُستضاف على أي خادم ثابت؛ صفر تبعيات (tech.md «Source files»، «External runtime deps») |
| Tailwind Plus/Figma kits: مكوّنات LTR عامة تُعرَّب لاحقاً؛ التباين «يبدو جيداً» | RTL من الجذر بخطَّين عربيَّين (Almarai + Amiri)؛ التباين **مقيس**: 15/15 فوق 4.5:1 بـgetComputedStyle، الأدنى 5.00:1 (measure.json) |
| قوالب: زر عائم يحجب النص أو يتداخل مع الشريط | زر عائم مرسى على `--tabbar-h` بمساحة محجوزة 70 px، 0 px تداخل بـgetBoundingClientRect، ويختفي أثناء التمرير (README؛ app.js) |
| Anima/Figma→code: كود مولّد ثقيل بإطار | HTML/CSS/JS مكتوبة يداً: 9.7 KB مضغوطة، 20 طلباً، LCP 232 ms محلياً (tech.md) |
| — | لوحة ألوان بـ21 متغيّراً مُعلَنة في `:root` وتدرّج ذهب بخمس نقاط — قابلة لإعادة الاستخدام كعلامة (styles.css) |

**نقطة صدق:** البدائل تعطي CMS واستضافة ونشراً في دقائق وعشرات الشاشات؛ مشروعنا **شاشة واحدة**، **بلا رابط حي**، بلا اختبارات، وصوره السبع **مولّدة بالذكاء الاصطناعي** (README)، وفيه عيبان مقيسان: القائمة الجانبية على الديسكتوب خارج إطار الجهاز، وreduced-motion جزئي (tech.md «Cleanup notes»).

## 4. الكلمات المفتاحية
**عربي (10):** واجهة جوال فاخرة · تصميم واجهة عربية RTL · تباين WCAG مقيس · واجهة HTML بلا إطار · زر واتساب عائم · تصميم تطبيق ضيافة · لوحة ألوان ذهبية داكنة · واجهة جوال خفيفة · إمكانية الوصول في التصميم العربي · صفحة هبوط للمشاريع الصغيرة
**English (10):** premium mobile UI no framework · Arabic RTL mobile interface · WCAG AA contrast getComputedStyle · floating WhatsApp button overlap · dark gold luxury UI palette · single-page vanilla JS UI · hospitality app UI design · lightweight mobile landing page · measured accessibility audit · static mobile UI small business
(بلا أحجام بحث — لا أداة بيانات هنا؛ الاختيار من صياغات ظهرت في نتائج البحث المؤرّخة ومن محتوى المستودع.)

## 5. ثلاث زوايا محتوى مقترحة
1. **«التباين يُقاس لا يُقدَّر»** — سكربت Playwright من 40 سطراً يقرأ getComputedStyle ويحسب نسبة WCAG لكل نص، ولماذا كشف فرقاً واحداً عن جدول README (tab_txt 7.45 لا 5.00) وحالة لا تُقاس (نص التدرّج) (shoot.py، measure.json).
2. **«زر عائم لا يحجب شيئاً»** — لماذا يفشل أي زر ثابت أمام النص مهما ضُبط موضعه، وحل «اختفِ أثناء التمرير وعُد بعد 420 ms» بقياس getBoundingClientRect (app.js تعليق؛ README «الزر العائم»).
3. **«تدقيق SEO/وصولية تقني لواجهة جميلة»** — ما يكشفه فحص عشر دقائق: لا meta description/OG/canonical، reduced-motion لا يطابق `::after`، قائمة الديسكتوب خارج الإطار، أحجام خط 8 px، 11 طلب خطوط من أصل 20 — مع قائمة إصلاح قبل النشر (tech.md «Cleanup notes»).

## 6. الفجوات (صريحة)
- **تقنية:** لا رابط حي ولا وسوم meta description/OG/canonical/manifest · لا اختبارات ولا CI · commitان بتاريخ واحد (2026-08-08) · `.drawer` مموضعة نسبة إلى `.device-stage` فتفتح خارج إطار الجهاز على الديسكتوب · `prefers-reduced-motion` لا يوقف لمعة `.btn-gold::after` · **11 طلباً لخطوط Google من أصل 20** (CSS + 10 woff2) في واجهة تُوصَف بأنها «بلا تبعيات» — التبعية الوحيدة لكنها نصف الطلبات؛ الحل: self-host لوزنَين فقط أو `font-display: swap` مع subset عربي · أحجام خط 8–8.6 px في التذييل وشريط الثقة والمربعات.
- **محتوى:** أرقام شريط الثقة (+500 مناسبة · 4.9 · 3 مدن) نص ثابت بلا مصدر — بيانات عرض · README يجمع tab_txt مع foot_tag عند 5.00:1 بينما القياس 7.45:1.
- **تسويقية/خصوصية:** الصور السبع مولّدة بالذكاء الاصطناعي (يُفصَح على شرائح اللقطات + SOURCES + الشرح) · زر واتساب برقم نائب في href · العلامة لها 4 مشاريع أخرى على المنصة — يُقدَّم كنمط تقني · شاشة واحدة فقط (لا صفحات حجز/باقات فعلية خلف التبويبات — روابط # فقط).

## 7. المصادر
- README.md · index.html · styles.css · app.js — https://github.com/moain2028/keif-aldiafa-mobile-ui (commitان 2026-08-08)
- tech.md وmeasure.json وshoot.py الخاصة بهذا التسليم (قياس محلي 2026-09-23)
- Framer: https://www.framer.com/pricing · https://goodspeed.studio/blog/framer-pricing-explained (2026-05-28، وصول 2026-09-23)
- Tailwind Plus: https://tailwindcss.com/plus · https://toolradar.com/tools/tailwindcss/pricing (وصول 2026-09-23)
- Figma community / Envato Elements / Etsy (وصول 2026-09-23) · Anima: https://www.animaapp.com/pricing

---
## English summary
Buyers: small hospitality/service businesses wanting a premium, low-light-readable mobile UI without a platform subscription; and, as a sellable pattern, any small business wanting a "no-framework mobile UI with measured contrast" in three owned files. Market size: no dated figure — "to be completed". The brand has four other projects on the platform; this delivery presents the technical pattern, not the brand.
Alternatives (accessed 2026-09-23): Framer (Free; $10/$30/$100+ per month; $20 editor seat), Tailwind Plus ($249 personal / $849 team, one-time), Figma restaurant UI kits (free community / Envato subscription / Etsy ≈$7), Anima (from $500/month).
Positioning (from README/tech.md/measure.json only): three owned files, 31.2 KB / 9.7 KB gzipped, zero dependencies; RTL from the root with two Arabic typefaces; contrast measured — 15/15 above 4.5:1, lowest 5.00:1; FAB with 0 px overlap that hides while scrolling; a 21-variable palette with a five-stop gold gradient. Honest gaps: single screen, no live URL, no tests, AI-generated images (disclosed), desktop drawer outside the frame, partial reduced-motion, sub-12 px fonts, 11 font requests, unsourced trust numbers.
