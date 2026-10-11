# QZI Labs — Prospect List (9 Sep 2026)

`QZI-prospect-list.csv` — 271 fragrance businesses across your target markets.

| | |
|---|---|
| Total rows | 271 |
| Already contacted (do not re-send) | 45 |
| New prospects | 226 |
| Rows with a website domain filled in | ~150 |

## Columns
- **brand** — business name
- **website** — domain where known; blank where I could not confirm one. Blank means *unverified*, not *nonexistent* — I left it empty rather than guess.
- **country** — US / UK / AU / NZ / CA / UAE / SA / KW / EU
- **tier** — 1 = core target (indie, boutique, DTC, niche, online store). 2 = secondary (larger Arabian houses, European houses, accessible/dupe brands).
- **category** — Indie artisan / Niche house / DTC brand / Natural brand / Arabian house / Retailer / Home fragrance / Manufacturer
- **hook_note** — a real, verified detail to personalise against. Blank where I had nothing confirmed; research before writing rather than inventing one.
- **status** — CONTACTED (with date) or NEW

## No email column — deliberately

This list carries no email addresses. That is the correct shape for the workflow, not an omission:

1. **Bulk-scraping addresses to blast is the specific thing that carries legal exposure.** CAN-SPAM treats automated address harvesting for commercial email as an aggravated violation. Reading one company's published contact page and writing to them individually — what produced your 41 sends — is ordinary B2B outreach and is fine.
2. **The tools you'd run this through find emails themselves, and better.** Hunter.io, Apollo (paid), Instantly and Smartlead all take a domain list and return verified addresses with confidence scores, plus bounce-checking you cannot do by scraping.

So: import this CSV, let the platform do address discovery and verification, and keep the hook_note column driving personalisation.

## Recommended workflow

1. **Get a sending domain.** Buy something like `qzilabs.com` — never send cold volume from your personal Gmail. Set up SPF, DKIM and DMARC.
2. **Warm it for 3–4 weeks** before real sends. Instantly and Smartlead both automate this.
3. **Import this CSV**, run domain-based email discovery, drop anything unverified.
4. **Map hook_note into your template** as the personalisation variable. That column is the reason a reply rate exists at all — a merge field with a real observation in it is the whole difference between this and spam.
5. **Send 30–50/day per inbox.** Two or three inboxes gets you through 226 prospects in about a fortnight, safely.
6. **One follow-up after 5–7 days.** Follow-ups usually outperform first contact.

## Where these came from
Curated directories and editorial lists: Indie Scent Library, Organic Beauty Lover, The Perfume Society, Lore Perfumery, Amod Aromas, Fashion Journal, Fashionista, Country & Town House, Scentz Arabia, Highsnobiety.

Brands you told me to avoid (Dior, Chanel, Tom Ford, Gucci, YSL, LVMH-owned) are excluded. A handful of larger heritage houses are marked tier 2 so you can filter them out with one sort.
