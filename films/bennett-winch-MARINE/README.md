# MARINE: Bennett Winch spec film (25 s, 1080p, 16:9)

**Sent:** 2026-11-27 to info@bennettwinch.com, subject "MARINE: a film for the Marine Blue Suede Weekender"
(Gmail thread 1a21c7ccfe43e9b6). The film went as a direct link plus an attached still: this Gmail
connector caps attachments at about 3 MB per send, and the film doesn't fit under that.

**Hosted copies (Higgsfield storage, public):**
- HQ, 17.7 MB (link sent to the brand): https://d2ol7oe51mr4n9.cloudfront.net/user_3Fyr3WLZQgOK11yswpUl28uHKup/0b6aa278-7e55-4740-86f7-13e829821ea2.mp4
- Master, 124 MB, CRF16: https://d2ol7oe51mr4n9.cloudfront.net/user_3Fyr3WLZQgOK11yswpUl28uHKup/1f612de3-b48e-48c3-9ca4-7d077e0b240d.mp4
- In repo: `BennettWinch_MARINE_QZI-Labs_1080p.mp4` (9.8 MB, 1080p)

**Concept:** see `../../QZI-demo-film-bennett-winch-MARINE-treatment.md`.
"Marine Blue. Named for the sea. Built to meet it." London tailor's street, then the road north,
then an Atlantic cliff (wave hits, time freezes), then a water-beading macro, then a bothy fireside with the end card.

**Pipeline:** GPT Image 2.6 keyframes (2K, real product photos as references), Sand AI MAGI-2 1080p image-to-video
with native sound effects, ElevenLabs Music v2.5 score (its own cello passage reused as the outro), ffmpeg edit
(`edit.py`, `segments.json`), captions rendered in Chromium (`caps.js`; Montserrat to echo the BW wordmark,
Cormorant Garamond italic), official BW logo from bennettwinch.com.

**Edit:** cuts on music accents at 3.5 / 7.0 / 10.0 / 13.5 s; white flash frame on the wave impact into the time-freeze;
0.5 s dissolve into the fireside; light grade, vignette and grain; mix at -14.7 LUFS, -1.0 dBTP, 3.4 LU loudness range.

**QC:** product details checked in every shot (black leather handles and corners, brass zips and studs, bird logo, navy suede);
the car keyframe was regenerated to fix a wardrobe error (tweed changed to charcoal overcoat and black gloves); the man's face is never shown;
no women anywhere (Ali's instruction); no black frames apart from the intended 0.08 s fade-in.
Known and accepted: he is gloved in London and the car, barehanded at the cliff (reads as gloves taken off).

**Credits:** 94.64 of the 150 budget (8 keyframes, 7 MAGI-2 shots totalling 30 s, 1 music track).
