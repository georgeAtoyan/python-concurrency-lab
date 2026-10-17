# Python Concurrency Lab

A hands-on lab where I learn **concurrency, parallelism, processes, threads and asyncio in Python**
by building, measuring and breaking things, not by reading about them.

Every exercise starts with a **real problem**, asks me to **predict** what will happen,
then has me **build** the solution myself, **measure** it, **break** it on purpose, and **explain** the result.
It ends with a real tool: a concurrent TCP port checker for my homelab.

> No solutions are included. All code under `exercises/` is mine.
> My predictions, measurements and explanations are in [LEARNING_LOG.md](LEARNING_LOG.md).

## What's covered

| # | Exercise | The problem it solves | Concepts |
|---|---|---|---|
| 00 | [Baseline](exercises/ex00_baseline/) | How slow is it, and *why*? | I/O-bound vs. CPU-bound |
| 01 | [Threads for waiting](exercises/ex01_threads_io/) | Waits add up when done one by one | `threading.Thread`, `start`/`join`, thread pools |
| 02 | [The GIL experiment](exercises/ex02_gil/) | Why don't threads speed up math? | GIL, concurrency vs. parallelism |
| 03 | [Processes](exercises/ex03_processes/) | Using all CPU cores | `ProcessPoolExecutor`, pickling cost, fork vs. spawn |
| 04 | [Race conditions](exercises/ex04_race_condition/) | Shared memory corrupts data | race conditions, `Lock`, deadlock |
| 05 | [asyncio](exercises/ex05_asyncio/) | Threads don't scale to 10,000 connections | event loop, `async`/`await`, `gather`, `Semaphore` |
| 06 | [Port checker](exercises/ex06_port_checker/) | Real tool: check a whole lab's services fast | choosing an approach and defending it |

## Progress

- [ ] 00 Baseline
- [ ] 01 Threads for waiting
- [ ] 02 The GIL experiment
- [ ] 03 Processes
- [ ] 04 Race conditions
- [ ] 05 asyncio
- [ ] 06 Port checker (capstone)

## Results on my machine

<!-- Fill in as you go. Machine: e.g. Ubuntu 24.04 VM, 4 vCPU, Python 3.12 -->

| Workload | Sequential | Threads | Processes | asyncio |
|---|---|---|---|---|
| 20 server checks (I/O) | | | | |
| 4 × count_primes (CPU) | | | | — |
| 1,000 server checks (I/O) | — | | — | |

## Running it

```bash
git clone https://github.com/<your-username>/python-concurrency-lab.git
cd python-concurrency-lab
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt

pytest tests/test_ex00_baseline.py -v      # tests for one exercise
python -m exercises.ex00_baseline.run      # run its experiment
```

Requires Python 3.10+. Standard library only (pytest for tests).

## How I'm working through it

See [HOW_TO_LEARN.md](HOW_TO_LEARN.md): predict → build → test → measure → break → explain → commit.
