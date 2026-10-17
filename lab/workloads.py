"""
Workloads used across the exercises.

You don't need to EDIT this file, but you SHOULD read it before exercise 00.
Knowing what a function spends its time on (waiting vs. computing) is half
of every concurrency decision you will ever make.
"""

from __future__ import annotations

import asyncio
import os
import time
import zlib


# ---------------------------------------------------------------------------
# I/O-bound work: the function spends almost all its time WAITING.
# time.sleep() stands in for "waiting for a server to answer over the network".
# ---------------------------------------------------------------------------

def _latency_for(host: str) -> float:
    """Deterministic fake network latency: 0.1, 0.2 or 0.3 seconds per host."""
    return 0.1 + (zlib.crc32(host.encode()) % 3) * 0.1


def _is_up(host: str) -> bool:
    """Deterministic fake health result: roughly 1 in 10 hosts is 'down'."""
    return zlib.crc32(host.encode()) % 10 != 0


def fake_server_check(host: str) -> dict:
    """Pretend to ask `host` whether it is healthy (blocking version)."""
    latency = _latency_for(host)
    time.sleep(latency)  # the CPU does nothing here, it just waits
    return {"host": host, "up": _is_up(host), "latency": latency}


async def fake_server_check_async(host: str) -> dict:
    """Same as fake_server_check, but written for asyncio (non-blocking wait)."""
    latency = _latency_for(host)
    await asyncio.sleep(latency)  # "wake me up later, run someone else meanwhile"
    return {"host": host, "up": _is_up(host), "latency": latency}


def make_hosts(n: int) -> list[str]:
    """Return n fake hostnames: server-0000.lab.local, server-0001.lab.local, ..."""
    return [f"server-{i:04d}.lab.local" for i in range(n)]


# ---------------------------------------------------------------------------
# CPU-bound work: the function never waits, it just computes.
# ---------------------------------------------------------------------------

def count_primes(limit: int) -> int:
    """Count prime numbers below `limit` using slow trial division (on purpose)."""
    count = 0
    for n in range(2, limit):
        is_prime = True
        i = 2
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            count += 1
    return count


# ---------------------------------------------------------------------------
# Small helper used by the tests to see WHICH process ran a function.
# It lives here (not in a test file) so child processes can import it.
# ---------------------------------------------------------------------------

def whoami(_: object = None) -> int:
    """Return the process ID (PID) of the process running this function."""
    return os.getpid()
