Ai_Alabbasi | الباحث | 2026-09-23 | v2 — D (300–500-word explainer + summary)

# How Ai_Alabbasi works — an agent core you own

Off-the-shelf coding agents are rented: one model you did not pick, knowledge that stays with the vendor, code that passes through a closed platform. Ai_Alabbasi starts from the opposite question: what if the agent core were a handful of Python files you can read in one sitting, run on your own server, and re-brain at will? The repository is 31 Python files, 3,318 lines, one required dependency (PyYAML), MIT-licensed.

**The brain: one line.** `brain/brain_config.yaml` holds 8 presets and a single `active_brain` key; changing it swaps the model for the whole loop, including a local model behind any OpenAI-compatible server. Keys live in `config/.env`, outside git (the full history was scanned: no key ever committed). If the key is missing nothing crashes — an explicit `error` event is emitted in both the CLI and the web UI, exactly what we saw running without one.

**The loop: plan, act, reflect.** Before acting, the planner produces a numbered plan, and a todo manager keeps "reciting" the goal so it is not lost across steps. A six-state machine (idle → running → interrupted/resuming → done/failed) guards transitions, and a thread-safe interrupt handler can stop execution mid-flight. Each task is capped at 25 steps, and every step lands in an event stream with six unified event types rendered back to the brain as context.

**The tools: nine, fenced in.** Read, write, append and surgically replace files; list and create directories; web search; shell commands; and `run_python`, which executes code in an isolated process inside `projects/` (the CodeAct pattern). Every path goes through `_safe_path`, so the agent never leaves its folder. The sandbox backend is switchable — local, Daytona or E2B — with a safe fallback to local.

**Knowledge: search before you build.** A SQLite base with FTS5 for text and semantic vectors (sentence-transformers when available, otherwise a built-in hashing fallback), fused with Reciprocal Rank Fusion (k=60). `ingest.py` loaded 87 chunks across three stacks in our run. Before each task the relevant knowledge is injected into the brain; after each success the experience is stored as a skill. A skill index discloses skills progressively in three layers with fuzzy Arabic matching, seeded with 5 skills.

**Two front ends.** A CLI with six commands, and an RTL web UI with live streaming and 12 API routes showing the active brain, the skills panel and the execution trace. 74 tests cover loop, knowledge and tools — re-run locally: 74 passed in 2.18 s.

**Generation two.** Mansur was later rebuilt from scratch "inspired by its patterns" (as its decisions log records), with seven agents and 13,908 lines. Ai_Alabbasi remains the readable core that shows how an agent you own is put together.

## Five-point summary
1. An open-source (MIT) agent core: 31 Python files, 3,318 lines, one required dependency — readable in a sitting, runnable on your server.
2. Swap the brain with one YAML line across 8 presets or a local model; a missing key yields an explicit error event, not a crash.
3. A plan-and-execute loop with a six-state machine, safe interrupts and a 25-step cap; 9 fenced tools with isolated Python execution.
4. Hybrid knowledge, FTS5 + vectors via RRF: 87 chunks ingested, every success saved as a skill (5 seeded).
5. 74 tests re-run locally without an API key; the first generation Mansur grew from.
