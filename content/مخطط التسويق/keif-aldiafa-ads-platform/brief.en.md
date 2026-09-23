keif-aldiafa-ads-platform | مخطط التسويق | 2026-09-23 | draft (for editor sign-off)

# Keif Aldiafa Ads Platform — an always-on Google Ads connection that answers: who changed what, and when?

**Segment:** Companies
**Problem:** A business owner pays for Google Ads campaigns yet cannot answer the simplest question: who changed the budget, who re-enabled a paused campaign, and why did Google delete keywords on its own through Auto-Apply? The Google Ads UI shows history but does not watch, and no external tool can reach it except through OAuth with tokens that expire every hour.
**Solution:** An always-on connection layer on Cloudflare (Hono + D1): it refreshes the access token automatically from a refresh token and caches it in D1 so Google is not hit on every request; 13 API endpoints including a free-form GAQL query that opens the whole account to any agent or script, and a four-part health check (secrets, token, Ads, Search Console); an Arabic RTL dashboard showing status, campaigns, performance and top search queries, refreshing every 5 minutes. Plus 10 operational docs: a GAQL cookbook with 19 tested recipes and 5 documented failing queries, and a forensic method for reading `change_event` that reveals who edited what, in Riyadh time.
**Result in numbers:** 13 API endpoints, 3 D1 tables, 4 health checks, 19 GAQL recipes, 10 docs — in 758 lines of TypeScript and a 14.5 KB gzipped Worker with a single dependency (Hono). Phase 0 (the always-on connection) is complete and field-verified; the change guard and 7 analysis engines are on the roadmap, not built yet. Live URL: none — runs locally.
**Who it helps:** Business owners and small agencies running one or a few Google Ads accounts who want independent oversight of changes, and a documented Arabic API layer that AI agents can build on without touching the account.
**Contact:** Want to know who changed your campaigns and when? DM me.

<!-- Sources: README · src/index.tsx (13 routes) · migrations/0001_init.sql (3 tables) · src/google.ts (healthCheck 4, token cache) · docs/07 (19 + 5) · docs/04 (change_event) · docs/08 (phase 1) · npm run build (14.52 kB gzip) · wc -l src (758). ≈230 words. -->
