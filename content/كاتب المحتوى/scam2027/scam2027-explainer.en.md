scam2027 | كاتب المحتوى | 2026-09-23 | draft-for-editor

# scam2027 — Project explainer

## Executive summary
1. **Status first:** a multi-tenant course and assessment platform under construction — the foundation is complete and 37% of the roadmap is done (24 of 65 tasks; P0 16/16, P1 8/15). Not started yet: assessment and online exams, assignments and grading, AI, SIS import, full PDPL compliance, MFA and SSO, and LTI/QTI/OneRoster.
2. What is built: multi-tenancy isolated by PostgreSQL Row Level Security on 30 tables, Auth.js with revocable sessions and account lockout, and RBAC with 114 dotted permissions, 5 system roles and custom roles.
3. Modules that work today: users, academic structure (years/semesters/colleges/departments/majors/levels), courses, sections and enrolment, files with signed downloads, notifications, and a unified recycle bin with 30-day retention.
4. Quality measured locally on 2026-09-23: 181 Vitest tests passing, zero type errors, a 28-route build, and 33 docs plus 9 ADRs updated with every PR.
5. Gaps, stated plainly: CI is an unactivated template, there is no live URL or documented university, the final license is undecided ("all rights reserved"), and the README points to another account.

## The problem
Nine legacy repositories for a university course system: a near-complete UI, three partial backends, scattered docs — none with multi-tenancy, serious tests, CI or data-protection compliance. A university wanting one deployment for several institutions had no foundation to build on.

## The solution
One repository unifying them on Next.js 16, React 19, Prisma and PostgreSQL 16 with Zod-validated Server Actions. Isolation lives in the database, not the application: shared schema, tenantId column and Row Level Security on every tenant table; the app's DB user cannot bypass RLS and the tenant is set per request. On top: Auth.js v5 with Argon2id and revocable sessions, and 114 dotted permissions in 14 categories generated from a documented matrix. The UI is Arabic RTL, mobile-first, with an app shell and per-role dashboards.

## The key engineering decision
Isolation in PostgreSQL. A query that forgets the tenant filter leaks nothing, because the database itself refuses it — and tenant-isolation integration tests guard that. And STATUS.json and CHANGELOG change in the same commit as every task, so the stated status is the real one.

## The numbers (from the code and from pnpm test)
114 permissions · 34 data models · 30 RLS tables and 30 policies · 181 tests passing · 0 type errors · 28 routes · 61 UI components · 1,042 translation keys · 33 docs + 9 ADRs · 24 / 65 tasks.

## Not done yet
P2 (assessment, file viewer, AI, SIS import, basic PDPL), P3 (assignments, MFA, platform admin, full PDPL, OpenAPI), P4 (SSO, push, attendance, PWA, webhooks) and P5 (LTI 1.3, QTI 3.0, OneRoster 1.2) have not started. CI is a template only. README claims 68 models (planned) and 80 Playwright tests — not re-measured here, so not shown. No live URL; 23 commits in four days. License undecided; README points to MoTechSys rather than moain2028 and carries the developer's phone and a `/developer` page inside the product.

## Who it is for
Universities and colleges that want a course platform serving several institutions from one deployment, or their own — and anyone building an academic platform who wants a tested multi-tenant foundation. DM me.

<!-- Sources: tech.md scam2027; research.md; STATUS.json. ~500 words. Status first; no "open source"; no "ready". -->
