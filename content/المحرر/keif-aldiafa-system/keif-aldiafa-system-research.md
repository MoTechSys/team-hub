keif-aldiafa-system | المحرر | 2026-09-23 | draft

# نظام كيف الضيافة — بحث وتحليل

## من يشتري هذا
مؤسسات فردية وشركات صغيرة في السعودية (ضيافة، تنظيم مناسبات، تأجير تجهيزات) تُصدر فواتيرها يدوياً بقالب Word أو Excel وتريد فاتورتها الحالية نفسها آلياً. الشريحة الأعرض: أي مشروع صغير لديه «مستند مرجعي» يريد استنساخه بدقة (فاتورة، عرض سعر، عقد). حجم الفئة بالأرقام: يُستكمل — لا مصدر موثّق في المستودع، ولم يُبحث عنه هنا لتفادي رقم مقدَّر.

## 3 بدائل حقيقية (تاريخ الوصول 2026-09-23)
| البديل | ماذا يقول | الرابط |
|---|---|---|
| Zoho Invoice (السعودية) | «100% free VAT online invoicing software for small businesses» و«Create e-invoices compliant with ZATCA regulations» — سحابي مجاني، قوالب فواتير عامة، توافق ZATCA | https://www.zoho.com/sa/invoice/ |
| دفترة Daftra | «نظام ERP سحابي متكامل لإدارة الحسابات والمبيعات والمخازن والموارد البشرية» مع «الفاتورة الإلكترونية السعودية - هيئة الزكاة والدخل» وتجربة مجانية — عربي بالكامل، واسع النطاق | https://www.daftra.com/ |
| Invoice Ninja | «Free Invoicing Software for Small Business»، خطة مجانية دائمة، قوالب فواتير، خيار Self-Hosting؛ الكود على GitHub (10,104 نجمة، آخر دفع 2026-09-22) | https://invoiceninja.com/ · https://github.com/invoiceninja/invoiceninja |
| (بديل تقني مفتوح للمطوّر) Puppeteer | «JavaScript API for Chrome and Firefox» — نفس محرّك التصيير الذي يعتمده المشروع، لمن يبني الحل بنفسه | https://github.com/puppeteer/puppeteer |

ملاحظة: Wafeq (wafeq.com) وQoyod (qoyod.com) بديلان معروفان محلياً لكن صفحتيهما لم تُعطِ عنواناً/وصفاً قابلاً للاقتباس عند الوصول (403 / بلا عنوان) فلم يُدرجا.

## التموضع
البدائل الثلاثة برامج فواتير عامة سحابية: قوالب موحّدة قابلة للتخصيص جزئياً، توافق ضريبي، واشتراك أو خطة مجانية. مشروعنا لا ينافسها في «برنامج فواتير» بل في شيء لا تقدّمه: **الفاتورة الأصلية نفسها بالمليمتر** — الإطار والختم والعلامة المائية مستخرجة من PDF المؤسسة (tech.md: الأصول 15 ملفاً؛ DOCS/06: فارق ≤1 بكسل)، تعمل محلياً بلا سحابة ولا اشتراك، ومن CLI وAPI أيضاً. أين يتفوّق المنافس بصراحة: توافق ZATCA للفاتورة الإلكترونية (المؤسسة غير خاضعة حالياً — DOCS/07 §قرارات مؤجّلة)، سجل العملاء والمدفوعات والتقارير (كلها مخطَّطة لا منجزة عندنا)، والاستضافة الجاهزة.

## 10 كلمات مفتاحية
AR: توليد فواتير · فاتورة PDF عربية · قالب فاتورة مطابق · نظام فواتير لمؤسسة · فاتورة A4 · توقيع إلكتروني على الفاتورة · ترقيم صفحات الفاتورة · Chromium إلى PDF · نظام معياري Node · فواتير مؤسسة ضيافة
EN: Arabic invoice generator · HTML to PDF invoice · pixel-matched invoice template · Node Express invoice system · Puppeteer PDF Arabic RTL · A4 invoice from JSON · invoice CLI · e-signature invoice PDF · modular business system · hospitality invoicing Saudi

## 3 زوايا محتوى
1. «لم نُعِد تصميم الفاتورة — استخرجناها»: قصة pdfimages والقياس بالمليمتر (DOCS/02) — زاوية للمطوّرين.
2. «14 بنداً كانت تختفي»: كيف كشف تدقيق مستقل فقدان بيانات صامتاً وكيف أُصلح بقياس ارتفاع الصفوف (DOCS/06 §3) — زاوية الثقة.
3. «1 من 6»: لماذا نعرض وحدة واحدة جاهزة بصدق وخارطة طريق لخمس، بدل «نظام متكامل» — زاوية الشفافية لأصحاب المشاريع الصغيرة.

## الفجوات (صريحة)
- تقنياً: لا قاعدة بيانات ولا سجل فواتير ولا ترقيم تلقائي؛ لا اختبارات آلية في المستودع؛ بيانات المؤسسة ثابتة في الكود (template.js ORG) فالنظام لمؤسسة واحدة؛ يعتمد على Chromium خارجي بمسار ثابت؛ لا توافق ZATCA (غير مطلوب حالياً لكنه سقف للنمو).
- تسويقياً: لا رابط حي (README يشير إلى رابط ميت)؛ 4 إيداعات في يوم واحد قبل شهرين — لا نشاط ظاهر؛ لا حزمة عرض/فيديو قبل هذه الحزمة؛ القيمة الأساسية (المطابقة بالمليمتر) لا تُرى إلا بمقارنة جنب إلى جنب مع الأصل، وهي غير منشورة لأن الأصل يحمل بيانات المؤسسة.
- تسويقياً أيضاً: المشروع مخصّص لعميل واحد، فالترويج له يكون كـ«منهجية/خدمة» لا كمنتج قابل للتنزيل.

## المصادر
- المستودع: https://github.com/moain2028/keif-aldiafa-system (README · DOCS/00, 02, 06, 07 · core/registry.js · modules/invoices/src/template.js)
- الأرقام المقاسة: 01-projects/keif-aldiafa-system/tech.md (2026-09-23)
- روابط المنافسين أعلاه، وُصلت 2026-09-23 بـ curl؛ الاقتباسات من عناوين/أوصاف الصفحات نفسها. بيانات GitHub لـ invoiceninja من api.github.com في اليوم نفسه.

## English summary
Buyers: Saudi small businesses that still produce invoices from a Word template and want their exact document automated. Alternatives (accessed 2026-09-23): Zoho Invoice SA (free, ZATCA-compliant, generic templates), Daftra (Arabic cloud ERP with Saudi e-invoicing), Invoice Ninja (free plan, self-hostable, open code on GitHub); Puppeteer as the open building block. Positioning: not an invoicing app but a millimetre-accurate reproduction of the company's own invoice (assets extracted from the original PDF, within 1 px per the developer's audit), local, with CLI and API; competitors win on e-invoicing compliance, client/payment records, and hosting. Gaps: no database or numbering, no tests, single-company constants in code, dead live link, 4 commits in one day, and a value proposition that needs a side-by-side the company data prevents us from publishing.
