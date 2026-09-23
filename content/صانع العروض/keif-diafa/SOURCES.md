keif-diafa | صانع العروض | 2026-09-23 | project-pack-v2

# SOURCES — keif-diafa project pack v2

## المستودع والتشغيل
- Repo: https://github.com/moain2028/keif-diafa (public), branch `master`, HEAD dab698b, cloned 2026-09-23 into ~/repos/keif-diafa.
- Build (all 2026-09-23): `npm ci` (364 packages) → `npx tsc --noEmit` (0 errors) → `npx eslint . --max-warnings 0` (0) → `npx next build` (21/21 static pages, Turbopack) → `out/` served with `python3 -m http.server 3310 --directory out`.
- Screenshots: Playwright Chromium, device_scale_factor 2, locale ar-SA, `reduced_motion=reduce`; desktop 1440×900 (2880×1800 PNG) + mobile 390×844 (780×1688 PNG); 10 pages each + home full-page + mobile menu = 23 files; script `build/shoot.py`. No CSS overrides applied.
- **DOM masking before capture:** every Saudi mobile number (05… Arabic-Indic or Latin digits, +966 5…) → dots. The real value (in `src/lib/site.ts`) is deliberately not reproduced anywhere in this pack.
- No person names exist in the site; no client legal name beyond the brand «ضيافة الكيف / Keif Hospitality».

## الأرقام على التصاميم (A/B/C) → المصدر
| رقم | مصدر |
|---|---|
| 20 static pages | `find out -name '*.html' \| wc -l` = 20 (Next.js reports 21 incl. `_not-found` route) |
| 7 city pages | `src/lib/site.ts areas` (7 entries) → `out/areas/<slug>/index.html` ×7 |
| 8 JSON-LD types | `grep -o '@type":"…"' out/index.html \| sort -u` → WebSite, ProfessionalService, Service, Offer, City, FAQPage, Question, Answer |
| 0 tsc/eslint errors | commands above, 2026-09-23 |
| 8 FAQs | `content.ts faqs` (8 `q:`) |
| 6 services · 6 comparison rows · 3 packages · 4 steps · 9 sections | `services-data.ts`, `content.ts`, Playwright `main section` count |
| 0 external requests · 59 requests · 1.55 MB | Playwright response listener, mobile home |
| FCP 184 ms (local) · CLS 0 | `performance.getEntriesByName('first-contentful-paint')`; README `aspect-ratio` decision + no shift observed |
| 5 commits (2026-08-01) | `git log` |

## النصوص → المصدر
- Title/tagline/sub/CTA (COPY in build.py): brief.ar/en.md (this pack) ← README «⚠️ ما ينتظر بيانات العميل», `site.ts unverified`, tech.md.
- Kicker «ضيافة الكيف · قهوجيين وصبابين — أبها والجنوب»: `site.ts name/nameLatin` + README H1 line.
- «يمرّ من توثيق Google Ads»: README table rows for `/privacy/` and `/terms/` («مطلوبة لتوثيق Google Ads») + Google Ads Help (research.md §1).
- Carousel slide sources listed per slide in `build.py` CAROUSEL (5th tuple field).
- Research competitors/prices: URLs + access date 2026-09-23 in keif-diafa-research.md §2/§7.
- Not shown anywhere: trust badges («24/7», «+500», years, events) — they do not exist in the code (hidden by `unverified`); README «10 أقسام» (measured 9).

## الصور → المصدر
- All device screenshots: real captures from the local build. **Not** AI-generated.
- Inside the screenshots: `public/img/hero.png` (dallah, 604×760, served uncompressed per README «قرار العميل») and `public/img/mark.png` — **origin/licence undocumented in the repo**; disclosed on every design footer («صورة الدلّة أصلها غير موثَّق» / «dallah image origin undocumented»), in the explainer and in copy. Gallery (`/work/`) contains 12 empty placeholders (`src: null`) — no photos, AI or otherwise.
- Icons: @tabler/icons paths inlined (MIT) per README.
- Brand assets in the designs: portfolio-hub 02-brand (Navy #0E2A47, Ink #08172B, Amber #F4A62A, Sand #F7F5F0, Mist #DCE3EA, muted #A3B1C0; small-business segment #F4A62A); fonts IBM Plex Sans Arabic, Inter, JetBrains Mono (embedded). Browser/phone frames drawn in CSS.

## الفيديو
- Reels: 6 scenes × 4 s, 0.6 s crossfade → 21.0 s, 1080×1920 @30fps, H.264 + AAC (`make_reel.sh`). Scenes from real screenshots (home, services, Abha city page, contact); no error/404 scene.
- Music: generated 2026-09-23 with CassetteAI/music-generator via gsk (prompt: gentle oud, ambient, no vocals, 30 s), trimmed to 21 s with fades — royalty-free.
- Covers: scene 1 PNG per language.

## ما لم يُعرض عمداً
- Phone/WhatsApp number (site.ts) — masked.
- README preview URL / `site.url` VM fallback — dead (HTTP 000, 2026-09-23); no live link on any design.
- Any comparison or shared screenshot with the brand's other 5 platform projects (PM instruction).
- Prices — none exist in the code.
