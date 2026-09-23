asoul-aldiafa-ops | متخصص SEO | 2026-09-23 | draft — to be sealed by المحرر

# An SEO audit that corrects its own conclusions by measurement

## 5-point summary
1. A 49-page "service × city" local-services site was accused, in a first-pass analysis, of duplicate content and code-generated 404s; merging pages and 301 redirects were proposed.
2. The pack crawled all 49 pages (26 fields each) and built a 49×49 similarity matrix — 1,176 pairs — after neutralising city names: 0 pairs above 40%, max 28.3%, median 8.9%.
3. The 404s (`/&`, `/$`) were traced to the literal React 19 streaming-SSR markup — HTML comments a crawler misread as paths, not a site bug.
4. Every recommendation was checked against Google's own text (67 unique official URLs); the 301 proposal was withdrawn and archived in a "rejected" folder with its reason.
5. The README opens with four corrections of the earlier claims and closes with eight "could not verify" items — and every number was re-measured from the repo's data files.

## Explainer
When an SEO report says "you have 20 duplicate pages, code-generated 404s, and you should merge 49 pages into 20 and 301 the rest", the expensive mistake is not the report — it is executing it on a live site before measuring anything. This repository is what happens when everything is measured first.

The crawl covered all 49 sitemap URLs and extracted 26 fields per page: status, timing, size, title and its length, description and its length, canonical, h1/h2 counts, visible words, language, images, scripts and JSON-LD types. On the technical checks the result is 49/49 on every line: exactly one h1, matching canonical, description present, `lang="ar"`, and zero titles over 60 characters.

Then similarity. Because the pages are "service × city", city names were neutralised first (Jeddah, Yanbu, Makkah, Madinah, Badr and their Latin forms), Arabic text was normalised, split into 6-grams and Jaccard computed for every pair: 1,176 pairs. Before reading results the method was tested with two controls: a page against itself = 100%, and a page against a copy with its city swapped = 100%. Any two templated copies would have scored 100% — none did: 804 pairs sit below 10%, and only 24 fall between 20% and 28%.

For the 404s the code was opened rather than a tool: the fragment `if("/$"===d||"/&"===d)` inside React's inline script, 241 `<!--/$-->` comments on the page, and zero `href` values containing `&` or `$` across 1.2 MB of JavaScript. The earlier advice to redirect those two paths to the homepage was withdrawn because Google's documentation says a 404 for a page with no replacement is not a problem — so the redirects file was moved to a "rejected" folder with the reason.

What remained a real problem was measured too: 10 preloaded font files weighing 298.1 KB (two of them 68%), and serving from a region far from the audience. What could not be verified — which pages sit in "Crawled – currently not indexed", real Core Web Vitals — was written into an eight-row table rather than guessed.

Preparing this material, I recomputed every README figure from the committed CSV/TSV files with an independent script; all matched (rounding aside). What cannot be re-run — the scripts themselves, since their intermediate files are not committed — is listed as a gap.

The project was for a single client, who is not named here; what generalises is the method: measure, control your measurement, check the recommendation against the policy text, and keep what you withdrew together with why.

<!-- ≈480 words. Sources: tech.md numbers table; SOURCES.md. No business name, phone, or Search Console figures. -->
