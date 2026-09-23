unicore-os | كاتب المحتوى | 2026-09-23 | draft-for-editor

# UniCore-OS — Project Explainer

## Executive summary
1. One university management system with a fully Arabic RTL interface and optional AI features, built on Next.js 16, React 19, Prisma 5 and Tailwind 4, open source.
2. Fine-grained permissions: 52 permission codes from a single source in the code, custom roles and a Super Admin, with every page and every server action checking before it runs.
3. A full academic hierarchy (colleges → departments → majors → courses → sections) and a quiz engine with three question types and a timer, plus optional AI question generation and essay grading via OpenAI or Gemini.
4. Status: 2.0.0-rc.4 — 22 database models, 26 pages, 15 feature modules, zero TypeScript and ESLint errors, and a 102-page crawl across 3 roles with zero issues; but no unit tests or CI yet.
5. Gaps, explicitly: no tests or CI, the AI center is disabled without an API key, /logs returned 404 for the admin in the local run, the README lags the code, and no user numbers.

## The problem
University administration is scattered: users and roles in one system, academic structure in another, quizzes and grades in a third — and most of these systems don't speak Arabic or offer permissions granular enough to separate a dean, a lecturer and a student at the level of a single action.

## How it works
UniCore-OS is a Next.js App Router application with Server Actions. Pages are server components that check permission before rendering, and sensitive operations run on the server only and return a uniform success-or-error result. The 52 permission codes live in one constants file and are assigned to custom roles; the system role holds all of them.

Data lives in Prisma across 22 models: SQLite for development, PostgreSQL for production. Deletion is always soft — a record is stamped with a deletion date and appears in the trash bin, where it can be restored or permanently removed with the right permission. Authentication uses NextAuth v5 with JWT sessions and bcrypt password hashing; inputs are validated with Zod.

The academic hierarchy runs from college down to the semester section, which gets an instructor and enrolled students. The quiz engine supports multiple choice, true/false and short answer with a timer, moves through draft → published → closed, and feeds a gradebook with CSV export. The AI module generates questions from a topic and proposes grades for essay answers through OpenAI or Gemini when a key is present; without one it clearly shows as disabled. Drag-and-drop file management, notifications, an audit log and a role-aware live dashboard complete the picture.

## Who it's for
Capstone students and computer science departments that want an open-source, extensible Arabic university system, and anyone who needs a ready base for an academic information system with fine-grained permissions.

## What sets it apart
Arabic RTL from the ground up rather than a later translation; permissions at the action level, not just the page; nothing hard-deleted; and a modern stack (Next.js 16, React 19, Tailwind 4) that any CS student can build on.

## Current status and what remains
Release 2.0.0-rc.4 dated 2026-09-04 after a "recovery" of the first version: build and crawl are clean, but there are no unit tests, no E2E and no CI. The README still says Next 15 and 20 tables while the code is on 16.1.6 and 22 models. The /logs page returned 404 for the system admin in my local run, and the AI center showed as "disabled" because no API key was set — the AI features are optional and off by default. No live site, no user numbers.

<!-- Sources: tech.md unicore-os (all numbers) · README "Key features" and "Security" · docs/HANDOFF.md §0 and §3 · .env.example · local run 2026-09-23. ~540 words excluding the summary (editor may trim). -->
