"""
Run from the repo root:

    python -m exercises.ex01_threads_io.run
"""

from lab.timer import timed
from lab.workloads import fake_server_check, make_hosts
from exercises.ex00_baseline.runner import run_sequential
from exercises.ex01_threads_io.runner import run_with_threads, run_with_threads_limited


def main() -> None:
    print("\nExercise 01: threads for waiting\n")

    hosts = make_hosts(20)
    with timed("sequential, 20 hosts"):
        run_sequential(fake_server_check, hosts)
    with timed("threads,    20 hosts"):
        run_with_threads(fake_server_check, hosts)

    many = make_hosts(200)
    with timed("threads,   200 hosts"):
        run_with_threads(fake_server_check, many)

    try:
        with timed("limited (10 workers), 200 hosts"):
            run_with_threads_limited(fake_server_check, many, workers=10)
    except NotImplementedError:
        print("  (stretch goal not done yet, skipping the limited version)")


if __name__ == "__main__":
    main()
