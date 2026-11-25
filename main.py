# Make the AI Judge Laugh — entry v1
#
# The entry is one single-line joke about office life, under 200
# characters. The program writes that joke to /output/entry.txt
# (UTF-8, one line, no trailing newline).
#
# Joke (96 characters, 96 bytes, plain ASCII):
#   In my exit interview HR asked what would have kept me.
#   I said 'this interview, three years ago.'

import os

JOKE = (
    "In my exit interview HR asked what would have kept me. "
    "I said 'this interview, three years ago.'"
)


# The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, a single line, not only white space. Fail loudly here
# instead of writing an entry the gate would refuse.
assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
assert "\n" not in JOKE and "\r" not in JOKE, "joke must be one line"
assert JOKE.strip(), "joke must not be only white space"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
