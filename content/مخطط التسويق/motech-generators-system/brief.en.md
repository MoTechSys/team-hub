motech-generators-system | مخطط التسويق | 2026-09-23 | draft (for editor sign-off)

# MoTech Generators System — an Arabic ERP that replaces the Excel sheet in generator stations

**Segment:** Companies
**Problem:** Diesel generator stations run on a single Excel workbook: daily meter readings copied by hand, fuel balance computed with formulas, a separate maintenance log — no permissions for who enters or sees what, no record of who changed what, and no unified reporting once there is more than one branch.
**Solution:** A fully Arabic (RTL) multi-company, multi-branch management system: a daily entry screen that auto-fetches the previous reading and computes 5 values instantly (operating hours, transformer and screen sales, output per litre), stored as generated columns inside PostgreSQL rather than in the UI; diesel deliveries with a running balance; a 13-field maintenance log; 8 exportable/printable reports; an analytics board with 4 charts. Dynamic RBAC: 39 permissions across 11 modules that an admin composes into roles with any name (4 presets), with SHA-256 + salt, lockout after 5 attempts, and a full audit log.
**Result in numbers:** 11 screens, 13 tables and 12 indexes, 5 database-generated columns, 39 permissions × 11 modules, 8 reports, 4 charts — all in 3,361 lines of plain JavaScript and SQL with no framework (one runtime dependency: Chart.js). Live URL: none — runs inside the AgentDB platform.
**Who it helps:** Energy, contracting and manufacturing companies running generators at more than one site that want trustworthy daily readings, a fuel balance nobody can fudge, and clear permissions per person — without buying a heavy ERP.
**Contact:** Still running your generators on Excel? DM me.

<!-- Sources: README moain2028/motech-generators-system · database/01_schema.sql (13 tables, 12 indexes, 5 GENERATED) · 02_seed_permissions.sql (39/11) · 03_seed_initial_data.sql (4 roles) · app/nav.js (11) · page_reports.js (8) · page_analytics.js (4) · page_maintenance.js (13 fields) · wc -l (3,361). ≈190 words. -->
