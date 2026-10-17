"""
Exercise 03: processes for CPU-bound work (and meeting concurrent.futures).

Read exercises/ex03_processes/README.md first.
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor  # noqa: F401
from typing import Any, Callable, Iterable


def run_with_thread_pool(
    func: Callable[[Any], Any], items: Iterable[Any], workers: int = 10
) -> list[Any]:
    """
    Same job as your ex01 run_with_threads_limited, but using ThreadPoolExecutor.
    Results in the original order.
    """
    # TODO: your code here
    raise NotImplementedError("Your turn! See README.md in this folder.")


def run_with_processes(
    func: Callable[[Any], Any], items: Iterable[Any], workers: int | None = None
) -> list[Any]:
    """
    Run func(item) for every item in a pool of worker PROCESSES.
    workers=None means "one per CPU core" (the executor's default).
    Results in the original order.
    """
    # TODO: your code here
    raise NotImplementedError("Your turn! See README.md in this folder.")
