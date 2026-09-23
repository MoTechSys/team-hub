sayed-aldiafa | المصمم | 2026-09-23 | draft

# sayed-aldiafa — Technical Sheet

- **Repo:** moain2028/sayed-aldiafa (public — استُنسخ بلا مصادقة 2026-09-23). README يحيل على اسم أقدم `dallat-alkaif-static` في أمر الاستنساخ وعلى نسخة Next.js في `moain2026/dallat-alkaif-nextjs`.
- **Primary language / stack:** HTML5 · CSS3 · JavaScript (ES2020) — بلا إطار، بلا build، بلا `node_modules` (README «نظرة عامة»؛ الشجرة: لا package.json). خطوط Amiri للعناوين وAlmarai للمتن من Google Fonts (الاعتماد الخارجي الوحيد؛ README «نظام التصميم»).
- **Problem:** متعهّد حفلات ومناسبات (كوش، جلسات، خيام، بيوت شعر، كراسي، تكييف، صوتيات، قهوجية، تنسيق) يحتاج موقعاً عربياً يعمل على أي استضافة بلا Node، ويقود الزائر إلى واتساب لطلب عرض سعر (README «لماذا بلا إطار»؛ `index.html` سطر 971–975).
- **Solution / core features:** 15 صفحة ثابتة RTL بالكامل: رئيسية + خدمات + باقات + حجز + معرض + تغطية + 9 صفحات خدمة. نموذج حجز 8 حقول يُحوَّل إلى رسالة واتساب مُعبّأة مسبقاً (`booking.html`، `index.html#send`). JSON-LD (LocalBusiness · WebSite · OfferCatalog · 18 Service · 18 Offer · BreadcrumbList في 14 صفحة). Open Graph 7 وسوم + canonical في كل صفحة. `<picture>` WebP+JPEG (25 موضعاً)، `loading="lazy"` (51)، `prefers-reduced-motion`، `aria-live` للتحقق من النموذج، لا `maximum-scale`. تبويب سفلي ثابت وقائمة جانبية. sitemap.xml (15 URL) + robots.txt + manifest.webmanifest.
- **Architecture notes:** `index.html` تنسيقها مضمَّن في `<style>` (24.2 KB مقاسة) لإلغاء طلب حاجز؛ الصفحات الـ14 الأخرى تشترك في `sv.css` (10.1 KB). تخطيط جوال-أولاً بعرض أقصى `.app{max-width:480px}` — على الحاسوب يظهر العمود نفسه متمركزاً بظل (README «الاستجابة»: للتجاوب الكامل نسخة Next.js). الزخرفة: «قوس المحراب» ثلاثة مسارات SVG (README «نظام التصميم»).
- **Status:** prototype/pre-launch — README «ما زال مطلوباً»: صور حقيقية، أسعار، سنة التأسيس، شعارات عملاء بإذن، النطاق النهائي.
- **Last commit:** 2026-08-09 (`git log -1`) · 5 commits كلها في اليوم نفسه.
- **Live URL:** none مؤكَّد. الرابط المضمّن في canonical/OG/sitemap `suppdizl.gensparkclaw.com/sayed-static/` يعيد HTTP 000 (لا استجابة) عند الفحص 2026-09-23.

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| HTML pages | **15** | `ls *.html \| wc -l` · sitemap.xml 15 `<loc>` (README يقول ١٣ — أُضيفت av.html وclimate.html بعد كتابته؛ لا يُعرض رقم README) |
| Service pages | **9** (art, zamzam, sweets, hospitality, equipment, climate, av, coffee, events) | services.html «تسع خدمات» + الملفات (README يقول ٨ — متضارب، لا يُعرض) |
| Dependencies / build step | **0 / none** | لا package.json في الشجرة؛ README «نظرة عامة» |
| External requests | 1 origin (Google Fonts) | `grep -oh 'href="https://fonts…'` |
| Shared CSS (`sv.css`) | 10,091 B ≈ 10 KB | `wc -c sv.css` |
| Inline CSS in index.html | 24,210 B ≈ 24 KB | python: مجموع `<style>` (README يقول ~32KB — متضارب، لا يُعرض) |
| HTML+CSS total | 286,403 B ≈ 280 KB | `du`/python على *.html + sv.css |
| Assets referenced | 40 ملفاً · 2.70 MB (WebP 0.99 MB · JPEG 1.62 MB) | python: كل `assets/*` المُشار إليه في HTML/manifest |
| Assets in repo | 48 ملفاً · 4.04 MB (8 غير مُشار إليها) | `ls assets \| wc -l` · `du -sb assets` (README يقول ≈١.١ MB — متضارب، لا يُعرض) |
| `<picture>` WebP+JPEG | 25 | grep `<picture` |
| `loading="lazy"` | 51 | grep |
| `<img>` with non-empty alt | 56 / 56 | python regex |
| JSON-LD blocks | 27 across 15 pages (LocalBusiness 1 · WebSite 1 · OfferCatalog 1 · Service 18 · Offer 18 · BreadcrumbList 14) | grep `"@type"` |
| Open Graph tags per page | 7 · canonical 1 | grep `property="og:` · `rel="canonical"` |
| WhatsApp deep links | 30 | grep `wa.me/966` |
| Booking form fields | 8 (booking.html) · 7 (index.html) | grep `<input\|<select\|<textarea` |
| FAQ items | 58 across 14 pages | grep `class="q"` |
| Cities listed (coverage.html) | 13 | قسم CITIES: العليا · الملقا · حطين · الياسمين · النرجس · القيروان · الرحمانية · الدرعية · العارض · الخرج · حريملاء · المزاحمية · ثادق |
| `maximum-scale` | 0 occurrences | grep (WCAG 1.4.4 — README «الوصولية») |
| HTML LOC | 4,355 (+169 CSS) | `wc -l` |
| Commits | 5 · 2026-08-09 | `git log` |
| Repo size | 4.3 MB working tree | `du -sh --exclude=.git` |
| Tests | none | لا ملفات اختبار؛ «بوابات الجودة» في README أوامر grep يدوية |
| Users / clients / events | يُستكمل | README «قواعد المحتوى»: لا إحصائيات لأن المالك لم يوفّرها |

