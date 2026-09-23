keif-diafa | صانع العروض | 2026-09-23 | draft

# keif-diafa — Technical Sheet

- **Repo:** moain2028/keif-diafa (public) · HEAD dab698b · branch master
- **Primary language / stack:** TypeScript strict · Next.js 16.2.12 (App Router, `output: export`, Turbopack) · React 19.2.8 · Tailwind CSS 4.3.3 (`@theme`) · @tabler/icons paths inlined · `next/font` (Tajawal + Amiri, self-hosted) · JSON-LD
- **Problem:** a hospitality provider needs a Google-Ads-verifiable, SEO-ready, WhatsApp-converting site without unconfirmed claims.
- **Solution / core features:** 11 route files → 20 static HTML pages (home, services, work, packages, areas + 7 city pages, faq, about, contact, privacy, terms, 404) + sitemap.xml + robots.txt; 9-section home; 6 detailed services + 6-row comparison table; 3 packages; 8 FAQs (also emitted as FAQPage schema); gallery with 12 placeholders (`src: null`) across 5 categories; fixed 5-item bottom bar; WhatsApp deep link with prefilled message; `unverified` object gating 4 unconfirmed facts out of the UI.
- **Architecture notes:** single data source `src/lib/{site,content,services-data,gallery,cities}.ts`; `NEXT_PUBLIC_BASE_PATH` for sub-path deploys; documented Arabic typography decisions (`adjustFontFallback:false`, `letter-spacing:normal`, line-height 1.38/1.85, logical properties, `.flip-rtl`); `ProfessionalService` schema (no self-authored ratings); `aspect-ratio` reserved on hero → CLS 0.
- **Status:** prototype awaiting client data (HANDOFF.md: 12 real photos, 4 unverified facts, 7 areas to confirm, domain, Ads/Analytics IDs)
- **Last commit:** 2026-08-01 (dab698b, «v5: تدقيق شامل — إصلاح 4 أعطال مقيسة»)
- **Live URL:** none confirmed

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source (file/line or command) |
|---|---|---|
| Commits | 5 (all 2026-08-01, v1→v5) | `git log --oneline` |
| TS/TSX files · LOC | 32 · 3,432 | `find src -name '*.ts*' \| wc -l`, `cat … \| wc -l` |
| Route files (`page.tsx`) | 11 | `find src/app -name page.tsx` |
| Static pages built | 21/21 (Next.js) → 20 HTML files in `out/` (+ sitemap.xml, robots.txt) | `npx next build` 2026-09-23; `find out -name '*.html'` |
| `npx tsc --noEmit` | 0 errors | run 2026-09-23 |
| `npx eslint . --max-warnings 0` | 0 errors, 0 warnings | run 2026-09-23 |
| Export size | 4.6 MB total · `_next/` 936 KB · `img/` 360 KB | `du -sh out out/_next public/img` |
| Home HTML | 143,195 bytes | `wc -c out/index.html` |
| Home sections | 9 (`main section`) | Playwright DOM count, 390×844 |
| Services (home) / detailed services / comparison rows | 4 / 6 / 6 | `content.ts services`, `services-data.ts detailedServices`, `compareRows` |
| Steps («كيف نعمل») | 4 | `content.ts steps` |
| Packages | 3 (solo, full, custom) — no prices published | `content.ts packs`; FAQ a: «السعر يختلف…» |
| FAQs | 8 | `content.ts faqs` (also `FAQPage` JSON-LD) |
| Service areas / city pages | 7 | `site.ts areas`; `out/areas/*/index.html` |
| Gallery items · categories · real photos | 12 · 5 · 0 (`src: null` ×12) | `gallery.ts` |
| JSON-LD types on home | 8 (WebSite, ProfessionalService, Service, Offer, City, FAQPage, Question, Answer) | `grep -o '@type' out/index.html` |
| Sitemap URLs | 17 | `grep -c '<loc>' out/sitemap.xml` |
| Requests / bytes (home, mobile, local) | 59 · 1,554,024 · 0 external | Playwright response listener |
| FCP (mobile, local) | 184 ms | `performance.getEntriesByName('first-contentful-paint')` |
| CLS | 0 (hero `aspect-ratio` reserved) | README decision + no layout shift observed |
| Console errors (desktop + mobile, 10 pages each) | 0 | Playwright console/pageerror listeners |
| `aria-*` attributes in source | 40 | `grep -rc aria- src` |
| `prefers-reduced-motion` blocks | 2 | `grep -c … src/styles/*.css` |
| Smallest rendered font (mobile home) | 8.8 px — 18 visible text nodes < 12px (`text-[0.66rem]` 10.6px, `text-[0.72rem]` 11.5px, one 8.8px) | computed-style scan, 390×844 |
| Images in repo | 2 (hero.png 604×760 uncompressed by client decision, mark.png) + empty `img/work/` | `ls public/img` |

## ملاحظات التنظيف / Cleanup notes
- **Real phone/WhatsApp number in `src/lib/site.ts`** (`phone`, `phoneDisplay`, `whatsapp`) rendered in header, contact, bottom bar and JSON-LD — masked in every screenshot via DOM replacement; should move to env/config before public promotion.
- **No live URL:** README preview and `site.url` fallback point to a temporary VM that does not respond (2026-09-23); canonical/sitemap/JSON-LD inherit it.
- **Gallery is 100% placeholders** (12 dashed boxes) — the site cannot be promoted visually until the client supplies photos (HANDOFF.md §1 forbids AI/stock).
- **4 unverified facts** (`available247`, `femaleStaff`, `yearsExperience`, `eventsServed`) correctly hidden; 7 areas still «تحتاج تأكيداً».
- **Small text:** 18 nodes under 12px on mobile (contradicts the team's 12px floor used elsewhere); `text-[0.66rem]` labels in the trust strip and bottom bar.
- README «20 مسار مبني» matches (20 HTML); «10 أقسام» on home vs 9 `<section>` measured — one section is likely the hero `<header>`; not shown as a number.
- Google Ads / Analytics intentionally not wired (no IDs) — correct, documented.
- No tests, no CI, no LICENSE; 5 commits in one day then silence since 2026-08-01.
