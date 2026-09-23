electricity-billing-flutter | المصمم | 2026-09-23 | draft

# Electricity Billing — a native offline-first Android app whose invoice matches the original

## Executive summary
1. A native Android app in Flutter + Drift for a private power station: subscribers, invoices, archive, settings, backup — all data on the device, no server, no cloud.
2. The PDF invoice matches the official original: a 1024px reference grid, 36 derived constants, a page height derived from the last element, and colours extracted from the source file.
3. Invoice math, Arabic amount-in-words and filenames are covered by 14 unit tests, all passing when re-run.
4. Invoices and backups are saved to a public `Documents/` folder that survives uninstall, through a Kotlin/MediaStore layer with no permission prompt on Android 10+.
5. Status: v1.1.0 (2026-09-01), 10 screens, 3 tables, 7,379 lines of Dart; no confirmed public download, and the developer's contact details are baked into the code — a cleanup item.

## The problem
A private power station bills its subscribers by hand. The field employee has no guaranteed internet, and the invoice is not an internal note but an official document handed to the subscriber; a shifted title or a wrong shade of blue makes it a different document from the approved template.

## How it works
The app is built in Flutter with Riverpod for state and go_router for navigation, on a local SQLite database via Drift with three tables: subscribers, invoices, settings. There is no networking library or cloud service among the dependencies.

The invoice journey: the employee picks a subscriber, enters previous and current readings, unit price, services, arrears and payments; the app computes consumption, value, gross and net with the same formulas ported from the web version, and writes the amount in Arabic words automatically. The invoice is saved as a draft or issued, then previewed, printed or shared as PDF.

The heart of the project is `invoice_pdf.dart`: a landscape A4 page 297 mm wide, where every position is computed from a 1024-pixel reference grid (the original's preview width) through one conversion formula. Horizontal `_X` and vertical `_Y` axes are constants chained by derivation, and the page height itself derives from the last element, so nothing is clipped if a font grows. Colours were not eyeballed: `0000FF` was extracted from bill.docx where it appears 31 times, and the table header `FCD5B4` from the shading definition. Verification reads the PDF itself — character boxes and font sizes — not a rendered image, after a costly lesson the repo documents.

Saving: since Android 10, direct writes to shared storage are forbidden, so a small Kotlin layer uses MediaStore to create a named sub-folder inside Documents, with a legacy path for older devices. The invoice filename is subscriber name + issue date + invoice number, sanitised of forbidden characters.

## Who it's for
Private generation stations and small utilities that want an official invoice from the field employee's phone, with no server and no subscription.

## What sets it apart
- Zero cloud services; the backup is a JSON file the user owns and can re-import.
- An invoice matching a specific document, not a generic template, with a documented, repeatable method.
- 14/14 tests passing for math, amount-in-words and filenames.
- A web preview built from the same code (the build succeeded here).

## Current status and what remains
Last commit 2026-09-01 (8 commits). Remaining: a public download link, separating developer contact data from code, UI tests and CI, multi-tariff pricing, and 62 outdated packages. The APK size in the README (~10 MB) was not measured here.

Source: README, CHANGELOG, docs/ and repo code; figures in tech.md.
