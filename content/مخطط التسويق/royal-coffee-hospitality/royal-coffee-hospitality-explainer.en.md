royal-coffee-hospitality | مخطط التسويق | 2026-09-23 | draft (for editor seal)

# Royal Coffee — a luxury Saudi hospitality site rendered at the edge with no framework

## Executive summary (5 points)
1. A complete rebuild of a Saudi coffee-service and hospitality website (originally 15 repetitive pages on GitHub Pages) with a luxury Onyx + Gold identity and native RTL, aimed at an audience that is 95% mobile.
2. Architecture: Hono and TypeScript with hono/jsx rendered on Cloudflare Workers (edge SSR), with no React, no Tailwind and not a single runtime library; the same code also builds for Vercel Edge.
3. One data layer (`src/data.ts` + `src/cities.ts`) generates 73 pages: 8 services, 6 occasions, a menu of 8 categories and 71 items, a price guide, FAQs, and 10 cities with service×city combination pages for local search.
4. Numbers: 179.65 KB worker (52.59 KB gzip), 17.7 KB CSS and 4.8 KB JS gzipped, a 23 KB mobile hero, 49 hand-drawn SVG icons, 13 JSON-LD builders, zero horizontal overflow across 32 captures.
5. Status: complete and running locally; not deployed, contact details are placeholders — live link to be confirmed.

## The problem
Saudi coffee-server (qahwaji) and hospitality sites are usually built on heavy WordPress templates or site builders, with duplicated per-city pages carrying the same text, full-size images and a weak mobile experience — while the customer searching for "qahwajiin Riyadh" opens the site on a phone days before the event and decides in seconds. Royal Coffee's original site was 15 pages on GitHub Pages with no unified identity and no structured data.

## How it works
The site renders at the edge: every request reaches a Cloudflare Worker running Hono — a lightweight framework built on Web Standards — which generates full HTML from hono/jsx components and returns it directly. No always-on application server, no database, no state.

All content lives in two files: `src/data.ts` (brand, services, occasions, menu, prices, FAQs, gallery) and `src/cities.ts` (10 cities with local copy). From them, `views.tsx` composes the pages, `layout.tsx` wraps them in an RTL shell with full SEO, and `index.tsx` maps them onto 18 routes producing 73 URLs in sitemap.xml, plus robots and a designed 404.

The identity is built without any CSS framework: one file of variables, the Amiri and Tajawal typefaces (the only external request), and 49 hand-drawn SVG icons — no icon fonts, no emoji. On mobile, a bottom-sheet menu and a bottom navigation bar with a gold WhatsApp circle; the booking form turns the request into a formatted WhatsApp message straight from the browser. For search: 13 JSON-LD builders (LocalBusiness, FAQPage, Service, Menu, BreadcrumbList…) wired to every page, and titles capped at 70 characters by a `fitTitle()` routine.

## Who it is for
Hospitality, coffee-service and events businesses that want a site as refined as the service and instant on mobile, and any multi-city local business that needs a page per city managed from one file.

## What sets it apart
Luxury without weight: a cinematic Onyx + Gold design (image cross-fade, Ken Burns, a gold light sweep — all on `transform` and `opacity` only) with a 52.6 KB gzipped worker and zero runtime libraries. And genuine RTL — `inset-inline` properties, Arabic-Indic numerals, phone-number direction isolation — not a translation layered over an English template.

## Current status and what remains
The build succeeds and the site runs locally (checked 2026-09-23). Not deployed to Cloudflare Pages; contact and social details are placeholders in `src/data.ts`. The README accumulates five rounds with successive figures; the numbers here come from the current code and build. In-site hero figures (6,500+ events, ratings) are marketing content, not metrics. To be completed: deployment and domain, real contact data, an English version, customer reviews.

<!-- Sources: README moain2028/royal-coffee-hospitality · tech.md (2026-09-23) · src/data.ts · src/cities.ts · src/index.tsx · src/icons.tsx · src/ld.ts · npm run build. ≈ 480 words. -->
