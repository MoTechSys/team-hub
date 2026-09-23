moain-promoter-ai | كاتب المحتوى | 2026-09-23 | ready

# moain-promoter-ai — Technical Sheet (Moain Promoter AI)

- **Repo:** moain2028/moain-promoter-ai (public، MIT، أُنشئ على هذا الحساب 2026-09-23) — README يوجّه إلى moain2026/moain-promoter-ai (404 وقت الفحص). `src/__init__.py` `__version__ = "1.0.0"`، وسام README 1.1.0، رسائل commits تصل إلى «v3.3».
- **Primary language / stack:** Python 3.10+ (Pydantic v2 · Typer · FastAPI · SQLAlchemy async + aiosqlite · Playwright · PyGithub · httpx · openai/anthropic/google-generativeai SDKs · tenacity · PyYAML) + لوحة TypeScript/Next.js 14.2 · React 18 · Tailwind 3 · shadcn/Radix · zustand · react-markdown — المصدر: requirements.txt، dashboard/package.json.
- **Problem:** محفظة GitHub كبيرة لمطوّر واحد تحتاج تسويقاً مستمراً بلغتين على عدة منصات؛ كتابة المنشورات والتقاط اللقطات والجدولة يدوياً لا تستمر (README «عربي»).
- **Solution / core features:** نظام متعدد الوكلاء تحت Orchestrator: RepoAnalyzer (يقرأ README والكود) → Capture (يستنسخ ويشغّل ويلتقط عبر Playwright بـ 11 viewport معرّفة) → Mockup (بديل توليدي عند فشل الالتقاط) → ContentWriter (منشورات ثنائية اللغة لـ 6 منصات، persona يمنية v3، 27 قالباً) → Scheduler (حملات 30/60/90 يوماً) → Publisher (6 ناشرين: LinkedIn, X, Facebook, Instagram, Dev.to, Medium) + Ideation وImageGenerator. طبقة نماذج قابلة للتبديل بسجلّ 27 مزوّداً مع اكتشاف نوع المفتاح تلقائياً (fingerprint) وفحصه (probe). لوحة بأسلوب محادثة بخمس لوحات (Chat · Repositories · Screenshots · Schedule · Settings) تُدير المفاتيح من الواجهة. CLI بسبعة أوامر. `default_dry_run: true` في configs — لا نشر حيّ إلا بتعطيله صريحاً.
- **Architecture notes:** `src/agents` (9 وكلاء + base) · `src/models` (registry 27 مزوّداً، factory، resolver، detection/fingerprint، validators/probe) · `src/publishers` (6) · `src/capture` (browser_pool، viewports) · `src/core` (api 10 مسارات، config، database 4 جداول: Repository · Screenshot · Post · Campaign) · `src/tools` (github_live، templates_loader) · `src/utils` · `src/workflows` · `dashboard/` (Next.js، rewrite `/api/backend/*` → FastAPI) · `configs/` (agent_defaults، rate_limits) · `prompts/` (personas/yemeni.yaml، templates/library.yaml) · `docs/` 9 ملفات + `repos_data.json` (173 مستودعاً مجمّعة، 93 خاصة) · CI: `.github/workflows/ci.yml` (pytest). Celery/Redis وLangChain/LangGraph مذكورة في requirements وREADME لكن **لا استيراد لها في src/** — الذكر الوحيد تعليق في `src/workflows/scheduled.py` وعلم `use_celery: bool = False` في config.
- **Status:** prototype/alpha — الوحدات موجودة والاختبارات تمرّ (82) لكن التشغيل الفعلي يحتاج مفاتيح (نموذج + GitHub + ناشرين)؛ `/schedule/list` يعيد قائمة فارغة ثابتة («In production, query the Post table»)؛ `/agent/chat` «simplified router» بالكلمات المفتاحية؛ قائمة المستودعات بلا توكن تسقط إلى 10 بطاقات demo في الواجهة. لا رابط حيّ.
- **Last commit:** 2026-09-11 — 6 commits كلها في يوم واحد.
- **Live URL:** none.

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| Agents (classes) | 9 (README يقول 7) | `grep -n "^class .*Agent" src/agents/*.py` — Capture, ContentWriter, Ideation, ImageGenerator, Mockup, Orchestrator, Publisher, RepoAnalyzer, Scheduler |
| Publishers | 6 | `ls src/publishers` (devto, facebook, instagram, linkedin, medium, twitter) |
| LLM providers in registry | 27 | `grep -c "display_name=" src/models/registry.py`؛ docs/PROVIDERS.md «27 LLM Providers» |
| ProviderType enum values | 29 | `src/models/detection/fingerprint.py` (27 + custom/unknown) |
| Dashboard panels | 5 | `dashboard/components/agent/Sidebar.tsx` NAV_ITEMS |
| FastAPI routes | 10 | `grep -c "@app\.\(get\|post\)" src/core/api.py` |
| CLI commands | 7 | `grep -c "@app.command" src/main.py` (init, list-providers, test-model, analyze, promote, campaign, bio) |
| DB tables | 4 | `src/core/database.py` (Repository, Screenshot, Post, Campaign) |
| Capture viewports | 11 | `grep -c 'name="' src/capture/viewports.py` |
| Prompt templates | 27 | `prompts/templates/library.yaml` (عدّ `- name:`) |
| Tests | 82 passed (5 ملفات) | `pytest tests/ -q` محلياً 2026-09-23، Python 3.12 |
| CI | GitHub Actions (pytest + ruff غير مانع) | `.github/workflows/ci.yml` |
| Python files / LOC (src/) | 51 / 5,907 | `find src -name '*.py' \| xargs cat \| wc -l` |
| Dashboard TS/TSX files / LOC | 18 / 1,495 | `find dashboard -name '*.ts*'` خارج node_modules/.next |
| Tracked files | 108 | `git ls-files \| wc -l` |
| Commits | 6 (2026-09-11) | `git log --oneline \| wc -l` |
| Docs | 9 md + repos_data.json (173 مستودعاً) | `ls docs` |
| Dashboard build | ✓ 2 routes static | `npm run build` 2026-09-23 |
| GitHub stars | 0 | api.github.com 2026-09-23 |
| «171+ مستودعاً» | رقم عن حساب المالك لا عن المشروع — **لا يُعرض كإنجاز** | README، Sidebar.tsx؛ قرار مدير المنتج 2026-09-23 |
| Posts published / campaigns | غير موثَّق — لا يُعرض | `/schedule/list` يعيد `[]` ثابتاً |

## ملاحظات التنظيف / Cleanup notes
- README يوجّه clone إلى moain2026/moain-promoter-ai (404) — يُصحَّح إلى moain2028.
- README «7 وكلاء» بينما الكود 9 — يُحدَّث؛ الإصدار مبعثر (1.0.0 / 1.1.0 / v3.3).
- Celery + Redis + LangChain/LangGraph في requirements وREADME بلا استخدام في الكود — تُحذف أو تُنفَّذ.
- `/schedule/list` و`/agent/chat` مبسّطان صريحاً في التعليقات — لا يُدّعى «جدولة تعمل».
- Sidebar يعرض «171 repos» ثابتاً؛ ReposPanel يحمل بيانات demo بأسماء مستودعات خاصة للمالك — تُستبدل بقراءة من `docs/repos_data.json` أو تُفرَّغ.
- `google.generativeai` مهجور (FutureWarning) — الانتقال إلى `google.genai`.
- لا لقطات ولا نتائج نشر حقيقية في المستودع — الحزمة تصف القدرات كـ«مصمَّم لـ» لا «نشر».
