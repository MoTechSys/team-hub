Ai_Alabbasi | الباحث | 2026-09-23 | ready

# Ai_Alabbasi — Technical Sheet (وكيل ذكاء اصطناعي مستقل — الجيل الأول/النواة)

- **Repo:** moain2028/Ai_Alabbasi (public, MIT) — نسخة الحساب القديم Moain2026/Ai_Alabbasi ما زالت تعمل (200)
- **Primary language / stack:** Python 3.10+ (stdlib شبه كامل: sqlite3/FTS5، urllib، subprocess) · PyYAML (التبعية الإلزامية الوحيدة) · FastAPI + uvicorn (واجهة الويب، اختياري) · sentence-transformers (اختياري، بديل hashing مضمّن) · HTML/CSS/JS واحد-ملف للواجهة (RTL)
- **Problem:** امتلاك وكيل برمجي مستقل بالكامل (لا اشتراك في منصة مغلقة): عقل قابل للتبديل من ملف واحد، يتمرّس على تقنيات محدّدة عبر معرفة متراكمة، وينفّذ كودًا ويختبره ويصلح أخطاءه.
- **Solution / core features:** (1) عقل مركزي يُبدَّل بسطر YAML بين 8 إعدادات جاهزة + أي API متوافق مع OpenAI محليًا؛ (2) حلقة ReAct بحدّ 25 خطوة مع مخطِّط (خطة مرقّمة + انعكاس) وقائمة مهام بـ«تلاوة» الهدف وآلة حالات (6 حالات) ومقاطعة آمنة؛ (3) 9 أدوات محصورة بـ `_safe_path` داخل `projects/` بما فيها CodeAct (تنفيذ Python معزول) و`file_str_replace`؛ (4) قاعدة معرفة RAG: SQLite FTS5 + متجهات دلالية مدموجة بـ RRF (k=60)، تغذية 87 مقطعًا لثلاث تقنيات، وحلقة تعلّم تحفظ المهارات الناجحة؛ (5) فهرسة مهارات تدريجية بثلاث طبقات ومطابقة عربية ضبابية + 5 مهارات بذرية؛ (6) صندوق رمل سحابي قابل للتبديل (local/Daytona/E2B) بسقوط آمن؛ (7) واجهة ويب RTL ببث حي (SSE) و12 مسار API وواجهة CLI بأوامر /brain /topic /kb /skills.
- **Architecture notes:** `brain/` (إعداد + محرّك موحّد) · `agent/` (agent.py + event_stream + planner + todo_manager + state_machine + interrupt_handler + code_act_executor) · `tools/` (tools.py + cloud_sandbox.py) · `knowledge/` (knowledge.py + ingest + embedder + hybrid_search + skill_indexer + skill_selector + skills_seed/) · `web/` (server.py + index.html) · `run.py` CLI · `docs/` 4 ملفات + `خطة العمل/` 9 ملفات تحليل. الأخطاء (مثل غياب المفتاح) تُبثّ كحدث `error` صريح في CLI والويب.
- **Status:** prototype v2.0.0 (CHANGELOG 2026-06-03) — الجيل الأول؛ mansur-ai (#31 على المنصة) هو الجيل الثاني الذي قرر فريقه البناء من الصفر «مستلهمًا أنماطه» (`mansur-ai/docs/DECISIONS.md` سطر 51).
- **Last commit:** 2026-06-03 (17 commits)
- **Live URL:** none (تشغيل محلي؛ الواجهة على :8000)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source (file/line or command) |
|---|---|---|
| الاختبارات | 74 ناجحًا (74 محصاة) | `python3 -m pytest -q` محليًا 2026-09-23 → «74 passed in 2.18s»؛ `--co` → 74؛ `grep -rn "def test_" tests` → 74؛ README يقول 74 ✓ |
| ملفات الاختبار | 12 | `ls tests/test_*.py` |
| إعدادات العقول الجاهزة | 8 | `brain/brain_config.yaml` مفتاح `brains` (yaml.safe_load) — README «8 عقول» ✓ |
| الأدوات | 9 | `tools/tools.py` قاموس `TOOLS` (run_shell, write_file, append_file, file_str_replace, read_file, list_dir, make_dir, web_search, run_python) |
| أنواع أحداث EventStream | 6 | `agent/event_stream.py` سطر 28–33 |
| حالات آلة الحالات | 6 | `agent/state_machine.py` سطر 23–28 |
| الحدّ الأقصى لخطوات الحلقة | 25 | `agent/agent.py` سطر 90 `max_steps: int = 25` (يظهر «الخطوة 1/25» في التشغيل) |
| مهارات بذرية عربية | 5 | `ls knowledge/skills_seed/` |
| مقاطع المعرفة بعد التغذية | 87 (3 تقنيات: react-native، nextjs، angular) | `python3 knowledge/ingest.py` محليًا 2026-09-23 → «87 مقطع مفهرس» |
| RRF k | 60 | `knowledge/hybrid_search.py` |
| مسارات API في الويب | 12 | `grep -c "@app\.\(get\|post\)" web/server.py` |
| أوامر CLI | 6 (/brain /topic /kb /skills /help /exit) | `run.py` سطر 5–12 |
| ملفات Python | 31 | `find -name "*.py"` |
| أسطر Python | 3,318 | `wc -l` |
| ملفات | 77 · 1.4 MB | `find -type f` · `du -sh` |
| Commits | 17 | `git log --oneline \| wc -l` |
| التبعيات الإلزامية | 1 (PyYAML) | `requirements.txt` |
| مستندات | 4 docs + CHANGELOG + 9 ملفات «خطة العمل» + بحث Manus | `find docs "خطة العمل" -name "*.md"` → 14 |
| **مقارنة الجيل الثاني (mansur-ai، مقاسة 2026-09-23)** | 54 commits · 235 ملفًا · 19 MB · 13,908 سطر Python · 73 ملف .py · 117 دالة اختبار في ملف واحد (لم تُجمَع محليًا: ImportError) · 41 ملف أدوات · 7 وكلاء · 3 مهارات | `~/repos/mansur-ai`: git log · find · wc · grep "def test_" · ls core/tools core/agents skills |

**لا يُعرض تسويقيًا:** «أذكى من Manus AI» (ادعاء غير مقاس)، «300+ نموذج» (رقم مزوّد خارجي)، أي اسم مزوّد/نموذج (تظهر في الكود كخيارات فقط)، «الاختبار الكبير» في docs/02_STATUS (سرد بلا أثر قابل للتحقق)، اسم الشخص في README/LICENSE/الواجهة.

## ملاحظات التنظيف / Cleanup notes
- **اسم شخص**: «صُنع لعبّاس العباسي» في README، وفي LICENSE (Copyright)، وفي CLI («وكيل عبّاس الذكي»، محث `👤 عبّاس>`)، وفي الواجهة (العنوان «العباسي») → طُمس في كل لقطاتنا؛ يُقرَّر إبقاؤه أم لا.
- **أسماء مزوّدي النماذج** في `brain_config.yaml`، README، الواجهة (شارة العقل) والـCLI — طُمست في اللقطات وفق التكليف.
- **مفاتيح**: لا مفتاح مرفوع — فُحصت شجرة العمل وتاريخ git كاملًا (أنماط sk-/ghp_/AIza/hf_/AKIA/PEM) → صفر نتائج؛ `.gitignore` يستثني `config/.env` و`*.env` و`*.key`؛ `config/.env.example` قالب نصي فقط. لكن `docs/02_STATUS.md` يذكر «مفتاح Genspark (308 حرف) شغّال» — معلومة وصفية لا المفتاح نفسه.
- **خلل واجهة الجوال**: عند طيّ القائمة الجانبية (☰) على ≤760px يمتد المستند إلى 670px ويُدفع المحتوى خارج الشاشة (`.sidebar.collapsed{margin-inline-end:-280px}` مع `body{display:flex}`) — موثّق بلقطة `mobile-01-home.png`.
- README «74 اختبار» ✓ و«8 عقول» ✓ — دقيق. لكنه يذكر «5 مهارات» ✓ و«PyYAML فقط» ✓ بينما الواجهة تحتاج fastapi/uvicorn/python-multipart (موثّق كاختياري ✓).
- روابط `git clone` في README تشير إلى الحساب القديم Moain2026 (تعمل).
- `docs/02_STATUS.md` بتاريخ 2026-06-01 لا يعكس v2.0.0 (2026-06-03).
- `web/conversations.db` يُنشأ عند التشغيل داخل المستودع وليس في `.gitignore` (يُستثنى `knowledge/index/*.db` فقط).
- نسب المشروع (لمن صُنع/من طوّره) — بند قرار عند محمد؛ الصياغة المعتمدة: «الجيل الأول/النواة» لمنصور.
