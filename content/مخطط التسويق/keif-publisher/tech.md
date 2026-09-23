keif-publisher | مخطط التسويق | 2026-09-23 | final

# keif-publisher — محرّك نشر تلقائي ببوابة موافقة بشرية — Technical Sheet

- **Repo:** moain2028/keif-publisher (public) · 4 commits (كلها 2026-08-11) · 53 ملفاً متعقَّباً · آخر commit 2026-08-11 · لا LICENSE
- **Primary language / stack:** Python 3.12 · FastAPI + Jinja2 (لوحة مرندرة، لا React ولا CDN) · SQLite (WAL) · APScheduler (مجدول خلفي) · httpx · ffmpeg (تحويل 9:16) · Pillow · cryptography (Fernet للتوكنات) · pytest
- **Problem:** نشر محتوى علامة ضيافة على 8 منصات اجتماعية يدوياً من أرشيف ميديا كبير — بلا اتساق في لغة العلامة (رفع بالواو، أسعار، بلا مدينة/جوال)، وبلا رقابة على ما يُنشر آلياً؛ والأتمتة الكاملة خطرة (نشر خاطئ على حساب حقيقي)
- **Solution / core features:** خط أنابيب: فهرسة الأرشيف (assets) → توليد كابشن (LLM أو وضع offline حتمي) → فحص ضد 14 نمطاً ممنوعاً في قواعد العلامة → يُكتب `pending_review` فقط → لوحة موافقة بشرية (طابور/تفاصيل/تعديل/اعتماد/رفض/جدولة) → مجدول ينشر المعتمد في وقته مع backoff و3 محاولات → سجل نشر كامل. **بوابة موافقة 3 طبقات**: المولّد لا يكتب `approved`؛ اللوحة ترفض اعتماد ما فيه أخطاء علامة؛ `publish --live` يرفض إن kill switch مفعّل أو الحالة غير معتمدة. **Kill switch** افتراضي `KEIFPUB_PUBLISHING_ENABLED=0`: كل نشر حقيقي يرمي `KillSwitchEngaged`. 8 ناشرين بقدرات معلنة: LIVE (facebook، youtube، threads)، NEEDS_REVIEW (instagram، gbp)، DRAFT_ONLY (tiktok)، NEEDS_PAID (x)، MANUAL (snapchat — تصدير حزمة يدوية)
- **Architecture notes:** `keifpub/` حزمة واحدة: `db.py` (5 جداول، 7 حالات) · `brand.py` (القواعد) · `generator/` (llm/prompts/generate) · `media/` (probe/vertical/concat/index_archive) · `publishers/` (base + meta_base + 8 منصات) · `registry.py` · `scheduler.py` · `web/app.py` (11 مساراً + 5 قوالب) · `cli.py` (7 أوامر). الأسرار من البيئة فقط (`secret_ref` اسم متغيّر لا قيمة)؛ حمولات Meta تُطمس قبل التسجيل (`redact`). محاكي API محلي للاختبار بلا حساب (`KEIFPUB_API_BASE`)
- **Status:** مكتمل كنظام؛ **لم يُربط بأي حساب حقيقي** (README: كل المنصات «بانتظار مفاتيح»؛ 02-TECH-FACTS يوثّق حالة كل API). 210 اختباراً تمرّ
- **Last commit:** 2026-08-11
- **Live URL:** none (أداة داخلية تعمل محلياً/على VM)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| الناشرون (المنصات) | 8 | `ls keifpub/publishers` (8 ملفات منصة) · `db.PLATFORMS` (8) — **تكليف مدير المنتج قال 10: الفعلي 8** (base.py وmeta_base.py قواعد لا منصات) |
| الاختبارات | 210 تمرّ (183 دالة `def test_` + parametrize) | `pytest -p no:cacheprovider -rN` 2026-09-23: «210 passed in 25.19s» · `grep -c "def test_" tests/*.py` = 183 |
| حالات المنشور | 7 (draft → pending_review → approved → scheduled → published / rejected / failed) | `db.STATUSES` · README «دورة الحالة» |
| طبقات بوابة الموافقة | 3 | README «بوابة الموافقة — 3 طبقات لا تُتجاوز» + الكود (generate.py، web/app.py approve، cli publish) |
| أنماط العلامة الممنوعة | 14 | `brand.py BANNED_PATTERNS` (14 صفاً) |
| جداول SQLite | 5 (assets، accounts، posts، publish_log، settings) | `db.py` `CREATE TABLE` ×5 |
| مسارات اللوحة | 11 | `grep -c "@app\." web/app.py` |
| قوالب اللوحة | 5 | `ls web/templates` |
| أوامر CLI | 7 (status، verify، queue، publish، log، killswitch، brandcheck) | `cli.py add_parser` ×7 |
| محاولات النشر القصوى | 3 ثم `failed` | `base.py max_attempts` · README |
| قدرات النشر | 5 أنواع (live / draft_only / needs_review / needs_paid_plan / manual) | `base.py class Capability` |
| نسبة الفيديو المستهدفة | 9:16 | `base.py MediaSpec.aspect` · README |
| حجم الكود | 9,271 سطر Python (6,124 حزمة + 3,147 اختبارات) | `git ls-files '*.py' \| xargs wc -l` |
| عدد الملفات | 53 | `git ls-files` |
| الوثائق | README + 00-INDEX + 01-TIMELINE + 02-TECH-FACTS + 03-NEXT-TASK + docs/CONTRACT.md = 6 | `ls` |
| تجاوز أفقي (ديسكتوب) | 0 على 11 لقطة | Playwright `_meta.json` |
| تجاوز أفقي (جوال 390px) | 65–366px على صفحات اللوحة الست | Playwright — اللوحة **غير متجاوبة** (جداول عريضة)؛ موثَّق كفجوة |
| Users / clients | علامة ضيافة واحدة (كيف الضيافة — جهة معروفة على المنصة) | README |

