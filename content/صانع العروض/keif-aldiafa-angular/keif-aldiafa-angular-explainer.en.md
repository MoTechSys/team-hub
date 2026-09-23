keif-aldiafa-angular | صانع العروض | 2026-09-23 | draft — to be sealed by المحرر

# Keif Al-Diafa Management System — project explainer (English)

## Executive summary (5 points)
1. A fully Arabic progressive web app that replaces the paper ledger of a Jeddah hospitality company that staffs events with hosts. (README «What is this?»)
2. Serverless: Angular 22 with Signals and zoneless change detection, all data in IndexedDB on the device, a Service Worker for install, offline use and auto-update. (README «Architecture» · ADR-002)
3. Solves seven documented problems: digital bookings, minute-level host conflict prevention, inventory shortage detection, quote/invoice generation, a receivables ledger per host, debt aging with reminders, and equipment check-out/return matching. (README «seven problems»)
4. 232 green tests in 24 files, 60 atomic permissions, 12 documented architecture decisions, money in integer halalas. (tech.md numbers)
5. Status: in development; an independent audit (AUDIT-GAPS.md) flags gaps such as the host-assignment notification being built but not wired; live user count: TBD. (README status badge · AUDIT-GAPS.md · tech.md)

## The problem
A small company provides hosts who serve Saudi coffee at corporate and home events, and ran everything in a paper notebook: the same host booked twice, supplies (cups, dallahs, coolers) running short when events overlap, quotes and invoices written by hand, host debts piling up with no central view, companies paying late, and equipment going missing. (README «seven problems»)

## How it works (architecture in plain words)
There is no server at all. The app runs entirely in the browser on the manager's phone or laptop: Angular 22 standalone components with Signals, data in IndexedDB, backups by JSON export or optionally to Google Drive. An event is created through a 4-step wizard (client → details → needs → review); when a host is picked the system checks time overlap to the minute (`newStart < existingEnd && newEnd > existingStart`) and sums reservations across overlapping events to detect inventory shortage before it happens. From the event page a quote is generated and converted into a PDF invoice; every money movement is written to an append-only receivables ledger in integer halalas, so each host and client has a running "owed to / owed by" balance, statement and debt aging. After the event, equipment handed out is matched against returns with damage and loss charged to the host or the event. Permissions are hybrid: 60 atomic permissions (10 resources × 6 actions), 3 protected system roles and unlimited custom roles, checked by permission never by role name. (README «core features» · docs/ARCHITECTURE.md §3–4 · permission.model.ts)

## Who it is for
Small service businesses that book people, hand out equipment and track receivables, often working at venues without coverage. (README «why no server?» · brief «Who it helps»)

## What sets it apart
- Conflict prevention in logic, not UI, covered by 13 tests including adjacency and midnight boundaries. (README · conflict.service.spec.ts)
- Absolute money precision: `toCents` kills the 0.1 + 0.2 error. (README · ADR-004)
- A binding contract: files ≤400 lines, zero `any`, a test per logic service, mandatory visual verification. (CONTRACT.md · README «Quality»)
- 12 ADRs explaining every decision — including the "traps" learned the hard way. (docs/DECISIONS.md · README «documented traps»)
- Zero running cost: no server, no subscription. (ADR-002)

## Current status and open items
- In development; 40 commits over 5 days (2026-08-01 → 08-05). Build and full test suite pass on re-run 2026-09-23. (git · tech.md)
- Known gaps: host-assignment notification built but not wired; reminders are in-app/WhatsApp, not SMS; linking equipment to a host at hand-out is optional. (AUDIT-GAPS.md)
- TBD: real user and event counts · live URL (internal deployment). (tech.md)
- Screenshots come from a local run on seed data; the company's real identifiers (CR number, phone, IBAN) and one real client name were masked. (tech.md «run & capture»)

<!-- ~480 words · Sources: README.md · docs/ARCHITECTURE.md · docs/DECISIONS.md · AUDIT-GAPS.md · tech.md -->
