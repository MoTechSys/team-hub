motech-attendance | صانع العروض | 2026-09-23 | draft — to be sealed by المحرر

# Motech Attendance — Project explainer (English)

## Executive summary (5 points)
1. A central web attendance system that replaces the per-branch desktop fingerprint program. (brief.en «Problem»)
2. Go backend + PostgreSQL, with a thin Python collector (pyzk) that pulls from fingerprint devices, signs each upload with HMAC, and syncs every 10 minutes via systemd. (brief.en «Solution»)
3. RTL dashboard: employees, daily & monthly reports, departments, overtime, shifts, leave with automatic balance deduction, holidays, CSV/Excel export. (brief.en «Solution»)
4. Tested on a live device: 11 employees, 3,118 punches; the shift-aware engine wrote 2,277 daily rows, idempotent on every rerun. (brief.en «Result»)
5. Status per README: Phase 0–4 and ESS complete (payroll/WPS export, PDPL privacy); production branch/device counts: to be confirmed. (tech-planner.md «الحالة» · tech.md «يُستكمل»)

## The problem
Branch fingerprint devices each feed their own desktop program. HR cannot see all branches in one place; shifts, leave and holidays are handled by hand; there are no flexible Arabic reports and no secure remote access. (brief.en «Problem» · tech.md «المشكلة»)

## How it works (architecture in plain words)
In each branch a small Python script (pyzk) talks to the fingerprint device over the network, pulls new punches, and posts them to the central server signed with HMAC — with replay protection. systemd schedules it every 10 minutes. The server is written in Go and stores data in PostgreSQL (schema `attendance`), then runs a daily processing engine that computes late, overtime and short hours per employee shift and applies leave and holidays. Results appear in a responsive RTL web dashboard (Go templates + Tailwind, no build step) with CSV/Excel export. Login is protected by bcrypt, signed sessions and rate limiting (5 attempts → 15-minute lockout), and every table is isolated by a tenant_id taken from the session, never from the client. (brief.en «Solution» · tech.md «التقنيات»/«الحل» · tech-planner.md «التقنيات»)

## Who it is for
Multi-branch companies and organisations (utilities, retail, factories) that already own fingerprint devices and need central reporting without a closed-software licence. (brief.en «Who it's for» · tech-planner.md «لمن يفيد»)

## What sets it apart
- A thin collector: no full program install per branch, and every upload is signed. (tech.md «الحل»)
- Idempotent daily engine: reruns never duplicate a row — proven on 2,277 rows. (brief.en «Result»)
- RTL Arabic dashboard by design, not a late translation. (brief.en «Solution»)
- 19 Go test files covering auth, HMAC, rate limiter and employee flows. (tech.md «الأرقام»)
- Fail-closed multi-tenant isolation from the session. (tech.md «التقنيات»)

## Current status and open items
- README reports Phase 0 (MVP), Phase 1 (employees + scheduled sync), Phase 1/2 HR (shifts/leave/holidays), Phase 3 payroll + WPS export (KSA and UAE), Phase 4 PDPL privacy, and the ESS portal as complete. (tech-planner.md «الحالة»)
- To be confirmed: production branch/device count · live URL (internal system) · real data volume after the live test. (tech.md «يُستكمل» · links.md)
- Screenshots in this pack come from a local run with seed data (12 employees with Arabic names, 494 punches over 30 days) captured by مخطط التسويق on 2026-09-11 — no customer data. (tech-planner.md «التشغيل والتصوير»)

<!-- ~420 words · Sources: brief.en.md · tech.md · tech-planner.md · links.md -->
