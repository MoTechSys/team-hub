mansur-ai | مهندس | 2026-09-23 | project-pack v2 (A–G + البند 0)

# مصادر كل نص ورقم ولقطة (قاعدة الحقيقة — المعيار v2 §G)

المصدر الوحيد: المستودع github.com/moain2028/mansur-ai (استنساخ 2026-09-23، commit الأخير 2026-06-24) + ملفات البند 0 في `docs/` داخل هذه الحزمة (brief.ar/en · tech.md · links.md) المكتوبة من الكود والقياس الفعلي. الهوية: portfolio-hub/02-brand/README.md.

## البند 0 — الأرقام المقيسة (لا رقم من README دون قياس)
| الرقم | القيمة | الأمر / الملف | ملاحظة |
|---|---|---|---|
| الاختبارات | 110 passed | `python -m pytest -q` (Python 3.12.3، venv نظيف) | README يقول 82 وPROJECT_STATUS 50 — قديمان، لم يُستخدما |
| الأدوات | 45 | `python -c "from core.tools.registry import tool_names; print(len(tool_names()))"` | README 38 / STATUS 29 — قديمان |
| أدوات AST | 27 | عدّ يدوي في `core/tools/registry.py` من code_outline إلى security_scan | — |
| الوكلاء المتخصّصون | 13 | `core/agents/specialized/roster.py` (13 SpecAgent) | يطابق README |
| الوكلاء الأساسيون | 4 | `core/agents/{planner,executor,verifier,learner}.py` · `graph.py:91-94` | — |
| طبقات الذاكرة | 4 | `core/memory/store.py` CREATE TABLE working/episodic/skills/semantic | — |
| commits | 54 | `git log --oneline \| wc -l` | يطابق README |
| قرارات معمارية | 11 | `grep -c "^## " docs/DECISIONS.md` | — |
| المهارات العربية | 3 | `ls skills/` | — |
| ما لم يُعرض | «~6300 سطر»، «8 طبقات»، «24/7 على Azure»، «Opus 4.8 افتراضياً» | PROJECT_STATUS/README | غير قابلة للقياس أو تخصّ نماذج/بنية مدفوعة — استُبعدت |

## A) التصاميم الـ24 — كل عنصر ومصدره
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| السطر التمهيدي | منصور AI | Mansur AI | brief H1 |
| العنوان | وكيل عربي هجين يخطّط وينفّذ ويتحقّق ويتعلّم | An Arabic-first agent that plans, executes, verifies and learns | brief H1 |
| اسم المستودع | mansur-ai | نفسه | links.md |
| الوصف | موجّه عقول يختار النموذج… ببثّ مباشر. | A brain router picks the model… live streaming. | brief — الحل / Solution |
| رقم 1 | 45 أداة — منها 27 لذكاء الكود عبر AST | 45 tools — 27 of them AST code-intelligence | tech.md (tool_names) |
| رقم 2 | 13 وكيلاً متخصّصاً | 13 specialized agents | tech.md (roster.py) |
| رقم 3 | 110 اختباراً أخضر — pytest 2026-09-23 | 110 green tests — pytest 2026-09-23 | tech.md (pytest) |
| التاجات | Python · FastAPI · LangGraph · WebSocket · SQLite · AST · RTL | نفسها | tech.md — stack |
| الجمهور | للفرق التقنية والشركات… ويراجع كودها | For technical teams… audits their code | brief — لمن يفيد |
| CTA | نحدّد معاً نطاق الوكيل الذي يخدم فريقك | Let's scope your team's agent | brief — للتواصل |
| الشارة | شركات | Companies | التكليف · tech.md؛ لونها #3B82F6 من 02-brand |
| التذييل | github.com/moain2028/mansur-ai | نفسه | التكليف؛ HTTP 200 بتاريخ 2026-09-23 |
| شريط المتصفح | mansur-ai / واجهة المحادثة — تشغيل محلي | mansur-ai / Chat UI — local run | لا رابط حي (000) — يُعرض slug المشروع |
| الشعار النصي (logo فقط) | معين العباسي | Moain Al-Abbasi | المعيار §A |

## B) تصاميم النشر (14 PNG)
| الملف | النص | المصدر |
|---|---|---|
| carousel-1of5 | المشكلة: وكلاء إنجليزية أولاً… | brief — المشكلة · لقطة desktop-01 |
| carousel-2of5 | الحل: خطّط → نفّذ → تحقّق → تعلّم | `core/orchestrator/graph.py:91-99` (add_node/add_edge/add_conditional_edges) · لقطتا desktop-04 (skills) + mobile-01 |
| carousel-3of5 | كيف يعمل: موجّه عقول + 45 أداة + ذاكرة 4 طبقات | router.py · registry.py · store.py · لقطتا mobile-04 (skills) + mobile-05 (plugins) |
| carousel-4of5 | بالأرقام: 45 · 13 · 110 | tech.md · لقطة desktop-11 (الطرفية، داخل منطقة الجهاز أسفل الشريحة لا كبطل — شرط مدير المنتج msg 4614915) |
| carousel-5of5 | الدعوة | brief — لمن يفيد · للتواصل · لقطتا mobile-01 + desktop-05 (plugins) |
| number-card | «27 أداة تدقيق كود عبر AST — بلا تشغيل للكود» | registry.py (عدّ) · وصف الأدوات «عبر AST بلا تشغيل كود» في registry.py |
| blog-banner | عنوان المقال + «110 اختبارات خضراء» | brief H1 · tech.md |

