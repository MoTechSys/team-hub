alabbasi-tech-platform | متخصص SEO | 2026-09-23 | draft — to be sealed by the editor

# Alabbasi Tech — static official site and client portal for a software house

**Segment:** Companies
**Problem:** A Sana'a software house needs a site that loads on cheap Android over weak networks, plus client requests and tickets without a server per page.
**Solution:** A fully static Next.js 15 export — 19 Arabic RTL pages, zero images — and an Express + SQLite portal: projects, tickets with attachments, requests, three roles, 11 permission codes.
**Results in numbers:** 19/19 pages build, zero TypeScript errors, 11 passing tests, and a 14-page pixel audit with zero horizontal overflow and zero text overlap.
**Who it helps:** Companies that want to own their site and portal's code and data, not rent a closed subscription.
**Get in touch:** Let's scope a site and portal you own — DM or email.

<!-- Sources: root README (19 pages, quality gates, 11 permissions, 3 roles); site/README.md (static export, zero images, design system); portal/README.md (four layers, SQLite WAL); docs/pixel-audit-site.md (14 pages × 390/768, 0 px overflow, 0 overlap); local verification 2026-09-23: npm run typecheck = 0 errors, npm run build = 19/19, vitest = 11 tests. ≈120 words. -->
