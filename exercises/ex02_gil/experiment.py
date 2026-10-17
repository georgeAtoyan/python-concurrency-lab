"""
Exercise 02: the GIL experiment. YOU write this experiment.

Run from the repo root:

    python -m exercises.ex02_gil.experiment

There are no tests for this exercise. The "test" is whether your measurement
matches your prediction, and whether you can explain why or why not.
"""

import os
import sys

from lab.timer import timed  # noqa: F401
from lab.workloads import count_primes  # noqa: F401
from exercises.ex00_baseline.runner import run_sequential  # noqa: F401
from exercises.ex01_threads_io.runner import run_with_threads  # noqa: F401


def main() -> None:
    print("\nExercise 02: do threads speed up computing?\n")
    print(f"  CPU cores on this machine: {os.cpu_count()}")
    print(f"  Python: {sys.version.split()[0]}")
    gil_check = getattr(sys, "_is_gil_enabled", None)
    print(f"  GIL enabled: {gil_check() if gil_check else True}\n")

    limits = [200_000] * 4  # 4 equal CPU-bound tasks

    # TODO 1: time count_primes over `limits` with run_sequential.
    #         Use `with timed("..."):` like the run.py files in ex00/ex01.

    # TODO 2: time the same thing with run_with_threads.

    # TODO 3 (optional): try 8 tasks instead of 4. Does anything change?


if __name__ == "__main__":
    main()
