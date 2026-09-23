espreso | صانع الفيديو | 2026-09-23 | draft

# Espresso Coffee — A Luxury Site for a Local Roaster · Project Explainer

## Executive summary
1. A multi-page static site for a specialty coffee shop with three branches in Al Hudaydah whose only online presence was an Instagram account.
2. No UI framework and zero runtime dependencies: plain HTML/CSS/JS built by Vite, runs on any static host.
3. 6 pages in Arabic and English from one dictionary, a 15-drink menu, an 18-photo gallery with lightbox, and an installable PWA.
4. A Sharp image pipeline emits 139 AVIF and 139 WebP files at graded sizes with an LQIP preview per image.
5. Status: builds and runs locally with zero errors, but no README, no confirmed live URL, and 8 stock photos without documented provenance.

## The problem
A specialty coffee shop branded "where the mood is brewed" runs three branches in Al Hudaydah, yet everything a visitor finds online is an Instagram account: no browsable menu, no branch addresses and hours, no brand story, no fixed contact button. The goal was a luxury site worthy of the identity that works phone-first.

## How it works
The site is seven HTML files at the root (six pages plus a 404) that Vite builds as multiple entries. Shared parts — header, footer, logo — are merged at build time through a custom partials plugin driven by an `@include` comment, so there is no runtime cost. Language comes from `?lang=` or localStorage and swaps text from a single dictionary along with the RTL/LTR direction.

Content lives in one data file: 15 drinks in four categories (espresso, signature, iced, tea) with instant filtering, three branches with their roles, and 18 items in the "ambience" gallery using the account's real photos with a lightbox. Images go through Sharp: from each source, AVIF, WebP and JPG variants are generated at 400 to 1024 px, and dimensions, dominant colour and a compressed LQIP preview are recorded in a JSON file the site reads for lazy loading without layout jumps. The motion layer uses IntersectionObserver and respects reduced-motion preferences.

The four typefaces are self-hosted as 24 woff2 files, and the site is a PWA with a manifest, icons and shortcuts to the menu and branches, plus JSON-LD, a sitemap, hreflang and security headers in a `_headers` file for Cloudflare Pages. Build output: 69.5 KB JS and 62.1 KB CSS before compression, and zero console errors across 18 page×language runs locally.

## Who it is for
Café and small food-business owners who want a luxury site without a site-builder subscription or a server, deployable to free static hosting and updated from simple data files.

## What makes it different
Luxury without weight: no framework and no animation library; the whole identity sits in CSS variables and local fonts. The photos are real — from the brand's account and a shoot of the park kiosk — not generated product imagery. And bilingualism is built into the dictionary, not into two copies of the site.

## Current status and what remains
No README in the repository, and the only branch on GitHub is genspark_ai_developer. No confirmed live URL: the sitemap points to a Cloudflare Pages domain that does not respond. No automated tests, only a visual QA tool. Eight stock photos (beans, cappuccino, latte…) have no licence file or source and need documenting or replacing before launch. The Instagram figures on the home page (followers/posts) are static as of 2026-09-18 and need refreshing or a live hook.
