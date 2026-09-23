almham-electricity-erp | صانع العروض | 2026-09-23 | design-pack-v1

# مصادر كل نص ورقم على التصاميم (24 ملف PNG)

المصدر الحي: https://github.com/moain2028/portfolio-hub → 01-projects/almham-electricity-erp/ · الهوية: 02-brand/README.md

| العنصر على التصميم | AR | EN | المصدر |
|---|---|---|---|
| العنوان H1 | ERP لتوليد وتوزيع الكهرباء | An ERP for electricity generation & distribution | brief.ar.md / brief.en.md — H1 |
| السطر فوق العنوان | أنظمة العباسي المتخصصة | Al-Abbasi Specialized Systems | brief.ar.md / brief.en.md — H1 |
| اسم المستودع (Amber, Mono) | almham-electricity-erp | almham-electricity-erp | اسم مجلد المشروع في portfolio-hub (بلا رابط GitHub — المستودع خاص) |
| السطر التعريفي | نظام واحد من قراءة العداد إلى القيد | One system from meter reading to ledger | brief — «لمن يفيد» / «Who it's for» |
| الوصف (X, Portrait, Hero) | متعدد الشركات والفروع والمحطات — فوترة مدمجة، ديزل وطاقة شمسية، خزينة، موظفون ومهام، خرائط المشتركين | Multi-company, multi-branch, multi-station — integrated billing, fuel & solar, treasury, employees & tasks, subscriber maps | brief — «الحل» / «Solution» |
| تاجات التقنيات | Angular 22 · NestJS 11 · PostgreSQL · Drizzle · Leaflet · PWA | نفسها | brief «الحل» + tech.md «التقنيات» |
| رقم 9 | نطاقات وظيفية | functional domains | tech.md «الأرقام» ← README §4 |
| رقم 687 | فترة فوترة مطابَقة | billing periods reconciled | tech.md «الأرقام» ← README §6 |
| رقم 515 | ملف اختبار | test files | tech.md «الأرقام» ← git ls-tree 2026-09-11 |
| رقم 48 (X/Portrait/Story/Hero) | شاشة Flutter | Flutter screens | tech.md «الأرقام» ← git ls-tree |
| السطر السفلي | دراسة حالة · نظام داخلي — يعمل ببيانات حقيقية لدى شركة كهرباء محلية | Case study · internal system — running on live data at a local electricity utility | brief «النتيجة» + tech.md «الحالة» + links.md (بلا اسم عميل) |
| CTA (Story فقط) | أُقدّم دراسة لنظام محطتك — راسلني | Let's scope your utility's system — DM or email | brief — «تواصل» / «Contact» |
| شارة الشريحة | شركات | Companies | tech.md «الشريحة: شركات» · لون #3B82F6 من 02-brand |
| نسخة بشعار (wordmark نصّي) | معين العباسي | Moain Al-Abbasi | design-pack-standard-v1 §2 — بلا أيقونة M |

## اللقطات (حقيقية، من screenshots/ — لا لقطة مولّدة)
- إطار المتصفح: `screenshots/desktop-02-dashboard.png` (2880×1800)
- إطار الجوال: `screenshots/mobile-02-dashboard.png` (780×1688)
- الجوال الثاني في Story: `screenshots/mobile-06-subscribers-map.png` (780×1688)

## الهوية (02-brand/README.md)
- ألوان: Navy #0E2A47 · Ink #08172B · Amber #F4A62A · Sand #F7F5F0 · Mist #DCE3EA · Slate #7A8A9C · شركات #3B82F6
- خطوط: IBM Plex Sans Arabic (AR) · Inter (EN) · JetBrains Mono (اسم المستودع والتاجات) · الأرقام غربية
- تباين: Sand على Navy ≈ 13:1 · Amber على Navy ≈ 7.5:1 · Sand على #3B82F6 ≈ 4.6:1 — كلها AA فأعلى

## قاعدة الشعار
- `-nologo`: لا شعار ولا أيقونة؛ مساحة أمان خالية 12% من العرض أعلى-يمين (AR) / أعلى-يسار (EN).
- `-logo`: الاسم كنص فقط في نفس الموضع، بخط الهوية.

## ملاحظات
- الأرقام «عدد المشتركين/المستخدمين» لم تُستخدم لأنها «يُستكمل» في tech.md.
- المصدر القابل للتعديل: `build.py` (HTML/CSS → PNG عبر Chromium) — أي تغيير نص أو لون يُعاد توليده للـ24 ملفاً دفعة واحدة.
