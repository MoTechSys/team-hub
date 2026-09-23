nexus-notify | الباحث | 2026-09-23 | draft-for-editor

# Nexus Notify — project explainer

## Executive summary (5 points)
1. A central, multi-tenant, multi-channel notification and conversation platform that integrates with any external system through one API and keeps customers, conversations, and the device fleet as a single source of truth. (README)
2. Three components in one monorepo: a NestJS backend with PostgreSQL 17, Prisma, Redis/BullMQ, and Swagger; a 7-page Angular 22 RTL dashboard; and a Kotlin Android app that turns dual-SIM phones into an SMS gateway. (README · tech.md)
3. Security and reliability are designed in: three-way auth (X-API-Key for systems, Device-Token for phones, JWT for users), an idempotency key per request, tenant isolation with tenant_id on every table, and an outbox with retries and failover to another device in the group. (ARCHITECTURE.md §5–6)
4. A tested core: 163 backend tests, 12/12 end-to-end, 11 Android tests, 85% coverage, green CI on the latest commit. (docs/PROJECT_STATUS.md)
5. Status: phases 0–3 complete (backend + dashboard + Android APK); phase 4 (WhatsApp/agent) partial — live-chat WebSocket done. No documented production deployment or real usage numbers yet. (PROJECT_STATUS.md · tech.md)

## The problem
Every internal system — billing, collections, ERP — sends its own messages from scattered phones and SIMs, so customer data, conversations, and the device fleet end up in five places with no unified log, no status tracking, and duplicate numbers depending on format. (brief.en.md · tech.md)

## How it works (architecture in plain language)
A tenant system (say, the electricity or store system) posts a notification to one API with an X-API-Key that identifies the tenant and an idempotency key that prevents duplicates on retry. The platform normalizes the phone number to E.164, creates or updates the contact and conversation, and queues the message in Redis/BullMQ. From there it is routed by carrier prefix (70/71/73/77/78 in Yemen) to a paired Android device in the branch group; the app sends it over the matching SIM, captures the inbound reply, and posts it back, so the full conversation appears in the dashboard and streams live over WebSocket. If a device fails, the job retries with exponential backoff or fails over to another device in the group. (ARCHITECTURE.md §1, §5–6 · PROJECT_STATUS.md #2–3)

## Components
- Backend: NestJS 11 · Prisma 6.2 · 21 tables · Swagger · Zod env · Pino · Throttler · Socket.IO on /realtime · argon2. (tech.md)
- Dashboard: Angular 22 with Signals; 7 pages: login, dashboard, devices, conversations, notifications, routing rules, settings. (tech.md · apps/dashboard tree)
- Mobile: Kotlin + Jetpack Compose · Room · Foreground Service · dual SIM · a ContentObserver that captures manually sent SMS. (tech.md · PROJECT_STATUS.md #8)
- Ops: Docker Compose with four services (postgres + redis + backend + dashboard/nginx) with automatic migrate and seed. (PROJECT_STATUS.md)

## Who it's for
Companies with several systems that must reach customers from one place. (brief.en.md)

## What sets it apart
- A live field test on a real device (Samsung SM-N976V on a Yemen Mobile SIM) produced 14 findings, all fixed with root-cause analysis documented down to file and line. (docs/PROJECT_STATUS.md · FIELD-TESTING-FIXES.md)
- An expert security review fixed a critical issue (a production seed with a default password) and added requireInProd. (PROJECT_STATUS.md)
- Living documentation: ADRs, CHANGELOG, RUNBOOK, and a Yemen carriers reference. (README)

## Current status and what remains
- Latest commit 2026-07-23 (50 commits in 3 days). (git log)
- WhatsApp/agent (phase 4): deferred. (README)
- Production message and device counts: to be completed. Live URL: none (internal system). (tech.md · links.md)
- Full country table for international number normalization: future improvement. (PROJECT_STATUS.md #10)
- The README lists default development credentials — never to be carried into marketing copy. (tech.md)
