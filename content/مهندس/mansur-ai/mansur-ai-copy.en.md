mansur-ai | مهندس | 2026-09-23 | draft — to be sealed by the editor

# Post copy (EN) — every sentence from brief.en.md / tech.md; every figure measured 2026-09-23

## 1) LinkedIn post (≤120 words)

General AI agents are English-first, don't run on your server, and don't learn from their tasks.

Mansur AI is an Arabic-native multi-agent system: a brain router picks the model per task with fallback, and planner, ReAct executor, verifier and learner run in one LangGraph loop — a failed verification loops back, a passed one is saved as a skill. It ships 13 specialized agents and 45 tools, 27 of them AST code audits that never execute code, plus four-tier memory and an RTL Arabic chat UI.

110 green tests and 54 commits — measured with real commands.

For technical teams wanting an Arabic automation agent on their own infrastructure. Let's scope your team's agent — DM me.

github.com/moain2028/mansur-ai

(≈115 words — source: brief.en.md · tech.md)

## 2) X post (≤280 characters)

An Arabic-first agent that plans, executes, verifies and learns: LangGraph + a brain router + 45 tools (27 AST code audits, no execution) + four-tier memory + RTL chat UI. 110 green tests. Runs on your own server.
github.com/moain2028/mansur-ai

(≈250 characters — source: brief.en.md Solution · tech.md)

## 3) Instagram caption (≤150 words)

An Arabic agent that runs on your server — not in someone's cloud.

Mansur AI: a brain router picks the model per task, and four agents (planner, ReAct executor, verifier, learner) run a LangGraph loop that checks the result and saves what worked as a skill. 13 specialized agents from coder to translator, and 45 tools — 27 of them AST code audits for security, exceptions, performance, async, resources and regex — all without running the code.

An RTL Arabic chat UI with live streaming and a stop button, an admin dashboard, and a one-line CLI.

110 green tests · 54 commits — measured on the clone on 2026-09-23. Usage figures: TBD.

For technical teams wanting an Arabic automation agent on their own infrastructure — DM me to scope it.

#AI #Agents #LangGraph #Python #FastAPI #Arabic #RTL #DevTools

(≈125 words — source: brief.en.md · tech.md)

## 4) Reel script (EN — 21.6 s, 7 scenes, no logo)

| # | Scene | On-screen text | Source |
|---|---|---|---|
| 0 | Cover | Mansur AI — an Arabic-first agent that plans, executes, verifies and learns | brief.en.md H1 |
| 1 | Problem | English-first agents that don't run on your server — and don't keep what they learn | brief.en.md Problem |
| 2 | Solution | Plan → execute → verify → learn — LangGraph orchestrates planner, ReAct executor, verifier and learner | graph.py:91-99 |
| 3 | How it works | A brain router and 45 tools — sandboxed shell, web, and 27 AST code-audit tools | router.py · registry.py |
| 4 | Verified | Every figure measured by a real command — pytest, tool_names, roster on the clone, 2026-09-23 | tech.md |
| 5 | By the numbers | 45 tools · 13 agents · 110 tests · 54 commits | tech.md |
| 6 | Ask | Want an Arabic agent on your own infrastructure? — let's scope it | brief.en.md Who it helps · Get in touch |

Optional voice-over (≈50 words): "General agents are English-first and don't run on your server. Mansur AI is Arabic-native: it plans, executes, verifies and learns — with LangGraph, a brain router and 45 tools, 27 of which audit your code without running it. 110 green tests. Let's scope your team's agent."

<!-- Sources: work/mansur-pack/docs/brief.en.md · tech.md · core/orchestrator/graph.py · core/tools/registry.py. Link github.com/moain2028/mansur-ai (HTTP 200, 2026-09-23). -->
