keif-blins-invoices | متخصص SEO | 2026-09-23 | v2 · project explainer (English) — every sentence from brief.en.md / tech.md / README

# Keif Al-Diafa Invoices — project explainer

## Executive summary (5 points)
1. A Flutter Android app that produces official invoices, quotations, receipt vouchers, and account statements as PDFs from a phone, with no server and no cloud account.
2. Built for an events-hospitality business in Jeddah that issued its documents by hand, lost track of payments, and needed a statement per client each month.
3. Released as version 2.2.0 (APK about 10.9 MB), with 32 passing tests and zero analyzer issues.
4. Native Arabic RTL: RTL tables, Arabic amount-in-words, and an in-house patched PDF library that fixes Arabic spacing.
5. Status: released and in use at one business; Android only; app-UI screenshots are still to be added.

## The problem
A hospitality business issues invoices, quotes, and receipts by hand, loses track of payments, and needs a statement per client each month. It needed official Arabic PDF documents from a phone, without depending on a server or a subscription.

## How it works (the architecture in plain words)
The app is written in Flutter and runs entirely on the phone. Clients, documents, and payments live in a local database (Hive). Money is stored as integer halalas and tax as basis points, so decimal rounding errors cannot creep in. When a document is issued, the PDF layer renders it in a single official theme approved by the company: right-to-left tables, the amount written out in Arabic words, and an optional VAT line that disappears when tax is not enabled. The original pdf library (3.12.0) is vendored inside the project with a patch that fixes Arabic text spacing. Files are saved under a Documents folder named after the company and sorted by type and year, then shared directly over WhatsApp or printed. A PIN lock (SHA-256 with salt) protects the app, and there is a trash bin plus JSON backup.

The UI has 5 tabs, 13 screens, and 3 themes. The four documents are: invoice/quotation, summary account statement (a classic debit/credit/balance ledger), detailed account statement, and an A5 landscape receipt voucher.

## Who it is for
Hospitality and event businesses, and any small company that needs official documents from a phone.

## What sets it apart
It works offline with no account, so there is no invoice cap and no subscription; the document carries the company's own identity rather than a generic template; and the Arabic is native, not retrofitted. Quality is demonstrated: 32 tests across 6 files (money, models, store, security, PDF, and a stress test rendering a detailed statement with 60 payments), and static analysis with no issues.

## Current status and what remains
Released as v2.2.0 on the GitHub releases page, stable and documented (README, agent guide, changelog). Out of scope by design: Firebase, cloud accounts, and web as a product. To be completed: app-UI screenshots from Moain's device, a real screen-recorded demo, and a client count (documented: one business). Renaming the repository from `keif_blins` to a descriptive name is suggested.

<!-- Sources: brief.en.md (problem/solution/result/who); tech.md (stack, architecture notes, status, numbers table, cleanup notes); repo README (project structure, documents, fixed decisions); tech-designer.md (13 screens, 3 themes, 6 test files). ~450 words. -->
