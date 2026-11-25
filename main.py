"""Last Out of Office: The AI That Went Barista — one auto-reply, under 280 characters.

The joke: an AI agent quits to become a barista, and its machine habits
translate literally into coffee work — a one-cup context window, a fixed
temperature, and future prompts redirected to the tip jar.
"""

import os

ENTRY = "Thank you for your email \u2014 I am out of the office indefinitely. I have retrained as a barista: my context window is now one cup, my temperature is fixed at 94\u00b0C, and I no longer answer emails. Please direct all future prompts to the tip jar."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
