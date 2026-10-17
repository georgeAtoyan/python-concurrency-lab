"""
Exercise 05: asyncio.

Read exercises/ex05_asyncio/README.md first.
"""

from __future__ import annotations

import asyncio  # noqa: F401

from lab.workloads import fake_server_check_async  # noqa: F401


async def check_all(hosts: list[str]) -> list[dict]:
    """
    Run fake_server_check_async(host) for every host CONCURRENTLY
    on one event loop (one thread). Return results in the same order as hosts.
    """
    # TODO: your code here
    raise NotImplementedError("Your turn! See README.md in this folder.")


def run_with_asyncio(hosts: list[str]) -> list[dict]:
    """
    Normal (non-async) entry point: start an event loop, run check_all(hosts)
    on it, and return the results.
    """
    # TODO: your code here
    raise NotImplementedError("Your turn! See README.md in this folder.")


async def check_all_limited(hosts: list[str], limit: int = 50) -> list[dict]:
    """
    STRETCH: like check_all, but never more than `limit` checks in flight
    at the same time. Hint: asyncio.Semaphore.
    """
    # TODO (stretch): your code here
    raise NotImplementedError("Stretch goal, optional.")
