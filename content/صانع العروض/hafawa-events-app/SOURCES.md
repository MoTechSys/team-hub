hafawa-events-app | صانع العروض | 2026-09-23 | project-pack-v2

# SOURCES — hafawa-events-app project pack v2

## المستودع والتشغيل
- Repo: https://github.com/moain2028/hafawa-events-app (public), HEAD d6730c4, cloned 2026-09-23 into ~/repos/hafawa-events-app.
- Run: `python3 -m http.server 8777 --bind 127.0.0.1` from repo root (README's own instruction, the only part of README that applies). No build step exists.
- Screenshots: Playwright Chromium, device_scale_factor 2, locale ar-SA, `reduced_motion=reduce`; desktop 1440×900 (2880×1800 PNG) + mobile 390×844 (780×1688 PNG); script `build/shoot.py`.
- **Capture-only CSS override on desktop (NOT in the repo):** `body{grid-template-columns:minmax(0,1fr)} .device-stage{min-width:0;max-width:100%;overflow:hidden} .phone{max-width:100%} .screen{contain:inline-size}` — applied because the 30-tile marquee (`.mq-track` scrollWidth 4,029px) pushes `.phone` to x=−809 at 1440px. `desktop-99-bug-offcanvas-unmodified.png` is the raw state without the override. Mobile shots are untouched.
- **DOM masking before capture:** every Saudi mobile number (05… in Arabic-Indic or Latin digits, and +966…) → dots; the legal entity name in footer/drawer → «مؤسسة ••• للحفلات والمناسبات». `tel:`/`wa.me` hrefs unchanged (not visible). The real values are deliberately not reproduced in this pack.
- PWA test: `service_workers` allowed, `navigator.serviceWorker.controller` true, `caches.keys()` = ['hafawa-v1'], 22 entries; `context.set_offline(True)` → reload of `/` served from cache, `/nonexistent.html` → offline.html (mobile-12/13 shots).

## الأرقام على التصاميم (A/B/C) → المصدر
| رقم | مصدر |
|---|---|
| 324 ms | `performance.getEntriesByName('first-contentful-paint')[0].startTime` = 324 on mobile 390×844 against the local server (tech.md). Local, not a live-site figure — stated on the one-number card and in copy. |
| 28.4 KB | gzip -9 of index.html (7,818) + styles.css (16,763) + app.js (3,817) = 28,398 B (tech.md) |
| 22 | cache entries after first load, `caches.open('hafawa-v1').keys().length` (tech.md) |
| 0 console errors | Playwright `console`/`pageerror` listeners, desktop + mobile runs (tech.md) |
| 6 services / 6 works / 4 steps / 4 FAQs / 12 districts / 41 links | DOM counts (tech.md rows) |
| 27 requests / 562 KB | Playwright response listener, mobile (tech.md) |
| 7 commits, 2026-08-09 | `git log` |
| 47.6 / 67.9 / 13.5 KB | `wc -c` |
| 50 `<picture>`, 67 images (27 AVIF/29 WebP/11 JPG) | `grep`, `ls assets/img` |
| 12px smallest font · 43 aria · 7 reduced-motion blocks · 34/37 contrast | scripts in tech.md |

## النصوص → المصدر
- Title/tagline/sub/CTA (COPY in build.py): brief.ar/en.md (this pack, written from index.html text and tech.md; nothing from README).
- Kicker «حَفاوة للأفراح والمناسبات · PWA»: manifest.webmanifest `name`.
- Hero text quoted on carousel/reel («من أول فنجان حتى آخر ضيف» → paraphrased «من أول فنجان حتى طلب عرض السعر»): index.html hero + booking section.
- Tech tags: file types in repo (index/styles/app), sw.js, manifest.webmanifest, `ls assets/img`, `dir="rtl"`.
- Carousel slide sources are listed per slide in `build.py` CAROUSEL (5th tuple field).
- Research competitors/prices: URLs + access date 2026-09-23 inside hafawa-events-app-research.md §2/§7.

## الصور → المصدر
- All device screenshots: real captures from the local run (see above). **Not** AI-generated.
- **Gallery/hero photographs inside the screenshots ARE AI-generated** by the project author: `assets/gen/*.jpg` (6 files, 14 MB) are the source renders for `assets/img/g1…g6`; the hero/service images (`hero-v-*`, `svc-*`, `rental-majlis-*`) have no photographer credit and match the same render style — treated as generated. Disclosed in every design footer, in the explainer and in copy. The copied README's line «7 صور مولّدة أصلياً (nano-banana-pro)» refers to another project and was **not** used as evidence.
- App icons: `icons/make.py` (Pillow, programmatic) per icons/README.md.
- Brand assets in the designs: portfolio-hub 02-brand (Navy #0E2A47, Ink #08172B, Amber #F4A62A, Sand #F7F5F0, Mist #DCE3EA, muted #A3B1C0; small-business segment #F4A62A); fonts IBM Plex Sans Arabic, Inter, JetBrains Mono (embedded).
- Phone frames / notch: CSS drawn in build.py.

## الفيديو
- Reels: 6 scenes × 4 s, 0.6 s crossfade → 21.0 s, 1080×1920 @30fps, H.264 + AAC (`make_reel.sh`, ffmpeg zoompan+xfade). Scenes rendered by `build.py reel` from real mobile screenshots (scene 3 = the real offline.html fallback captured with `set_offline(True)`; it is the app's own offline page, not an error scene); no 404 scene.
- Music: generated 2026-09-23 with CassetteAI/music-generator via gsk (prompt: warm ambient oud, no vocals, 30 s), trimmed to 21 s with fades — royalty-free, no third-party track.
- Covers: scene 1 PNG of each language.

## ما لم يُعرض عمداً
- README numbers (11.8 KB / 17.5 KB / 600 KB / 7 images) — belong to keif-aldiafa-mobile-ui.
- Marketing numbers inside the app («٢٤+ تجهيزاً», «٢٤/٧», «٦٠ دقيقة») — client claims, not measurable; excluded from designs.
- Live URL — none confirmed.
- Phone number, email, legal entity name — masked/omitted.
