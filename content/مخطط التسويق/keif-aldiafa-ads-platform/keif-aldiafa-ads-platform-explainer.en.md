keif-aldiafa-ads-platform | مخطط التسويق | 2026-09-23 | draft (for editor sign-off)

# Keif Aldiafa Ads Platform — executive explainer

## The 5-point summary
1. An always-on connection layer to Google Ads and Search Console on Cloudflare (Hono + D1): the token refreshes itself and is cached in D1, so Google is not hit on every request.
2. 13 API endpoints, led by a free-form GAQL query that opens the whole account to any agent or script, plus a four-part health check (secrets, token, Ads, Search Console).
3. An Arabic RTL dashboard: connection status, impressions/clicks/cost/conversions, campaigns, top search queries, event log — refreshing every 5 minutes.
4. 10 operational docs, including a GAQL cookbook with 19 tested recipes and 5 documented failing queries, and a forensic method for reading `change_event` (who changed what, when, in Riyadh time).
5. Phase 0 is complete and field-verified; the change guard and 7 analysis engines are on the roadmap, not built. 758 lines of TypeScript, a 14.5 KB gzipped Worker, one dependency.

## The explainer
The problem is familiar to anyone paying for Google Ads: things happen in the account that the owner cannot trace. A budget changes several times in a few days, a paused campaign is switched back on, keywords disappear because Google's Auto-Apply feature applied a recommendation on its own, and a second admin permission exists that the owner does not remember granting. The Google Ads UI shows a change history but does not watch or alert, and any external tool needs OAuth, an access token that expires hourly, a developer token and very specific headers — get one wrong and the error messages are opaque.

The platform solves the first layer of that problem: **the always-on connection**. A Cloudflare Worker built with Hono holds the refresh token as a secret, derives an access token when needed and caches it in D1 with a 120-second safety margin before expiry; subsequent requests read from the cache and never touch Google. On top sit 13 API endpoints: a ready token, a four-part health check, account and accessible-customer data, campaigns, performance for the last 7/14/30 days, Search Console sites and top queries, an event log, a periodic snapshot stored in D1 for later comparison, an agent catalogue — and most importantly `POST /api/ads/query`, which accepts any GAQL query and returns the raw result. That single endpoint turns the platform into a gateway any AI agent or script can build on without knowing anything about OAuth.

The Arabic RTL dashboard consumes those endpoints: a status strip with the four checks in colour, four number cards, the campaign list with statuses, a table of top Search Console queries, the list of agent-ready endpoints, and recent events — auto-refreshing every 5 minutes. Protecting the dashboard and API with a `DASH_KEY` is optional locally and mandatory on deployment.

What really distinguishes the repository is its ten documents: a handover file stating where things stand and what comes next, setup from scratch, the Google connection explained with translated errors, account state, a forensic method that decodes `client_type` in `change_event` to tell whether a change came from the UI, the API or Google itself (with the warning that the `change_event` window is only 30 days), a tag and conversion audit, a campaign audit against global standards, a GAQL cookbook with 19 working recipes and 5 failing queries each paired with its correct alternative, a roadmap, and an API reference. The field rules baked into the code — no `login-customer-id`, v24 only because v17–v21 are dead, Basic Auth with the web client — are the residue of real mistakes, documented so they are not repeated.

The limits are stated in the repo itself: this is Phase 0. The change guard (alert and auto-revert), the seven engines (impression share, search-term waste, keyword quality, budget stability, conversion health, devices and hours, keyword conflicts), and guarded write access are all in docs/08 as a plan, not in code. The project is not deployed yet.

Who is it for? Business owners and small agencies running one or a few accounts who want independent oversight of what changes in them, and developers who want a documented Arabic API layer their agents can build on without touching the account.

<!-- ≈560 words. Sources: README · src/index.tsx (13 routes) · src/google.ts (cache −120 s, healthCheck 4, v24 / login-customer-id rules) · src/ui.tsx (5 min) · migrations (3 tables) · docs/00, 02, 04, 07 (19+5), 08 (phase 1) · npm run build · developers.google.com change-event (30 days) -->
