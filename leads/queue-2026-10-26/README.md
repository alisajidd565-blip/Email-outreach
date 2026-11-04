# Send queue for 26 Oct 2026: A/B test, 13 new brands

Found 25 Oct via Apollo (AU/NZ/CA, DACH/CEE, US South) + site scrape. Not in known_domains, no Gmail history, MX checked. Instagram stats from Apify (last 10 posts).

- `full-html-7.json`: current full HTML template (4 links, offer, Meta line, price card). Send with `htmlBody`.
- `short-plaintext-6.json`: new short plain-text version (one reel link, free first ad, price card). Send with `body` only.

Purpose: since mail-tester scored 9.8/10, test whether a shorter, plainer email gets more replies than the full one.
Measure: replies per group after 5 days (by 31 Oct).
