moain-promoter-ai | كاتب المحتوى | 2026-09-23 | draft-for-editor

# Moain Promoter AI — Project explainer

## Executive summary
1. An open-source (MIT) multi-agent marketing system: from a GitHub repository to an Arabic and English post scheduled on six platforms — Python and FastAPI behind a chat-style Next.js 14 dashboard.
2. Nine agents under one orchestrator: repository analysis, real screenshots via Playwright, a visual fallback when capture fails, bilingual writing with a local persona and 27 templates, ideation and image generation, 30/60/90-day campaign scheduling, and publishing.
3. Provider-agnostic: 27 model providers in one registry, the key type detected from its fingerprint and probed before use, with per-provider and per-platform rate limits in config files.
4. What works today without keys: the dashboard, the backend and 82 tests passing locally and in CI. What needs keys: live analysis, capture, writing and publishing.
5. Gaps, stated plainly: prototype, no live URL, empty schedule endpoint, simple chat router, README behind the code, no documented published post.

## The problem
Each new project deserves a post, and each post means re-reading the repository, running it for screenshots, writing in Arabic and English for each platform, then scheduling. Off-the-shelf schedulers start from a written post — not from the code.

## The solution
Moain Promoter AI starts from the repository. One orchestrator hands work to specialized agents: RepoAnalyzer extracts what is marketable from README and code; Capture runs the project and shoots it at 11 viewports; Mockup provides a visual fallback; ContentWriter writes in two languages with a local persona and 27 templates; Ideation and ImageGenerator propose angles and images; Scheduler builds a 30/60/90-day campaign; Publisher posts to LinkedIn, X, Facebook, Instagram, Dev.to and Medium.

All of it runs from a five-panel dashboard (chat, repositories, gallery, calendar, settings) or a seven-command CLI.

## The key engineering decision
No lock-in to a single model vendor: a registry of 27 providers, key-type detection from the key's fingerprint, a probe before use, and conservative rate limits in `configs/`. The default is `dry_run: true` — nothing goes live unless explicitly disabled.

## The numbers (from the code)
9 agents · 6 publishers · 27 providers · 11 capture viewports · 27 templates · 7 CLI commands · 10 API routes · 4 tables · 82 tests passing · 5,907 lines of Python + 1,495 lines of TypeScript.

## What is not done yet
No live URL. The schedule endpoint returns a fixed empty list and the chat router is keyword-based — both marked "simplified" by the author. Celery and LangChain sit in requirements unused. The README says 7 agents, points to a 404 repository, and cites "171+ repositories" — a figure about the owner's account, not this project. No screenshot or generated post exists in the repository; this pack's screenshots come from a local run with no keys, and the repositories list shows demo data.

## Who it is for
Developers, freelancers and small studios who want what they build to be marketed without stopping building. The repository is open — DM me.

<!-- Sources: tech.md moain-promoter-ai; research.md. ~500 words. -->
