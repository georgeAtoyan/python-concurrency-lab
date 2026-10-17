"""
Exercise 04: race conditions and locks.

Read exercises/ex04_race_condition/README.md first.
"""

from __future__ import annotations

import threading  # noqa: F401
import time


class UnsafeCounter:
    """A counter that looks correct. Do not edit this class: study it."""

    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        current = self.value      # step 1: READ
        time.sleep(0)             # step 2: let other threads run right here
                                  #         (simulates being switched out at the worst moment)
        self.value = current + 1  # step 3: WRITE


class SafeCounter:
    """
    Same behaviour and same three steps as UnsafeCounter (keep the sleep(0)!),
    but correct when many threads call increment() at the same time.
    """

    def __init__(self) -> None:
        # TODO: your code here
        raise NotImplementedError("Your turn! See README.md in this folder.")

    def increment(self) -> None:
        # TODO: your code here
        raise NotImplementedError("Your turn! See README.md in this folder.")


def hammer(counter, n_threads: int, increments_per_thread: int) -> int:
    """
    Start `n_threads` threads. Each thread calls counter.increment()
    `increments_per_thread` times. Wait for ALL of them to finish,
    then return counter.value.
    """
    # TODO: your code here
    raise NotImplementedError("Your turn! See README.md in this folder.")
