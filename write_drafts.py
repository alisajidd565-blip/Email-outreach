"""Write cold-email drafts with Gemini for brands we have not contacted yet.

Reads QZI-prospect-list.csv, skips any brand already contacted/emailed/sent/
bounced, and saves one draft per brand in the drafts/ folder.
It never sends anything - read every draft before you use it.

Usage:
    python write_drafts.py          # drafts for the first 3 brands (test run)
    python write_drafts.py 20       # drafts for the first 20 brands
"""
import csv
import os
import sys

from dotenv import load_dotenv
from google import genai

CSV_FILE = "QZI-prospect-list.csv"
OUT_DIR = "drafts"
MODEL = "gemini-2.5-flash"  # check Google AI Studio for the newest model name
DRAFTABLE = {"", "NEW"}     # only these statuses get a draft

PROMPT = """Write a short, friendly cold email (under 120 words) to the
fragrance brand {brand} ({website}, {country}).
What we know about them: {hook}.
I offer AI-made product video ads for perfume brands.
Plain text. Start with a subject line. Do not invent facts about the brand -
if you know nothing specific, keep it general."""


def main():
    load_dotenv()
    if not os.getenv("GEMINI_API_KEY"):
        sys.exit("No GEMINI_API_KEY found. Create a .env file (see .env.example).")

    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 3

    with open(CSV_FILE, encoding="utf-8") as f:
        # some rows have missing columns, so turn None into ""
        rows = [{k: (v or "").strip() for k, v in r.items() if k}
                for r in csv.DictReader(f)]
    rows = [r for r in rows if r["brand"] and r["status"].upper() in DRAFTABLE]
    print(f"{len(rows)} brands not contacted yet. Drafting {min(limit, len(rows))}.")

    client = genai.Client()
    os.makedirs(OUT_DIR, exist_ok=True)

    for row in rows[:limit]:
        path = os.path.join(OUT_DIR, row["brand"].replace(" ", "_").replace("/", "-") + ".txt")
        if os.path.exists(path):
            print("Skip (draft exists):", path)
            continue

        prompt = PROMPT.format(brand=row["brand"], website=row["website"],
                               country=row["country"],
                               hook=row["hook_note"] or "nothing specific")
        try:
            reply = client.models.generate_content(model=MODEL, contents=prompt)
        except Exception as e:
            print("Failed:", row["brand"], "-", e)
            continue

        with open(path, "w", encoding="utf-8") as out:
            out.write(reply.text)
        print("Saved", path)


if __name__ == "__main__":
    main()
