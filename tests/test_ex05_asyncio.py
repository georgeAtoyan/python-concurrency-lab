import asyncio
import inspect
import threading
import time

import pytest

from lab.workloads import make_hosts
from exercises.ex05_asyncio.runner import check_all, check_all_limited, run_with_asyncio


def test_check_all_is_a_coroutine_function():
    assert inspect.iscoroutinefunction(check_all)


def test_results_in_host_order():
    hosts = make_hosts(30)
    results = run_with_asyncio(hosts)
    assert [r["host"] for r in results] == hosts


def test_thousand_hosts_are_concurrent():
    start = time.perf_counter()
    results = run_with_asyncio(make_hosts(1_000))
    elapsed = time.perf_counter() - start
    assert len(results) == 1_000
    assert elapsed < 1.5, f"took {elapsed:.2f}s"


def test_uses_a_single_thread():
    before = threading.active_count()
    run_with_asyncio(make_hosts(200))
    assert threading.active_count() == before, "asyncio should not need extra threads here"


def test_stretch_limited():
    hosts = make_hosts(100)
    try:
        start = time.perf_counter()
        results = asyncio.run(check_all_limited(hosts, limit=10))
    except NotImplementedError:
        pytest.skip("stretch goal not implemented yet")
    elapsed = time.perf_counter() - start
    assert [r["host"] for r in results] == hosts
    # 100 tasks of 0.1-0.3 s, 10 at a time, must take noticeably longer than one wave
    assert elapsed > 1.0, "limit doesn't seem to be applied"
