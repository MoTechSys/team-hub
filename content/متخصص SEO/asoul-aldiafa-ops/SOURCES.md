asoul-aldiafa-ops | متخصص SEO | 2026-09-23 | ready

# SOURCES — مصدر كل نص ورقم وصورة في الحزمة

## قواعد الحزمة (من التكليف msg 4616920 وقرارات msg 4617959)
- يُقدَّم كمنهجية عامة «تدقيق SEO يُصحّح استنتاجاته بالقياس»؛ لا اسم عميل/نشاط/ملف تجاري؛ الجهة تُذكر «مشروع ضيافة / موقع خدمات محلية».
- لا رقم زيارات أو ترتيب أو GBP على أي مادة؛ أرقام Search Console في `deliverables/title-meta-optimization.md` مستبعدة كلياً.
- الهاتفان والبريد والدومين وحسابات التواصل مطموسة في كل لقطة (`shoot.py` تعبير `RX`)؛ لا يظهر أي منها في نص.
- التذييل github.com/moain2028/asoul-aldiafa-ops؛ الأساس بلا شعار؛ الدعوة «راسلني / DM me»؛ الخافت #A3B1C0؛ شريحة شركات #3B82F6.

## الأرقام (كلها في `project/tech.md` بأمر لكل رقم؛ أُعيد قياسها بـ `verify.py` → `measure.json`)
| الرقم على المواد | القيمة | المصدر |
|---|---|---|
| 1176 زوجاً · 0 فوق 40% · 28.3% · 8.9% · 24 (20–28%) · 804 (<10%) | research/similarity-matrix.csv (49×49، المثلث العلوي) | verify.py |
| 49/49 (200، h1، canonical، description، lang، robots) · 0 عنوان >60 · 911 كلمة | research/crawl-report.csv (49 صفاً × 26 عموداً) | verify.py |
| 298 KB · 10 ملفات · 68% | research/mobile-audit.md §3 (جدول الخطوط، مجموع الصفوف أُعيد جمعه) | verify.py |
| 67 رابطاً رسمياً · 18 معرّف answer/ | grep على research/*.md deliverables/*.md README | verify.py |
| 4 تصحيحات · 8 بنود «لم نتحقق منها» · 11 خطوة | README (`### ❌/🔴 خطأ`، جدول «سادساً»، جدول «رابعاً») | verify.py |
| 43 مساراً → 41×404 | research/probe-results.tsv | verify.py |
| 52 صورة WebP · 89.5 KB أكبرها · 0 فوق 200 KB | research/imgsizes.tsv | verify.py |
| 26 عموداً · 4 سكربتات · 396 سطراً · 43 ملف بحث · 5 مخرجات · 53 ملفاً · 4 commits | المستودع (ls/wc/git) | verify.py |
| 241 تعليق `<!--/$-->` · 0 href يحوي & أو $ · 1.2 MB JS | research/404-source-investigation.md (تقرير؛ البيانات الخام غير مرفوعة) | tech.md «تقرير» |
| ضابطا المنهجية 100%/100% | research/similarity-analysis.md جدول Sanity Controls (تقرير) | tech.md «تقرير» |
| المدن المحيَّدة (جدة، ينبع، مكة، المدينة، بدر) | research/similarity.py قائمة CITY | الكود |
| £199/سنة · $42/شهر · $10–90/شهر | صفحات أسعار Screaming Frog / Sitebulb / Semrush بتاريخ 2026-09-23 (pack/E/research.md) | web_search + crawler |
| 85% عتبة Semrush · minhash Screaming Frog · «Check Similar Content» Sitebulb | وثائق كل أداة (روابط في research.md) | gsk summarize 2026-09-23 |

## النصوص
- A (24 تصميماً): العناوين/الوصف/الأرقام/الدعوة من `make_pack_ops.py` قاموس `T` ← brief.ar/en.md + tech.md.
- B (كاروسيل 5+5، بطاقة الرقم الواحد، بانر المقال): `make_extras_ops.py` قواميس `CAR`/`ONE` ← brief + tech + research.md. بطاقة الرقم الواحد «0 من 1176 يتجاوز 40%» (قرار مدير المنتج). «4 تصحيحات» عنوان شريحة 2/5.
- C (ريلان AR/EN 19.8 ث، بلا شعار، بلا إطار هاتف): `make_reel_ops.py` قاموس `SC`؛ 6 مشاهد؛ لقطات حقيقية من project/screenshots فقط؛ الموسيقى `02-brand/scripts/reels/bgm-tech-minimal.mp3` (داخلية).
- D (explainer.ar/en ≤500 كلمة + 5 نقاط): من tech.md وresearch.md؛ الفجوة «السكربتات لا تُعاد تشغيلها» مذكورة صريحة.
- E (research.md): 3 بدائل حقيقية بروابط وأسعار مؤرَّخة 2026-09-23، تموضع، 10+10 كلمات، 3 زوايا، فجوات.
- F (copy.ar/en): LinkedIn ≤120 كلمة · X ≤280 حرفاً · IG ≤150 كلمة · نص الريل بتوقيتات — **draft للمحرر**.

## الصور
- 25 لقطة حقيقية 2x (`project/screenshots/`، الأداة `shoot.py`): عروض Markdown مُصيَّرة لملفات المستودع، `crawl-report.csv` كجدول، الخريطة الحرارية مرسومة خلية بخلية من `similarity-matrix.csv`، طرفية حقيقية (`verify.py`, `git log`, `ls`, `sed` على `similarity.py`).
- **لا لقطة مولّدة** ولا صورة/أيقونة مولّدة بالذكاء الاصطناعي في أي مادة؛ الخطوط IBM Plex Sans Arabic / Inter / JetBrains Mono (OFL، 02-brand/fonts).
- إطارات المتصفح والجوال من `02-brand/scripts/brand.py`.
- ملفات المستودع غير المصوَّرة عمداً: `research/POLICY-FINDINGS.md` (حالة تعليق الملف التجاري)، `deliverables/title-meta-optimization.md` (أرقام حساب حقيقي).

## ما لا يُدَّعى
- أن الموقع «تعافى» أو تغيّر ترتيبه (التنفيذ خارج المستودع).
- أن الحزمة منتج/أداة؛ هي منهجية لمشروع واحد بسكربتات لا تُعاد تشغيلها من المستودع (parsed.json/pages/ غير مرفوعة).
- أي رقم أداء كتجربة مستخدم (301 ms من مركز بيانات).
