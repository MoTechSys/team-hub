crypto-lab | كاتب المحتوى | 2026-09-23 | draft-for-editor

# Crypto Lab — Project Explainer

## Executive summary
1. An educational Android app built in Flutter that explains four ciphers (Caesar, Vigenère, RSA, AES-256-GCM) step by step and visually, with a full Arabic RTL interface.
2. Built as a student project for a cybersecurity course; the goal is that students understand why the output looks the way it does instead of memorizing it.
3. No server: email OTP accounts (SMTP), a SQLite lab notebook with trash, PIN or fingerprint lock, and JSON/CSV or encrypted export.
4. Signed release 1.2.0, 54 passing tests, zero analyzer issues, an APK of about 9 MB.
5. Still open: updating README/CHANGELOG to 1.2.0, higher-resolution screenshots, Moain's approval to name the student developer and his own role, and any user numbers.

## The problem
A security student sees the encrypted output but not how it got there, so the algorithm is memorized instead of understood. Existing teaching tools are either English-only or show the result without the steps.

## How it works
Crypto Lab is a Flutter app for Android 7.0 and above. Each cipher has a screen that exposes what happens inside: the shift table in Caesar (on both the Latin and Arabic alphabets, with a button that lists all 25 brute-force candidates), key extension over the text in Vigenère, generating p, q, n, φ, e and d in a textbook RSA built on BigInt.modPow, and PBKDF2-HMAC-SHA256 key derivation with 10,000 rounds plus the nonce and GCM tag in AES-256-GCM through the pointycastle library, alongside a passphrase strength meter that warns about weak passwords.

The architecture is feature-first: UI, then controllers, then repositories, then a local SQLite database via sqflite. The crypto core is independent of the Flutter UI, so it is covered by pure unit tests. Accounts are verified with a six-digit OTP delivered by email over Gmail SMTP, and passwords are stored as salted, iterated SHA-256 hashes. The app locks with a PIN or fingerprint, auto-locks after 20 seconds in the background, and blocks for 30 seconds after five failed attempts. Every experiment is saved to the lab notebook, soft-deleted into a trash bin, and exported as JSON, CSV, or an encrypted .cryptolab envelope.

## Who it's for
Cybersecurity students and capstone teams, and anyone who wants to understand encryption rather than memorize it.

## What sets it apart
Arabic RTL from the first screen, set in IBM Plex Sans Arabic and JetBrains Mono, with light and dark modes. It pairs visual explanation with real implementation: the AES-256-GCM is actual encryption, not a simulation, and all data stays on the device.

## Current status and what remains
The current release is 1.2.0 (build 3) dated 2026-09-07, a signed arm64 APK, with 54 tests, zero flutter analyze issues, and 77 Dart files. README and CHANGELOG still read 1.0.0 and are to be updated. The documented screenshots are 12 at 500×757. To be confirmed by Moain before publishing: naming the student developer and Moain's own role, and any user or download figures.

<!-- Sources: brief.en.md (Problem, Solution, Result, Who it's for) · tech.md (stack, numbers, status, notes) · readme-source.md (educational goal, features, structure) · links.md. ~450 words excluding the summary. -->
