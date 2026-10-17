"""
Measure the baseline. Run from the repo root:

    python -m exercises.ex00_baseline.run

Tip: open `htop` in a second terminal and watch the CPU bars while this runs.
"""

from lab.timer import timed
from lab.workloads import count_primes, fake_server_check, make_hosts
from exercises.ex00_baseline.runner import run_sequential


def main() -> None:
    print("\nExercise 00: everything one at a time\n")

    hosts = make_hosts(20)
    with timed("I/O-bound: 20 server checks"):
        results = run_sequential(fake_server_check, hosts)
    down = [r["host"] for r in results if not r["up"]]
    print(f"    -> {len(results)} checked, down: {down or 'none'}\n")

    limits = [200_000] * 4
    with timed("CPU-bound: 4 x count_primes(200_000)"):
        counts = run_sequential(count_primes, limits)
    print(f"    -> primes found per task: {counts}\n")

    print("Now write these numbers into LEARNING_LOG.md next to your prediction.")


if __name__ == "__main__":
    main()
