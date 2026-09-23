electricity-billing-flutter | المصمم | 2026-09-23 | draft

# Electricity Billing — native Android app (Flutter)

**Segment:** Companies
**Problem:** A private power station bills subscribers by hand, and the invoice is an official document that must not drift from its original template by a position or a colour.
**Solution:** A native Android app in Flutter + Drift that works offline: subscribers, invoices with automatic math and Arabic amount-in-words, archive, settings, JSON backup. The PDF invoice is laid out on a reference grid with derived measurements — no magic numbers — and colours extracted from the source file; it is saved to a public folder through a Kotlin/MediaStore layer.
**Results in numbers:** 14/14 tests passing · 10 screens · 3 tables · 0 cloud services · 7,379 lines of Dart (sources in tech.md).
**Who it's for:** Private generation stations and small utilities that want official invoices from a field employee's phone, with no server.
**Contact:** I build offline-first billing apps — message me.
