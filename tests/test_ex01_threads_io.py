import threading
import time

import pytest

from lab.workloads import fake_server_check, make_hosts
from exercises.ex01_threads_io.runner import run_with_threads, run_with_threads_limited


def slow_reverse(x):
    """Earlier items sleep LONGER, so threads finish in reverse order."""
    time.sleep(0.05 * (5 - x))
    return x * 10


def test_results_keep_input_order_even_if_threads_finish_out_of_order():
    assert run_with_threads(slow_reverse, [0, 1, 2, 3, 4]) == [0, 10, 20, 30, 40]


def test_empty_input():
    assert run_with_threads(slow_reverse, []) == []


def test_waits_overlap():
    # 20 hosts sequentially take about 4 s. Concurrently: about the slowest one (0.3 s).
    start = time.perf_counter()
    results = run_with_threads(fake_server_check, make_hosts(20))
    elapsed = time.perf_counter() - start
    assert len(results) == 20
    assert elapsed < 1.0, f"took {elapsed:.2f}s, are the threads really running at the same time?"


def test_actually_uses_other_threads():
    main = threading.get_ident()
    idents = run_with_threads(lambda _: threading.get_ident(), range(5))
    assert main not in idents, "func ran in the main thread; did you call start()?"


# ---- stretch goal: skipped until you implement it --------------------------

def _limited_or_skip(*args, **kwargs):
    try:
        return run_with_threads_limited(*args, **kwargs)
    except NotImplementedError:
        pytest.skip("stretch goal not implemented yet")


def test_stretch_limited_keeps_order():
    assert _limited_or_skip(slow_reverse, [0, 1, 2, 3, 4], workers=2) == [0, 10, 20, 30, 40]


def test_stretch_limited_uses_at_most_n_threads():
    idents = _limited_or_skip(lambda _: (time.sleep(0.01), threading.get_ident())[1], range(40), workers=4)
    assert len(set(idents)) <= 4


def test_stretch_limited_is_concurrent():
    start = time.perf_counter()
    _limited_or_skip(fake_server_check, make_hosts(40), workers=20)
    assert time.perf_counter() - start < 1.5
