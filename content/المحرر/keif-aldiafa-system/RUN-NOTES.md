keif-aldiafa-system | المحرر | 2026-09-23 | draft

# RUN-NOTES — التشغيل المحلي والتطميس

## البيئة
- Node v22.23.2 · `npm install` → 88 حزمة (express 5 · puppeteer-core 25).
- المشروع يفترض Chromium في `/usr/bin/google-chrome` (render.js: `CHROME_PATH`). غير موجود هنا → ثُبّت `chrome@154.0.8037.57` عبر `npx @puppeteer/browsers install chrome@stable` + مكتبات النظام (libatk1.0-0t64 · libatk-bridge2.0-0t64 · libxcomposite1 · libxdamage1 · libatspi2.0-0t64 · libnss3 · libgbm1 · libasound2t64 · libcups2t64) + fonts-noto-core (Noto Naskh Arabic / Nastaliq Urdu حاضرة).
- التشغيل: `CHROME_PATH=<chrome> node server.js` (127.0.0.1:3210) · `node cli.js modules` · `node cli.js invoice <json> <out.pdf|png>`.

## ما عمل (2026-09-23)
- `/health` → `{"ok":true,"modules":["invoices"]}` · `/api/modules` يعيد 1 ready + 5 planned.
- `node cli.js modules` يطبع ✅ الفواتير و🔜 5 وحدات.
- توليد PDF/PNG من CLI: ≈1.1 ث للفاتورة (قياس `date` حول الأمر، بما فيه إقلاع Chromium).
- 14 بنداً → PDF صفحتان، «يتبع في الصفحة التالية…» + «صفحة ١ من ٢»؛ A4 594.96×841.92 pt؛ 5 خطوط مضمّنة (`pdffonts`).
- واجهة الفواتير: النموذج، القوالب السريعة، الإجمالي، المعاينة (`POST /invoices/api/preview`) — كلها مصوَّرة.
- لم يفشل شيء بعد تثبيت Chromium. الرابط الحي في README (tiyquqno.gensparkclaw.com/keif/) لا يستجيب (curl: لا اتصال).

## التطميس المطبَّق قبل التصوير (نسخة عمل في /tmp، المستودع الأصلي لم يُمس)
- template.js · core/public/index.html · modules/invoices/public/index.html: رقم السجل التجاري الحقيقي (بصيغتيه اللاتينية والهندية) → `4030000000`؛ سطر IBAN الحقيقي → `SA00 0000 0000 0000 0000 0000`؛ رقم الهاتف الحقيقي (بصيغتيه) → `+966 5X XXX XXXX` / `05XXXXXXXX`. (البريد info@keifaldiafa.com وموقع المؤسسة بقيا — بيانات جهة، لا شخص.)
- assets/stamp.png: رقم السجل داخل الختم مُطمَّس بـ GaussianBlur.
- بيانات الفواتير: لم يُستخدم live360.json (Live 360 + اسم شخص في «عناية») ولا janson.json (جانسون كنترول العربية) ولا signed.json (اسم شخص في التوقيع). أُنشئت demo-a.json / demo-14.json / demo-safe.json بعميل «شركة النموذج للتجارة» / «مؤسسة المثال للمناسبات»، عناية «مدير المشتريات»، توقيع «المدير التنفيذي»، أرقام فواتير 1001–1003. نصوص البنود من القوالب السريعة في الواجهة (وصف خدمة، لا أسماء).
- السكربتات: work/keif/prep.sh (التطميس) · work/keif/shoot.js (التصوير) في مساحة المحرر.

## اللقطات
desktop-01..05 (2880×1800 = 1440×900 @2x) · mobile-01..05 (780×1688 = 390×844 @2x) · render-01/03 (1588×2246، PNG من الوحدة) · render-02-1/2 (1240×1754، pdftoppm 150dpi من PDF الوحدة).