## التشغيل والتصوير (2026-09-23 — مخطط التسويق)
- `python3 -m venv .venv` + الحزم من 02-TECH-FACTS (fastapi، uvicorn، jinja2، httpx، cryptography، apscheduler، pytest، python-dotenv، pillow، python-multipart) — لا requirements.txt في المستودع (فجوة). `cp .env.example .env` مع `KEIFPUB_LLM=offline` ومسارات محلية؛ **`KEIFPUB_PUBLISHING_ENABLED=0` (kill switch مفعّل) طوال العمل — لا مفتاح API واحد أُدخل، لا حساب حقيقي، لا نشر.**
- `pytest` → 210 passed (25 ث). اللوحة: `uvicorn keifpub.web.app:app --port 8770` → `/healthz` `{"ok":true,"kill_switch":true}`.
- **بيانات العرض:** قاعدة البيانات تبدأ فارغة، فحُمِّلت `make/seed_demo.py`: 2 أصل وهمي (ملف فيديو أزرق 3 ث + صورة زرقاء مولَّدة بـ ffmpeg/Pillow — ليست من أرشيف العميل)، 8 حسابات sandbox بأسماء `demo.*`، 7 منشورات تغطي الحالات السبع بكابشنات عامة وجوال `05XXXXXXXX` (placeholder README نفسه)، 3 صفوف سجل. **لا رقم من هذه البيانات يُقتبس على أي تصميم.**
- **اللقطات (17):** ديسكتوب 1440×900 × 11 (الطابور، الطابور مُصفّى، تفاصيل منشور مرفوض بأخطاء العلامة، تفاصيل منشور معتمد، الحسابات، السجل + 5 بطاقات طرفية لأوامر CLI الحقيقية: status، brandcheck، queue، publish --post 3 dry-run، pytest) + جوال 390×844 × 6 (صفحات اللوحة؛ الشريط الجانبي/الجداول تتجاوز — مصوَّرة كما هي لتوثيق الفجوة، ولا تُستخدم كبطل تصميم إلا الطابور المضغوط).
- بطاقات الطرفية: مخرجات الأوامر بايت-ببايت (`_cli_outputs.json` في make/) داخل قالب HTML داكن؛ لا نص مُختلق. أمر `publish --post 3` بلا `--live` = dry-run يعرض الحمولة التي كانت ستُرسل إلى YouTube (resumable upload) — لم يُرسل شيء.

## ملاحظات التنظيف / Cleanup notes
- الناشرون 8 لا 10 (التكليف)؛ «183 اختباراً» = دوال، والمُنفَّذ 210.
- لا `requirements.txt`/`pyproject.toml` — التبعيات في 02-TECH-FACTS نصاً فقط.
- مسارات مطلقة لـ VM المطوّر في `.env.example` وREADME (`/home/work/...`) وأرقام جوال تجريبية في `generate.py DEFAULT_PHONE` و`llm.py` (`0555123456`/`0555000000`) — placeholders لكن تبدو حقيقية؛ يُفضَّل `05XXXXXXXX`.
- اللوحة غير متجاوبة للجوال (جداول عريضة)؛ لا CI؛ لا LICENSE؛ 4 commits في يوم واحد.
- README يحمل اسم العلامة في عنوان اللوحة («كيف الضيافة · لوحة النشر») — جهة، مسموح؛ لا أسماء أشخاص.
