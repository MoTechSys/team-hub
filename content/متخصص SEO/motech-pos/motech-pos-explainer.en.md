motech-pos | متخصص SEO | 2026-09-23 | v2 addendum · project explainer (English) — every sentence from brief.en.md / tech.md

# Motech POS — project explainer

## Executive summary (5 points)
1. An Arabic web point of sale (PWA) in React 19 and NestJS that runs on the company's live Oracle database without touching it: it reads the production schema read-only and writes to its own schema.
2. It replaces a legacy desktop POS locked to an Oracle client, where every change risked the live database.
3. It covers 71 of 71 buildable screens of the incumbent system (88.75% of 80), with 26 backend modules, 215 REST endpoints, and 27 frontend feature modules.
4. Quality: 348 unit tests green, 160/160 live checks across 3 roles × 3 screen sizes, zero horizontal overflow, and a 59-table backup in 420 ms.
5. Status: beta/pilot — an independent audit called it a "parallel pilot system"; some P0 findings remain to be closed, and there is no live URL yet.

## The problem
Retailers on a legacy point of sale are locked into an Oracle desktop client; every change risks the live database. The business needed a modern Arabic RTL web alternative on phone, tablet, and desktop that reads the same live data without touching it.

## How it works (the architecture in plain words)
The front end is a React 19 PWA (TanStack Query, Zustand, Tailwind, shadcn RTL) that completes a full sale on a 390 px screen, with a bottom-sheet cart on mobile and touch targets of at least 48 px. The NestJS backend connects to Oracle through node-oracledb, reads the live production schema read-only, and writes everything the new system owns — invoices, shifts, permissions — into its own separate schema with 33 SQL migrations, so production stays untouched. The architecture is layered, with no SQL outside repositories and money stored as NUMERIC. Security: JWT in httpOnly cookies, CSP, login throttling, and 12 permission codes enforced per request.

Features: a complete checkout with partial and multi-currency payment, held invoices, guarded returns, shifts with cash reconciliation, vouchers, loyalty, promotions, stock counts, e-invoice QR, scheduled backups, a customer display, and Arabic thermal printing over Web Serial, WebUSB, and Bluetooth — field-tested on a Bixolon SPP-R310.

## Who it is for
Retailers who want to leave a closed POS without losing data.

## What sets it apart
No migration and no breakage: the data stays where it is and the new system runs beside the old one. Arabic RTL by design, not retrofitted. Quality documented in numbers: 348 tests, 160/160 live checks, zero horizontal overflow at 390/820/1440 px, and a 2,391-item catalog sync in about 966 ms.

## Current status and what remains
Beta/pilot: 71/71 buildable screens done, 9 screens closed by architecture decision records. An independent audit (2026-07-03) judged it "fit as a parallel pilot, not a full replacement" and logged 4 P0 issues, some since fixed; the rest remain to be closed. The demo domain in the docs does not respond, there is no root README, and USB printing on Windows failed due to an OS driver constraint. Last commit 2026-07-13; 170 commits.

<!-- Sources: brief.en.md (problem/solution/result/who); tech.md (Problem, Solution, Architecture notes, Status, Numbers table, Cleanup notes, Live URL). The incumbent product name is deliberately omitted (brief decision). ~490 words. -->
