alabbasi-tech-platform | متخصص SEO | 2026-09-23 | v2 · project explainer (English) — every sentence from README / tech.md / docs

# Alabbasi Tech — project explainer

## Executive summary (5 points)
1. A fully static Next.js 15 official site (19 Arabic RTL pages, zero images) and a separate Express + SQLite client portal, for a software engineering house in Sana'a.
2. The positioning written in the repo: "We replace closed systems with software you own — code and data belong to the client."
3. Portal: projects, tickets with attachments, inbound requests, three roles with 11 permission codes; httpOnly JWT, CSRF guard, bcrypt, throttling, RFC 9457 errors.
4. Measured quality: 19/19 pages build, zero TypeScript errors, 11 tests, and a pixel audit across 14 pages × two widths with zero horizontal overflow and zero text overlap.
5. Status: code is ready and runs locally, but there is no live URL today — the alabbasi.tech domain is unregistered and the temporary deployment is down.

## The problem
A Sana'a software house needs a site that loads on cheap Android over weak networks (every byte cacheable at the edge), shows numbers verified by git commands rather than claims, and takes client requests and tickets without turning the marketing site into a server-backed app.

## How it works (the architecture in plain words)
The site is built with Next.js 15.5 and React 19 using static export: it is built once into HTML, CSS, and JS files served from any host or CDN. It has no images; icons are inline SVG, styling is plain CSS with `@layer` and logical properties only, light comes from the top-left so shadows are not mirrored in RTL, and shadow opacity stays at or above 0.26 to survive a cheap screen in sunlight. Every page carries `dir="rtl"`, a single h1, JSON-LD, and Open Graph.

The portal is a separate decision (ADR-P001): client-side pages under `/portal/` call an independent Express API that Caddy exposes at `/api/*`. The database is SQLite in WAL mode with numbered migrations. Each module has four layers: domain → application → infrastructure → presentation. Security: JWT HS256 in httpOnly cookies (refresh token scoped to `/api/auth`), CSRF via SameSite=Strict plus a Sec-Fetch-Site check, bcrypt cost 12, five login attempts per 15 minutes, constant-time comparison, and RFC 9457 problem details. Ticket attachments are checked by magic bytes, not extension. Notifications go through an outbox drained to Telegram every 15 minutes, so a failed notification never fails a client request.

## Who it is for
Companies that want a site and client portal whose code and data they own, not a closed subscription.

## What sets it apart
Measured honesty: a pixel audit measures every element from rendered pixels, fixed four flaws in its own tool before accepting any number, and logged 151 contrast defects whose root causes were then fixed. The content excludes a large project because including it would be "inflation above 1300%".

## Current status and what remains
Runs fully locally (built and tested on 2026-09-23). No live URL; the commercial registration is "in progress". To be completed: domain registration and deployment, automated portal tests, re-measuring contrast after the fixes, and removing a local path from the portal audit report.

<!-- Sources: root README (structure, security, roles, design system, quality gates, resolved bugs, content rule); site/README (stack, positioning); portal/README (ADR-P001, SQLite WAL, layers); portal/CHANGELOG (outbox/Telegram); docs/pixel-audit-site.md §1–2; tech.md (local verification). ~500 words. -->
