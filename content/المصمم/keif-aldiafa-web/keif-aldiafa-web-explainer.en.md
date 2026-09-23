keif-aldiafa-web | المصمم | 2026-09-23 | draft — to be sealed by the editor

# Keif Al-Diafa — Project Explainer

## Executive summary (5 points)
1. A marketing website for Keif Al-Diafa, a Jeddah hospitality business (Arabic coffee servers and event hosts), live at keifaldiafa.com and built with Next.js 14, TypeScript and Tailwind CSS on Vercel.
2. One goal governs every element: the WhatsApp or call button — no cart, no prices, no accounts — because 95% of customers arrive on mobile and give a page five seconds.
3. 24 service-by-city pages (3 services × 8 cities) statically generated from a single component; adding a city is one line in a data file.
4. Measured, not estimated: watermarks on 15 images after 5 iterations, a QR code machine-verified down to 180px with pyzbar, a clean type-checked build, and 11 docs explaining every decision and the alternatives it beat.
5. Status: production; openly unresolved: mobile home performance (Lighthouse 0.53 · LCP 9.4 s) is being fixed, and social-account handles must be confirmed before the QR code is promoted.

## The problem
A Saudi hospitality customer arrives from Google on their phone, scans rather than reads, decides in seconds, and wants to talk, not browse. Conventional sites distract them with packages, prices and carts — while in this sector the price is settled in the conversation anyway. Before this project there was a trail of experimental versions (around 50 repos named Keif Al-Diafa) with no single standard for what "working" meant.

## How it works (the architecture in plain words)
The site is Next.js 14 with the App Router, exported statically at build time. Services and cities live in one data file (`localPages.ts`); one dynamic route (`[serviceCity]`) with `generateStaticParams()` produces the 24 pages through a shared `LocalServicePage` component, with copy and imagery mapped in sibling files. The `/social` page shows a QR code that was machine-tested down to 180px after testing revealed the image optimizer was breaking it. Images (430 webp/avif files) carry an engraved watermark; Schema structured data, sitemap, image sitemap and robots are in place. Measurement tools (Pillow/pyzbar/playwright) live in `research/`, decisions in `docs/`.

## Who it's for
Hospitality and event businesses — and any service sold through a conversation — that want a site producing messages rather than visits.

## What makes it different
Discipline: every element is tested against one question ("does it bring the visitor closer to the contact button?"), every assumption is measured with a tool rather than by eye, and the red numbers sit in the README next to the green ones.

## Current status and what's next
Live at keifaldiafa.com (HTTP 200 on 2026-09-11), 8 commits, the last on 2026-08-21. Next: mobile home performance, confirming social handles with the owner, an approved demo video, and settling which copy (moain2026 vs MoTechSys) is canonical before promoting the link.

<!-- Sources: brief.en.md · case-study.en.md · tech.md · links.md (portfolio-hub, sealed 2026-09-11). -->
