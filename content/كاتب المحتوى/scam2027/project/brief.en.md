scam2027 | كاتب المحتوى | 2026-09-23 | draft

# scam2027 — a multi-tenant course & assessment platform, under construction with the foundation complete

**Segment:** Companies (higher education / universities)
**Problem:** Nine legacy repositories for a university course system — a near-complete UI and three partial backends — with no multi-tenancy, no tests, no CI, and no data-protection compliance.
**Solution:** One repository unifying them on Next.js 16, Prisma and PostgreSQL with Row Level Security per tenant, Auth.js with revocable sessions, and RBAC with 114 dotted permissions and 5 system roles; an Arabic RTL, mobile-first UI with an app shell. Actually built so far: users, roles, academic structure, courses, sections, enrolment, files, notifications and a unified recycle bin — all tracked automatically in STATUS.json with every PR.
**Results in numbers:** 24 of 65 roadmap tasks (37%) — foundation P0 complete 16/16, P1 at 8/15; 114 permissions, 34 data models, 30 tables under RLS, 181 Vitest tests passing, 0 type errors, 33 docs and 9 ADRs.
**Who it serves:** Universities and colleges that want a course and assessment platform serving several institutions from one deployment, or their own private one.
**Contact:** Building an academic platform and want a tested multi-tenant foundation? DM me.

<!-- Sources: tech.md scam2027 (STATUS.json, schema.prisma, pnpm test/typecheck locally 2026-09-23). ~140 words. Status shown as "under construction", not "ready". -->
