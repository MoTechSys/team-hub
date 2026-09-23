sayed-aldiafa | المصمم | 2026-09-23 | draft

# Sayed Al-Diafa — an events website that sells on WhatsApp, with no framework and no build

## Executive summary
1. A fully RTL Arabic website for an event and hospitality contractor in Riyadh and its governorates, built in plain HTML, CSS and JavaScript: zero dependencies, zero build step.
2. 15 static pages: home, services, packages, booking, gallery, coverage, plus 9 standalone service pages.
3. The booking form needs no server: JavaScript turns 8 fields into a pre-filled WhatsApp message opened through wa.me.
4. JSON-LD structured data (LocalBusiness · 18 Service · 18 Offer · BreadcrumbList), Open Graph and canonical on every page, WebP images with JPEG fallback.
5. Status: pre-launch prototype — no confirmed live URL, and all site imagery is AI-generated per the README; prices and business figures are "to be completed".

## The problem
A small event contractor needs a site that presents its services (wedding stages, seating, tents, chairs and tables, cooling, AV, coffee servers, coordination) and takes a visitor — usually on a phone — to a quote request in as few taps as possible. It must not depend on Node, special hosting or a build pipeline.

## How it works
The site is HTML files uploaded as-is to any file server: shared hosting, S3 or GitHub Pages. The home page inlines its CSS in a `<style>` block (≈24 KB) to remove a render-blocking request on first load, while the other 14 pages share one cached `sv.css` (≈10 KB).

A serverless booking flow: `booking.html` and the home page carry an 8-field form (name, phone, date, event type, city, guests, package, notes). On submit, JavaScript prevents the default post, validates missing fields and announces them via `aria-live`, then builds the message text and opens `wa.me` with it ready to send. No database, no email, no endpoint.

The layout is mobile-first with a 480px maximum width — on desktop the same column appears centred (full responsive layout lives in a separate Next.js version, per the README). Navigation is a fixed bottom tab bar plus a side drawer. Fonts are Amiri and Almarai from Google Fonts — the only external dependency.

## Who it's for
Small service businesses that sell through WhatsApp and want a fast site anyone who knows HTML can edit.

## What sets it apart
- Zero dependencies: no `node_modules`, no build (no package.json in the tree).
- Full SEO plumbing: 27 JSON-LD blocks, 7 Open Graph tags and a canonical per page, sitemap, robots, manifest.
- Documented accessibility: no `maximum-scale` (WCAG 1.4.4), 56/56 images with Arabic alt text, touch targets ≥ 44px, `prefers-reduced-motion`.
- Explicit content rules in the README: no invented statistics, no numeric prices ("price depends on the event"), no partner logos.

## Current status and what remains
Last commit 2026-08-09 (5 commits). The README is stale: it names a different service region while all code targets Riyadh and its governorates, and lists 13 pages and 8 services where the tree has 15 and 9 (details in research.md). It also lists what remains: real event photos, package prices, founding year and event count, client logos with consent, and the final domain. No automated tests; the "quality gates" are manual grep commands.

Source: repository README and page code; figures in tech.md.
