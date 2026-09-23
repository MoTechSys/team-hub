mansur-ai | مهندس | 2026-09-23 | draft — to be sealed by the editor

# Mansur AI — an Arabic-first agent that plans, executes, verifies and learns

**Segment:** Companies
**Problem:** General-purpose AI agents are English-first, don't run on the owner's own server, and don't learn from their tasks.
**Solution:** A brain router picks the model per task with fallback; planner, ReAct executor, verifier and learner run on LangGraph; 13 specialized agents; 45 tools, 27 of them AST code-intelligence; four-tier memory; an RTL Arabic chat UI with live streaming.
**Results in numbers:** 45 tools · 13 agents · 110 green tests · 54 commits (re-measured in tech.md). Usage figures: TBD.
**Who it helps:** Technical teams wanting an Arabic automation agent on their own infrastructure that audits their code.
**Get in touch:** Let's scope your team's agent — DM or email.

<!-- Sources: README.md (features, structure) · tech.md (numbers & sources: pytest 110, tool_names 45, roster 13, git log 54, DECISIONS 11) · core/orchestrator/graph.py (plan→execute→verify→learn). No live URL (not responding). -->
