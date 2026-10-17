import time

from exercises.ex04_race_condition.counter import SafeCounter, UnsafeCounter, hammer

THREADS = 20
EACH = 500
EXPECTED = THREADS * EACH


class SlowCounter:
    """Helper: proves hammer() waits for every thread before returning."""

    def __init__(self):
        self.value = 0

    def increment(self):
        time.sleep(0.001)
        self.value += 1


def test_hammer_waits_for_all_threads():
    assert hammer(SlowCounter(), 5, 20) == 100


def test_hammer_reveals_the_race_in_unsafe_counter():
    # If this FAILS, your hammer() probably isn't running threads at the same time.
    result = hammer(UnsafeCounter(), THREADS, EACH)
    assert result < EXPECTED, "no updates were lost, so no real concurrency happened"


def test_safe_counter_starts_at_zero():
    assert SafeCounter().value == 0


def test_safe_counter_is_exact():
    for _ in range(3):
        assert hammer(SafeCounter(), THREADS, EACH) == EXPECTED
