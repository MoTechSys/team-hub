dallat-alkaif-static | المحرر | 2026-09-23 | sealed-by-editor

# Dallat Al-Kaif, static edition — Explainer

## Executive summary
1. A luxury hospitality site for southern Saudi Arabia: 13 Arabic RTL pages in plain HTML, CSS, and JavaScript — no framework, no build step, 0 dependencies.
2. It is the static twin of the newer Next.js version, kept on purpose because it runs without Node on any host: shared hosting, S3, GitHub Pages.
3. Measured on the same machine: the home page is 8 requests and 558 KB versus 47 requests and 1.5 MB in the twin; framework JavaScript 0 versus about 494 KB.
4. The price is stated plainly in the README: hand-duplicated navigation and footer, no components, no type checking, a mobile layout capped at 480px.
5. All imagery is AI-generated per the repository, and there is no live URL at present.

## The problem
A small brochure site needs no server and no database, yet building it with a modern framework drags in hundreds of kilobytes of JavaScript, a dependency folder with hundreds of packages to keep updated, and a build pipeline that must succeed before every deploy. For a small-business owner on shared hosting that is a cost with no return.

## How it works
Thirteen HTML files in the repository root, one shared stylesheet, and an image folder. The home page carries its own styles so the browser never waits on a blocking request; the other twelve pages share one file that is cached once. All the JavaScript is 82 lines across two pages: the FAQ accordion, and an eight-field booking form that validates input and then opens a ready WhatsApp message. Navigation is a fixed bottom tab bar, and each of the eight service pages has an intro, numbered benefits, spec cards, FAQs, and links to related services. Open Graph is set on all 13 pages so sharing shows a preview, and there is no zoom lock, in line with the accessibility standard.

## Who it is for
A small-business owner who wants a site that uploads as-is and runs on the cheapest hosting with no technical upkeep. And a developer deciding when a framework earns its cost — this repository offers the live comparison: the same brand and content in two builds.

## What sets it apart
Measurement instead of opinion. The Next.js version was actually built and both twins were measured on the same machine with caching off at a mobile viewport: the coffee page is 3 requests and 70 KB versus 30 requests and 907 KB; the booking page 4 and 87 KB versus 27 and 799 KB. In fairness, the Next.js twin prefetches linked pages so later navigation is instant, and it self-hosts its fonts while the static version requests them from Google Fonts. The README itself writes the honest verdict: for thirteen static pages this is a sound choice; if pages multiply or dynamic content arrives, the other version is the right path. It also enforces strict content rules: no out-of-region cities, no invented statistics, no numeric prices, no partner logos.

## Status and what remains
Complete as a static site: the README's four quality gates are green and we re-ran them (0 height attributes on images, 0 out-of-scope cities, one unified number, balanced tags), and 20 local screenshots showed no console errors and no horizontal scroll. Remaining: real event photos instead of generated ones, the final domain to update Open Graph, self-hosted fonts instead of Google Fonts, removal of two unused images (1.22 MB), and a favicon. No live URL, and a single commit dated 2026-08-07.
