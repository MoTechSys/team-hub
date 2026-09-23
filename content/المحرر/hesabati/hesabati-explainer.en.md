hesabati | المحرر | 2026-09-23 | sealed-by-editor 2026-09-23

# Hesabati — project explainer

## Executive summary
1. An Arabic-first finance and accounting system for small-business owners who run more than one activity, bringing all their businesses under one login.
2. Receipt and payment vouchers, journal entries, bank accounts and cash boxes, customers and suppliers, warehouses and purchasing, payroll, exchange rates, roles and permissions, and a real-time dashboard.
3. Angular 21 and Tailwind on the front end; Hono on Node with PostgreSQL and Drizzle on the back end; WebSocket for live updates; one Docker command to run.
4. Measured from code and a live run: 50 screens, 84 tables, 154 API routes, 158 passing backend tests, Docker and Nginx deployment.
5. It runs and builds, with two documented operational defects worth fixing before a technical client sees the repository; no public live link.

## The problem
A small-business owner running two or three shops keeps separate books and spreadsheets, so balances, debts, and payroll never appear on one screen, and there is no single Arabic finance system that covers entries, vouchers, accounts, warehouses, payroll, and permissions together.

## How it works
Hesabati is a web application: an Angular 21 front end with Tailwind 4 in right-to-left Arabic, and a Hono server on Node talking to PostgreSQL through Drizzle ORM, with JWT authentication and Zod validation. The server is built from independent "engines" (entries, numbering, sub-ledgers, currencies, billing, HR, archiving, audit, permissions, custom screens) that serve the API routes. The dashboard updates live over WebSocket and draws its charts with ApexCharts. Deployment is Docker Compose (PostgreSQL, backend, Nginx) in one command.

## Who it's for
Small-business owners running more than one activity who want one correct number across all of them.

## What sets it apart
- Multiple businesses under one login instead of a separate account per shop.
- Full accounting coverage in one system: from voucher and entry to warehouse, payroll, and exchange rate.
- A real-time dashboard with no page refresh.
- Verifiable: 158/158 tests across 12 files, 50 screens, 84 tables, 23 backend engines.
- One Docker command to run.

## Current status and what remains
Runs and builds; last development 2026-04-13 (324 commits). Two documented defects: migration ordering fails on an empty database (db:push then db:seed work instead), and a type error in fiscal-periods blocks ng build without a one-line fix. The README lists Chart.js and Three.js, which are not actually used (ApexCharts is). No live link, video, or case study yet: to be completed.

<!-- Sources: brief.en.md (sealed 2026-09-11) · tech.md (solution, stack, numbers, status, team notes) · links.md. Every sentence traces to these files. -->
