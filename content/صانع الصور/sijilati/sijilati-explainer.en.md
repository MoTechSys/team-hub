sijilati | صانع الصور | 2026-09-23 | draft-for-editor

# Sijil (سِجِل) — Project explainer

## Executive summary
1. An offline-first Android app in Flutter that replaces the paper debt ledger in Yemeni shops, designed for the owner and a worker who may not read. (brief.en, tech.md)
2. A debt entry in four steps (customer photo → took/paid → amount by banknotes → spoken confirmation) with an eight-second undo. (brief.en Solution)
3. Append-only ledger: no edits or deletes on transactions, corrections are reversing entries with a reason, and money is stored as integers, never floats. (tech.md)
4. Version 0.2.0, 93 passing tests, zero analyzer issues, a 21–23 MB APK, and offline activation with a 30-day trial. (brief.en Result)
5. Status: pre-release for field testing; next step is testing on a real phone and rotating the activation secret before sale. (tech.md Status)

## The problem
In Yemeni shops — grocers, restaurants, pharmacies — credit is written on paper and then forgotten or disputed. The worker may not read or write, only 17.7% of the population has internet access, and a "free + ads" model does not work because AdMob does not pay out in Yemen. (tech.md, from docs/01_CONTEXT.md)

## How it works
Sijil is an Android app that works fully offline. The daily flow is stripped to the minimum: the worker picks the customer by photo, taps one of two large buttons — "took from me" or "paid me" — enters the amount by tapping banknote images or a keypad, and hears the app read the entry aloud before saving. A mistake can be undone within eight seconds.

Under the surface the architecture is strict: the transactions table is append-only, enforced at the database level with SQLite triggers, so nothing is edited or deleted; corrections are reversing entries with a reason. Money is stored as integers, not doubles, and a single ledger service is the only writer. Each currency has its own ledger: Yemeni rial (new/old), Saudi riyal, and US dollar. Core logic lives in `core/` with no UI, governed by ten ledger rules, each with a test. (tech.md Solution, Stack, Numbers)

## What the owner gets
- Overdue aging at 30/60/90/180 days, bulk reminders over WhatsApp/SMS, and promise-to-pay.
- Six Arabic A4 PDF document types (short/detailed statement, A5/80 mm thermal receipt, demand notice, overdue report, debt acknowledgement) × three templates, with a live header/footer editor.
- Worker accounts with photos, PIN, permissions, and an activity log.
- Daily local backup + a verified `.sijil` file + Google Drive.
- Offline activation with a device-bound HMAC code, a 30-day trial, free up to 15 customers.
- Voice help on 11 topics. (tech.md Solution)

## Who it is for
Shop owners who sell on credit and want a correct number every evening — and the worker who records entries even without reading. Segment: individuals and small shop owners, Arabic-first. (brief.en Who it's for; tech.md Segment)

## What sets it apart
Three things the design insists on: it works fully offline, not "partly offline"; it is built for a worker who cannot read (huge buttons, pictured banknotes, spoken confirmation, touch targets ≥56 dp, never colour alone); and the ledger cannot be tampered with because deletes and edits are blocked at the database level. (tech.md)

## Current status and what remains
- Version 0.2.0+2 (2026-09-09), 13 commits, 74 Dart files and 13,477 lines, 37 screens across 11 feature modules. (tech.md Numbers)
- Phases 0→4 are built and tested on the web preview; field testing on a real phone is still needed (camera, voice, WhatsApp, PDF, Drive). (tech.md Status)
- Before sale: rotate the activation secret, settle the canonical repository, and confirm repositories are private because signing files are inside them. (tech.md Status)
- Users/clients: to be completed (not documented).

<!-- Every sentence traces to brief.en.md (sealed) or tech.md (ready) in 01-projects/sijilati. No code link: the repository is treated as private. -->
