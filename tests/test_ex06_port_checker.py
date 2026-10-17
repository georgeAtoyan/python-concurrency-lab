import socket
import time

import pytest

from exercises.ex06_port_checker.checker import check_many


@pytest.fixture
def open_port():
    """A real listening TCP socket on localhost for the duration of a test."""
    server = socket.socket()
    server.bind(("127.0.0.1", 0))
    server.listen(50)
    yield server.getsockname()[1]
    server.close()


@pytest.fixture
def closed_port():
    """A port that was free a moment ago and has nothing listening on it."""
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def test_open_port_is_up(open_port):
    assert check_many([("127.0.0.1", open_port)]) == {f"127.0.0.1:{open_port}": True}


def test_closed_port_is_down(closed_port):
    assert check_many([("127.0.0.1", closed_port)]) == {f"127.0.0.1:{closed_port}": False}


def test_unknown_host_is_down_not_a_crash():
    result = check_many([("this-host-does-not-exist.invalid", 80)], timeout=2)
    assert result == {"this-host-does-not-exist.invalid:80": False}


def test_mixed_targets_all_reported(open_port, closed_port):
    targets = [("127.0.0.1", open_port), ("127.0.0.1", closed_port), ("nope.invalid", 1)]
    result = check_many(targets, timeout=2)
    assert result == {
        f"127.0.0.1:{open_port}": True,
        f"127.0.0.1:{closed_port}": False,
        "nope.invalid:1": False,
    }


def test_many_targets_are_checked_concurrently():
    # 10.255.255.1 is normally unroutable, so connections hang until the timeout.
    # 30 targets x 0.5 s sequentially would be 15 s.
    # (If your network rejects it instantly this test passes trivially, which is fine.)
    targets = [("10.255.255.1", 1000 + i) for i in range(30)]
    start = time.perf_counter()
    result = check_many(targets, timeout=0.5)
    elapsed = time.perf_counter() - start
    assert len(result) == 30 and not any(result.values())
    assert elapsed < 4, f"took {elapsed:.1f}s, are targets checked concurrently?"
