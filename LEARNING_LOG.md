# Learning log

> Written by me, in my own words, while working through the lab.
> Predictions are committed **before** running the code. The git history proves it.

**Machine:** <!-- e.g. Ubuntu 24.04 VM, 4 vCPUs, Python 3.12 -->

---

## Ex 00: Baseline

**Prediction**
- 20 server checks will take:
- CPU during server checks / during count_primes:

**Measured**
- 20 server checks:            s
- 4 x count_primes(200_000):   s

**Why (my explanation)**

**What surprised me**

---

## Ex 01: Threads for waiting

**Prediction**
- 20 hosts with threads:
- 200 hosts with threads:

**Measured**
| Run | Time |
|---|---|
| sequential, 20 hosts | |
| threads, 20 hosts | |
| threads, 200 hosts | |

**Break it on purpose: what happened and why**
1. No `join()`:
2. `run()` instead of `start()`:
3. `start()` + `join()` in the same loop:

**Why (my explanation)**

**What surprised me**

---

## Ex 02: The GIL experiment

**Prediction** (committed before running)
- 4 CPU tasks with 4 threads on my ___ cores:

**Measured**
| Run | Time |
|---|---|
| sequential | |
| threads | |

**Why (must include "GIL" and "released")**

**Was my prediction wrong? Which part of my mental model was wrong?**

---

## Ex 03: Processes

**Prediction**
- Part A (big CPU tasks) winner:
- Part B (20k tiny tasks) winner:
- Part C (I/O tasks) threads vs processes:

**Measured**
| Part | Sequential | Thread pool | Process pool |
|---|---|---|---|
| A | | | |
| B | | | |
| C | | | |

**Why processes lost Part B**

**"Use threads when ___, use processes when ___, because ___."**

**fork vs spawn, and why `if __name__ == "__main__"` matters**

---

## Ex 04: Race conditions

**Two-thread interleaving that loses an update (step by step)**

**Prediction / Measured**
- UnsafeCounter:
- SafeCounter (time):

**Break it on purpose**
1. Lock only around the write:
2. Removing `sleep(0)`:

**"The GIL makes Python thread-safe": true or false, and why**

---

## Ex 05: asyncio

**Prediction / Measured**
| Run | Predicted | Measured |
|---|---|---|
| threads, 1,000 hosts | | |
| asyncio, 1,000 hosts | | |
| asyncio, 10,000 hosts | | |
| bad_check, 10 hosts | | |

**What the event loop is doing during 10,000 "in-progress" checks**

**Why bad_check was slow**

**Why races are rarer in asyncio**

---

## Ex 06: Port checker

See [DECISION.md](exercises/ex06_port_checker/DECISION.md) for the design decision.

**What was harder than expected**

---

## Final summary: my own decision guide

<!-- After finishing everything, write your own version of "which tool when", from memory. -->
