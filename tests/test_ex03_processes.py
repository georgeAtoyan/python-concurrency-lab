import os
import time

from lab.workloads import count_primes, fake_server_check, make_hosts, whoami
from exercises.ex03_processes.runner import run_with_processes, run_with_thread_pool


def test_thread_pool_keeps_order():
    assert run_with_thread_pool(lambda x: x * x, [3, 1, 2], workers=3) == [9, 1, 4]


def test_thread_pool_is_concurrent():
    start = time.perf_counter()
    run_with_thread_pool(fake_server_check, make_hosts(20), workers=20)
    assert time.perf_counter() - start < 1.0


def test_thread_pool_respects_worker_count():
    # 4 tasks of ~0.2-0.3 s with only 1 worker must take at least ~0.8 s
    start = time.perf_counter()
    run_with_thread_pool(fake_server_check, make_hosts(4), workers=1)
    assert time.perf_counter() - start > 0.7, "workers parameter seems to be ignored"


def test_processes_give_correct_results_in_order():
    limits = [5000, 1000, 3000]
    assert run_with_processes(count_primes, limits) == [count_primes(n) for n in limits]


def test_processes_run_outside_this_process():
    pids = run_with_processes(whoami, range(4), workers=2)
    assert os.getpid() not in pids, "work ran in the main process, not in worker processes"


def test_processes_empty_input():
    assert run_with_processes(count_primes, []) == []
