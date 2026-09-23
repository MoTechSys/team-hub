osoul-aldiafa | صانع الصور | 2026-09-23 | draft-for-editor

# Osoul Al-Diafa — Project explainer

## Executive summary
1. A luxury website for an events-hospitality company in the Makkah and Madinah regions, built with Next.js 14, TypeScript and Tailwind in a gold-on-black identity; live at asoulaldiafa.com. (brief.en, tech.md)
2. 54 built pages including 40 service-by-city pages for exactly the five cities the business serves, with structured data that matches that footprint word for word. (brief.en Solution)
3. Homepage LCP dropped from 2,240 ms to 956 ms (local measurement documented in README), with zero WCAG 2.1 AA violations across 9 audited pages. (brief.en Result; tech.md caveats)
4. 15 inaccurate geographic claims ("the whole Kingdom") were removed — geographic honesty is the condition for trust with Google and customers. (brief.en, tech.md)
5. Status: the live site serves V2; V3 is in development with 136 commits through 2026-08-23. (tech.md Status)

## The problem
Luxury hospitality sites look good, load slowly, and claim to serve "the whole Kingdom," losing trust with Google and customers alike. The company needs a site that ranks for "coffee server / hospitality + city," converts the visitor to WhatsApp or a call — no packages, no prices — and performs well on mobile. (brief.en Problem; tech.md)

## How it works
The site is Next.js 14 (App Router), Arabic RTL, set in Amiri and Tajawal. Local pages are statically generated for every (service × city) pair from a single data source (`src/lib/localPages.ts`): two local services (coffee servers, events hospitality) × five cities (Jeddah, Makkah, Madinah, Yanbu, Badr). ProfessionalService structured data declares service areas as 30 km GeoCircles around those five cities, so what Google reads matches what the business actually delivers. Hero entrance animations use CSS keyframes instead of the motion library — a documented performance lesson. (tech.md Solution, Stack)

Quality is tested inside the repository: Vitest for units (4/4 on schema), Playwright for three E2E files (critical path, a11y, WCAG 2.2) with 12 cases, and axe-core on 9 pages. SEO, asset and similarity check scripts (`check:seo`, `check:assets`, `check:similar`) ship with the repo. (tech.md)

## Who it is for
Hospitality and event services in five Saudi cities, including Makkah, Madinah and Jeddah; segment: small businesses, Arabic-first. (brief.en Who it's for; tech.md)

## What sets it apart
Measured in numbers, not impressions: 54/54 pages built with 87.4 KB shared JS under a 90 KB ceiling; LCP 956 ms and CLS ≤ 0.0001; a clean 48/48 sitemap and a maximum Jaccard similarity of 0.259 between any two pages (limit 0.60); 65 WebP images totalling 2.6 MB. Above all: "all regions of the Kingdom" is never said — an explicit README rule. (tech.md Numbers, Status)

## Current status and what remains
- asoulaldiafa.com serves V2 (HTTP 200, re-verified 2026-09-23); the numbers above are from V3 and local measurement — do not claim the live site achieves 956 ms without a live measurement. (tech.md caveats)
- V3 in development: 136 commits between 2026-06-05 and 2026-08-23. (tech.md)
- Cleanup: four Osoul Al-Diafa repositories (site/v2/v3) — pick the canonical one and archive the rest. (tech.md)
- To be completed: a live performance measurement on the domain, WhatsApp/phone details from the live site, and a case study. (links.md)

<!-- Every sentence traces to brief.en.md (sealed 2026-09-11), tech.md (final 2026-09-11) or links.md. -->
