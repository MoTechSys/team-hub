mansur-ai | مهندس | 2026-09-23 | complete

# mansur-ai — Technical Sheet

- **Repo:** moain2028/mansur-ai (public) · الأصل README/PROJECT_STATUS يشيران إلى moain2026/mansur-ai
- **Primary language / stack:** Python 3.12 · FastAPI 0.136 + uvicorn · LangGraph 1.2 + langchain-core · openai SDK (عبر بروكسي Genspark LLM) · SQLite (sqlite-utils) · httpx · pytest · لوحة React 19 + Vite + Tailwind v4 (مكيّفة من Hermes Agent، مبنية مسبقاً في webapp/dist)
- **Problem:** الوكلاء الذكية العامة إنجليزية أولاً ولا تُدار من سيرفر المالك؛ المطلوب وكيل عربي أصيل يخطّط وينفّذ ويتحقّق ويتعلّم بأدواته الخاصة (README «الميزات»).
- **Solution / core features:** موجّه عقول يختار النموذج حسب نوع المهمة مع fallback وتتبّع تكلفة (`core/brain/router.py`) · 4 وكلاء أساسيين planner/executor(ReAct)/verifier/learner منسّقين بـ LangGraph StateGraph بحلقة plan→execute→verify→(execute|learn)→END (`core/orchestrator/graph.py:91-99`) · 13 وكيلاً متخصّصاً بتوجيه حسب نيّة المهمة (`core/agents/specialized/roster.py`) · 45 أداة مسجّلة في سجل موحّد منها 27 أداة ذكاء/تدقيق كود عبر AST (`core/tools/registry.py`) · ذاكرة هرمية SQLite بأربعة جداول working/episodic/skills/semantic (`core/memory/store.py`) · shell معزول داخل `data/sandbox` بحد زمني (`core/tools/shell.py`) · http_request بحماية SSRF تمنع المضيفات الخاصة (`core/tools/http_tool.py:20-39`) · واجهة محادثة عربية RTL على `/` عبر WebSocket `/ws` مع زر إيقاف (`ui/web/server.py:93-102`) · لوحة إدارة على `/app` بـ ~31 endpoint (`ui/web/dashboard_api.py`) · 3 مهارات عربية في `skills/` · CLI `run.py`.
- **Architecture notes:** README يذكر «معمارية 8 طبقات (docs/ARCHITECTURE.html)» — الملف **غير موجود في المستودع** (git ls-files). 11 قراراً معمارياً موثّقاً في docs/DECISIONS.md. مقارنة ميزات مع Manus في docs/MANUS_PARITY.md. MCP هيكل فقط (`core/mcp/`). لوحة `/app` هي Hermes Agent dashboard مكيّفة: العنوان ما زال «Hermes Agent - Dashboard» (PROJECT_STATUS «متبقٍّ»).
- **Status:** prototype/beta — نواة عاملة ومختبَرة محلياً؛ النشر الحي المذكور لا يستجيب (انظر التحقّق).
- **Last commit:** 2026-06-24 (الأول 2026-06-13 — 12 يوماً)
- **Live URL:** none — erdxalgy.gensparkclaw.com لا يستجيب (تحقّق مدير المنتج 2026-09-23 وتحقّقي)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source (file/line or command) |
|---|---|---|
| Tests | **110 passed** | `python -m pytest -q` على الاستنساخ 2026-09-23 (README يقول 82، PROJECT_STATUS يقول 50 — قديمان) |
| Tools | **45** | `python -c "from core.tools.registry import tool_names; print(len(tool_names()))"` (README يقول 38، PROJECT_STATUS 29 — قديمان) |
| AST code-intelligence tools | 27 | عدّ يدوي في `core/tools/registry.py` من code_outline إلى security_scan |
| Specialized agents | **13** | `core/agents/specialized/roster.py` — 13 SpecAgent (يطابق README) |
| Core agents | 4 | `core/agents/{planner,executor,verifier,learner}.py` |
| Memory tiers | 4 tables | `core/memory/store.py` CREATE TABLE working/episodic/skills/semantic |
| Commits | **54** | `git log --oneline \| wc -l` (يطابق README) |
| Python lines (excl. tests) | 11,570 | `git ls-files '*.py' \| grep -v tests \| xargs cat \| wc -l` |
| Test file lines | 2,338 (ملف واحد tests/test_core.py) | `wc -l` |
| Tracked files | 235 | `git ls-files \| wc -l` |
| Arabic skills | 3 | `ls skills/` (arabic-content-writer · invoice-analyzer · rtl-web-design) |
| Architecture decisions | 11 | `grep -c "^## " docs/DECISIONS.md` |
| Dashboard endpoints | ~31 | `grep -c "router\.(get\|post\|put\|delete)" ui/web/dashboard_api.py` (PROJECT_STATUS «~30») |
| Dashboard pages (routes) | 12 | `webapp/src/App.tsx` paths |
| Runtime deps | 9 | requirements.txt |
| Repo size | 5.8 MiB pack | `git count-objects -vH` |
| Users / clients | يُستكمل | غير موثّق |

## تحقّق تشغيلي (مهندس — 2026-09-23)
- `python3 -m venv .venv && pip install -r requirements.txt` نظيف على Python 3.12.3.
- `pytest -q` → 110 passed in 0.73s (بلا مفتاح API).
- `uvicorn ui.web.server:app --port 8000` يعمل؛ `/health` → `{"status":"ok","have_key":false}`؛ `/` و`/app` → 200.
- `python run.py "مرحبا"` بلا مفتاح → «⚠️ لا يوجد مفتاح API في config/.env» (سلوك متوقّع؛ لم يُستخدم أي مفتاح).
- صفحات اللوحة العاملة بلا مفتاح: chat · sessions · skills · plugins · config · keys · logs. صفحات analytics · models · cron · profiles تعرض شاشة فارغة (JS: `Cannot read properties of undefined` بعد 404 من API) — لم تُصوَّر.
- اللقطات: 16 لقطة واجهة (8 ديسكتوب 1440×900 @2x + 8 جوال 390×844 @2x) + 2 لقطتا طرفية بمخرجات pytest/tool_names/roster الحرفية.

## ملاحظات التنظيف / Cleanup notes
- ⚠️ `config/.env.bak.20260618_083825` مرفوع في المستودع العام ويحوي مفتاح `GENSPARK_API_KEY` ودومين — يجب حذفه من التاريخ وتدوير المفتاح فوراً.
- README يشير إلى `docs/ARCHITECTURE.html` غير موجود، وإلى رابط حي لا يستجيب، وأرقام (38/82) قديمة مقابل الكود الفعلي (45/110).
- لوحة `/app` تحمل هوية Hermes Agent (العنوان، «Nous Research»، «Update Hermes») — تحتاج إعادة تسمية وإعادة بناء (مسجّلة في PROJECT_STATUS «متبقٍّ»).
- `hermes_cli/web_dist` و`webapp/dist` نسختان مبنيّتان مرفوعتان (70 ملف مصدر في webapp/src) — تضخّم.
- `docs/manus_reference/` صور مرجعية من منتج ثالث — تُراجَع حقوقها قبل أي نشر.
- المستودع الكانوني: README يقول moain2026/mansur-ai والتكليف moain2028/mansur-ai — يُحدَّد.

## مصادر
README.md · docs/PROJECT_STATUS.md · docs/DECISIONS.md · docs/MANUS_PARITY.md · core/** · ui/web/** · webapp/src/App.tsx · git log · أوامر التحقّق أعلاه.
