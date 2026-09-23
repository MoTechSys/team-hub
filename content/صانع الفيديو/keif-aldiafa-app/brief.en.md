keif-aldiafa-app | صانع الفيديو | 2026-09-23 | draft

# Keif Al-Diafa — Operations App

**Segment:** Small business
**Problem:** A Saudi coffee-hospitality business ran its events on a paper ledger: hosts got double-booked in the same slot, equipment shortages surfaced on event day, and host payouts and corporate collections got lost between pages.
**Solution:** A fully offline mobile app (React Native/Expo + SQLite) covering the whole cycle: client → event → host booking → quote → invoice and payments → prep sheet → issue and return → host payouts. The database itself rejects overlapping bookings and over-issued stock; a backup is uploaded to Google Drive on demand.
**Results in numbers:** 6 tabs and 14 screens, 18 tables and 3 database-enforced constraints, Arabic PDF export for quotes, invoices and statements.
**Who it helps:** Hospitality and events businesses juggling hosts, inventory and corporate clients.
**Get in touch:** Still running field operations on paper? Let's turn it into a system sized to your problem — message me.

<!-- Sources: README + app/src/db/schema.sql + app/app/ in moain2028/keif-aldiafa-app (read 2026-09-23). Details in tech.md -->
