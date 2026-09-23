keif-publisher | مخطط التسويق | 2026-09-23 | draft (for editor sign-off)

# keif-publisher — executive explainer

## The 5-point summary
1. An automated publishing engine for 8 platforms (Facebook, YouTube, Threads, Instagram, Google Business Profile, TikTok, X, Snapchat) fed from a media archive — with a human approval dashboard before any post.
2. Every caption is generated (LLM or a deterministic offline mode) and then checked against 14 banned patterns in the brand rules; anything that fails never enters the queue.
3. A three-layer approval gate that cannot be bypassed: the generator cannot write "approved"; the dashboard refuses to approve anything with a brand error; the live publish command refuses if the kill switch is on or the status is not approved.
4. A default kill switch (`KEIFPUB_PUBLISHING_ENABLED=0`) stops all real publishing; dry-run always works; secrets come from the environment only and are redacted in logs.
5. Python + FastAPI + Jinja2 + SQLite + APScheduler, 9,271 lines, 210 passing tests, each platform's capability declared honestly (3 live, 2 awaiting review, 1 draft-only, 1 paid, 1 manual) — and not connected to a real account yet.

## The explainer
The problem has two faces. The operational one: a hospitality brand has a media archive of hundreds of videos and photos and wants a regular presence on 8 platforms, each with its own sizes, limits and interface. The risk one: once publishing is fully automated, any caption mistake — the wrong Arabic plural form, an unintended price, a post with no city or phone — becomes a public post on a real account with no way back. The README starts exactly there: "the safe default: everything is dry-run".

The pipeline is simple and orderly: index the archive into an `assets` table (kind, dimensions, duration, category); generate a caption per asset × platform via an LLM or a deterministic `offline` mode for testing; check the text against the brand rules in `brand.py` — 14 banned patterns covering the wrong plural, prices, missing city or phone, and a mandatory brand lexicon; convert media to 9:16 with ffmpeg; then write the post as `pending_review` only. Rejected posts never enter the queue, and the reason is recorded in `brand_check`.

Then comes the dashboard — FastAPI + Jinja2, server-rendered, no React, no CDN — with 11 routes: a queue filtered by status and platform, a detail page per post showing the preview, caption and brand errors point by point, with edit, approve, reject, schedule and publish-now actions, plus accounts and log pages. The approval gate is three independent layers in code, not policy: the generator has no code path that writes `approved`; the dashboard's `approve` route rejects any post with `brand_check.errors`; and `cli publish --live` refuses if the kill switch is on, the status is not `approved`/`scheduled`, or brand errors exist.

The scheduler (APScheduler) picks up due posts and publishes them through the platform account, with three attempts, exponential backoff and special handling for RateLimited, logging every attempt in `publish_log` with who, when, the outcome and whether it was a dry run. The kill switch is a single environment variable: any value other than 1 makes every real publish raise `KillSwitchEngaged`, and its state is always visible in the dashboard's red/green bar and in `cli killswitch`.

What stands out in the repository is honesty about platform limits: each publisher declares its capability — Facebook, YouTube and Threads publish live; Instagram and Google Business Profile await app review; TikTok is draft-only without an audit; X needs a paid plan "and the price is not to be invented"; Snapchat has no organic publishing API, so it exports a manual bundle. 02-TECH-FACTS documents all of it with a check date. The 210 tests pass against a local API mock with no real account, and Meta payloads are redacted before logging.

The limits are clear too: the project is not connected to any real account ("awaiting keys" on every platform), there is no requirements.txt, the dashboard is not mobile-responsive, and there is no CI.

Who is it for? Marketing teams and small agencies that want multi-platform publishing automated without giving up the final human decision, and any brand with strict language rules that wants them enforced automatically before a post goes out.

<!-- ≈590 words. Sources: README · 02-TECH-FACTS · brand.py (14) · db.py (7 states, 5 tables) · web/app.py (11) · cli.py (7) · scheduler.py · base.py (Capability, 3 attempts) · meta_base.py redact · pytest 2026-09-23 (210) -->
