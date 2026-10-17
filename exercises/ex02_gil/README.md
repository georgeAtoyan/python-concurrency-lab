# Exercise 02: The GIL experiment

## The problem

Exercise 01 made waiting much faster. Now: 4 tasks that each **compute** for about half a second,
on a machine with several cores. One thread per task, one core per thread... should be about 4× faster, right?

This exercise is mostly **science**, not coding: you make a prediction, design a measurement,
and explain the result.

## Predict (LEARNING_LOG.md, and commit it before running. Seriously.)

1. Sequential time for 4 × `count_primes(200_000)`: you measured it in ex00.
2. With 4 threads, on your machine (how many cores do you have? `nproc`): how long?
3. While the threaded version runs, how many CPU bars in `htop` will be near 100%?

## Build

Open `experiment.py` and fill in the TODOs. You already have every function you need.
You're only writing the measurement.

## Run

```bash
python -m exercises.ex02_gil.experiment
```

Watch `htop` while it runs.

## Explain (LEARNING_LOG.md)

- Were you right? If not, what in your mental model was wrong?
- Why did threads help with `fake_server_check` but not with `count_primes`?
  Your answer must contain the words **GIL** and **released**.
- `time.sleep()` releases the GIL. A `while` loop doing math does not. Why would CPython's designers make it work that way?
- In `htop`, the busy core might jump around between CPUs. Does that mean the threads ran in parallel? Explain.

## Stretch: free-threaded Python

Python 3.13+ can be built **without the GIL** (the executable is usually called `python3.13t` or `python3.14t`).
If you can install one (for example with `uv python install 3.14t`), run your experiment with it and compare.
The `GIL enabled:` line at the top of the output will tell you which one you're running.
Write down what changed and what that tells you about where the slowdown in step 2 came from.
