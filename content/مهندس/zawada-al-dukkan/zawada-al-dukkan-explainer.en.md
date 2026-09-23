zawada-al-dukkan | مهندس | 2026-09-23 | draft — to be sealed by the editor

# Zawada Al-Dukkan Market — Project Explainer

## Executive Summary

1. **Problem:** A small grocery wants to show its products online properly, without the cost of a full store or a payment gateway.
2. **Solution:** An RTL Arabic customer storefront with a look borrowed from fine hospitality — teal primary and gold gradient, Cairo and Amiri type, an animated mesh background with glass effects — built in Next.js, TypeScript, and Tailwind.
3. **Experience:** The customer browses 10 categories, from daily deals to incense, and ordering sends a ready WhatsApp message; no server, no payment gateway.
4. **Status:** Phase 1 (design system + data) is live on GitHub Pages as a static HTML page; Phases 2 and 3 (Zustand store, cart, WhatsApp checkout) are planned and not yet built.
5. **Data:** 20 products in 10 categories as demo data, with product images from Unsplash/Pexels — not a real client's inventory.

---

## What is the problem?

A small grocery owner today lists stock in plain WhatsApp text lists or scattered photos — nothing that suits the brand or helps a customer choose. The off-the-shelf alternative — a full online store with a payment gateway and a monthly subscription — is bigger and costlier than the need. What is required is an Arabic shopping storefront that suits the brand and gets the customer to an order in the fewest steps, with no payment gateway and no server.

## How does it work?

- **Frontend:** A Next.js app (App Router) in TypeScript and Tailwind CSS, with Framer Motion for motion and lucide-react for icons. A complete design system lives in `tailwind.config.ts` and `globals.css`: a teal `#009BC5` primary and a gold gradient `#D4AF37 → #F27628` on a pearl background, an animated mesh gradient, glassmorphism, and CTA buttons with a shimmer effect.
- **Type and direction:** Cairo for body text and Amiri for display, a full RTL layout with mobile safe areas.
- **Data:** 20 products in 10 categories in `lib/mockData.ts` as Phase 1 demo data, with Unsplash/Pexels images served through next/image as AVIF/WebP.
- **SEO:** Metadata, a manifest, and GroceryStore JSON-LD structured data (name, phone, country).
- **Ordering:** The principle is that an order becomes a ready WhatsApp message to the shop's number — no server, no payment gateway. The WhatsApp checkout itself (Cart Sheet + WhatsApp Checkout) is planned for the unbuilt Phase 3.
- **Deployment:** GitHub Pages serves a static `index.html` built with the Tailwind CDN, independent of the Next app; this pack's screenshots come from that live page.

## Who is it for?

Grocery and small-shop owners who want a fast showcase that connects straight to the customer over WhatsApp — without adopting a full store platform.

## What sets it apart?

- **A premium identity for a category that rarely gets one:** fine-hospitality styling applied to a grocery, with a documented design system rather than a generic template.
- **Zero running cost:** no server, no database, no payment gateway — a static page on GitHub Pages and a WhatsApp message.
- **Arabic first:** native RTL with suitable Arabic type, not a translated foreign template.
- **Indexable from day one:** GroceryStore structured data built in.

## Current status and what remains

- Phase 1 done (Design System + Mock Data). Phase 2 (Zustand Store + Header + Bottom Nav + Product Grid) and Phase 3 (Homepage + Cart Sheet + WhatsApp Checkout) not yet built.
- Last repository change 2026-04-28 (4 commits in one day); no tests, no CI.
- README says Next.js 15 while package.json says 14.2 — to be unified. The `zawada-aldukkan.com` domain in JSON-LD is not active — to be fixed or removed.
- Figures shown inside the live UI (4.8 rating, 12 countries of origin, 20+ products) are demo interface content, not metrics.

**Contact:** Want one like it for your shop? DM me.

<!-- Sources: brief.en.md (Problem, Solution, Result, Who it's for, Contact) · tech.md (problem, solution, stack, status, figures, cautions) · README moain2026/zawada-al-dukkan (visual identity, Phase 1 done, Phases 2–3, 20 products / 10 categories, WhatsApp) · live page moain2026.github.io/zawada-al-dukkan (read 2026-09-23). No customer or sales figures — the project is a Phase 1 prototype. -->
