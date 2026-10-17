"""
Run from the repo root:

    python -m exercises.ex04_race_condition.run
"""

from lab.timer import timed
from exercises.ex04_race_condition.counter import SafeCounter, UnsafeCounter, hammer

THREADS = 20
EACH = 500


def main() -> None:
    expected = THREADS * EACH
    print(f"\nExercise 04: {THREADS} threads x {EACH} increments, expected {expected}\n")

    for attempt in range(1, 4):
        result = hammer(UnsafeCounter(), THREADS, EACH)
        lost = expected - result
        print(f"  UnsafeCounter attempt {attempt}: {result:>6}  (lost {lost} increments)")

    print()
    with timed("SafeCounter"):
        result = hammer(SafeCounter(), THREADS, EACH)
    print(f"  SafeCounter: {result}  {'correct' if result == expected else 'WRONG'}")


if __name__ == "__main__":
    main()
