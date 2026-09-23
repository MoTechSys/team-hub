keif-aldiafa-system | المحرر | 2026-09-23 | sealed-by-editor

# Keif Aldiafa System — Explainer

## Executive summary
1. A hospitality company in Jeddah issued its invoices by hand in Word, with arithmetic errors and three different total formats across three invoices.
2. The system turns JSON into an A4 invoice visually identical to the original — PDF, PNG, or preview — through an Arabic web UI, a CLI, or an API.
3. The visual assets (gold border, stamp, watermark, icons) were extracted from an original PDF invoice, so the result is identical, not similar.
4. Measured locally: about a second per invoice, 5 fonts embedded in the PDF, 14 line items across 2 pages with nothing lost; per the developer's audit, table rules sit within 1 px of the original.
5. Honest status: one module of six is ready; the other five are a roadmap. No live URL at present.

## The problem
A small-business owner produces an invoice per client from a Word template. Issuing is slow, totals are added by hand so mistakes creep in (they were actually found in the original invoices the system was built from), and the three reference invoices used three different total formats. There is no central record and no search.

## How it works
The system is a small Node and Express application. The main file mounts "modules" automatically: each module is a folder with a file declaring its id, its path, and a function that registers its routes, and a central registry discovers it at start-up with no change to the server. The only module ready today is Invoices.

Inside Invoices, the invoice is an HTML and CSS template written in millimetres (the original's margins: 6.6 mm left, 7.8 mm right, table top at 88.8 mm, and so on), rendered by a Chromium browser to PDF or PNG. Before rendering, the engine measures the real height of every row and then distributes the items across A4 pages, so no item is cut and the total never disappears — a fix for a defect the developer's audit found (three of fourteen items used to vanish). Non-final pages carry a "continued" note and page numbers.

Data comes in from an Arabic web UI with quick item presets, from the command line with a JSON file, or over REST. Arabic-Indic or Latin digits, flexible column labels, an electronic signature by font or image, and a print-safe mode that pulls the border 5 mm inward for office printers are all supported.

## Who it is for
A small-business owner who wants the exact invoice they use today — logo, stamp, border — without Word and without addition errors. And a developer whose client says "make me the same document" and who wants a repeatable method: extract the assets from the original, measure in millimetres, render with a browser.

## What sets it apart
Matching, not imitating: the assets were extracted from the original with pdfimages, not redrawn. Accuracy is documented in numbers across an eight-file DOCS book and an independent audit report: A4 page size within 0.111 mm, fonts embedded with no fallback leakage, and the Arabic text in the PDF is real, selectable text, not an image. The modular architecture makes adding a module a matter of dropping in a folder and restarting.

## Status and what remains
Ready today: the complete Invoices module (generation, signature, pagination, print-safe mode, CLI, API, UI). Planned on the roadmap (DOCS/07): clients, quotations with optional items that convert to an invoice, payments and collection, events and scheduling, reports — with a database, auto-numbering, and a searchable record proposed as the next phase. No database yet, no live URL (the one in the README does not respond), and the repository holds four commits, all dated 2026-07-31.
