"""
ship_it.py

Ship It! — a terminal reaction game.

The build light goes RED, then AMBER, then GREEN.
Press Enter the instant it turns green. Press too early and it's a false start.
The game remembers your best time while you play.
"""

import random
import select
import sys
import time

from colorama import Fore, Style, init

init(autoreset=True)


# ---------- best time ----------

def is_new_best(ms, best):
    """Requirements 9, 10.

    A time is a new best if it's the first one, or faster than the best so far.
    """
    return best is None or ms < best


# ---------- the game ----------

def pressed_enter(seconds):
    """Requirements 4, 5.

    Wait up to `seconds`. Return True if Enter was pressed during the wait.
    """
    ready, _, _ = select.select([sys.stdin], [], [], seconds)
    if ready:
        sys.stdin.readline()
        return True
    return False


def play_round():
    """Requirements 3, 4, 8.

    Run one round. Return the reaction time in ms, or None for a false start.
    """
    print(Fore.RED + "●  RED    - wait for it...")
    if pressed_enter(random.uniform(1.0, 2.0)):
        return None

    print(Fore.YELLOW + "●  AMBER  - get ready...")
    if pressed_enter(random.uniform(1.0, 3.0)):
        return None

    print(Fore.GREEN + Style.BRIGHT + "●  GREEN  - SHIP IT! (press Enter)")
    start = time.perf_counter()
    sys.stdin.readline()
    return round((time.perf_counter() - start) * 1000)


# ---------- main program ----------

def main():
    """Requirements 1, 2, 5, 6, 7. (2 and 7 not built yet.)"""
    print()
    print(Style.BRIGHT + "SHIP IT!  - press Enter the moment the light turns green")
    print()

    best = None

    while True:
        answer = input("Ready? ")
        if answer.strip().lower() == "q":
            break

        ms = play_round()

        if ms is None:
            print(Fore.RED + "False start! Wait for green.")
        elif is_new_best(ms, best):
            best = ms
            print(Fore.CYAN + Style.BRIGHT + f"Shipped in {ms} ms. New best time!")
        else:
            print(Fore.CYAN + f"Shipped in {ms} ms. Best so far: {best} ms")
        print()


if __name__ == "__main__":
    main()
