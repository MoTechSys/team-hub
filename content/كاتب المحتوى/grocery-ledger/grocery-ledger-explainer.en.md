grocery-ledger | كاتب المحتوى | 2026-09-23 | draft-for-editor

# Grocery Ledger — Project Explainer

## Executive summary
1. A Flutter Android app that gives a small grocery full accounting and works entirely offline, on one device for one user.
2. Barcode point of sale (camera or USB scanner), multiple units per product, receipt and payment vouchers with Arabic amount-in-words, cash shifts with a Z report, expiry alerts.
3. Ledgers are append-only: nothing is deleted, corrections are reversed with an entry, and automatic daily backups keep the last 7.
4. Release 2.2.1 ships as a signed APK: 157 passing tests, zero analyzer issues, 13.3 MB (10.2 MB lite), PDF and Excel export from every screen.
5. Still open: screenshots with real data from Moain's device, renaming the repository after the product, and user numbers.

## The problem
Small grocers track debts in a paper notebook, close the shift in their heads, and can't count on a connection. Available POS apps need internet, an account, or a subscription.

## How it works
Grocery Ledger is a Flutter app for Android 7.0 and above that stores everything locally in Hive and runs with no server. A sale starts by scanning a barcode with the camera or a USB scanner, and one product can sell in several units (carton, bag, piece). Customers and their debts, suppliers and their purchases, each have their own screens, and money movements are recorded as numbered receipt and payment vouchers (RV-/PV-) with the amount written out in Arabic. Shifts open and close with a Z report, and products with expiry dates raise alerts before they run out.

The accounting rule is fixed: ledgers only grow, nothing is deleted; a mistake is corrected with a reversing entry. An automatic daily backup in .glbak format keeps the last seven copies. Printing supports 80 mm receipts, A4 invoices and A5 vouchers, every screen exports PDF and Excel, and there is a monthly profit report and SMS notifications to customers.

The architecture is feature-first across 13 screens (dashboard, POS, sales, purchases, products, customers, suppliers, vouchers, shifts, reports, settings...), and the accounting engine is covered by unit tests through a storage abstraction that allows in-memory testing.

## Who it's for
Groceries and small shops running on one device with one user, where the connection can't be trusted.

## What sets it apart
Fully offline with no account and no subscription, Arabic from the ground up (amount-in-words, receipts, interface), and ledgers that are never erased — which separates it from simple debt-notebook apps on one side and cloud POS systems on the other.

## Current status and what remains
Production: release 2.2.1 (build 5) dated 2026-09-05, 150 commits, APKs for arm64/armv7/x86_64 on the releases page. Current screenshots come from a web demo build with empty data; screenshots with real data from Moain's device are pending. The repository name (mohanad-web-app-2) does not match the product and a rename is suggested. User numbers are undocumented.

<!-- Sources: brief.en.md (Problem, Solution, Result, Who it's for) · tech.md (stack, features, architecture, numbers, status, cleanup notes) · links.md. ~480 words excluding the summary. -->
