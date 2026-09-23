keif-aldiafa-app | صانع الفيديو | 2026-09-23 | draft

# Keif Al-Diafa — Operations App · Project Explainer

## Executive summary
1. A mobile app for a Saudi coffee-hospitality business that ran events on a paper ledger; it closes 4 gaps documented in the client's own words.
2. Fully offline (React Native/Expo + SQLite), single user, with an on-demand backup to Google Drive.
3. Constraints are enforced in the database, not the UI: an overlapping host booking or over-issued stock is rejected by a trigger.
4. 6 tabs and 14 screens cover the cycle from client to host payouts, with Arabic PDF export.
5. Status: a working full-cycle prototype, with no automated tests and no published APK yet.

## The problem
Keif Al-Diafa serves Saudi coffee at corporate and home events and ran its field operation on a paper ledger, producing quotes and invoices by hand. The result was four gaps stated verbatim by the client: a host registered twice on the same day or slot; no view of what runs short in cups, dallahs and coolers when two events coincide; host dues lost because "they have an account" that is never written down; and corporate clients paying late with no follow-up or reminder.

## How it works
The app is built with React Native 0.86 and Expo SDK 57 using expo-router, and stores everything in an on-device SQLite database (18 tables, 14 indexes). The workflow: client → event → host booking → quote → client approval → invoice → deposit → prep sheet → issue items → execute → return and audit → host payouts → close. Events have five states: draft, quoted, confirmed, in progress, completed.

Three decisions define the system. First, constraints in the database: instead of hiding a button, one trigger rejects inserting or updating a host assignment that overlaps another in time, and another rejects an issue movement that exceeds availability — any attempt aborts the whole transaction. Second, inventory is time-reserved, not deducted: availability on a date equals owned minus damaged/lost minus items issued to overlapping events, so the stock screen shows the right shortages for any upcoming day. Third, sync is a backup, not a cloud database: with a single user, the app uploads the SQLite file to its private appDataFolder in Google Drive using only the drive.appdata scope, after `PRAGMA wal_checkpoint(TRUNCATE)` so the latest writes are not lost.

On the finance side, document numbering is atomic via `UPDATE counters ... RETURNING`, tax is computed per line and then summed with banker's rounding to two decimals, and an invoice moves automatically between issued, partial and paid while rejecting any payment above the remaining balance. Quotes, invoices and statements export as Arabic PDFs in Amiri and Tajawal.

## Who it is for
An owner of a hospitality or events business who personally manages hosts, equipment stock and corporate clients, and wants a system that works from their phone on site without depending on the network.

## What makes it different
It is built from the client's verbatim inputs (texts, transcribed recordings, real forms) and documented with ten architecture decisions that name the rejected alternative and why, plus six in-depth research notes (RBAC, Saudi e-invoicing, RN architecture, database schema, design system, API contract). The seeded data — 15 beverages, 11 stock items and 6 preset quote lines — comes from the client's own menu and forms.

## Current status and what remains
The code covers the full cycle and runs (it was run locally and screenshotted). There are no automated tests despite a test script. No APK is published: there are no GitHub releases and the last build workflow run (2026-09-22) failed. The dynamic role model and notifications described in the research are not implemented; the app is single-user. Google sync requires an OAuth client from the business owner. ZATCA e-invoicing is researched but not implemented.
