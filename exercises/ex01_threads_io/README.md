# Exercise 01: Threads for waiting

## The problem

20 servers, each answers in about 0.2 seconds. Sequentially that's the **sum** of all the waits (≈ 4 s),
and during almost all of it the CPU does nothing. If you were checking 500 servers in a real
monitoring job, you'd be waiting minutes for no reason.

## The idea

A thread is an independent line of execution inside your program. While thread A waits for
server A, thread B can already be asking server B. The waits **overlap** instead of adding up.

## Predict (LEARNING_LOG.md first!)

1. Sequential, 20 hosts ≈ 4 s. With one thread per host, how long? Why that number and not 0?
2. With **200** hosts and 200 threads, how long?

## Build

In `runner.py`, implement `run_with_threads(func, items)`:

- one `threading.Thread` per item
- results come back **in the original order**
- do **not** use `ThreadPoolExecutor` yet. You'll meet it in ex03 and understand what it does for you once you've done the work by hand.

You'll hit a puzzle right away: **a thread can't `return` a value to you.** Whatever the target
function returns is thrown away. Figuring out where the results should go is part of the exercise.

Docs to read: [threading.Thread](https://docs.python.org/3/library/threading.html#thread-objects), especially `start()` and `join()`.

## Check and run

```bash
pytest tests/test_ex01_threads_io.py -v
python -m exercises.ex01_threads_io.run
```

## Break it on purpose (predict first, then try, then undo)

1. Delete the `join()` calls. What does the function return now? Why?
2. Call `t.run()` instead of `t.start()`. How long does it take now? Why?
3. Call `start()` and `join()` for each thread **inside the same loop**. How long does it take? Why?

The third one is the most common real-world threading bug. Remember it.

## Explain (LEARNING_LOG.md)

- Why did total time become roughly the **slowest single task**, not the sum?
- What does each thread spend most of its life doing?
- What exactly does `join()` guarantee?

## Stretch: limit the threads

One thread per item is fine for 200. For 100,000 it'd eat memory and the OS would spend its time
switching between threads. Implement `run_with_threads_limited(func, items, workers)` with exactly
`workers` threads that keep pulling jobs from a `queue.Queue`.

What you just built is a **thread pool**, which is the thing `ThreadPoolExecutor` gives you for free.
