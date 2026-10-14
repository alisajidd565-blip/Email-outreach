# QZI Outreach Script — find leads, verify, send, log
Written 2026-09-22 from a session that found and emailed 13 verified new
brands in one sitting. Load OUTREACH-BRIEF.md first for identity/rules; this
file is the operating procedure for actually running a batch.

Paste this whole file (or just say "run the outreach script") in a session
that already has OUTREACH-BRIEF.md loaded, optionally naming regions:
"run the outreach script for Poland, Czechia and Mexico."

---

## Step 0 — tools you need
- `firecrawl_search` / `firecrawl_scrape` (web discovery)
- Gmail MCP: `search_threads`, `send_message` (dedup + sending)
- Bash/Python for the dedup set and CSV logging
If firecrawl isn't loaded, `ToolSearch` for it first.

## Step 1 — build the dedup set (once per session)
Pull every domain and email already known, from every CSV in the Portfolio
folder and any Codex prospect exports, into one flat text file:

```bash
python -c "
import csv,re,glob
doms=set()
def add(s):
    s=(s or '').strip().lower()
    if not s: return
    if '@' in s: s=s.split('@')[-1]
    s=re.sub(r'^https?://','',s); s=s.split('/')[0]; s=re.sub(r'^www\.','',s)
    if '.' in s and ' ' not in s and s.isascii(): doms.add(s)
for f in glob.glob('QZI-prospect*.csv')+glob.glob('QZI-tracker*.csv'):
    for r in csv.DictReader(open(f,encoding='utf-8-sig',errors='ignore')):
        for k in ('website','email'): add(r.get(k))
        for m in re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+',' '.join(str(v) for v in r.values())): add(m)
for f in glob.glob('C:/Users/HP/Documents/Codex/**/*prospect*',recursive=True):
    try:
        t=open(f,encoding='utf-8',errors='ignore').read()
        for m in re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+',t): add(m)
        for m in re.findall(r'https?://[\w.-]+',t): add(m)
    except Exception: pass
open('known_domains.txt','w',encoding='utf-8').write('\n'.join(sorted(doms)))
print(len(doms))
"
```
Run this from `Portfolio/`. Expect ~1,900+ domains. This is the single source
of truth for "have we ever touched this brand" — check every candidate
against it before doing anything else with that candidate.

## Step 2 — discover, one region/category query at a time
Call `firecrawl_search` with a narrow query and `excludeDomains` for the
obvious noise (reddit, instagram, facebook, youtube, etsy, amazon and its
country TLDs, pinterest, tiktok, fragrantica, major local marketplaces).
Good query shapes that worked:
- `"handmade beard oil brand <Country>"`
- `"independent niche perfume house <Country> eau de parfum"`
- `"<Country> perfume brand made in <Country>"`

Immediately after each search, call `firecrawl_search_feedback` with the
`searchId`: rate `good`/`partial` and list the URLs that were actually brand
homepages in `valuableSources`. This refunds a credit and costs nothing.

Expect 3–5 real brand homepages per 10 results; the rest are listicles,
retailers, and social posts. Skip anything that isn't the brand's own site.

## Step 3 — dedup candidates before spending any more effort
```bash
python -c "
known=set(open('known_domains.txt',encoding='utf-8').read().split())
c=['candidate1.com','candidate2.co.nz', ...]
new=[d for d in c if not any(k==d or k.endswith('.'+d) or d.endswith('.'+k) for k in known)]
print(new)
"
```
Only proceed with the `new` list.

## Step 4 — get a verified email per new candidate
Cheapest path first, in this order, stopping as soon as one works:
1. `firecrawl_scrape` the domain's `/policies/contact-information` — Shopify
   stores publish a plain-text email here almost every time. Cheapest, most
   reliable source found this session.
2. `/contact`, `/contact-us`, `/pages/contact`, `/pages/contact-us`.
3. `firecrawl_scrape` the homepage with `formats: ["links"]` and grep the
   result for a `mailto:` link.
4. If none of the above surface a plain-text email and the page is only a
   contact FORM (often with reCAPTCHA/hCaptcha), or only gives an Instagram
   handle or WhatsApp number — **stop**. Do not guess `info@`/`hello@`
   patterns; log it in the send-log as "no email, form/DM only" for the human
   to reach manually. This was roughly 30–40% of candidates this session.

Never use `firecrawl_scrape` with `formats: ["json"]` for a single email
lookup — it costs 5 credits per call versus 1 for markdown/links, for the
same result.

## Step 5 — cross-check against Gmail (the CSVs are incomplete)
```
search_threads: in:anywhere (domain1 OR domain2 OR domain3 OR ...)
```
Batch up to ~10 domains per query. Drop anything that already has a thread
(sent, bounced, or replied) before drafting.

## Step 6 — draft and send
Per email, apply every rule from OUTREACH-BRIEF.md's FORMAT RULES section:
- Category-correct video: Café Kiss link for perfume, beard oil ad link for
  beard/grooming.
- One true, specific hook about THEIR brand (a product name, a founding
  detail, a real claim from their own site) — never generic flattery.
- Drive video link: ALWAYS raw plain URL on its own line (never hyperlinked)
  so Gmail renders its inline video preview card. Fiverr link: ALWAYS
  hyperlinked behind anchor text, never raw. (Corrected 2026-09-22; no more
  per-email 50/50 raw/hyperlink choice for the Drive link.)
- Sign off as "— Ali, QZI Labs". Opt-out goes after the signature as a P.S.:
  "P.S. If you'd rather not receive messages like this, reply "unsubscribe"
  and I won't follow up." (Corrected 2026-09-22.)
- THE OFFER, in every email (updated 2026-10-13): first ad with no advance,
  made in their own style from their product photos; if they like it, we
  move forward. Use the standard line from OUTREACH-BRIEF.md ("your first ad
  is on us ... No advance, nothing to pay ... short ads starting at just
  $30"). "From $30" is the only number allowed.
- Samples: The Beast (IG reel), Bad Influence (Drive 4K) and Café Kiss
  (client work), each described as made in that brand's own style.
- Fiverr as one low-key closing line, never the pitch itself.
- No em dashes. Vary structure — don't reuse the last email's shape.
- Different subject line every time.

Send with `send_message` (new thread) or `reply`/`send_message` with
`replyThreadId` (existing thread, e.g. a follow-up nudge).

## Step 7 — log everything, every time
Append each sent row to `QZI-prospects-chrome.csv` with a status string like
`CONTACTED <date> email <batch note> | raw URL|hyperlinked | very affordable|no price`.
Write or append to a dated file in `QZI-send-logs/2026-MM-DD-<batch-name>.md`
listing: brand, country, email, which video, link style, whether price was
mentioned, and a short "skipped/no email" section for anything found but not
emailable.

## What to skip on sight
- Any candidate whose brand is clearly the same company under a different
  country TLD as one already contacted (e.g. `beardoctane.com` vs
  `beardoctane.com.au`) — treat as the same brand, don't double-contact.
- Off-category brands that surface in search noise: skincare-led lines,
  general men's grooming (razors/pomade) without a beard-oil focus, home
  fragrance/candles unless ALI has explicitly reopened that category.
- Retailers and marketplaces, not brands (they don't want an ad made for
  someone else's product).
- Brands already in a live conversation thread of any kind, even a bounce or
  an autoresponder — a bounce means don't retry that address, not "email
  again."

## Realistic yield, for setting expectations
Per 10 fresh search results: about 3–5 real brand homepages, of which about
half publish a usable email. So budget roughly 1 sendable lead per 4–5 raw
search results, and about 10–15 verified sends per hour of this loop running
end to end at normal pace.
