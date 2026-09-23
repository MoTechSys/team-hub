electricity-billing-pwa-v2 | كاتب المحتوى | 2026-09-23 | ready

# electricity-billing-pwa-v2 — فهرس اللقطات (20 لقطة حقيقية، 2x)

التقاط: تشغيل محلي للمستودع moain2028/electricity-billing-pwa-v2 (commit 9ee69cb، main) — `npm install` → `npm run build` → `PORT=3105 npm start`، ثم Playwright/Chromium بـ deviceScaleFactor=2: ديسكتوب 1440×900 (ملف 2880×1800) وجوال 390×844 (780×1688)، locale ar. لا خادم ولا قاعدة بيانات خارجية: البيانات أُدخلت عبر ميزة «استيراد نسخة» في /settings من ملف `_demo-backup.json` (12 مشتركاً باسم «مشترك تجريبي NN»، 20 فاتورة، اسم محطة «محطة تجريبية للكهرباء») — لا أسماء ولا هواتف حقيقية. المبالغ كتابةً حُسبت بدالة المشروع نفسها `numberToArabicWords`. رمز الترخيص المستخدم للدخول هو الثابت في `src/components/OnboardingGate.tsx`. سكربت الالتقاط: `_portfolio-shoot.mjs`.

| الملف | الصفحة | ملاحظة | استخدام مقترح |
|---|---|---|---|
| desktop-03-gate-license | بوابة التهيئة — رمز الترخيص | أول تشغيل | |
| desktop-05-settings-backup | /settings — الإعدادات + تصدير/استيراد النسخة الاحتياطية | رسالة «تم الاستيراد ✅ (12 مشترك، 20 فاتورة)» | زاوية «بياناتك في جهازك» |
| desktop-06-dashboard | /dashboard — لوحة التحكم (12 · 10 · 20 · 18 · 2 · 3,240,200) | | بطاقة أرقام |
| desktop-07-subscribers | /subscribers — قائمة المشتركين (12) | | |
| desktop-10-invoice-new | /invoices/new — نموذج فاتورة فارغ | | |
| desktop-11-invoice-new-filled | /invoices/new — مثال README (24,149 → 25,254 = 1,105 kWh = 243,100 ريال) | حساب فوري + تفقيط | **اللقطة الرئيسية (ديسكتوب)** |
| desktop-12-archive | /invoices/archive — أرشيف 20 فاتورة | | |
| desktop-13-invoice-print | /invoices/[id]/print — فاتورة A4 أفقية | طباعة / PDF / مشاركة | لقطة ثانية |
| mobile-01-splash | شاشة البداية (0.6 ث من الفتح) | | الريل |
| mobile-02-gate-install | بوابة التثبيت PWA | | |
| mobile-03-gate-license | رمز الترخيص | | |
| mobile-05-settings-backup | الإعدادات + نسخة احتياطية | | |
| mobile-06-dashboard | لوحة التحكم — شبكة 2×2 + شريط سفلي عائم | | **اللقطة الرئيسية (جوال)** |
| mobile-07-subscribers | المشتركون | | |
| mobile-08-subscribers-kebab | قائمة ⋮ (إصدار فاتورة / تعطيل / حذف) | | |
| mobile-09-subscriber-new | إضافة مشترك | | |
| mobile-10-invoice-new | نموذج فاتورة فارغ | | |
| mobile-11-invoice-new-filled | نموذج فاتورة محسوب | | مروحة |
| mobile-12-archive | الأرشيف (أعمدة مخفية على الجوال) | | |
| mobile-13-invoice-print | الفاتورة A4 مصغّرة لتلائم الجوال | | |

لقطات إضافية غير مستخدمة في `_extra/` (splash ديسكتوب، بوابة التثبيت ديسكتوب، لوحة فارغة، ⋮ ديسكتوب، إضافة مشترك ديسكتوب، /invoices).
