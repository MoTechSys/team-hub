motech-attendance | المحرر | 2026-09-23 | sealed-by-editor 2026-09-23

# Publishing copy (EN)

## LinkedIn (≤120 words)
Replace the desktop attendance tool with a central web system—Motech Attendance

Branch fingerprint devices feed one desktop program; HR can't see all branches, and shifts, leave, and holidays are handled by hand.

I built a Go backend with PostgreSQL and a thin Python collector that pulls from fingerprint devices, signs each upload with HMAC, and syncs every 10 minutes. The RTL dashboard covers employees, daily and monthly reports, shifts, leave with automatic balance deduction, and CSV/Excel export.

Tested on a live device: 11 employees, 3,118 punches; the shift-aware engine wrote 2,277 daily rows, idempotent on every rerun.

Let's scope your attendance setup—DM or email.

#TimeAndAttendance #HRTech #Go #PostgreSQL

## X (≤280 chars)
Every branch's fingerprints in one system: Go + PostgreSQL backend, a Python collector that HMAC-signs each upload and syncs every 10 min, and an RTL dashboard with reports, shifts and leave. Live test: 3,118 punches → 2,277 daily rows, zero duplicates. #HRTech #Go

## Instagram (≤150 words)
The desktop fingerprint program sees one branch. HR needs to see them all.

Motech Attendance: a thin collector in every branch pulls punches from the device every 10 minutes and posts them signed to a central server; a daily engine computes late, overtime and short hours per shift; an Arabic RTL dashboard exports everything to CSV/Excel.

Numbers from the live test: 11 employees · 3,118 punches · 2,277 daily rows—and reruns never duplicate a row.

For multi-branch companies with biometric attendance devices. DM to scope yours.

#TimeAndAttendance #HRTech #Go #PostgreSQL #Biometrics #Backend

## Reel script (21 s · 6 scenes · no logo)
1. Motech Attendance—Replace the desktop attendance tool with a central web system / Every branch's fingerprints in one system
2. Problem—Branch fingerprint devices feed one desktop program / HR can't see all branches
3. Solution—A thin collector pulls punches every 10 minutes / HMAC-signed uploads, synced via systemd to a central Go backend
4. How it works—Late · overtime · short—daily / Shift-aware daily engine; RTL dashboard with CSV/Excel export
5. Result—3,118 / punches from a live device · 11 employees · 2,277 daily rows
6. Call—One system for all your branches / Let's scope your attendance setup—DM or email

<!-- Sources: brief.en.md (all sections) · tech.md «الأرقام». No client name, vendor name withheld from titles, no code link.  · measured at seal: LinkedIn 116 words · X 265 chars · IG 95 words -->
