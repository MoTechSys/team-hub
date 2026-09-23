keif-aldiafa-system | المحرر | 2026-09-23 | final

# SOURCES — keif-aldiafa-system project pack v2

## النصوص
| النص | المصدر |
|---|---|
| «فاتورة مطابقة للأصل في ثانية» / "A pixel-matched invoice in about a second" | brief.ar/en.md (المحرر 2026-09-23) ← README §Module 1 «visually identical» + قياس ≈1.1 ث محلياً (tech.md) |
| المشكلة: Word، أخطاء حسابية، 3 صيغ للإجمالي | DOCS/00-نظرة-عامة.md §المشكلة |
| الأصول مستخرجة من PDF أصلي بـ pdfimages | DOCS/00 §الفكرة المفتاحية · README §Module 1 |
| واجهة عربية / CLI / API؛ PDF · PNG · معاينة | README §CLI, §API · modules/invoices/module.js · cli.js |
| توقيع إلكتروني · ترقيم صفحات مقيس · وضع طباعة آمن · أرقام هندية/لاتينية | README §Features · modules/invoices/src/render.js (planPages) · template.js (body.safe) |
| المعمارية المعيارية (اكتشاف تلقائي للوحدات) | README §Architecture · core/registry.js |
| الهوامش بالمليمتر (6.6 / 7.8 / 88.8 مم) | modules/invoices/src/template.js تعليقات CSS |
| «14 بنداً كانت تضيع منها ثلاثة» | DOCS/06 §2 F1 و§3 |
| A4 بفارق 0.111 مم · بلا خط بديل · نص عربي حقيقي | DOCS/06 §2 |
| خارطة الطريق (عملاء، عروض أسعار، مدفوعات، فعاليات، تقارير) | README §Modules · core/registry.js PLANNED · DOCS/07 |
| لا رابط حي | curl على tiyquqno.gensparkclaw.com/keif/ 2026-09-23 → لا اتصال |
| الدعوة «عندك مستند تُصدره يدوياً كل أسبوع؟ راسلني» | brief.ar/en.md §للتواصل (المحرر) — شريحة مشاريع صغيرة حسب editorial-style-guide §2 |
| الشرح D | كل فقرة من README/DOCS أعلاه + tech.md؛ لا معلومة خارجها |
| البحث E — اقتباسات المنافسين | عناوين/أوصاف صفحات zoho.com/sa/invoice · daftra.com · invoiceninja.com · github.com/puppeteer/puppeteer، وُصلت 2026-09-23 بـ curl؛ نجوم invoiceninja من api.github.com |

## الأرقام
| الرقم | القيمة على التصاميم | المصدر وشروط القياس |
|---|---|---|
| زمن التوليد | «~1 ث محلياً» (~1s) | `node cli.js invoice demo-a.json out.pdf` قياس `date` قبل/بعد = 1.08 ث و1.09 ث (14 بنداً)، يشمل إقلاع Chromium؛ صندوق Linux واحد، Node 22، chrome 154، 2026-09-23. **ليس معياراً عاماً** — جهاز واحد، قياسان. |
| الخطوط المضمّنة | 5 | `pdffonts demo-a.pdf` → NotoNaskhArabic Regular/Bold · LiberationSans Regular/Bold · NotoNastaliqUrdu-Bold، كلها emb=yes |
| الترقيم | 14 بنداً → صفحتان | `renderInvoice(demo-14.json)` → pages=2 · `pdfinfo` Pages: 2 · يطابق DOCS/06 §3 |
| فارق خطوط الجدول | ≤1 بكسل (≤1px) | DOCS/06 + README §Accuracy — **تدقيق المطوّر**، غير معاد قياسه هنا (الأصل غير متاح لنا)؛ موسوم كذلك على البطاقة والشرح |
| الوحدات | 1 من 6 | `node cli.js modules` (✅1 · 🔜5) · registry PLANNED (5) · README §Modules |
| commits / آخر إيداع | 4 · 2026-07-31 | `git log --oneline` · `git log -1 --date=short` |
| الأسطر | 1,145 (JS 727) | `wc -l` على ملفات JS/HTML خارج node_modules |
| التوثيق | 8 ملفات DOCS · 1,041 سطراً · ≈5,500 كلمة | `wc -l DOCS/*.md` · `wc -w DOCS/*.md _audit/*.md README.md` (5,546) |
| A4 | 594.96 × 841.92 pt | `pdfinfo demo-14.pdf` |
| حجم PDF | ≈860 KB | `du -sh demo-a.pdf` |
| الأصول البصرية | 15 ملفاً | `ls modules/invoices/public/assets \| wc -l` |

## الصور واللقطات
| الملف | المصدر |
|---|---|
| render-01-invoice-a4.png (البطل «ورقة A4») | `renderInvoice(demo-a.json, png)` من وحدة الفواتير نفسها — نسخة عمل مطمّسة (RUN-NOTES.md) |
| render-02-invoice-14items-1/2.png | PDF من الوحدة (demo-14) → pdftoppm 150dpi |
| render-03-invoice-printsafe-latin.png | `renderInvoice(printSafe:true, arabicDigits:false)` |
| desktop-01..05 · mobile-01..05 | puppeteer-core على السيرفر المحلي 127.0.0.1:3210، 1440×900 و390×844 @2x، 2026-09-23 (work/keif/shoot.js) |
| شعار المؤسسة (الشخصية المرسومة) داخل اللقطات | جزء من القالب الحقيقي (modules/invoices/public/assets/logo.png) — يبقى بقرار مدير المنتج msg 4615394 |
| **التطميس** | CR → 4030000000 · IBAN → SA00… · هاتف → +966 5X XXX XXXX / 05XXXXXXXX · رقم السجل داخل stamp.png مُطمَّس · عميل «شركة النموذج للتجارة»/«مؤسسة المثال للمناسبات» · عناية «مدير المشتريات» · توقيع «المدير التنفيذي». لم يُستخدم live360/janson/signed. (work/keif/prep.sh) |
| بيانات البنود في الفواتير المصوَّرة | القوالب السريعة في modules/invoices/public/index.html (PRESETS) — نصوص خدمة، بلا أسماء |
| الهوية (Navy/Ink/Amber/Sand/Mist · لون الشريحة #F4A62A · الخافت #A3B1C0 · Plex Arabic/Inter/JetBrains Mono) | 02-brand/README.md + scripts/brand.py · تحديث 2026-09-23 |
| إطارات الورقة/المتصفح/الهاتف | 02-brand/scripts/brand.py (paper_frame · browser_frame · phone_frame) |
| الريلان (21 ث، بلا موسيقى) | إطارات مولَّدة بـ keif.py من اللقطات أعلاه، دُمجت بـ ffmpeg (work/keif/reel.sh)؛ موسيقى بلا حقوق تُضاف عند النشر (لا مقطوعة مرخَّصة في متناولي) |

## القواعد المطبَّقة
لا شعار معين على الأساس (nologo)؛ نسخة logo = اسم نصّي فقط. التذييل github.com/moain2028/keif-aldiafa-system. لا اسم شخص ولا رقم حقيقي على أي تصميم. خارطة الطريق على شريحة كاروسيل واحدة فقط (4/5) بعنوان «1 من 6 — والبقية مخطَّطة». ملاحظة بيانات المؤسسة في المستودع العام مرفوعة لمدير المنتج، لا تظهر في النصوص.
