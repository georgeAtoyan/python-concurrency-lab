"""
Run from the repo root:

    python -m exercises.ex05_asyncio.run
"""

import asyncio
import threading
import time

from lab.timer import timed
from lab.workloads import fake_server_check, make_hosts
from exercises.ex01_threads_io.runner import run_with_threads
from exercises.ex05_asyncio.runner import check_all_limited, run_with_asyncio


async def bad_check(host: str) -> dict:
    """Looks async. Isn't. (Spot the problem before you run this.)"""
    time.sleep(0.2)
    return {"host": host, "up": True}


async def run_bad(hosts: list[str]) -> list[dict]:
    return await asyncio.gather(*(bad_check(h) for h in hosts))


def main() -> None:
    print("\nExercise 05: asyncio\n")

    hosts = make_hosts(1_000)
    before = threading.active_count()
    with timed("threads, 1,000 hosts (1,000 threads)"):
        run_with_threads(fake_server_check, hosts)
    with timed("asyncio, 1,000 hosts (1 thread)"):
        run_with_asyncio(hosts)

    lots = make_hosts(10_000)
    with timed("asyncio, 10,000 hosts (1 thread)"):
        run_with_asyncio(lots)
    print(f"    threads alive in this process now: {threading.active_count()} (was {before})\n")

    with timed("bad_check, only 10 hosts"):
        asyncio.run(run_bad(make_hosts(10)))

    try:
        with timed("stretch: limited to 50 in flight, 1,000 hosts"):
            asyncio.run(check_all_limited(hosts, limit=50))
    except NotImplementedError:
        print("  (stretch goal not done yet, skipping)")


if __name__ == "__main__":
    main()
