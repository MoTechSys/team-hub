asoul-aldiafa-ops | متخصص SEO | 2026-09-23 | ready

# asoul-aldiafa-ops — Technical Sheet (حزمة تشخيص SEO/GBP قائمة على الدليل لمشروع ضيافة)

- **Repo:** moain2028/asoul-aldiafa-ops (public) — 4 commits كلها بتاريخ 2026-09-18 (`git log`)
- **Primary language / stack:** Markdown (33 ملفاً، ~70,000 كلمة) + Python 3 (4 سكربتات، 396 سطراً: `parse.py` BeautifulSoup لاستخراج الوسوم والنص المرئي، `similarity.py` Jaccard على 6-grams، `dupmeta.py` تكرار الوسوم، `mkreports.py` توليد التقارير) + بيانات CSV/TSV/XML/JSON خام. الزحف بـ `curl` بوكيل جوال — بلا متصفح (TECHNICAL-SUMMARY.md سطر 4)
- **Problem:** موقع خدمات ضيافة محلية (49 صفحة «خدمة × مدينة») عُلِّق ملفه التجاري على Google، وتحليل أولي اتّهم الموقع بـ«20 صفحة محتوى مكرر» و«روابط 404 برمجية» واقترح تحويلات 301 ودمج 49 صفحة إلى 20. كان يلزم فصل ما يثبت بالقياس عمّا هو ظنّ قبل أي تغيير على موقع حي
- **Solution / core features:** (1) زحف كامل لكل روابط sitemap (49/49) واستخراج 26 عموداً لكل صفحة؛ (2) مصفوفة تشابه 49×49 = 1176 زوجاً بعد تحييد أسماء المدن مع ضابطَي منهجية (صفحة مع نفسها = 100%، صفحة مع نسخة بدّلت مدينتها = 100%)؛ (3) تحقيق في مصدر `/&` و`/$` بالمقطع الحرفي من كود React 19 Streaming SSR؛ (4) تدقيق جوال (صور، `srcSet`، lazy، خطوط preload، منطقة الخادم)؛ (5) بحث سياسات Google الرسمية بنصوصها الحرفية (67 رابطاً فريداً على support/developers.google.com، 18 معرّف مقال GBP)؛ (6) 5 مخرجات جاهزة (FAQ، وصف الملف، توحيد الاسم، عناوين/أوصاف، سكربت فيديو التحقق)؛ (7) مجلد `مرفوض/` يحفظ التوصية الملغاة (redirects) مع سبب رفضها؛ (8) README يبدأ بـ4 تصحيحات لاستنتاجات التحليل السابق وينتهي بـ8 بنود «لم نستطع التحقق منها»
- **Architecture notes:** مستودع وثائق ودليل لا واجهة له: `README` (الخلاصة والخطة) → `research/` (43 ملفاً: 26 md + 2 csv + 4 py + 11 بيانات) → `deliverables/` (5) → `مرفوض/` (2). السكربتات تعتمد ملفات وسيطة (`parsed.json`, `pairs.json`, `pages/`) غير مرفوعة → لا تُعاد التشغيل من المستودع وحده، لكن مخرجاتها (CSV/TSV) مرفوعة وأعدتُ حساب كل رقم منها (`verify.py`)
- **Status:** حزمة تشخيص مكتملة، مسلَّمة 2026-09-18؛ التنفيذ على الموقع/الملف التجاري خارج نطاق المستودع
- **Last commit:** 2026-09-18
- **Live URL:** none — أداة تحليل/وثائق (links.md)

## الأرقام ومصادرها / Numbers & sources
كل صف أدناه أُعيد قياسه بـ `work/asoul-aldiafa-ops/verify.py` (المخرجات في `measure.json`) من ملفات المستودع نفسها؛ الأرقام التي مصدرها نص تقرير فقط مُعلَّمة «تقرير».

