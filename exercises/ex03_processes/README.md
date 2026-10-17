# Exercise 03: Processes for computing

## The problem

Exercise 02 showed that in standard CPython, threads take turns holding the GIL,
so CPU-heavy work doesn't get faster with threads. But your machine has several cores sitting idle.

## The idea

Each **process** has its own Python interpreter, its own memory, and **its own GIL**.
Four processes can genuinely run on four cores at the same moment. That's real parallelism.

The price: processes don't share memory. Every argument you send to a worker and every result
it sends back must be **serialized** (pickled), copied between processes, and unpickled.

## Meet concurrent.futures

In ex01 you built threads (and maybe a pool) by hand. `concurrent.futures` gives you
ready-made pools with **the same interface** for threads and processes:
`ThreadPoolExecutor` and `ProcessPoolExecutor`.

## Predict (LEARNING_LOG.md)

For each part of `run.py`, predict which line is fastest and roughly by how much:

- **Part A:** 4 big CPU tasks: sequential vs. thread pool vs. process pool
- **Part B:** 20,000 *tiny* CPU tasks: sequential vs. process pool
- **Part C:** 20 server checks: thread pool vs. process pool

## Build

In `runner.py`, implement both functions with the executors.
Read: [concurrent.futures docs](https://docs.python.org/3/library/concurrent.futures.html), especially `Executor.map`.

Notice when you're done how similar your two functions look. That similarity is the whole point of the module.

## Check and run

```bash
pytest tests/test_ex03_processes.py -v
python -m exercises.ex03_processes.run
```

## Break it on purpose

1. Pass a `lambda` to `run_with_processes` instead of a normal function. Read the error carefully. What couldn't be done to the lambda?
2. In `run.py`, temporarily remove the `if __name__ == "__main__":` guard and call `main()` directly.
   On Linux it may still work; on Windows/macOS it breaks badly. Research **"fork vs spawn"** and explain why.

## Explain (LEARNING_LOG.md)

- Why did processes win Part A?
- Why did processes **lose** Part B? Where did the time go?
- Part C: processes "worked" for I/O but how did they compare to threads, and why would you not choose them?
- Fill in this sentence: *"Use threads when ___, use processes when ___, because ___."*

## Stretch

`Executor.map` has a `chunksize` parameter. Re-run Part B with `chunksize=500` (add a parameter to
your function if needed). Explain the change in terms of how many times data crosses between processes.
