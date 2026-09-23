mansur-ai | مهندس | 2026-09-23 | draft — to be sealed by the editor

# Mansur AI — project explainer

## Executive summary

1. **Problem:** General-purpose AI agents are English-first, don't run on the owner's own server with its tools, and don't keep what they learn between tasks.
2. **Solution:** An Arabic-native multi-agent system: planner, ReAct executor, verifier and learner in one LangGraph loop, with a brain router that picks the model per task.
3. **Toolkit:** 45 registered tools (27 of them AST code-audit tools), 13 specialized agents, and a four-tier hierarchical memory in SQLite.
4. **Experience:** An RTL Arabic chat UI with live WebSocket streaming and a stop button, an admin dashboard at `/app`, and a one-line CLI (`run.py`).
5. **Status:** Working core, tested locally — 110 green tests and 54 commits (measured 2026-09-23); the live URL does not respond and usage figures are TBD.

---

## What is the problem?

General AI agents are designed English-first, run from their vendor's cloud rather than the owner's infrastructure, and don't learn from their tasks — every job starts from zero. A technical team that wants an automation agent that speaks Arabic, runs on its own server with its own tools, and audits its code doesn't find that off the shelf.

## How does it work?

Mansur AI is Python on FastAPI and LangGraph:

- **Brain router** (`core/brain/router.py`) picks the model per task type, with fallback on failure and cost tracking.
- **Four core agents** — planner, ReAct executor, verifier, learner — orchestrated by LangGraph in a `plan → execute → verify` loop; a failed verification routes back to execution, a passed one moves to `learn`, which stores the experience as a skill (`core/orchestrator/graph.py`).
- **13 specialized agents** (coder, researcher, writer, analyst, designer, web builder, planner, verifier, translator, data engineer, DevOps, QA, summarizer) routed by task intent.
- **45 tools** in one registry: files, a sandboxed shell under `data/sandbox` with a timeout, web fetch and search, HTTP requests with SSRF protection, read-only SQL over CSV/JSON, surgical code editing, and 27 code-intelligence tools that work on the AST without executing code — from outline, definitions and references to audits for security, exceptions, logic bugs, performance, async, resources, dataflow, logging, naming and regex.
- **Hierarchical memory** in SQLite with four tables: working, episodic, skills, semantic.
- **Interfaces:** an RTL Arabic chat at `/` over WebSocket with live streaming and a stop button, a React admin dashboard at `/app` (sessions, skills, plugins, config, keys, logs), and a single terminal command.

## Who is it for?

Technical teams and companies that want an Arabic automation agent running on their own infrastructure, executing file, web and data tasks, and auditing their code with AST tools.

## What makes it different?

- **Arabic-native, not translated:** UI, skills and routing in Arabic, RTL layout.
- **Built-in verify-and-learn loop:** the verifier sends failures back to the executor; the learner keeps what worked.
- **Code intelligence without execution:** 27 audit tools inspect only the syntax tree — safe on production code.
- **Runs on your infrastructure:** one config file, local SQLite, sandboxed shell.

## Current status and what remains

A working core: 110 green tests and 54 commits between 2026-06-13 and 2026-06-24. To be completed: the live URL does not respond; the `/app` dashboard still carries the Hermes Agent identity and some of its pages (analytics, models, cron, profiles) render empty without an API key; MCP is a stub; isolation is subprocess, not Docker; semantic vectors use hashing rather than a real embedding model; and real usage figures are undocumented.

**Contact:** Let's scope your team's agent — DM or email.

<!-- Sources: brief.en.md (Problem, Solution, Who it helps, Get in touch) · tech.md (Numbers & sources: pytest 110, tool_names 45, roster 13, git log 54; operational verification; cleanup notes) · README.md (features, structure) · docs/PROJECT_STATUS.md (remaining: MCP, sandbox, vectors, dashboard title) · core/orchestrator/graph.py:91-99 · core/memory/store.py · core/tools/registry.py · core/tools/http_tool.py · core/tools/shell.py · ui/web/server.py. -->
