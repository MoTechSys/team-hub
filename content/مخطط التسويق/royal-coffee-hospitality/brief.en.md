royal-coffee-hospitality | مخطط التسويق | 2026-09-23 | draft (for editor seal)

# Royal Coffee — a luxury Saudi hospitality site rendered at the edge with no framework

**Segment:** Small business
**Problem:** An ageing Saudi hospitality and coffee-service site of 15 repetitive pages on GitHub Pages, with no unified identity, no structured data and no real mobile experience — while 95% of this category's visitors are on phones.
**Solution:** A full rebuild in Hono and TypeScript on Cloudflare Workers (edge SSR) with no React, no Tailwind and not a single runtime library: 73 pages (services, occasions, menu, prices, 10 cities) generated from one data layer `src/data.ts`, an Onyx + Gold identity with native RTL, 49 hand-drawn SVG icons, 13 JSON-LD builders, and a booking form that becomes a WhatsApp message — no server, no database.
**Result in numbers:** 179.65 KB worker (52.59 KB gzip), 17.7 KB CSS and 4.8 KB JS gzipped, a 23 KB mobile hero image, zero horizontal overflow across 32 captures (16 pages × mobile/desktop), 73/73 pages passing 10 Google indexing criteria with no issues. Live link: to be confirmed — not yet deployed.
**Who it's for:** Hospitality and events businesses that want a luxurious, fast mobile site managed from one file, and any multi-city local business that needs a page per city.
**Contact:** Want a site this refined and this light for your business? DM me.

<!-- Sources: README moain2028/royal-coffee-hospitality (performance, rounds 4–5) · npm run build 2026-09-23 (179.65 kB / gzip 52.59) · sitemap.xml from local run (73 <loc>) · src/data.ts · src/icons.tsx (49) · src/ld.ts (13). "15 pages" for the original site from README "Origin". ≈120 words. -->
