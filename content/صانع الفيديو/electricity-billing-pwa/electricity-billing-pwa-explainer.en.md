electricity-billing-pwa | صانع الفيديو | 2026-09-23 | draft — for editor seal

# Electricity Billing PWA — Project Explainer

## Executive summary
1. A progressive web app that installs on a station clerk's phone and issues an official A4 electricity invoice — all data on the device, no server, no internet.
2. Built with Next.js, TypeScript, and Tailwind; storage in IndexedDB via Dexie with three tables (subscribers, invoices, settings); the PDF is generated in-browser with Arabic shaping and amount-in-words.
3. Subscriber management, automatic consumption and balance-due math, a searchable archive, and JSON backup export/import to move between devices.
4. A documented architectural pivot: v1 was a full server (Prisma/SQLite/JWT); on 2026-06-09 the client decided "no server, every device independent", and the app was rebuilt fully local.
5. Status: locally production-ready (last commit "SW v20", 2026-06-10), no automated tests, the announced Vercel link returns 404, and the README still describes the old version — to be completed.

## The problem
Small power stations and private generators handwrite invoices and compute consumption and arrears by hand. An arithmetic mistake costs a subscriber relationship, internet at the station is unreliable, and any off-the-shelf accounting system needs a server, a network, and logins.

## How it works
The clerk opens the app from an icon on the phone like any other app. All data lives in a local database inside the browser (IndexedDB via Dexie) in three tables: subscribers, invoices, settings. To issue an invoice, the clerk enters the previous and current readings and the kWh price; the app computes consumption, amount, and balance due with the formula every collector knows (consumption = current − previous, amount = consumption × price, due = amount + services + arrears − paid) and writes the total in Arabic words. The A4 invoice is generated as a PDF inside the browser itself (pdf-lib/jsPDF with arabic-reshaper and bidi) with no server involved. The archive is searchable, and one button exports all data as JSON or imports it on another device. There is no authentication because the device is personal, and no sync because each device is independent by the client's decision.

## Who it's for
Small power stations, private generator operators, and collectors who work from a phone in places without reliable internet.

## What sets it apart
- "No server" is a decision, not a gap: zero running cost, zero network dependency, and data never leaves the device.
- Fully RTL Arabic down to the PDF (shaping + amount-in-words) — where most generic invoicing tools stumble.
- A mobile UI the client redesigned himself: a 2×2 stats grid and a bottom navigation bar — every note documented in docs/ with its implementation status.
- Eight decision and review documents in the repo (MASTER_PLAN, PIVOT_LOCAL_PWA, MOBILE_AUDIT…) explaining the "why", not just the "what".

## Current status and open items
- Last functional commit 2026-06-10 (31 commits); the code has no server and no authentication.
- The README is outdated and describes Prisma/SQLite/JWT — to be rewritten per PIVOT_LOCAL_PWA.md (top priority).
- The announced Vercel link returns 404 — redeploy or remove.
- No automated tests; page count differs between sources (brief: 7, tech.md: 9) — to be unified.
- Real number of stations/users: to be confirmed.

<!-- Sources: brief.en.md (Problem/Solution/Result/Who), case-study.ar.md (formula, 2026-06-09 pivot, mobile UI), tech.md (stack, numbers, status, cleanup notes). -->
