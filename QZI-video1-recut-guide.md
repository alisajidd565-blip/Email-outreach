# Fixing Portfolio Video 1 (Erba Pura) — step by step

**Read this first.** The label spelling is not the only problem. I mapped all 21 seconds
frame by frame and the bottle itself breaks in three places. You cannot fix that by
re-rendering one shot. The fix is to **re-cut the video using only the shots that hold up.**

Good news: this is a CapCut job. No regeneration, no new credits, about 40 minutes.

---

## What is wrong, second by second

| Time | What is on screen | Verdict |
|---|---|---|
| 0s to 2s | Bottle with limes and lemons, label legible and correct | **KEEP** |
| 3s to 4s | Extreme macro, teal texture, single water droplet. No text at all | **KEEP.** Best shots in the film |
| 5s | Bottle with lilac fabric, label small | **KEEP** |
| 6s | Close up, "ERBA PURA" on the collar | Borderline, keep if it cuts smoothly |
| 7s | Big close up, text above medallion is garbled ("ERNEA COLL SERJTY SANDE") | **CUT** |
| 8s to 9s | Bottle with white petals, medallion small | **KEEP** |
| 10s | Same shot but a chunk is missing from the bottom left of the bottle | **CUT** |
| 11s | Medallion reads **"EREA PURA MAGICA"** and "L'AU DE PARFUM" | **CUT** |
| 12s to 13s | Bottle among orange blossoms | **KEEP** |
| 14s | Close up, reads "SOSPIRO COLLE... EAU DE PARFUM / ERBA PURA MAGICA" | **KEEP**, this one is correct |
| 15s | **Different bottle.** Brighter blue, glossier, narrower, deformed notch | **CUT** |
| 16s | Bottle is semi transparent, cap deformed | **CUT** |
| 17s | Bottle lying down, top view | Keep if it cuts smoothly |
| 18s | Bottle with blossoms, label legible and correct | **KEEP** |
| 19s | Small bottle, wide shot | **KEEP** |
| 20s | QZI logo end card | **CUT** (see below) |

**The core issue:** between 10s and 16s the product changes shape, changes colour, loses a
chunk, and goes semi transparent. To a perfume brand, the bottle is the product. A bottle
that morphs mid ad is worse than a misspelled label.

---

## Do this in CapCut

1. Open CapCut, new project, **9:16 vertical**
2. Import `Portfolio Video-1.mp4`, drag to timeline
3. Put the playhead at **7s**, press **Split**. Playhead to **8s**, Split. Select the
   middle piece (7 to 8s), press **Delete**
4. Repeat the same split, split, delete for each bad range: **10 to 12s**, then
   **15 to 17s**, then **20s to end**
5. You should be left with roughly **13 to 14 seconds**. That is a good length. Do not
   pad it back out
6. Between each join add a **cross dissolve of 0.2 to 0.3 seconds** so the cuts do not
   snap. CapCut: click the small white box between two clips, choose Dissolve
7. Re-time the music so the track ends with the video. Easiest way: drag the audio's
   right edge to match, then add a 1 second fade out on the audio
8. **End card:** delete the QZI logo. Replace with 1 second of black, or nothing at all.
   The reel should end on the product, not on your logo
9. Export: **1080x1920, 30fps, high quality**. Name it `ErbaPura-recut-v2.mp4`

---

## Then check your work

Scrub through at quarter speed and ask one question at every frame:

> Is this the same bottle as the last shot? Same colour, same shape, same label?

If the answer is no anywhere, cut that piece too. A shorter clean film beats a longer
broken one. 10 seconds of flawless product is a portfolio. 21 seconds with a morphing
bottle is a liability.

---

## Going forward, so this stops happening

The failure mode is always the same: **AI cannot hold text or fine geometry steady across
shots.** So direct around it.

- **Prefer macro.** Your 3s to 4s droplet shot is the strongest thing in the whole
  portfolio precisely because there is no text and no full silhouette to get wrong
- **Keep the label out of focus** in most shots. Shallow depth of field is what real
  perfume commercials do anyway
- **One hero shot only** where the label is sharp and readable. Generate that shot ten
  times and keep the one that is perfect
- **Never show the full bottle silhouette for more than about 2 seconds.** That is where
  shape drift becomes visible
- Check every generated shot at 100% zoom before it goes in the timeline

---

## Same pass on the other two

**`Portfolio Video-2.mp4` (Velara)** — the type is embossed and correct, so this is your
cleanest asset. One job only: crop 4K landscape to 9:16 vertical.
CapCut: new 9:16 project, import, right click the clip, **Crop**, then reposition so the
bottle stays centred. You have 4K source so there is no quality loss cropping to vertical.

**`Portfolio video-4.mp4` (Wild Self / Autumn Eve)** — retire it. 480x854 is below HD and
the first 8 seconds carry **@COLORCASEUSA**, somebody else's Instagram handle.
The closing product shot of the Autumn Eve bottle is genuinely good, so keep that footage
and rebuild around it at full resolution, but the current file cannot go to a prospect.
