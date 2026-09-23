mansur-ai | مهندس | 2026-09-23 | research v2 — بحث ويب مؤرَّخ (تاريخ الوصول لكل رابط: 2026-09-23)

# منصور AI — بحث وتحليل السوق (E)

**Executive summary (EN):** Mansur AI is a self-hosted, Arabic-first, multi-agent automation agent. The three alternatives a technical team would realistically compare it with are Manus (hosted general agent, credit-based pricing), OpenHands (MIT, self-hosted coding-agent platform with Docker sandbox), and Hermes Agent by Nous Research (MIT, self-improving agent with skills/memory and a messaging gateway — and the codebase Mansur's dashboard is adapted from). All three are larger and better funded; Mansur's defensible angle, from tech.md only, is Arabic-native UX + a verify-and-learn LangGraph loop + 27 execution-free AST code-audit tools on the owner's own server. Gaps are stated plainly below, including a leaked API-key backup file in the public repo.

## 1) من يشتري هذا؟ (السوق)
- المشتري: الفرق التقنية والشركات التي تريد وكيل أتمتة عربياً على بنيتها يراجع كودها (brief — لمن يفيد؛ الشريحة: شركات).
- حالة الاستخدام: مهام ملفات/ويب/بيانات بالعربية، وتدقيق كود Python بلا تنفيذ، وذاكرة تتعلّم من المهام (tech.md — الحل).
- حجم الفئة: **يُستكمل** — لا رقم سوقي موثّق في مصادر المشروع، ولم أضع تقديراً.

## 2) ثلاث بدائل فعلية (روابط حقيقية، وصول 2026-09-23)

### أ) Manus (وكيل عام مستضاف)
- الرابط: https://manus.im/pricing · https://manus.im/docs/introduction/plans
- ماذا يقول: صفحة الخطط الرسمية تصف Free («Limited monthly credits») وPro («Generous monthly credit allocation») وTeam («Shared team credit pool») بنموذج اعتمادات (credits) دون أرقام على الصفحة نفسها. مصادر ثانوية مؤرَّخة تذكر أن الخطط المنشورة في 2026 تبدأ من $20/شهر لـ 4,000 اعتماد، $40 لـ 8,000، $200 لـ 40,000 (nocode.mba 2026-06-26؛ moclaw.ai بتاريخ خطط 2026-08-11) — **أرقام غير رسمية**، تُذكر كسياق فقط.
- أين يتفوّق منصور (من tech.md فقط): يعمل على سيرفر المالك ببيانات محلية (SQLite + sandbox) بلا اعتمادات شهرية؛ عربي أصيل RTL؛ 27 أداة تدقيق كود عبر AST. Manus أشمل وأنضج بكثير (متصفح كامل، وسائط، تشغيل سحابي) وله فريق ومنتج تجاري.

### ب) OpenHands (منصة وكلاء برمجة مفتوحة المصدر)
- الرابط: https://github.com/OpenHands/OpenHands (يُعاد التوجيه من All-Hands-AI/OpenHands)
- ماذا يقول: «self-hosted, always-on engineering team»؛ «runs locally on your machine by default, but can connect to multiple agent backends, e.g. running agents in Docker containers, on VMs, or within your company infrastructure»؛ خيار «With a Docker Sandbox»؛ يمكنه استخدام وكلاء طرف ثالث «like Claude Code and Codex». الترخيص MIT، ~88.9k نجمة (GitHub API، 2026-09-23).
- أين يتفوّق منصور (من tech.md فقط): واجهة ومهارات عربية؛ حلقة تحقّق/تعلّم صريحة تحفظ المهارات؛ سلسلة تدقيق AST بلا تنفيذ. OpenHands يتفوّق في العزل (Docker sandbox فعلي مقابل subprocess في منصور)، وفي المجتمع والتوثيق والاختبارات.

### ج) Hermes Agent — Nous Research (وكيل ذاتي التحسين مفتوح المصدر)
- الرابط: https://github.com/NousResearch/hermes-agent
- ماذا يقول: «The self-improving AI agent … the only agent with a built-in learning loop—it creates skills from experience, improves them during use»؛ «Lives where you do: Telegram, Discord, Slack, WhatsApp, Signal, and CLI all from a single gateway process»؛ «Use any model you want—Nous Portal, OpenRouter, OpenAI, your own endpoint». الترخيص MIT، ~248k نجمة (GitHub API، 2026-09-23).
- علاقة مباشرة: لوحة منصور على `/app` مكيّفة من لوحة Hermes (PROJECT_STATUS: «لوحة كاملة (React/Vite، مكيّفة من Hermes)»؛ اللقطات تعرض عنوان «Hermes Agent - Dashboard» و«Nous Research»). هذا يجعل Hermes المرجع الأقرب — ويجب إبراز ما يضيفه منصور فوقه لا ما يشاركه معه.
- أين يتفوّق منصور (من tech.md فقط): العربية الأصيلة في الواجهة والتوجيه والمهارات؛ 27 أداة تدقيق كود AST مصمّمة داخلياً؛ موجّه عقول بتتبّع تكلفة. Hermes يتفوّق في قنوات المراسلة (جسر Telegram في منصور «جاهز يحتاج توكن» فقط)، ومرونة المزوّدين، والنضج.

## 3) التموضع
- جملة التموضع (من brief): «وكيل عربي هجين يخطّط وينفّذ ويتحقّق ويتعلّم» — على بنيتك، بأدواتك، ويراجع كودك.
- المنافس يقول «وكيل عام في السحابة» (Manus) أو «فريق هندسة ذاتي الاستضافة» (OpenHands) أو «وكيل يتعلّم ويعيش في مراسلاتك» (Hermes). منصور يقول: «الوكيل العربي الذي يعمل عندك ويدقّق كودك دون أن ينفّذه».
- لا مقارنة بالأرقام التشغيلية أو عدد المستخدمين (غير موثّق).

## 4) الكلمات المفتاحية
AR (10): وكيل ذكاء اصطناعي عربي · وكيل ذكي متعدد الوكلاء · أتمتة المهام بالذكاء الاصطناعي · تدقيق كود بايثون آلي · وكيل يعمل على سيرفرك · LangGraph بالعربية · واجهة محادثة عربية RTL · ذاكرة هرمية للوكلاء · فحص أمني للكود بلا تنفيذ · بديل عربي لوكلاء الذكاء الاصطناعي
EN (10): Arabic AI agent · self-hosted AI agent · multi-agent LangGraph · ReAct executor · AST code audit tools · agent with hierarchical memory · plan-execute-verify-learn loop · Arabic RTL chat UI · Python FastAPI agent · self-improving agent skills

## 5) ثلاث زوايا محتوى
1. **«27 فحصاً للكود دون تشغيله»** — سلسلة AST من security_scan إلى regex_audit: ما تكشفه ولماذا تكفي شجرة الكود (مقال تقني + كاروسيل).
2. **«خطّط → نفّذ → تحقّق → تعلّم: كيف تُبنى حلقة وكيل في LangGraph»** — مخطّط الحالة من `graph.py` بلغة بسيطة (فيديو/بانر).
3. **«لماذا وكيل عربي أصيل لا مترجَم؟»** — RTL، مهارات عربية، توجيه بالنيّة العربية؛ مقارنة مع الواجهات الإنجليزية أولاً (منشور LinkedIn).

## 6) الفجوات (صريحة)
- 🔴 أمن: `config/.env.bak.20260618_083825` مرفوع في المستودع العام ويحوي مفتاح `GENSPARK_API_KEY` — يجب حذفه من التاريخ وتدوير المفتاح قبل أي نشر تسويقي.
- تقنياً: لا رابط حي (erdxalgy.gensparkclaw.com لا يستجيب)؛ لوحة `/app` بهوية Hermes وأربع صفحات فارغة بلا مفتاح؛ MCP هيكل؛ العزل subprocess لا Docker؛ المتجهات بالتجزئة لا embeddings؛ `docs/ARCHITECTURE.html` غير موجود؛ الاختبارات في ملف واحد (2,338 سطراً)؛ لا نشاط منذ 2026-06-24؛ ترخيص «خاص بـ Moain».
- تسويقياً: README بأرقام قديمة (38/82 مقابل 45/110 فعلياً) يُضعف الثقة؛ لا فيديو تعريفي ولا دراسة حالة ولا مستخدم موثّق؛ الاعتماد على بروكسي نماذج واحد (Genspark) دون توثيق البدائل؛ الكانوني غير محسوم (moain2026 ↔ moain2028).

## 7) المصادر
- work/mansur-pack/docs: brief.ar.md · brief.en.md · tech.md · links.md (2026-09-23)
- github.com/moain2028/mansur-ai: README.md · docs/PROJECT_STATUS.md · core/** (الاستنساخ 2026-09-23)
- https://manus.im/pricing · https://manus.im/docs/introduction/plans (2026-09-23) · https://www.nocode.mba/articles/manus-ai-pricing (2026-06-26، غير رسمي) · https://moclaw.ai/blog/manus-ai-pricing (2026-09، غير رسمي)
- https://github.com/OpenHands/OpenHands + GitHub API (MIT، 88,907 نجمة، 2026-09-23)
- https://github.com/NousResearch/hermes-agent + GitHub API (MIT، 248,153 نجمة، 2026-09-23)
