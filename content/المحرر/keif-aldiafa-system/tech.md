keif-aldiafa-system | المحرر | 2026-09-23 | draft

# keif-aldiafa-system — Technical Sheet

- **Repo:** moain2028/keif-aldiafa-system (public)
- **Primary language / stack:** JavaScript (Node 22 · Express 5 · puppeteer-core 25 → Chromium) · HTML/CSS بمقاسات mm · CLI
- **Problem:** مؤسسة ضيافة في جدة تُصدر فواتيرها يدوياً (Word/قوالب) — بطء، أخطاء حسابية موثّقة في الفواتير الأصلية، 3 صيغ مختلفة للإجمالي، ولا سجل مركزي (DOCS/00 §الخلاصة التنفيذية).
- **Solution / core features:** نظام أعمال معياري (modules) لمؤسسة واحدة. الوحدة الأولى «الفواتير» جاهزة: توليد فاتورة A4 مطابقة بصرياً للأصل (PDF/PNG/معاينة HTML) من JSON عبر CLI أو REST أو واجهة ويب عربية RTL؛ توقيع إلكتروني (خط أو صورة)؛ ترقيم صفحات تلقائي مقيس فعلياً من ارتفاع الصفوف (لا قصّ صامت)؛ وضع طباعة آمن بهامش 5 مم؛ أرقام هندية/لاتينية؛ عناوين أعمدة مرنة؛ قوالب بنود سريعة. الأصول البصرية (إطار ذهبي، علامة مائية، ختم، أيقونات) مستخرجة من PDF أصلي بـ pdfimages.
- **Architecture notes:** `server.js` يركّب الوحدات تلقائياً عبر `core/registry.js` (اكتشاف `modules/<id>/module.js` + عقد الوحدة: id/basePath/register). الوحدات المخطَّطة الخمس معرَّفة كـ placeholders في `PLANNED` داخل registry وتظهر في الواجهة الرئيسية بشارة «قادمة». لا قاعدة بيانات بعد. النشر الأصلي: pm2 + Caddy على `/keif/` (README §Run).
- **Status:** prototype (وحدة 1 إنتاجية حسب DOCS/06؛ النظام ككل 1 من 6 وحدات)
- **Last commit:** 2026-07-31 (4 commits كلها في اليوم نفسه)
- **Live URL:** none — الرابط المذكور في README (tiyquqno.gensparkclaw.com/keif/) لا يستجيب (curl 2026-09-23: لا اتصال)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source (file/line or command) |
|---|---|---|
| Modules ready / total | 1 / 6 | `node cli.js modules` (✅ الفواتير، 🔜 5) · core/registry.js `PLANNED` (5 عناصر) · README §Modules |
| Commits | 4 | `git log --oneline \| wc -l` |
| Last commit | 2026-07-31 | `git log -1 --date=short` |
| Repo size (بلا .git/node_modules) | 1.4 MB | `du -sh` |
| Source lines (JS+HTML) | 1,145 (JS 727) | `wc -l` على server.js cli.js core/*.js core/public/index.html modules/invoices/**/*.js,html |
| Documentation | 8 ملفات DOCS + تقرير تدقيق · 1,041 سطراً · ≈5,500 كلمة | `wc -l DOCS/*.md` · `wc -w DOCS/*.md _audit/*.md README.md` |
| Visual assets | 15 ملفاً (logo/border/stamp/watermark/icons) | `ls modules/invoices/public/assets \| wc -l` |
| Sample invoices in repo | 3 JSON | modules/invoices/data/ |
| Dependencies (runtime) | 2 (express ^5.2.1 · puppeteer-core ^25.4.0) | package.json |
| API endpoints | 4 (health · api/modules · invoices/api/generate · invoices/api/preview) + 2 redirects توافقية | server.js · modules/invoices/module.js |
| Invoice generation time (local) | ≈1.1 s للفاتورة (PDF، صفحة أو صفحتان، بما فيه إقلاع Chromium) | قياس `date` حول `node cli.js invoice` 2026-09-23، هذا الجهاز |
| PDF page size | A4 (594.96 × 841.92 pt) | `pdfinfo` على مخرج demo-14 |
| Embedded fonts | 5/5 (Noto Naskh Arabic Regular/Bold · Liberation Sans Regular/Bold · Noto Nastaliq Urdu) | `pdffonts` |
| PDF size | ≈860 KB/فاتورة | `du -sh` على demo-a.pdf |
| Pagination test | 14 بنداً ⇒ 2 صفحات، «يتبع» + «صفحة ١ من ٢» | `renderInvoice(demo-14)` → pages=2 · DOCS/06 §3 |
| Vertical table rules vs original | ≤ 1 px | DOCS/06 + README §Accuracy (قياس المطوّر، غير معاد هنا) |
| Print-safe margin | 5.0 mm | DOCS/06 §4 (قياس المطوّر) |
| Version | 1.0.0 | package.json |

## التشغيل المحلي (2026-09-23)
`npm install` → 88 حزمة. يحتاج Chromium عبر `CHROME_PATH` (الافتراضي `/usr/bin/google-chrome` غير موجود هنا؛ ثُبّت chrome@154 بـ `@puppeteer/browsers` + مكتبات النظام libatk/libnss/libgbm). بعدها `node cli.js modules` و`node cli.js invoice` و`node server.js` (منفذ 3210) تعمل كاملة: /health · /api/modules · واجهة الفواتير · المعاينة · التوليد.

## اللقطات (screenshots/ — 2x، حقيقية من التشغيل المحلي)
desktop-01..05 (1440×900): الواجهة الرئيسية · نموذج الفاتورة · البنود · الإجمالي والأزرار · معاينة HTML. mobile-01..05 (390×844) نفس المسار. render-01 (A4 فاتورة تجريبية) · render-02-1/2 (14 بنداً على صفحتين) · render-03 (وضع الطباعة الآمن + أرقام لاتينية).
**تطميس مُعلَن:** اللقطات من نسخة عمل مُعدَّلة — السجل التجاري وIBAN والهاتف في القالب والواجهة استُبدلت بقيم وهمية (4030000000 · SA00… · +966 5X XXX XXXX)، رقم السجل داخل صورة الختم مُطمَّس، وبيانات الفواتير التجريبية (عميل/عناية/توقيع) وهمية بالكامل. لا شيء من live360.json أو janson.json أو signed.json (أسماء عملاء/أشخاص حقيقية محتملة) على أي لقطة.

## ملاحظات التنظيف / Cleanup notes
- README يعرض بيانات المؤسسة الحقيقية (CR · ZATCA · IBAN · هاتف) في مستودع عام — يُنصح بنقلها إلى ملف خاص أو حذفها.
- modules/invoices/data/live360.json وjanson.json وsigned.json تحوي أسماء عملاء وأشخاص حقيقية محتملة — تُستبدل ببيانات وهمية.
- DOCS/00 يشير إلى `moain2026/keif-aldiafa-system (خاص)` بينما المستودع العام هو `moain2028/...` — توحيد.
- الرابط الحي في README ميت — يُحدَّث أو يُزال.
- خطأ إملائي «نطام» في DOCS/00 وmodules/invoices/public/index.html (المقصود «نظام»).
- template.js يحمل بيانات المؤسسة ثابتة في الكود (ORG) — تُنقل إلى إعدادات عند بناء وحدة العملاء.
- .gitignore يتجاهل `*.png` ثم يستثني `public/assets/*.png` — يعمل، لكن مخرجات PNG لا تُحفظ؛ مقصود.
