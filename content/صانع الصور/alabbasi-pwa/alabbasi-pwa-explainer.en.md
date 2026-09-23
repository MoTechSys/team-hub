alabbasi-pwa | صانع الصور | 2026-09-23 | draft-for-editor

# Alabbasi PWA — Project Explainer

## Executive summary
1. A company profile page for a digital-services firm (website recycling · ad campaigns · automation · AI) built as a progressive web app in plain HTML, CSS and JavaScript — no framework, no build step, no npm dependencies, no JS CDN. (README "Specs", tech.md)
2. Genuinely offline: a Service Worker precaches 7 core files, serves pages network-first with cache then offline.html fallback, and assets/fonts stale-while-revalidate. Reloading the home page offline returned 200 from the SW in a real test. (sw.js, pwa-audit.json)
3. Installable as a standalone mobile app: manifest with `display: standalone`, `dir: rtl`, 3 icons (192/512/maskable) and 3 shortcuts, plus a custom install banner on `beforeinstallprompt`. (manifest.webmanifest, js/app.js)
4. Very light: ~18.6 KB of text assets gzipped, only 19 files in the repo, 744 lines of authored code, 0 console errors. (tech.md)
5. Status prototype/beta: one complete page, but the contact form is not wired to a backend, inner pages are pending, and the live URL in the README does not respond. (docs/00-INDEX.md, links.md)

## The problem
Company landing pages are usually built on heavy frameworks with hundreds of dependencies, or on site builders; they break on weak networks, cannot be installed, and treat Arabic as a second-class language — left-to-right layouts, Latin digits, and emoji standing in for icons on servers without an emoji font. The firm wanted a page that opens like an app, survives poor connectivity and respects Arabic fully, with the smallest possible dependency surface. (README "Specs", "Icons")

## How it works
One page, seven sections: a hero with a rotating six-node orbit, 4 services, website recycling in 4 steps, 6 AI solutions, a 5-stage process, 3 case cards, and a 6-field contact form validated live by 6 rules. All content is data in `js/app.js` rendered into the DOM on load, so there is no duplicated HTML. `dir="rtl" lang="ar"` sits on the root, and every counter is displayed in Eastern Arabic numerals through a single conversion helper. 18 inline SVG icons in `js/icons.js` share one gradient and replace emoji. The "aurora" design system uses 18 CSS variables, 5 keyframes, 3 breakpoints and `prefers-reduced-motion`. A single `sw.js` implements the three caching strategies; its `V` constant must be bumped on every asset change (the README documents the v1→v2 incident when it was forgotten). (index.html, js/app.js, js/icons.js, css/main.css, sw.js)

## Who it is for
Company and organisation owners who want a fast digital presence that opens like an app and works on weak networks — especially in markets with uneven connectivity — without a complexity tax or a platform subscription. (brief.en "Who it helps")

## What sets it apart
Zero dependencies and no build means deployment is a file copy and there is no software supply chain to watch. Offline is measured, not promised: home from the SW, unknown routes to offline.html. Arabic RTL first, from the root element to digits to icons. And ~18.6 KB gzipped for all text — lighter than a single image on most sites. (tech.md)

## Current state and what remains
The hero counters (84+ projects, 3.4× growth, 97/100 performance) and the "Our work" figures are demo data hard-coded without a source — they are not achievement numbers and were not used in any design in this pack. The form simulates submission locally and reaches no server. The live link does not respond, so there is no live URL. Lighthouse was unavailable in the test environment and was replaced by a documented Playwright audit (`pwa-audit.json`). The README says 19 icons; the code has 18. (tech.md "Cleanup notes")

<!-- ≈560 words. Sources: tech.md, README, sw.js, manifest, pwa-audit.json. No person name, no phone number. -->
