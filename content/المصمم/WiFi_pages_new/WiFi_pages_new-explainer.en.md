WiFi_pages_new | المصمم | 2026-09-23 | draft

# A hotspot portal in Glassmorphism — redesigning MikroTik templates without breaking router logic

## Executive summary
1. The project is a CSS-layer redesign of MikroTik RouterOS hotspot captive-portal templates — 8 HTML files uploaded to the router's `hotspot` folder — not a website.
2. The look is Glassmorphism: animated gradient background, frosted-glass cards via `backdrop-filter`, floating orbs and stars, 9 CSS animations, in plain CSS3 with zero external libraries.
3. The data-integrity contract is intact: 27 `$(…)` template variables, six form field names, form action, CHAP-MD5 hashing and cookies — none touched; the change is CSS only.
4. The stylesheet is 19.9 KB (was 4.7 KB), responsive down to 380px with seven media queries, inline SVG icons, and an `original/` copy to roll back.
5. Status: v2.0 (2026-02-13, 2 commits); one CSS bug hides the status-page buttons' text, and client data is hard-coded in the templates — two documented gaps.

## The problem
When a user joins a MikroTik hotspot, the router intercepts them with a login page from a stock template designed more than a decade ago: a grey table, system font, no phone layout. Editing it is risky: the page is not plain HTML but a template the router fills with variables such as `$(link-login-only)` and `$(chap-id)`; the form posts specific field names, and the password is hashed with MD5 in the browser. Change any of that and every user's login stops.

## How it works
The portal is 8 templates: login (speed selector, card number, a conditional free-trial button), session status (time left, bytes, balance), login success with redirect, logout with a session summary, error, temporary block after failed attempts, advert, and WISP redirect. All link one stylesheet, `style/style.css`.

The principle: **HTML and JavaScript stay as they are; all design lives in CSS.** The background is an eight-colour gradient moving with a `gradientShift` animation, with floating orbs and twinkling stars in pure CSS, then a frosted card with `backdrop-filter: blur(20px)` and a travelling shimmer, and purple-gradient buttons with a hover shine. Icons are inline SVG (user, lock) instead of external files.

Data integrity is documented in the README: form action `$(link-login-only)` preserved, field names username/password/speed/popup/domain/dst unchanged, JavaScript functions, cookie logic and MD5 CHAP working without modification, and every MikroTik variable in place. I verified it with grep: 27 unique variables in the new templates, and an `original/` folder keeps the previous version for rollback.

Performance: zero libraries, every animation on `transform` and `opacity`, no heavy background images; the full payload is 133 KB, 68 KB of which is the logo.

## Who it's for
Small wireless ISPs, rest-houses and cafés selling hotspot cards on MikroTik who want a UI worthy of their customers' phones without operational risk.

## What sets it apart
- Zero external libraries versus the common Bootstrap/jQuery templates.
- An explicit contract of what must not change, plus an original copy to roll back.
- 9 CSS animations and 16 `backdrop-filter` uses in 19.9 KB.
- Native Arabic RTL, responsive down to 380px.

## Current status and what remains
Last commit 2026-02-13. I found a real bug while capturing: the rule `.wrap h1:first-of-type` makes text transparent for the neon effect on the network name, but on the status page the first `h1` wraps the three buttons, so their labels vanish; the fix is one line. Also remaining: separating client data (phone, prices, LAN links) from the template so it becomes reusable, a test on a real router, a dedicated Arabic font, and a README update (it still lists the deleted index.html).

Source: README, CLEANUP_LOG and repo code; figures in tech.md.
