You are helping me (Ali Sajid, founder of QZI Labs, a cinematic AI ad studio) do WhatsApp outreach to independent brands. Use Claude in Chrome. WhatsApp Web is already logged in on this Chrome.

FILE: whatsapp-leads.csv (in this same folder, 167 brands). Columns:
id, brand, category, country, whatsapp_number, number_source, website, emailed_before, first_message, status, sent_at, notes

TASK: send ONE short first message on WhatsApp to each row whose status is QUEUED, then update the CSV.

HOW TO DO IT
1. Read whatsapp-leads.csv. Work through rows in order of id.
2. For each row, open https://web.whatsapp.com/send?phone=NUMBER (the number without the + sign). Wait until the chat has loaded.
3. Before typing, look at the chat:
   - Any earlier message in it (from me or from them): do NOT send. Set status = ALREADY_CONTACTED.
   - "Phone number shared via url is invalid" or not on WhatsApp: set status = NOT_ON_WHATSAPP.
   - The chat name or profile clearly belongs to a different business or a private person who is not the brand: do NOT send. Set status = WRONG_NUMBER and say what you saw in notes.
4. Otherwise paste the text from the first_message column exactly as written and send it. Set status = SENT and sent_at = the time.
5. Save the CSV after every row, so nothing is lost if Chrome closes.
6. Wait 3 to 4 minutes between brands. Never send faster. Fast sending gets my number banned.
7. Send at most 25 messages in one session. Stop after 25 even if rows are left.
8. If WhatsApp shows any warning, restriction, "too many messages", or logs out: STOP at once and tell me.
9. Do the FIRST brand only, show me the sent message, and wait for me to say "go" before continuing.
10. One message per brand. No follow-ups, no images, no links in the first message.

WHEN DONE: give me a short table: brand, status, time sent. Then tell me how many rows are still QUEUED.

IF A BRAND REPLIES
Never send a reply yourself. Draft the matching reply below in the chat box, leave it unsent, and tell me which brand it's for.
If they say no / stop / not interested: draft nothing, set status = DECLINED, tell me.
If they ask something not covered below: draft nothing, tell me the question.

REPLY A: they're interested ("yes", "sure", "tell me more", "how does it work")
Great, thank you! Here's some of our work. The music in each is written by us for that film:

The Beast (Maison Yusif): https://www.instagram.com/reel/Dd6mWo6CuaY/
Atlas Original: https://drive.google.com/file/d/1itvrPB-_hT69dSw_O2hqnsdql1V64_O4/view?usp=sharing
El Patrón (Maison Yusif): https://drive.google.com/file/d/1Voi9M31p4R8KsMH-YkYWjetsnM2CiXH8/view?usp=sharing

Send me a few photos of the product you'd like featured (phone photos from a few angles are perfect), and one line on the mood you want. I'll make the first ad free. You post it only if you like it, and if it performs well, we talk about next steps.

REPLY B: they ask about price ("how much", "what do you charge", "price list")
Of course. Single ads start at $59 for a short cinematic snippet, $119 for a 15-second ad with music and captions, and $189 for a 15-20 second ad with a story and voice-over. Short films run from $399, and a full 60-second film is $899.
Most brands start with the free ad first, then pick a campaign or a monthly plan, which brings the price per ad down. Happy to send the full price card.

REPLY C: they ask about a monthly plan or a campaign
We do both:
- Campaign: a set of ads built around one launch or season (for example a hero film plus short cut-downs and snippets in the same look), priced as a package.
- Monthly plan: a steady flow of ads every month, from about $429 a month for 4 ads, with the per-ad price dropping as the volume goes up (minimum 3 months).
If you tell me roughly what you'd like to spend each month, I'll put together the best plan for that budget.

REPLY D: they ask "who is Maison Yusif?" or want proof
Maison Yusif Fragrance is a Ghanaian perfume house, named 2026 Fragrance Brand of the Year at the Ghana Beauty Awards. We make their ads, including The Beast: https://www.instagram.com/reel/Dd6mWo6CuaY/

RULES
- Never invent results, client names, view counts or prices beyond what is written here.
- Never call Maison Yusif "the No. 1 perfume brand". Use exactly: "2026 Fragrance Brand of the Year at the Ghana Beauty Awards".
- No unsubscribe or "reply stop" lines.
