# Exercise 04: Race conditions and locks

## The problem

Threads share memory. That's what makes them convenient (no pickling, no copying)
and also what makes them dangerous. When two threads do *read → change → write*
on the same variable, their steps can interleave and updates silently disappear.
No error, no crash, just wrong numbers. In a real system that might be a wrong balance,
a duplicate order, or a corrupted counter in your monitoring.

## Read first

Study `UnsafeCounter` in `counter.py`. On paper, write out one exact sequence of steps for
**two** threads that ends with the counter going up by 1 instead of 2. Put it in your log.

## Predict (LEARNING_LOG.md)

20 threads × 500 increments = 10,000 expected.

1. What will `UnsafeCounter` end at? Same number every run?
2. How much slower will `SafeCounter` be, and why would it be slower at all?

## Build

In `counter.py`:

1. `hammer(counter, n_threads, increments_per_thread)`: you've done this pattern in ex01.
2. `SafeCounter`: same three steps, **keep the `time.sleep(0)`**, but make it correct.
   Read: [threading.Lock](https://docs.python.org/3/library/threading.html#lock-objects).

Do `hammer` first. The tests will show you `UnsafeCounter` actually losing updates before you fix anything.

## Check and run

```bash
pytest tests/test_ex04_race_condition.py -v
python -m exercises.ex04_race_condition.run
```

## Break it on purpose

1. Move the lock so it only protects the WRITE step (step 3). Predict, run, explain.
2. Remove `time.sleep(0)` from `UnsafeCounter` (temporarily, then restore it).
   Does the bug disappear? Does that mean the code became correct? Think about this one carefully.

## Explain (LEARNING_LOG.md)

- Your two-thread interleaving from "Read first", and how the lock prevents it.
- Why was `SafeCounter` slower? What did the lock turn your threads back into, inside that section?
- "The GIL already makes Python thread-safe." True or false? Use this exercise as evidence.

## Stretch: deadlock

Write `deadlock.py` yourself: two accounts, each with its own lock. Thread 1 transfers A→B
(lock A, then lock B), thread 2 transfers B→A (lock B, then lock A). Use `join(timeout=3)`
and `is_alive()` to detect that they got stuck (otherwise your terminal hangs).
Then fix it by making both threads acquire locks **in the same order**, and explain why that works.
