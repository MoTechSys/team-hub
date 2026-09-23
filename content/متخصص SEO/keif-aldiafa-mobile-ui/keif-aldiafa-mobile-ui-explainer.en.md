keif-aldiafa-mobile-ui | متخصص SEO | 2026-09-23 | draft — to be sealed by المحرر

# A premium mobile UI with no framework — measuring contrast instead of guessing it

A small hospitality business wanted a premium mobile UI that stays readable in a dim majlis, with no framework, no build step, and only a static file host. The result is one page in three files — `index.html`, `styles.css`, `app.js` — 31.2 KB raw, 9.7 KB gzipped.

**What was built.** A full RTL mobile screen: a header with a side drawer (closes on scrim tap or Escape), a hero with an Amiri title in gold gradient and a "Book now" button with a moving sheen, four category tiles, a "signature" card, six service cards with inline SVG icons, a trust strip, a footer, a floating WhatsApp button, and a four-tab bottom bar. Above 520 px it renders inside a 617/1376 device frame; below, it fills the screen.

**The palette.** 21 variables in `:root`; the CSS comment says they were "measured pixel by pixel" from a visual reference: background #17161a, surfaces #202125, borders #38383a, and a five-stop gold gradient from #ab7843 through #f6dc9f and back.

**Contrast measured, not estimated.** I re-measured it myself: each text's color and nearest opaque background read via `getComputedStyle` in Playwright, ratio computed with the WCAG formula. Fifteen texts, all above 4.5:1 — lowest the footer tag at 5.00:1, highest the headings at 15.89:1. The eight values named in the README match mine; one difference: the tab label measures 7.45:1, not 5.00. The hero title is gradient text (`background-clip:text`) and cannot be measured; it is excluded explicitly.

**The floating button.** Anchored to the tab-bar height with 70 px reserved under the content; it hides as soon as scrolling starts and returns after 420 ms so it never covers card text. By `getBoundingClientRect`: 0 px overlap with the bar.

**Local performance.** 20 requests on first load (9 local, 11 Google Fonts), LCP 232 ms and DOMContentLoaded 189 ms on a local server — relative, not production numbers; Lighthouse was not available in the measuring environment.

**Disclosure.** The seven images inside the UI are AI-generated per the README (`nano-banana-pro`), 590 KB in total after optimization. The trust-strip figures (+500 events, 4.9, 3 cities) are demo data and are not reported.

**Gaps.** No live URL and no meta/OG tags; no tests; on desktop the drawer opens outside the device frame; the button sheen keeps running under reduced-motion because `*{animation:none}` does not match `::after`; font sizes under 12 px in the footer and trust strip; and 11 of the 20 requests go to Google Fonts in a UI described as dependency-free.

## Five-point summary
1. One page, three files, 31.2 KB (9.7 KB gzipped) — no framework, no build, no dependencies.
2. Full RTL with a 21-variable palette and a five-stop gold gradient.
3. 15/15 texts above 4.5:1 by getComputedStyle — lowest 5.00:1, highest 15.89:1.
4. Floating WhatsApp button: 0 px overlap with the tab bar, hides while scrolling.
5. Gaps: no live URL, no tests, desktop drawer outside the frame, partial reduced-motion, and AI-generated images (disclosed).

<!-- Sources: tech.md and measure.json (my measurements 2026-09-23); README ("Specs", "Palette", "Measured contrast", "FAB"); styles.css :root; app.js FAB comment. ≈480 words. -->
