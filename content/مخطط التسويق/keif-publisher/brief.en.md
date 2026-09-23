keif-publisher | مخطط التسويق | 2026-09-23 | draft (for editor sign-off)

# keif-publisher — automated publishing to 8 platforms that publishes nothing before a human approves

**Segment:** Companies
**Problem:** Publishing a brand's content to 8 platforms from a large media archive is exhausting by hand, but full automation is riskier: a caption that breaks brand language (wrong plural form, a price, no city or phone) or a wrong post going out on a real account with no way back.
**Solution:** A Python pipeline that generates the caption (LLM or a deterministic offline mode), converts media to 9:16, and checks the text against 14 banned patterns in the brand rules — then writes it as "pending review" only. A three-layer human approval gate that cannot be bypassed: the generator cannot write "approved", the dashboard refuses to approve anything with a brand error, and the live publish command refuses if the kill switch is on or the status is not approved. A default kill switch stops all real publishing with a single environment variable, and a scheduler publishes approved posts on time with three attempts and a full log. 8 publishers with honestly declared capabilities: 3 live, 2 awaiting platform review, 1 draft-only, 1 needs a paid plan, 1 manual.
**Result in numbers:** 210 passing tests, 8 publishers, 7 post states, 14 brand rules, 5 SQLite tables, 11 dashboard routes, 7 CLI commands — in 9,271 lines of Python with a FastAPI + Jinja2 dashboard, no React, no CDN. Not connected to any real account yet (every platform "awaiting keys"). Live URL: none — an internal tool.
**Who it helps:** Marketing teams and small agencies that want multi-platform publishing automated without giving up the final human decision, and any brand with strict language rules that wants them enforced automatically before publishing.
**Contact:** Want automation that never leaves your hands? DM me.

<!-- Sources: README (3-layer gate, kill switch, per-platform steps) · pytest 2026-09-23 (210 passed) · keifpub/publishers (8) · db.py (7 states, 5 tables) · brand.py (14) · web/app.py (11) · cli.py (7) · base.py (3 attempts, 9:16) · git ls-files *.py | wc -l (9,271). ≈260 words. -->
