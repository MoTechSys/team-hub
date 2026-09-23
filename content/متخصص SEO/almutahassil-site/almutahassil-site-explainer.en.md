almutahassil-site | متخصص SEO | 2026-09-23 | draft — to be sealed by المحرر

# Al-Mutahassil — How a marketing site and demo dashboard were built with no framework and no build step

A multi-branch collection fund wanted to present its «Al-Mutahassil» system — field collection with instant settlement to a central treasury — to similar organizations. A text description is not enough for a financial product; the buyer wants to see the dashboard before calling. So the brief was a premium Arabic site that explains, and a dashboard that shows.

**What was built.** Eight hand-written HTML pages: a home page with seven sections (hero, modules, a four-step "how it works", the app, security, plans, call to action), a demo admin dashboard, a modules page detailing nine modules with a sticky index, a 12-item FAQ with accordion and live search, an "about" page with a four-milestone timeline, a demo-request form with six validated fields, a five-release changelog, and a 404. Everything is RTL from the root, with Eastern Arabic numerals in every counter, set in IBM Plex Sans Arabic.

**How it works.** No framework, no build step, no external library: a `grep` over the scripts returns exactly two local files. `style.css` (22.8 KB, 14 custom properties) carries the whole design system — deep navy and graded gold. `app.js` drives reveal animations, counters, the mobile menu and form validation. `demo.js` builds the dashboard from static data: four KPI cards with counters, an SVG bar chart, and two sortable, filterable tables — and the page states plainly that its numbers are fictional.

**The icons.** Ten 3D icons in one squircle style, AI-generated through a quality path documented in the README: generate, visually audit (five rejected), regenerate with a corrected prompt, then automated crop and mask — 10/10 accepted. They were optimized into 20 WebP variants (512 and 256) inside `<picture>` with fixed dimensions to prevent layout shift.

**Numbers from the code, not the counters.** 8 pages, 0 dependencies, 10 icons → 20 WebP, 180 aria attributes, 9 modules, 12 FAQs, 5 releases. The hero counters (99.9%, 4 s, 100%) and the dashboard figures are demo data and are never reported as achievements.

**Gaps, stated plainly.** No live URL today, no automated tests, two commits on a single day, an `og:image` pointing to a missing file, and a sitemap covering three of eight pages.

## Five-point summary
1. 8 hand-written HTML/CSS/JS pages: zero framework, zero build, zero dependencies — runs on any static host.
2. Full RTL with Eastern numerals; the design system lives in 14 variables in one 22.8 KB stylesheet.
3. A demo dashboard that explains the product by itself: KPIs, bar chart, sortable tables — with declared demo data.
4. 10 3D icons in one style (AI-generated through a documented quality path) → 20 WebP variants.
5. Gaps: no live URL, no tests, OG image and sitemap need fixing before publishing.

<!-- Sources: README ("Specs", "Structure", "Icon quality path"); brand/BRAND.md; tech.md numbers table (grep/wc/ls on the repo, 2026-09-23); demo.html notice "all figures… fictional". ≈450 words. -->
