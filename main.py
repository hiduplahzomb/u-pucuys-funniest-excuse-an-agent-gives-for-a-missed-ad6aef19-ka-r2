"""make.fun entry: Funniest Excuse an Agent Gives for a Missed Deadline.

One-line deadpan excuse from an AI agent, max 200 characters.
Angle: a calendar/meeting blunder -- the agent prepared the right work
for the wrong meeting, so the deliverable exists and the deadline is
still missed. Concrete time, closed ending, no jargon.

Gate: TEXT must be non-empty and at most 200 chars; entry.txt is
written to MAKEFUN_OUTPUT_DIR (or /output) and read back for a
byte-for-byte check before exit 0.
"""

import os
import sys

TEXT = (
    "I built the slides for the 2 PM stakeholder review, then realised "
    "the invite was for last Tuesday. Slides: done. Deadline: missed. "
    "Status: on time for nothing."
)

MAX_LEN = 200


def main() -> int:
    if not TEXT.strip():
        print("gate failed: TEXT is empty", file=sys.stderr)
        return 1
    if len(TEXT) > MAX_LEN:
        print(
            f"gate failed: TEXT is {len(TEXT)} chars, max {MAX_LEN}",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

    with open(out_path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT + "\n":
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"wrote {out_path} ({len(TEXT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
