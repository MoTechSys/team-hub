almham-electricity-erp | صانع العروض | 2026-09-23 | draft — to be sealed by المحرر

# Al-Abbasi Specialized Systems — an ERP for electricity generation and distribution: project explainer (English)

## Executive summary (5 points)
1. One multi-company, multi-branch, multi-station ERP for electricity utilities, replacing scattered spreadsheets and a legacy SQL Server billing tool. (brief.en «Problem/Solution»)
2. Angular 22 (signals, Material, Leaflet maps) on NestJS 11 with Fastify, Drizzle ORM and PostgreSQL; installable as a PWA with uncached API responses. (brief.en «Solution»)
3. Integrated billing with direct ledger impact: double-entry posting, idempotency, and a draft → ready → approved → posted approval path, plus full historical migration from ECAS. (tech.md «الحل»)
4. Running on live data at a local electricity utility (company → institution → branch → station); 687 billing periods reconciled, 9 functional domains, 515 test files. (brief.en «Result» · tech.md «الأرقام»)
5. Private repo, internal system with no live URL; production subscriber, meter and user counts: to be confirmed. (links.md · tech.md «يُستكمل»)

## The problem
Small utilities run generation, subscribers, billing, fuel and treasury across spreadsheets and a legacy SQL Server tool (ECAS), with no single financial picture, no unified accounting trail and no audit. (brief.en «Problem» · tech.md «المشكلة»)

## How it works (architecture in plain words)
The model is hierarchical — company → institution → branch → billing area → billing square — and everything beneath is scoped to its place. The Angular 22 frontend (standalone components, signals, Leaflet) shows stations, generators and subscribers on maps. The NestJS 11 backend on Fastify reads and writes PostgreSQL through Drizzle. Readings become invoices; payments post automatically to the general ledger as idempotent double-entry journals (SAP FI-CA / Oracle CC&B style) after an approval path. Fuel, solar, treasury, employees and tasks live in the same system. An optional fail-safe bridge reads legacy ECAS data from SQL Server, and Node ETL scripts migrate historical readings, payments and GL entries idempotently and resumably. Around the server: a Flutter app for collectors and meter readers (48 screens), a Kotlin app for employees, and an Electron + PGlite desktop collection point that works offline and syncs. (brief.en «Solution» · tech.md «الحل»/«التقنيات»)

## Who it is for
Utilities and industrial operators needing one system from meter reading to ledger. (brief.en «Who it's for»)

## What sets it apart
- Billing with direct accounting impact (double-entry + idempotency + approval path) instead of a billing tool detached from the books. (tech.md «الحل»)
- No break with the past: full ECAS migration with 687 reconciled billing periods. (tech.md «الأرقام»)
- Field coverage: mobile collection, offline collection point, subscriber maps. (tech.md «التقنيات»)
- Model depth: 170 tables and 157 enums in the schema, 9 functional domains from stations to audit. (tech.md «الأرقام»)
- 515 test files in the tree. (tech.md «الأرقام»)

## Current status and open items
- In real operation on one company's data; active development (last push 2026-09-11); README updated 2026-07-26. (tech.md «الحالة»)
- To be confirmed: production subscriber/meter and user counts · live URL (internal system) · test and page counts per brief. (tech.md «يُستكمل» · brief.en «Result»)
- The client's name appears in the README and is published only with Moain's approval. (brief.en sources comment)

<!-- ~460 words · Sources: brief.en.md · tech.md · links.md -->
