linkhub-3d | صانع الصور | 2026-09-23 | draft-for-editor

# LinkHub 3D — Project Explainer

## Executive summary
1. A link-in-bio pattern with real 3D cards and a physical material, built in plain HTML, CSS and JavaScript in a single file per brand — no framework, no build, and zero external requests measured in the browser. Applied to two hospitality brands. (README, linkhub-audit.json)
2. Interaction: tapping a card flips it with `rotateY(180deg)` under `perspective` and `preserve-3d` — measured as `matrix3d(-1,…,-1,…)` at 180° — an SVG ring completes in 900 ms, and the whole page recolours to the platform's identity (body background from `rgb(10,8,7)` to `rgb(21,2,7)` for Instagram) before navigating; a second tap or Escape cancels. (README "Interaction", audit)
3. Material: geometric thickness `translateZ(±3.5px)`, a specular highlight following the pointer with no rAF loop, `feTurbulence` grain, a recessed icon well, ±4° tilt — 15 `backgroundImage` layers and 5 `boxShadow` layers on a card face. (README "Material", audit)
4. Measured: 8.4 KB gzipped for the whole page (keif) and 8.0 (asoul), one screen with no scroll (844 = 844), smallest tap target 68/78 px, smallest font 14 px, and every contrast pair passing WCAG (lowest 4.64:1) via the measurement scripts inside the repo. (tech.md)
5. Accessibility and resilience: every card is a real `<a href>` that works without JavaScript (8/8 and 6/6), `:focus-visible`, `aria-live`, and `prefers-reduced-motion` disables motion and navigates immediately. Status: deploy-ready files, but both live URLs are down and the README itself calls the domain "temporary". (README "Principles", links.md)

## The problem
Commercial link-in-bio pages — Linktree and its kind — are flat, uniform lists hosted on the vendor's domain, loading its scripts and analytics, treating Arabic as a translation inside an English template. A luxury hospitality brand wanted a page with the feel of the majlis bench: a card that looks like a real object, flips in space and dyes the page in the platform's colour before taking you there — all in one file it owns. (docs/00-INDEX, research)

## How it works
Each page is one HTML file with inline CSS and JS. Links come from `docs/data.json` and are embedded literally in the HTML so everything works without JavaScript; `verify_hrefs.py` cross-checks them. On click the script prevents default navigation, adds the flip class, sets `data-theme` on `<html>` (keif) or the theme's CSS variables on the root (asoul), and starts a 1.5 s timer (550 ms flip + 900 ms ring) before opening the link. The ring is an SVG circle animated via `stroke-dashoffset` from 339.3 to 0. Themes cover 11 platforms in data.json; two colours were corrected after failing contrast (`phone` 1.09:1, `snapchat` 1.27:1), documented in docs/02. Images are local `<picture>` AVIF/WebP/JPG at three sizes, fonts are local Amiri and Kufi woff2, icons are hand-drawn SVG `<symbol>`s. (index.html, docs/02, README)

## Who it is for
Owners of small premium brands — hospitality, restaurants, studios — who put one link in their bio and want the visitor to feel the product from the first tap, without a monthly subscription or a third-party script on their page. (brief.en)

## What sets it apart
The difference is not "prettier design" but a change in the nature of the element: the card is an object with thickness, highlight and compound shadow, the flip is real in space rather than a scale/opacity fake, and the whole page reacts to the platform. All of it in 8.4 KB with not a single external request — lighter than one icon on most commercial link pages. Honesty is method: every number in the README is a command output or browser measurement, and I re-measured all of them here and they matched. (tech.md)

## Current state and what remains
Both live URLs are down, so there is no live link, and canonical/og/JSON-LD in both pages still point to them. No analytics or click tracking; editing is manual across two files. A single commit. Phone numbers and social handles are literal in the code — the numbers are masked in every screenshot and video here, and the project is presented as a technical pattern rather than the brands' page. docs/03 references tokens and private repos that need cleaning before the repo is shown publicly. Lighthouse was unavailable and replaced by a documented Playwright audit. (tech.md "Cleanup notes")

<!-- ≈600 words. Sources: tech.md, README, docs/02, index.html, linkhub-audit.json. No person name, no phone number, no social handle. -->
