hafawa-events-app | صانع العروض | 2026-09-23 | draft

# Hafawa Events — Progressive Web App: Explainer

## Executive summary
1. A single-screen, vertical progressive web app for a Riyadh hospitality and events company; installs on the phone from the browser with no app store.
2. Built in plain HTML/CSS/JS with no framework and no build step; the three code files gzip to 28.4 KB, first paint in 324 ms on a local mobile run.
3. Genuinely works offline: the Service Worker caches 22 files and any uncached path falls back to a dedicated offline page (tested).
4. Measured content: 6 services, a 6-item gallery, 4 steps, 4 FAQs, 12 districts, 41 links; smallest font 12px, 0 console errors.
5. Status: prototype (7 commits on 2026-08-09), no confirmed live URL, a README copied from another project and a layout bug on large screens — all documented in tech.md.

## The problem
The brand's website (hafawa-riyadh-events) serves search and desktop browsing. A hospitality customer wants something on the home screen they open and request a quote from in one tap — no browsing, no store download, no updates. Small business owners, for their part, do not want a monthly subscription to an app-builder platform.

## How it works (in plain language)
`index.html` is one page, shown inside a phone frame on large screens and full-screen on mobile. A full-screen hero with "Book your hospitality" and "See our work" buttons, then a "signature" section (coffee roasted in front of the guests), 6 service tiles, a 6-item gallery that opens each work in a lightbox, a 4-step "how we work", 4 FAQs, 12 Riyadh districts, and a "Request a quote" card with WhatsApp and call buttons. A fixed bottom tab bar, a floating WhatsApp button and a side drawer handle navigation.

`manifest.webmanifest` makes the app installable (standalone, 3 icons, 2 shortcuts: "Quote" and "Coffee service"), and an install bar appears on `beforeinstallprompt`. `sw.js` (46 lines) precaches the shell, serves images cache-first with background refresh, fetches pages network-first with cache fallback, then `offline.html`. Images are served through 50 `<picture>` elements as AVIF → WebP → JPG at three widths (400/800/1200).

## Who it is for
Small hospitality and events businesses that want an "app" with no store and no subscription, and any service business that needs a booking page living on the home screen.

## What sets it apart
Zero dependencies and zero subscription versus no-code alternatives starting at $25–29/month (see research.md); measured, not estimated, lightness; real offline behaviour; native RTL with 43 aria attributes and 7 `prefers-reduced-motion` blocks; and an `audit/` folder with a candid independent audit that caught the developer's own claims.

## Status and what remains
A prototype that stopped on 2026-08-09. Remaining: fix the README, fix the marquee overflow on viewports >520px, self-host fonts instead of CDN, replace the AI-generated gallery with real event photos, move the phone number and email out of code into config, a real request form with fields, tests, CI, a license and a live URL.

*Disclosure: the six gallery images in `assets/gen` are AI-generated; the phone number and legal entity name are masked in every screenshot.*
