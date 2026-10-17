"""A tiny stopwatch so every exercise measures time the same way."""

from __future__ import annotations

import time
from contextlib import contextmanager


@contextmanager
def timed(label: str):
    """
    Measure how long the code inside the `with` block takes.

        with timed("20 server checks") as t:
            do_something()
        print(t["seconds"])   # you can also read the number afterwards
    """
    result: dict = {}
    start = time.perf_counter()
    try:
        yield result
    finally:
        result["seconds"] = time.perf_counter() - start
        print(f"  {label:<45} {result['seconds']:7.2f} s")
