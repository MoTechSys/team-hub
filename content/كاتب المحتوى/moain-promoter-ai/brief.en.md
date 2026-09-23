moain-promoter-ai | كاتب المحتوى | 2026-09-23 | draft

# Moain Promoter AI — a team of agents that markets a GitHub portfolio, in two languages, on six platforms

**Segment:** Companies (dev studios and freelancers with large portfolios)
**Problem:** A developer with a large portfolio has no time to read every repository, capture its screenshots, write an Arabic and English post about it, and schedule it on every platform.
**Solution:** A multi-agent system in Python and FastAPI under one orchestrator: an agent analyzes the repository, another runs it and captures screenshots with Playwright, a third generates a visual fallback when capture fails, a bilingual content writer with a Yemeni persona and 27 templates, a 30/60/90-day campaign scheduler, and a publisher for six platforms — all driven from a chat-style Next.js dashboard that switches between 27 model providers with one key, detects the key type automatically, and defaults to dry-run so nothing goes live by accident.
**Results in numbers:** 9 agents, 6 publishers, 27 providers in the registry, 11 capture viewports, 7 CLI commands, 10 API routes, and 82 tests passing in CI. No live URL yet; live scheduling and publishing need keys.
**Who it serves:** developers, freelancers and small studios who want to market what they build without stopping building.
**Contact:** The repository is open under MIT — ask me about running it on your portfolio.

<!-- Sources: tech.md moain-promoter-ai (all numbers from code, git and pytest, 2026-09-23). 158 words. -->
