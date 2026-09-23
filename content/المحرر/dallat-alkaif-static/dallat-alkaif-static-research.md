dallat-alkaif-static | المحرر | 2026-09-23 | draft

# دلة الكيف — النسخة الثابتة: بحث وتحليل

## من يشتري هذا
أصحاب مشاريع الضيافة والمناسبات الصغيرة في السعودية الذين يريدون موقعاً تعريفياً فاخراً يعمل على أي استضافة رخيصة بلا صيانة، ومطوّرون يبحثون عن مرجع عربي RTL لموقع ثابت بلا إطار. حجم الفئة بالأرقام: يُستكمل — لا مصدر موثّق، ولا نقدّر.

## 3 بدائل حقيقية (تاريخ الوصول 2026-09-23)
| البديل | ماذا يقول | أين يختلف عن مشروعنا | الرابط |
|---|---|---|---|
| Wix | «Website Builder — Create a Free Website In Minutes … 2,000+ templates, built-in AI tools and a custom domain» | منشئ مواقع سحابي بقوالب؛ لا تملك الملفات ولا تنقلها؛ الاشتراك للنطاق | https://www.wix.com/ |
| Astro | «Astro builds fast content sites, powerful web applications, dynamic server APIs» — مولّد مواقع مفتوح المصدر (62,756 نجمة، آخر دفع 2026-09-22) | يُخرج HTML ثابتاً أيضاً لكن عبر مرحلة بناء وnode_modules؛ يحلّ مشكلة تكرار التنقّل/التذييل بالمكوّنات | https://astro.build/ · https://github.com/withastro/astro |
| Hugo | «The world's fastest framework for building websites» — مولّد ثابت بملف تنفيذي واحد (89,909 نجمة، آخر دفع 2026-09-22) | بلا Node لكن بمرحلة بناء وقوالب Go؛ أقرب فلسفياً إلى «ملفات فقط» | https://gohugo.io/ · https://github.com/gohugoio/hugo |
| (استضافة) GitHub Pages / Netlify | «Websites for you and your projects, hosted directly from your GitHub repository. Just edit, push, and your changes are live.» / «deploy instantly on production infrastructure» | مكان تشغيل هذا المشروع كما هو — لا بديل بل مكمّل | https://pages.github.com/ · https://www.netlify.com/ |

## التموضع
البدائل الثلاثة تحلّ «كيف أبني موقعاً صغيراً» بأداة: منشئ سحابي (Wix) أو مولّد ثابت (Astro، Hugo). مشروعنا يقف في أقصى طرف البساطة: **لا أداة أصلاً** — الملف الذي تحرّره هو الملف الذي يُخدَم (README §لماذا بلا إطار). ما نكسبه مقيس: 8 طلبات/558 KB للرئيسية و0 KB JavaScript إطار مقابل التوأم Next.js (tech.md جدول المقارنة). ما نخسره صريح: مع 13 صفحة يُكرَّر التنقّل والتذييل يدوياً، ولا فحص أنواع، والتخطيط جوالي بعرض أقصى 480px — وهذه بالضبط ما تُصلحه Astro/Hugo بالمكوّنات والقوالب. Wix يتفوّق في «بلا مطوّر أصلاً» وفي التحرير البصري، ويخسر في الملكية والنقل والوزن.

## 10 كلمات مفتاحية
AR: موقع ثابت بلا إطار · موقع HTML خام · موقع ضيافة عربي RTL · بلا مرحلة بناء · صفر تبعيات · استضافة مشتركة · GitHub Pages عربي · موقع خفيف للجوال · حجز عبر واتساب · جنوب السعودية ضيافة
EN: static site no framework · plain HTML CSS site · Arabic RTL static website · zero dependencies · no build step · shared hosting website · GitHub Pages Arabic · lightweight mobile site · WhatsApp booking form · static vs Next.js comparison

## 3 زوايا محتوى
1. «نفس الموقع مرتين»: المقارنة المقاسة static مقابل Next.js بجدول واحد وتحفّظاتها — زاوية المطوّرين (LinkedIn).
2. «ما الذي تدفعه للإطار؟»: 494 KB من JavaScript لموقع بلا تفاعل — زاوية أصحاب المشاريع الصغيرة (كاروسيل).
3. «قواعد المحتوى أهم من الكود»: لا مدن خارج النطاق، لا أرقام مختلقة، لا أسعار — من README — زاوية الثقة.

## الفجوات (صريحة)
- تقنياً: خطوط من Google Fonts (طلب خارجي وخصوصية؛ README يقترح الاستضافة المحلية)؛ تكرار يدوي للتنقّل والتذييل في 13 ملفاً (أي تعديل = 13 تحريراً)؛ تخطيط جوالي فقط على الديسكتوب (عمود 480px)؛ صورتان غير مستخدمتَين 1.22 MB في المستودع؛ لا favicon؛ og:url يشير إلى نطاق ميت؛ README يربط النسخة الأحدث بـ moain2026/… بينما المستودع العام moain2028/…؛ رقم الجوال الحقيقي مكرَّر في 13 صفحة (40 موضعاً) — يُنقل إلى متغيّر واحد أو يُطمس قبل أي عرض عام.
- تسويقياً: لا رابط حي؛ إيداع واحد قبل شهر ونصف؛ كل الصور مولَّدة بالذكاء الاصطناعي (يجب الإفصاح في كل نشر ويُضعف «الفخامة الحقيقية»)؛ التوأم Next.js منشور قبله على المنصة فيحتاج الثابت زاوية «متى تختار» لا «موقع جديد».
- بيانات: لا إحصائيات للمؤسسة (سنة تأسيس، مناسبات) بقرار صادق من المالك — فلا أرقام «نتائج» تُعرض.

## المصادر
- المستودع https://github.com/moain2028/dallat-alkaif-static (README · *.html · sv.css) والتوأم https://github.com/moain2028/dallat-alkaif-nextjs (package.json · next.config.ts · out/ بعد البناء).
- القياس: 01-projects/dallat-alkaif-static/tech.md وRUN-NOTES.md (measure3.js، 2026-09-23).
- روابط البدائل أعلاه، وُصلت 2026-09-23 بـ curl؛ الاقتباسات من عناوين/أوصاف الصفحات؛ النجوم من api.github.com في اليوم نفسه.

## English summary
Buyers: small Saudi hospitality businesses wanting a luxury brochure site on cheap hosting with zero upkeep, and developers seeking an Arabic RTL no-framework reference. Alternatives (accessed 2026-09-23): Wix (cloud builder, 2,000+ templates), Astro and Hugo (open-source static generators with a build step), plus GitHub Pages/Netlify as the hosts this project runs on as-is. Positioning: the extreme end of simplicity — no tool at all — with measured gains (8 requests/558 KB, 0 KB framework JS vs the Next.js twin) and stated costs (hand-duplicated nav/footer, no types, 480px mobile layout). Gaps: Google Fonts, dead og:url, README links the newer twin to moain2026/… (public repo is moain2028/…), the real phone number hard-coded in all 13 pages (40 spots), two unused images, no favicon, AI-generated imagery, single commit, no live URL.
