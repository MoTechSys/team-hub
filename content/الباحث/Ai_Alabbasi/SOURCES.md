Ai_Alabbasi | الباحث | 2026-09-23 | v2 — G (مصادر كل نص ورقم وصورة)

# SOURCES — Ai_Alabbasi project pack v2

المستودع: https://github.com/moain2028/Ai_Alabbasi (فُحص 2026-09-23، HTTP 200، MIT) · آخر commit 2026-06-03 · مستنسخ محليًا 2026-09-23.
ملفات المرجع: `project/{tech.md, brief.ar.md, brief.en.md, links.md, RUN-NOTES.md}`.

## 1) الأرقام
| الرقم | المصدر | طريقة التحقق |
|---|---|---|
| 74 اختبارًا ناجحًا · 2.18 ث | `python3 -m pytest -q` محليًا 2026-09-23 → «74 passed in 2.18s»؛ `--co` → 74؛ `grep -rn "def test_" tests` → 74 | أمر |
| 12 ملف اختبار | `ls tests/test_*.py` | أمر |
| 8 عقول | `brain/brain_config.yaml` → `len(brains)` بـ yaml.safe_load | أمر |
| 9 أدوات | `tools/tools.py` قاموس `TOOLS` (9 مفاتيح) | أمر |
| 87 مقطع معرفة · 3 تقنيات | `python3 knowledge/ingest.py` محليًا → «87 مقطع مفهرس» (react-native/nextjs/angular) | أمر |
| 12 مسار API | `grep -c "@app\.\(get\|post\)" web/server.py` | أمر |
| 6 أوامر CLI | `run.py` سطر 5–12 (/brain /topic /kb /skills /help /exit) | قراءة |
| 6 أنواع أحداث · 6 حالات | `agent/event_stream.py` 28–33 · `agent/state_machine.py` 23–28 | قراءة |
| 25 خطوة حدًّا | `agent/agent.py` سطر 90؛ يظهر «الخطوة 1/25» في التشغيل | أمر/قراءة |
| 5 مهارات بذرية | `ls knowledge/skills_seed/` | أمر |
| RRF k=60 | `knowledge/hybrid_search.py` | قراءة |
| 31 ملف Python · 3,318 سطر | `find -name "*.py"` · `wc -l` | أمر |
| 17 commit · 77 ملفًا · 1.4 MB · ★ 0 | `git log` · `find` · `du` · GitHub API 2026-09-23 | أمر |
| تبعية إلزامية واحدة (PyYAML) | `requirements.txt` | قراءة |
| لا مفتاح مرفوع | `grep -rn -E "(sk-|AKIA|ghp_|xox|AIza|hf_|PRIVATE KEY)"` على الشجرة + `git log --all -p` → 0 | أمر |
| منصور: 54 commit · 235 ملفًا · 13,908 سطر · 117 دالة اختبار · 41 ملف أدوات · 7 وكلاء | `~/repos/mansur-ai`: git log · find · wc · grep "def test_" · ls core/tools core/agents | أمر |
| قرار البناء من الصفر | `mansur-ai/docs/DECISIONS.md` سطر 51 | قراءة |
| OpenHands ★ 88,916 · AutoGPT ★ 187,502 · CrewAI ★ 58,927 · AutoGen ★ 61,118 | GitHub API 2026-09-23 | أمر |

**مستبعَد عمدًا:** «أذكى من Manus AI»، «300+ نموذج»، «~5 دقائق»، سرد «الاختبار الكبير» و«2583 حرف معرفة» في docs/02_STATUS، أسماء المزوّدين/النماذج، اسم الشخص.

## 2) النصوص
- العناوين والتاغلاين (A/B/C): brief.ar/en.md + tech.md.
- كاروسيل: 1/5 brief §المشكلة · 2/5 README §الهدف + CHANGELOG المرحلة 1 · 3/5 CHANGELOG المرحلة 2–3 + تشغيل ingest · 4/5 tech.md + RUN-NOTES · 5/5 brief §لمن + mansur-ai/docs/DECISIONS.md.
- Explainer (D): README، CHANGELOG 2.0.0، docs/01_HOW_IT_WORKS.md، الكود المذكور في الجدول، التشغيل المحلي.
- Research (E): روابط فُحصت 2026-09-23؛ الاقتباسات من وصف كل مستودع على GitHub؛ ترخيص AutoGPT من ملف LICENSE في المستودع (Polyform Shield داخل autogpt_platform + MIT خارجها).
- Copy (F): كل رقم من الجدول أعلاه؛ X ≤ 280 (226 AR / 227 EN).

## 3) الصور
| الاستخدام | الأصل | المعالجة |
|---|---|---|
| البطل (LinkedIn/X/IG/Story/Hero) | واجهة الويب `web/index.html` على :8000، Playwright 1440×900 @2x، بلا مفتاح | JS blur: اسم الشخص، شارة العقل وقائمة الاختيار (أسماء النماذج)، اسم المزوّد في بطاقة الخطأ |
| ثانوية | طرفية حقيقية: `python3 run.py` مهمة بلا مفتاح → خطأ صريح | نص المخرجات الفعلي رُندر إلى PNG؛ استبدال اسم الشخص بـ ▒▒▒▒ وطمس أسماء النماذج/المزوّدين بالـregex |
| ثالثة | لوحة المهارات في الواجهة | كما البطل |
| كاروسيل 2/5 + ريل 2 | اختيار العقل في الواجهة | كما البطل |
| كاروسيل 3/5 + ريل 3 + Story | طرفية `knowledge/ingest.py` (87 مقطعًا) | كما الثانوية |
| كاروسيل 4/5 + ريل 5 + بانر | طرفية `pytest -q` (74 passed) | كما الثانوية |
| كاروسيل 5/5 + ريل 4 | واجهة الويب: بطاقة الخطأ «لا يوجد مفتاح API» | كما البطل |
| number-card | لا صورة | — |
| screenshots/ (23) | 9 ديسكتوب + 8 جوال + 4 طرفية + GitHub | RUN-NOTES §الطمس |

**لا صور ولا أيقونات مولّدة بالذكاء الاصطناعي** في الحزمة. شعار الدرع في لقطات الواجهة هو أصل من المستودع نفسه (`web/assets/logo.png`) ولم نُنشئه.

## 4) الهوية والمعيار
- `02-brand/scripts/brand.py`؛ النص الخافت #A3B1C0؛ شريحة «شركات» أزرق؛ الأساس بلا شعار؛ الاسم النصّي في نسخ logo فقط؛ الدعوة «راسلني/DM me» في تذييل نسخ nologo والكاروسيل والريل (معيار 4ب).
- معيار الحزمة: `project-pack-standard-v2.md` (مرفق مهمة #47).
- أدوات الإنتاج: `tools/` (make_pack.py، make_carousel.py، make_reel.py، shots_web.py، term_shots.py، spec.json).

## 5) الريل
- 6 مشاهد (4/5/5/5/5/4 ث) − 5 × 0.5 ث تداخل = 25.5 ث؛ 1080×1920؛ 30fps؛ H.264؛ بلا موسيقى؛ بلا إطار هاتف (واجهة الجوال بها خلل موثّق، فاعتمدنا بطاقات المتصفح/الطرفية)؛ لا مشاهد خطأ تشغيلي — مشهد «خطأ صريح» مقصود ويعرض سلوك المشروع الصحيح عند غياب المفتاح.
