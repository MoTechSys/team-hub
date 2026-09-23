keif-diafa | صانع العروض | 2026-09-23 | draft

# Keif Hospitality — a local events website: Explainer

## Executive summary
1. A statically exported Next.js 16 site for an Arabic-coffee-service provider in Abha and southern Saudi Arabia: 20 HTML pages that run on any host with no server.
2. Built to pass Google Ads advertiser verification (privacy and terms pages), rank in 7 cities (one page per city from a single data source) and convert visitors to WhatsApp with a prefilled message.
3. Three quality gates re-run on 2026-09-23: tsc 0 errors, eslint 0 warnings, next build 21/21 — plus FCP 184 ms locally, CLS 0 and zero external requests.
4. Data honesty is in the code: 4 unconfirmed facts hidden behind `unverified`, 3 packages with no invented prices, 12 gallery placeholders until the client's real photos arrive.
5. Status: a prototype awaiting client data (photos, fact and area confirmation, domain, Ads IDs) — no live URL, 5 commits in one day, nothing since 2026-08-01.

## The problem
A hospitality provider in Abha wants to advertise on Google, but advertiser verification can restrict ads or pause the account without a privacy policy and terms of use. He also wants to be found for "coffee server in Khamis Mushait", not only Abha, and wants visitors to tap WhatsApp rather than browse. And he does not yet have confirmed numbers or photos — so none may be invented.

## How it works (in plain language)
All content lives in five data files (`site.ts`, `content.ts`, `services-data.ts`, `gallery.ts`, `cities.ts`). From them the build generates a 9-section home, a services page with 6 detailed services and a 6-row comparison table, 3 packages, 7 city pages, 8 FAQs shown to the reader and emitted verbatim as FAQPage schema, and a gallery with 5 categories and 12 slots. `next build` outputs 20 HTML files plus a 17-URL sitemap and robots.txt; the folder is uploaded to any static host. Arabic fonts (Tajawal, Amiri) are embedded via `next/font`, so there is not a single external request. A fixed 5-item bottom bar and a WhatsApp button that opens a chat with a prefilled message handle conversion.

The `unverified` object holds "24/7? female staff? years of experience? events served?" — all `null` — and none is rendered until the client confirms it.

## Who it is for
Event-service providers in regional cities who want a site that passes Google Ads verification, runs with no server or subscription, and converts to WhatsApp.

## What sets it apart
Zero running cost versus monthly Wix/Squarespace plans (see research.md); 8 structured JSON-LD types with no self-authored ratings; deliberate Arabic typography (font fallback disabled, zero letter-spacing, 1.38/1.85 line heights, logical properties) documented in the README; and data honesty written into the code rather than promised.

## Status and what remains
Waiting on the client: 12 real photos, confirmation of 4 facts and 7 areas, a real domain (canonical and sitemap point to a dead temporary VM), Ads/Analytics IDs. On the code side: move the phone number from `site.ts` to config, raise the font floor to 12px (18 smaller nodes), add tests, CI and a license.

*Disclosure: all screenshots are real captures from a local build; the phone number is masked; the site's dallah image (hero.png) has no documented source in the repository.*