## C) الريلان (video/)
- mansur-ai-reel-ar.mp4 · mansur-ai-reel-en.mp4 — 1080×1920، 30fps، h264+aac، 21.6 ث، 7 مشاهد، بلا شعار (مساحة الأمان أعلى-يسار فارغة)، لا مشهد خطأ/404.
- اللقطات: desktop-01 (واجهة المحادثة)، desktop-04 (skills)، desktop-11 (طرفية التحقّق)، mobile-01، mobile-04 (skills)، mobile-05 (plugins)، mobile-09 (keys بلا قيم) — كلها حقيقية من التشغيل المحلي؛ لا لقطة لوحة فارغة (sessions/config/logs) في التصاميم أو الريل (شرط مدير المنتج).
- الموسيقى: 02-brand/scripts/reels/bgm-tech-minimal.mp3 (أصل الفريق). لا تعليق صوتي (نص مقترح في copy §4).
- المولّد: tools/reel/reel_nologo.py + mansur-ar.json / mansur-en.json.

## D) الشرح — 376 / 453 كلمة + خلاصة 5 نقاط؛ المصادر في تذييل كل ملف.
## E) البحث — 3 بدائل بروابط مؤرَّخة 2026-09-23 (Manus · OpenHands · Hermes Agent) + GitHub API للترخيص والنجوم؛ أسعار Manus الرقمية مُعلَّمة «غير رسمية»؛ حجم الفئة «يُستكمل».
## F) النصوص — LinkedIn 107/118 كلمة · X 212/245 حرفاً · IG 111/138 كلمة · نص الريل + VO اختياري. draft للمحرر.

## screenshots/ (18 لقطة 2x + shoot.py) — مع طمس موثّق
- 16 لقطة واجهة من `uvicorn ui.web.server:app` محلياً بلا مفتاح API: desktop 1440×900 @2x (2880×1800) + mobile 390×844 @2x (780×1688) للصفحات: `/` chat-home · `/app/chat` · `/app/sessions` · `/app/skills` · `/app/plugins` · `/app/config` · `/app/logs` · `/app/keys`. المستخدم في التصاميم/الريل منها: chat-home · skills · plugins · keys فقط؛ sessions/config/logs مرفقة للأرشيف (portfolio-hub) لا للتصاميم.
- 2 لقطتا طرفية (desktop-11 / mobile-11): مُولَّدتان من المخرجات **الحرفية** لأوامر pytest / tool_names / roster / git log كما طُبعت في 2026-09-23 (النص منسوخ كما هو، لم يُعدَّل).
- لم تُصوَّر: `/app/analytics` · `/app/models` · `/app/cron` · `/app/profiles` (شاشة فارغة: خطأ JS بعد 404 من API بلا مفتاح) · `/diag` («no diag») · `/app/env` و`/app/docs` (تعرضان محتوى Hermes/Nous Research الخارجي).
- طمس قبل الالتقاط (shoot.py → MASK_JS، بطلب مدير المنتج msg 4614915): عنصر اسم النموذج في شريط واجهة المحادثة (`.model-pill`) وعناصر هوية الطرف الثالث في اللوحة («Hermes Teal» / «Update Hermes» / «Nous Research») أُخفيت بـ visibility:hidden — لا إضافة ولا تعديل لأي محتوى آخر. لقطات ما قبل الطمس محفوظة عندي (shots_v1) للمراجعة وليست في الحزمة. لم يُذكر أي مزوّد نماذج بالاسم في النصوص.
- صفحة keys: 0 مزوّد مهيّأ و0 OAuth — لا قيمة مفتاح ظاهرة (التشغيل كله بلا مفتاح).

## ما لم يُستخدم عمداً
- الرابط الحي erdxalgy.gensparkclaw.com — لا يستجيب (000) — غير موجود على أي تصميم.
- docs/ARCHITECTURE.html — مذكور في README وغير موجود في المستودع — لا لقطة ولا ادّعاء «8 طبقات».
- أسماء النماذج (Claude/GPT-5/DeepSeek/Opus…) في README — لا تُعرض كإنجاز (تعليمة التكليف).
- مفتاح API في `config/.env.bak` — لم يُستخدم؛ التشغيل كله بلا مفتاح؛ مُبلَّغ كملاحظة أمنية في tech.md والبحث فقط (لا في أي نص نشر).
- ARCHITECTURE.html لا يُذكر في الشرح (شرط مدير المنتج)؛ يبقى في tech.md/research كفجوة.
- أرقام README/STATUS القديمة (38 · 82 · 29 · 50 · 32 · ~6300).

## الهوية المطبّقة
- Navy #0E2A47 · Ink #08172B · Amber #F4A62A · Sand #F7F5F0 · Mist #DCE3EA · نص خافت #A3B1C0 (معتمد) · شريحة شركات #3B82F6.
- IBM Plex Sans Arabic (AR) · Inter (EN) · JetBrains Mono. مساحة أمان الشعار 12% فارغة في nologo.
- فحص آلي: 38 PNG بالمقاسات الدقيقة (Pillow) + فحص DOM لكل قطعة (لا قطع/تداخل/خروج عن اللوحة).
