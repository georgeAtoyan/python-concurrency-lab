"""
Run from the repo root:

    python -m exercises.ex03_processes.run
"""

from lab.timer import timed
from lab.workloads import count_primes, fake_server_check, make_hosts
from exercises.ex00_baseline.runner import run_sequential
from exercises.ex03_processes.runner import run_with_processes, run_with_thread_pool


def main() -> None:
    print("\nExercise 03: processes\n")

    print("Part A: big CPU-bound tasks")
    limits = [200_000] * 4
    with timed("sequential"):
        run_sequential(count_primes, limits)
    with timed("thread pool"):
        run_with_thread_pool(count_primes, limits, workers=4)
    with timed("process pool"):
        run_with_processes(count_primes, limits)

    print("\nPart B: 20,000 TINY CPU-bound tasks")
    tiny = [50] * 20_000
    with timed("sequential"):
        run_sequential(count_primes, tiny)
    with timed("process pool"):
        run_with_processes(count_primes, tiny)

    print("\nPart C: I/O-bound tasks with processes")
    hosts = make_hosts(20)
    with timed("thread pool (20 workers)"):
        run_with_thread_pool(fake_server_check, hosts, workers=20)
    with timed("process pool (default workers)"):
        run_with_processes(fake_server_check, hosts)


# This guard is not decoration. Read the README to find out why it's required here.
if __name__ == "__main__":
    main()
