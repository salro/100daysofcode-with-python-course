import itertools
import time
import sys
import random


def traffic():
    """Show an animated spinner while we sleep."""
    light = itertools.cycle(["red", "amber", "green"])
    while True:
        # '\r' is carriage return: return cursor to the start of the line.
        sys.stdout.write('\r' + next(light))  # no newline
        sys.stdout.flush()
        zeit = random.randint(1,5)
        time.sleep(zeit)
    print()


if __name__ == "__main__":
    traffic()
