electricity-billing-pwa-v2 | كاتب المحتوى | 2026-09-23 | draft

# Electricity Billing V2 — the official invoice from the clerk's phone, no server, no internet

**Segment:** Companies (small power stations and private generators)
**Problem:** Version one needed a server, a database and authentication; a small station wants an app installed on the clerk's phone that issues an official invoice even with no network.
**Solution:** I rebuilt the system as a fully local progressive web app in Next.js, TypeScript and Tailwind: the database lives on the device itself (IndexedDB via Dexie), zero API routes, an A4 invoice printed as text and shared as a real Arabic PDF inside the browser, instant consumption and balance calculation with Arabic amount-in-words, a filterable archive, and a one-tap JSON backup export/import.
**Results in numbers:** from 10 API routes and five Prisma models to 0 routes and 3 local tables; the pivot commit removed 3,169 lines and added 682; 9 pages, 31 commits, and a build with zero TypeScript errors. No automated tests yet.
**Who it serves:** small power stations, generator operators and collectors who work from a phone.
**Contact:** Does your station still write invoices by hand? Message me and I'll send the demo to your phone.

<!-- Sources: tech.md electricity-billing-pwa-v2 (all numbers measured from git and code, 2026-09-23). 128 words. -->