| Metric | Value | Source (file/line or command) |
|---|---|---|
| Pages crawled | 49 / 49 من sitemap | `grep -c '<loc>' research/sitemap.xml` · `wc -l research/urls.txt` · صفوف `crawl-report.csv` |
| Columns per page | 26 | `csv.DictReader` على `crawl-report.csv` |
| HTTP 200 · exactly one h1 · canonical==url · meta description · lang=ar · robots index,follow | 49/49 لكلٍّ | `verify.py` على أعمدة `status`,`h1_count`,`canonical`,`meta_description`,`lang`,`robots` |
| Titles > 60 chars · descriptions outside 70–160 | 0 · 0 (أطوال العناوين 36–60) | أعمدة `title_len`,`desc_len` |
| Words per page | avg 911 · min 76 (`/links`) · max 1434 | عمود `word_count` |
| Response time (datacenter, cached) | avg 301 ms (37–535) | عمود `time_total_ms` — **أرقام شبكة لا تجربة مستخدم؛ لا تُعرض على التصاميم** |
| HTML size | avg 140.1 KB · max 226.1 KB (`/`) | عمود `size_bytes` |
| Similarity matrix | 49×49 → 1176 pairs = C(49,2) | `research/similarity-matrix.csv` (المثلث العلوي) |
| Pairs > 40% | 0 | نفس الملف |
| Max similarity · median | 28.3% · 8.9% (README: 28.29 / 8.93) | نفس الملف؛ CSV مقرَّب لمنزلة واحدة |
| Pairs 20–28% · pairs < 10% | 24 · 804 | نفس الملف |
| Methodology controls | 100.0% · 100.0% | تقرير: `research/similarity-analysis.md` جدول Sanity Controls |
| Probed candidate paths | 43 → 41×404 · 1×200 (`/index`) · 1×308 | `research/probe-results.tsv` |
| Image sitemap URLs | 49 | `grep -c '<loc>' research/sitemap-images.xml` |
| Images measured | 52، كلها WebP، أكبرها 89.5 KB، 0 فوق 200 KB | `research/imgsizes.tsv` |
| Blocking preload fonts | 10 ملفات = 298.1 KB (ملفان = 203.6 KB = 68%) | جدول `research/mobile-audit.md` §3 — مجموع الصفوف أُعيد جمعه |
| `srcSet` tags · lazy images | 481 · 386 | تقرير: `mobile-audit.md` §2 (البيانات الخام `pages/` غير مرفوعة) |
| React comment markers | `<!--/$-->` 241 · `<!--$-->` 99 · `href:"&"` 0 | تقرير: `research/404-source-investigation.md` |
| Official Google URLs cited (unique) | 67 (منها 18 معرّف `answer/` لـ GBP) | `grep -ohE '(support\|developers)\.google\.com/…' research/*.md deliverables/*.md README*.md \| sort -u \| wc -l` |
| README corrections of the prior analysis | 4 | `grep -cE '^### (❌\|🔴) خطأ' README` |
| Execution plan steps | 11 (0–10) | جدول «رابعاً» في README |
| "Could not verify" items | 8 | جدول «سادساً» في README |
| research/ files | 43 = 26 md + 2 csv + 4 py + 11 data | `ls research \| wc -l` |
| deliverables/ · مرفوض/ | 5 · 2 | `ls` |
| Python lines | 396 | `cat research/*.py \| wc -l` |
| Markdown files · words | 33 · ~70,000 | `git ls-files '*.md'` + `len(text.split())` |
| Tracked files · repo size | 53 · 868 KB | `git ls-files \| wc -l` · `du -sk --exclude=.git` |
| Commits · authors · dates | 4 · 1 · 2026-09-18 (03:17→03:39 EDT) | `git log` |
| Tests | **0** آلية (الضوابط المنهجية داخل التقارير فقط) | لا ملف اختبار |
| Search-Console figures in deliverables (4,440 impressions · 130 clicks · 2.9% CTR · 86% mobile) | **بيانات حساب حقيقي — لا تُعرض** | `deliverables/title-meta-optimization.md` سطر 2؛ قاعدة التكليف (4) |
| Users / clients | مشروع لعميل واحد (مشروع ضيافة #2 على المنصة) — لا يُسمّى | قاعدة التكليف (2) |

## ملاحظات التنظيف / Cleanup notes
- أرقام هاتف (17 وروداً لرقمَين) وبريد (9) ودومين العميل (647) واسم النشاط في كل الملفات → مطموسة في كل لقطة عبر `shoot.py` (تعبير `RX`) ولا تظهر في أي نص من الحزمة. لا اسم شخص في المستودع (0).
- `deliverables/title-meta-optimization.md` يحوي أرقام Search Console للحساب الحقيقي؛ `POLICY-FINDINGS.md` يذكر حالة التعليق ورمز التوجيه → لم تُصوَّر هذه الملفات (صُوِّر `SEO-FINDINGS.md` و`policy-service-area.md` بدلاً منهما).
- README يكتب 28.29% و8.93% بينما `similarity-matrix.csv` مقرَّب لمنزلة واحدة (28.3 / 8.9) — نفس القيم، يُفضَّل ذكر التقريب في README.
- الملفات الوسيطة (`parsed.json`, `pairs.json`, `pages/`, `js/`) المذكورة في TECHNICAL-SUMMARY.md غير مرفوعة → السكربتات لا تُعاد التشغيل من المستودع؛ يُقترح رفعها أو ذكر ذلك.
- `wc -w` بإعدادات لغة C يعطي 901 كلمة للـ README مقابل 1686 بـ UTF-8 — رقم الكلمات هنا بـ UTF-8.
- لا LICENSE ولا requirements.txt (bs4 مطلوب لـ parse.py).
