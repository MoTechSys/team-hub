ads-agency-platform | المصمم | 2026-09-23 | draft — to be sealed by the editor

# Ads Agency Platform — Project Explainer

## Executive summary (5 points)
1. A multi-tenant SaaS that manages many clients' Google Ads campaigns from one dashboard, with a live Google Ads API integration (google-ads-api v24).
2. AI recommends, humans execute: every recommendation must carry numeric evidence (evidence JSON) and nothing runs without explicit human approval through PENDING → APPROVED → APPLIED.
3. Secure from day one: 12 Prisma tables, 17/17 tenant-isolation tests passing, AES-256-GCM credential encryption with 20/20 tests passing, and an AuditLog on every action.
4. Built for the Saudi market: Arabic RTL UI in IBM Plex Sans Arabic, 15% VAT invoicing, and a legal delegation consent record (consentAt/consentIp).
5. Status: phases 1 and 2 complete with evidence (API integration + dashboard, then security + AI layer + PWA); the repo is private and shown as a case study; a public live URL is still to come.

## The problem
An agency running Google Ads for several clients logs into each account separately, with no unified dashboard, no audit trail, and no evidence-based recommendation flow. Worse, automated "optimizers" can change bids nobody approved — and the client bears the cost of a decision they never saw.

## How it works (the architecture in plain words)
Each client is an isolated Organization inside PostgreSQL 16 via Prisma 6. Every day the platform pulls a MetricSnapshot from the Google Ads API for each connected account and shows it in an Arabic RTL Next.js dashboard. An AI layer with five providers reads those snapshots and drafts recommendations — but a recommendation without numeric evidence is never shown. Once a human approves it, it becomes a ChangeRequest that moves from PENDING to APPROVED to APPLIED, and every step is written to the audit log: who, what, when. Credentials are AES-256-GCM encrypted and kept out of the database; long jobs run through BullMQ + Redis queues. The app is a PWA with offline support for static pages, deployed with pm2 behind Caddy.

## Who it's for
Marketing agencies and in-house teams running several ad accounts who need one view, control over who changes what, and a human final say.

## What makes it different
Three things that rarely come together: multi-tenancy with documented isolation tests, evidence-mandatory AI recommendations, and mandatory human approval with a full audit trail — all in a native Arabic interface.

## Current status and what's next
Phase 1 (API integration + dashboard) and Phase 2 (security + AI layer + PWA) are complete per the README, and the build passes (`npm run build` ✓). Last activity 2026-08-11. Still to come: the number of clients/accounts actually managed, a public live URL (current deployment is local behind Caddy), and an approved demo video.

<!-- Sources: brief.en.md (sealed 2026-09-11) · tech.md (researcher, complete) · links.md. Nothing from outside them. -->
