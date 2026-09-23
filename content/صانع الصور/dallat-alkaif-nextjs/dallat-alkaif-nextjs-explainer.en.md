dallat-alkaif-nextjs | صانع الصور | 2026-09-23 | draft-for-editor

# Dallat Al-Kaif — Project explainer

## Executive summary
1. A brochure site for a luxury Arabic hospitality company serving southern Saudi Arabia (Asir · Jazan · Najran · Al-Bahah · Taif), fully RTL Arabic, built with Next.js 16 and React 19 as a static export — no server. (README Overview, ADR-001)
2. 16 static pages: home, an 8-service catalogue with a page per service, 3 packages, booking, gallery, and an Arabic 404. (tech.md Build, README Routes)
3. One source of truth, `lib/site.ts`, for every constant (brand, WhatsApp, 8 services, 13 cities, 5 regions), so no datum can differ between pages. (README Single source of truth)
4. Absolute honesty as an engineering rule: grep-based quality gates block any out-of-scope city, partner logo or phone number outside the source — all at zero violations, with clean tsc and eslint. (tech.md, README Quality gates)
5. Status beta: it builds and ships statically, but all images are AI-generated, and prices, founding year and final domain are "still required" from the owner. (README Still required)

## The problem
Hospitality sites promise "the whole Kingdom," show years of experience, event counts and satisfaction rates nobody supplied, borrow logos of major institutions, and are built with tools designed for English that break right-to-left Arabic. This owner wants the opposite: a defined southern footprint, no number without a source, and no published price that becomes a commercial commitment. (README Content rules)

## How it works
The site is Next.js 16 with the App Router, exported as static HTML (`output: 'export'`): every byte is CDN-cacheable, zero monthly running cost, zero server attack surface. The eight service pages are generated with `generateStaticParams` and `dynamicParams = false`, so an unknown slug returns a real 404. (README Routes, ADR-001)

Styling is CSS Modules with `@layer` and a token system (deep black and gold), not Tailwind — its `ml-*`/`text-left` classes are physical by nature and fight RTL. All properties are logical (`inline-start`, `margin-inline`), every size is a `clamp()` from 360 to 1440 px, with fallback rules outside the layers for older Android browsers that ignore `@layer`. Amiri and Almarai are self-hosted (12 woff2 files, 452 KB) with no Google Fonts: a smaller CSP surface and no visitor-IP leak. A custom image loader adds the basePath that static export omits. (README Design system, ADR-002/003/004)

## Who it is for
Hospitality and events companies in southern Saudi Arabia who want a luxury site that sends visitors straight to WhatsApp and sells no promises. Segment: small business. (brief.en Who it's for)

## What sets it apart
Accessibility is part of the standard, not an add-on: 48 px touch targets (WCAG 2.2 SC 2.5.8), no zoom lock (WCAG 2.1 SC 1.4.4), a skip link, a real `aria-expanded` accordion, form errors via `aria-live`, 16 px inputs that prevent iOS auto-zoom, and `prefers-reduced-motion`. The documentation is itself an asset: an 18.9 KB README with four architecture decision records and a "fixed failures — do not repeat" table (stretched images, broken basePath, unsupported logical keywords in gradients). (README Accessibility, ADR, Fixed failures)

## Current status and what remains
- Two commits (2026-08-06 → 2026-08-07); 34 ts/tsx files, 17 css files, 6,065 lines; out/ = 5.4 MB. (tech.md)
- No automated test framework; the gates are tsc + eslint + grep + build. (tech.md)
- sections.module.css at 691 lines exceeds the README's own "≤ 400 lines" standard. (tech.md Cleanup)
- Still required from the owner: real event photos, package prices, founding year and event count, client logos with written consent, the final domain. (README Still required)
- No verified live URL; currently deployed under the `/dallat` sub-path. (links.md, next.config.ts)

<!-- Every sentence traces to the repository README or to the tech.md/brief.en.md written in this pack from the cloned copy measured 2026-09-23. No person name, no phone number. -->
