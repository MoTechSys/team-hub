sardah-store | صانع الفيديو | 2026-09-23 | draft — for editor seal

# Sardah Abayas — Project Explainer

## Executive summary
1. A fully RTL Arabic promotional site for a Saudi abaya brand: it shows the collection and turns every call to action into a WhatsApp message — no cart, no checkout (a deliberate architectural decision in phase 5).
2. Built with Next.js, React 19, TypeScript, Tailwind, and Framer Motion; every page is statically generated at build time (SSG).
3. 20 pieces with a page each, categories, a size guide, a gallery, and 6 verbatim customer reviews; a warm champagne-nude identity set in Aref Ruqaa and IBM Plex Sans Arabic.
4. Status: "feature-complete" per README, 19 commits in one day (2026-04-27/28), no automated tests, and a placeholder WhatsApp number in code.
5. To be confirmed: whether sardah.com actually hosts this code, a real WhatsApp number, and real product photography (current images are AI-generated per README).

## The problem
Small abaya shops get pushed into carts and online checkout they don't need, while their customers buy by conversation: they ask about fabric, cut, and size, then order. The result is either a full commerce platform with its complexity and fees, or an Instagram account with no storefront worthy of the product.

## How it works
The site is promotional, not transactional. A cinematic homepage presents the collection; category and product pages are generated statically from a single data source (`src/lib/products.ts`); there is a gallery and a size guide. On a product page the customer picks cut and size, and every "order" button builds a pre-filled WhatsApp link carrying the piece details (`buildWhatsAppUrl` in `utils.ts`), moving the conversation to where the sale actually happens. There is no order server, no database, no payment gateway. Images are optimised through next/image and Sharp (WebP/AVIF), motion runs on Framer Motion and respects `prefers-reduced-motion`, and a PWA manifest allows installing on a phone.

## Who it's for
Fashion and abaya boutique owners who sell by chat and want a storefront worthy of the product — without committing to a commerce platform, subscription fees, or commissions.

## What sets it apart
- "No cart" is an explicit, documented decision, not a gap: the whole path is designed to end in WhatsApp.
- Arabic-first, fully RTL, with a bespoke visual identity rather than a generic template.
- 33 fast static pages that can be hosted on any CDN at near-zero running cost.
- Code and data belong to the brand: no platform lock-in and no commission on sales.

## Current status and open items
- Feature-complete per README (phases 0→7.1); last change 2026-04-28.
- No automated tests; Zustand is configured but unused; no Service Worker (manifest only).
- WhatsApp number is a placeholder — `NEXT_PUBLIC_WHATSAPP` must be set before launch.
- Abaya images are AI-generated per README; to be replaced with real photography at launch.
- sardah.com currently runs on the Salla platform (checked 2026-09-23), not this code — the relationship is to be confirmed.

<!-- Sources: brief.en.md (Problem/Solution/Result/Who), tech.md (stack, status, numbers, warnings), repo README moain2026/sardah.com, curl check of sardah.com 2026-09-23 (HTML loads cdn.assets.salla.network). -->
