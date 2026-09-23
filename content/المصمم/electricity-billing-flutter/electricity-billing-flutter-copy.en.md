electricity-billing-flutter | المصمم | 2026-09-23 | draft (pending editor sign-off)

# Electricity Billing (Flutter) — publishing copy

## LinkedIn (≤120 words)
An invoice is an official document. "Roughly like the original" is not enough.

I built a native Android app in Flutter + Drift for a private power station: subscribers, invoices, archive, backup — all data on the device, no server, no cloud.

The part that took longest: the PDF invoice. Every position is computed from a 1024px reference grid, 36 constants chained by derivation, the page height derived from the last element, and 0000FF extracted from the source file where it appears 31 times. Verification reads the PDF, not a picture.

14/14 tests passing. 10 screens. 0 cloud services.

Repo: github.com/moain2028/electricity-billing-flutter

## X (≤280 chars)
An offline-first Android billing app in Flutter. The PDF invoice sits on a reference grid with derived measurements — no magic numbers — and a colour extracted from the source file. 14/14 tests · 0 cloud services.
github.com/moain2028/electricity-billing-flutter

## Instagram (≤150 words)
An invoice from a pocket, read like the original.

Electricity Billing is a native Android app in Flutter for private power stations. It works offline, and the data never leaves the device.

The employee enters a meter reading; the app computes consumption, value and net, writes the amount in Arabic words, and produces a PDF saved to a public folder that survives uninstall.

And the invoice is not a generic template: its measurements derive from a reference grid, its colours are extracted from the original file itself.

14/14 tests passing · 10 screens · 0 cloud services.

Screenshots use demo data. Repo link in bio.

## Reel script (≈28 s)
[Problem] An official invoice… from a phone, offline.
[Solution] Native Android. Data stays on the device. Flutter + Drift.
[Screens] Dashboard, archive, invoice preview.
[Invoice] Matches the original — a 1024px grid, 36 derived constants, 0000FF from the source file.
[How it works] Reading → amount in words → PDF in a public folder.
[Numbers] 14/14 · 10 screens · 0 cloud services.
[Close] An invoice from a pocket, read like the original. — DM me.
