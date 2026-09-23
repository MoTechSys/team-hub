hafawa-events-app | صانع العروض | 2026-09-23 | draft

# hafawa-events-app — Technical Sheet

- **Repo:** moain2028/hafawa-events-app (public) · HEAD d6730c4
- **Primary language / stack:** HTML + CSS + vanilla JS (no framework, no build step) · Service Worker · Web App Manifest · AVIF/WebP/JPG responsive images · JSON-LD LocalBusiness · Google Fonts (Almarai, Alexandria, Aref Ruqaa)
- **Problem:** the brand needed an installable, phone-first "app" for quote requests, separate from its SEO website.
- **Solution / core features:** single vertical screen with 9 `<section>`s (hero, signature, services, works gallery + lightbox, how-we-work, FAQ, districts, booking, footer), side drawer, fixed bottom tab bar, WhatsApp FAB, install bar (`beforeinstallprompt`), SW with precache + stale-while-revalidate for images + network-first for pages + `offline.html` fallback, 2 manifest shortcuts (quote / coffee service).
- **Architecture notes:** `index.html` 47.6 KB · `styles.css` 67.9 KB · `app.js` 13.5 KB · `sw.js` 1.7 KB (46 lines) · `manifest.webmanifest` 1.3 KB. Desktop >520px shows the app inside a phone frame (`.phone`, 420px). Images are served via `<picture>` (50 elements) with AVIF → WebP → JPG fallbacks at 400/800/1200 widths.
- **Status:** prototype (7 commits, all on 2026-08-09; no live URL confirmed)
- **Last commit:** 2026-08-09 (d6730c4)
- **Live URL:** none confirmed

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source (file/line or command) |
|---|---|---|
| Commits | 7 (all 2026-08-09) | `git log --oneline \| wc -l`, `git log --date=short` |
| Files in repo (excl. .git) | 132 · 21 MB | `find . -path ./.git -prune -o -type f -print \| wc -l`, `du -sh` |
| index.html / styles.css / app.js | 47,597 / 67,944 / 13,473 bytes | `wc -c` |
| gzip -9 of the three | 7,818 / 16,763 / 3,817 bytes = 28.4 KB | `gzip -9c … \| wc -c` |
| `<section>` elements | 9 | `document.querySelectorAll('section').length` (Playwright, 390×844) |
| Services | 6 | index.html services tiles (القهوجية والصبّابون، كوش الأفراح، تنسيق الموائد، الجلسات العربية، الخيام والكراسي، الإضاءة والصوت) |
| Gallery works | 6 | `#works img` count = 6 |
| How-we-work steps | 4 | `<h3>` in `#how` |
| FAQ items | 4 | `<details>` count = 4 |
| Riyadh districts listed | 12 | `#areas` items = 12; commit 0c10ca7 «12 حياً في الرياض» |
| `<a href>` links | 41 | DOM count |
| Inline SVG icons | 24 | `grep -c '<svg' index.html` |
| Image files | 67 (27 AVIF · 29 WebP · 11 JPG) in assets/img | `ls assets/img` |
| `<picture>` elements | 50 | `grep -o '<picture' \| wc -l` |
| Requests / bytes per load (mobile, local) | 27 requests · 562,210 bytes (11 external = Google Fonts) | Playwright response listener, 390×844 |
| FCP (mobile, local server) | 324 ms | `performance.getEntriesByName('first-contentful-paint')` |
| Service Worker precache list | 6 entries (CORE) | sw.js lines 4–5 |
| Cache entries after first load | 22 | `caches.open('hafawa-v1').keys().length` |
| Offline: cached page reload | works (title «حَفاوة — ضيافة وتعهّد حفلات في الرياض») | Playwright `set_offline(True)` + reload |
| Offline: uncached URL | falls back to offline.html («حَفاوة — غير متصل») | same run |
| Manifest | standalone · 3 icons (192, 512, 512 maskable) · 2 shortcuts | manifest.webmanifest |
| Smallest rendered font (mobile) | 12.0 px | computed style scan over visible text nodes, 390×844 |
| Text styles ≥ 4.5:1 contrast | 34 of 37 measured styles; the other 3 are dark text on gold gradient buttons the script could not resolve (gradient bg), visually high-contrast | WCAG luminance script, 390×844 |
| Console errors (desktop + mobile) | 0 | Playwright console/pageerror listeners |
| `prefers-reduced-motion` blocks | 7 | `grep -o prefers-reduced-motion styles.css \| wc -l` |
| `aria-*` attributes | 43 | `grep -c aria- index.html` |
| Independent audit (repo) | 10 claims checked: 7 PASS · 3 FAIL (font floor 8px, tab bar fixed only ≤520px, logo ratio) — the font floor is fixed in HEAD (`.card p` clamp(13px…)) | audit/v5-verify.md, styles.css:285 |

## ملاحظات التنظيف / Cleanup notes
- **README.md does not describe this project** — it is copied from keif-aldiafa-mobile-ui («كيف الضيافة — واجهة جوال فاخرة», 11.8 KB index, 7 images). None of its numbers were used here.
- **Layout bug on viewports >520px (measured):** the 30-tile marquee (`.mq-track`, scrollWidth 4,029px) stretches `.device-stage` to 4,047px and pushes the phone frame off-canvas (`.phone` x = −809px at 1440×900). Screenshots `desktop-99-bug-offcanvas-unmodified.png` show the raw state; other desktop shots use a 4-rule capture-only CSS override (see SOURCES.md). Fix candidates: `.device-stage{min-width:0;overflow:hidden}` + `.screen{contain:inline-size}`.
- Real business phone number appears in `tel:`/`wa.me` links, footer, drawer and JSON-LD; a legal entity name and a contact email are in JSON-LD. All masked in screenshots via DOM replacement before capture.
- JSON-LD `url` points to a temporary gensparkclaw.com VM; unreachable on 2026-09-23.
- Images: `assets/gen/` (6 JPG, 14 MB) are the source renders for the gallery and are AI-generated (folder name + README line «صور مولّدة أصلياً (nano-banana-pro)» from the copied README — treat as disclosed, not verified). `assets/logo/emblem-*.png` (≈1.5 MB) are unreferenced (audit v5 §6).
- Google Fonts loaded from CDN (11 external requests) — contradicts offline-first intent; fonts are not in the SW precache.
- `assets/img/manifest.json` duplicate next to `manifest.webmanifest`.
- No tests, no CI, no LICENSE.