## ملاحظات التنظيف / Cleanup notes
- **تعارض النطاق الجغرافي:** README يقول «جنوب المملكة: عسير · جازان · نجران · الباحة · الطائف» وبوابة الجودة تمنع كلمة «الرياض»، بينما الكود كله (152 ذكراً، العناوين، JSON-LD، manifest) عن **الرياض ومحافظاتها**. الكود هو الحقيقة المنشورة؛ README قديم من مشروع سابق. في التسويق: «الرياض ومحافظاتها» أو بلا منطقة.
- README قديم في 4 أرقام (13 صفحة / 8 خدمات / ~32KB / ≈1.1MB) وأمر الاستنساخ يشير لمستودع باسم آخر — يُحدَّث.
- **كل الصور مولّدة بالذكاء الاصطناعي** بإقرار README («ما زال مطلوباً») — لا تُقدَّم كصور مناسبات حقيقية؛ يُفصَح عنها.
- شهادات العملاء (14 `<cite>` بأسماء) غير موثّقة المصدر — عوملت كمحتوى عرض؛ طُمست الأسماء في اللقطات.
- رقم الجوال +966 57… يظهر في 15 صفحة + JSON-LD — طُمس في اللقطات، ولا يظهر على أي تصميم.
- 8 ملفات في assets غير مُشار إليها (hero.jpg/webp, hero-card.webp, s1.*, logo-96/180, logo.svg) — 1.3 MB يمكن حذفها.
- لا رابط حي: canonical/OG/sitemap تشير إلى نطاق لا يستجيب — تُحدَّث عند النشر (README «ضبط روابط المشاركة»).
- الخطوط من Google Fonts (README نفسه يوصي بالاستضافة المحلية).
- لا اختبارات آلية ولا CI.
