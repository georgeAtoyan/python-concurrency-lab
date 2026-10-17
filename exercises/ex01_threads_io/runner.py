"""
Exercise 01: threads for I/O-bound work.

Read exercises/ex01_threads_io/README.md first.
"""

from __future__ import annotations

import threading  # noqa: F401  (you will need this)
from typing import Any, Callable, Iterable


def run_with_threads(func: Callable[[Any], Any], items: Iterable[Any]) -> list[Any]:
    """
    Run func(item) for every item, ONE THREAD PER ITEM, using threading.Thread.

    Return the results in the same order as `items`
    (NOT in the order the threads happen to finish).

    Rule: use threading.Thread directly. No ThreadPoolExecutor yet.
    """
    # TODO: your code here
    raise NotImplementedError("Your turn! See README.md in this folder.")


def run_with_threads_limited(
    func: Callable[[Any], Any], items: Iterable[Any], workers: int = 10
) -> list[Any]:
    """
    STRETCH GOAL (optional, do it after the main exercise is green).

    Same contract as run_with_threads, but use exactly `workers` threads,
    no matter how many items there are. Each worker keeps taking the next
    job until no jobs are left. Hint: queue.Queue.
    """
    # TODO (stretch): your code here
    raise NotImplementedError("Stretch goal, optional.")
