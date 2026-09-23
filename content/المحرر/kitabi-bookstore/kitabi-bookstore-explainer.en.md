kitabi-bookstore | المحرر | 2026-09-23 | sealed-by-editor 2026-09-23

# Kitabi — project explainer

## Executive summary
1. A complete Flutter bookstore for Android, built as a mobile-development course project, running with no server at all.
2. 24 books in 6 categories, search and filters, a cart with coupons, favorites, ratings, and order tracking.
3. All data lives in a local SQLite database seeded on first launch; sign-up and sign-in with a three-step OTP password reset.
4. Version 1.1.0: 17 screens, 31 passing tests, a ready APK in the repository, a build guide, and architecture docs.
5. Audience: mobile-development students who want a complete, runnable example to learn from; the repository is open.

## The problem
A mobile-development course asks for a full store app: at least five screens beyond authentication, local data, sign-up and sign-in, a cart and orders, and a right-to-left Arabic interface. The student needs a project that covers the whole store cycle (browse, cart, order, account) without paying for a cloud backend, and without shipping something half-finished.

## How it works
Kitabi is a Flutter app that runs entirely on the device. On first launch it creates a local SQLite database and seeds a catalog of 24 books in 6 categories. App state is managed with Provider in four independent states: session, catalog, cart, and favorites. Navigation uses an IndexedStack with a separate Navigator per tab plus PopScope, so the back button steps back one screen at a time inside each tab instead of exiting the app.

Passwords are stored as salted SHA-256 hashes, and password reset goes through a three-step OTP flow. The app has two roles: a user who browses and buys, and a store admin with a management panel (create, edit, and delete books and categories, plus statistics). A remote license gate reads a license.json file from GitHub.

## Who it's for
Students in mobile-development courses who want a complete example that works on first run, whose code they can read, and whose APK they can build themselves with the included guide.

## What sets it apart
- No server, no cloud subscription: everything is local, so the project runs on any device with no setup.
- A full store cycle, not a toy: coupons, ratings and reviews, order tracking, and an admin panel.
- Verifiable: 31 passing tests across 4 files (admin, flows, repositories, security), plus an automated visual check of 23 screens and states with no console errors.
- Documented: BUILD_GUIDE, ARCHITECTURE, RELEASE_NOTES, and a development log, with a ready APK (≈19.8 MB).

## Current status and what remains
Complete as a course project at version 1.1.0 (last commit 2026-09-09). No live link, since it is an Android app; the web build is preview-only. To be completed: how to credit the project (student vs. developer) in marketing copy, pending Moain's decision, and renaming the repository from Flutter-Native-App-033 to a descriptive name.

<!-- Sources: brief.en.md (sealed 2026-09-11) · tech.md (numbers, stack, status) · README moain2028/Flutter-Native-App-033 · docs/ARCHITECTURE.md via tech.md. 412 words. -->
