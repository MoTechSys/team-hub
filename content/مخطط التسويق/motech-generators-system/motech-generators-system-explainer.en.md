motech-generators-system | مخطط التسويق | 2026-09-23 | draft (for editor sign-off)

# MoTech Generators System — executive explainer

## The 5-point summary
1. A fully Arabic (RTL) ERP for diesel generator stations: multi-company, multi-branch, 11 screens from login to audit log.
2. Daily entry auto-fetches the previous reading and computes 5 values instantly — stored as generated columns inside PostgreSQL, so a screen and a report can never disagree.
3. A running diesel balance (opening + received − consumed) day by day, and a 13-field maintenance log with cost totals.
4. Dynamic permissions: 39 permissions across 11 modules that the admin composes into roles with any name (4 presets), plus an audit log for every sensitive action.
5. No framework: plain JavaScript + SQL in 3,361 lines, running on the AgentDB platform over PostgreSQL 12+.

## The explainer
The problem starts with an Excel workbook. In a single generator station, someone records the transformer meter, the screen meter, the hour meter and the diesel consumed for every generator every day, derives operating hours, sales and output per litre, and tracks the fuel balance with formulas. Once there are more generators, more branches or more than one operator on rotation, the workbook breaks: a previous reading copied wrong, a balance nobody can trace, and no way to give the maintenance technician access to the maintenance log without exposing everything. The project README acknowledges this origin explicitly in its table "Formulas extracted from the original Excel system".

MoTech takes those seven formulas and puts them where they belong: inside the database. The daily readings table in PostgreSQL carries 5 `GENERATED ALWAYS … STORED` columns — operating hours, transformer sales, screen sales, and the two output-per-litre ratios — so they are computed once on save and can neither be typed by hand nor differ between the entry screen and the monthly report. The daily entry screen itself is deliberately simple: pick a generator, the last recorded meter (or the generator's opening meter) loads, enter today's readings, see the deltas and computed values before saving, and get warned if the hour meter went backwards or exceeded 24 hours.

Everything else is built around that table: diesel deliveries with receipt numbers and sources and a running balance over the last 30 movements; a 13-field maintenance log (reason, fault, spare parts, parts and labour cost, engineer, supervisor, duration, result) with totals; an analytics board with four Chart.js charts (production trend, diesel vs hours, generator efficiency in litres per hour, running balance); and 8 reports (daily detail and totals, weekly, monthly, efficiency, diesel, balance, anomalies), all exportable to CSV and printable.

What Excel cannot do is permissions and accountability. The permission catalogue holds 39 permissions across 11 modules (generators, readings, diesel, maintenance, reports, analytics, users, roles, branches, company, audit). The admin creates a role with any name and picks its permissions from a module-grouped matrix with "all / none" shortcuts. Four presets ship as templates: Super Admin, data operator, viewer, maintenance technician. The sidebar only shows the screens a user may open. Passwords are SHA-256 with a per-user salt, sessions last 8 hours, accounts lock for 15 minutes after 5 failed attempts, and a password change is forced on first login. Every sensitive action — login, save, delete, permission change — lands in the audit log with who, when and what.

Technically the project is small on purpose: 20 files, plain JavaScript with no framework and no bundler, a single runtime dependency (Chart.js from a CDN), and 13 tables with 12 indexes in PostgreSQL. The UI talks to the database through named queries (52 of them) registered on the AgentDB platform. Its limits are stated in the README too: protection is application-level, not row-level security, and moving to a standalone Node.js + PostgreSQL deployment is the natural next step.

Who is it for? Energy, contracting and manufacturing companies that run generators at more than one site and want trustworthy daily readings, a fuel balance nobody can fudge, and clear permissions — without buying a heavy ERP or wiring IoT hardware to every generator.

<!-- ≈520 words. Sources: README · 01_schema.sql · 02_seed_permissions.sql · 03_seed_initial_data.sql · app/nav.js · page_reports.js · page_analytics.js · page_maintenance.js · page_daily_entry.js · 04_app_queries.sql -->
