# Exercise 00: The baseline

## The problem

Before you speed something up, you need to know **how slow it is** and **why it is slow**.
There are two very different kinds of "slow":

- **Waiting** (I/O-bound): the program asks someone else (network, disk, database) and sits idle until the answer comes.
- **Computing** (CPU-bound): the program is busy doing math the whole time.

Every tool in this lab fixes only *one* of these. So step one is learning to tell them apart.

## Read first

Open `lab/workloads.py` and read `fake_server_check` and `count_primes`.
Before going further, answer for yourself: which one is waiting, and which one is computing?

## Predict (write this in LEARNING_LOG.md before running anything)

1. Each server check takes 0.1, 0.2 or 0.3 seconds. How long will **20 checks** take in total, one after another?
2. While the server checks run, what will `htop` show for CPU usage? And during `count_primes`?

## Build

In `runner.py`, implement `run_sequential(func, items)`:

- call `func(item)` for each item, one at a time
- return the results as a list, **in the same order** as `items`

Yes, this one is easy. It's the reference point everything else is compared to.

## Check

```bash
pytest tests/test_ex00_baseline.py -v
```

## Run

```bash
python -m exercises.ex00_baseline.run
```

Run `htop` in a second terminal (or a second SSH session to your VM) and watch it.

## Explain (in LEARNING_LOG.md, in your own words)

- Your measured times vs. your prediction. Why the difference, if any?
- During the server checks the program is "busy" for seconds, yet the CPU is almost idle. What is it actually doing?
- If you had 4 CPU cores, would more cores make the *server checks* faster? Would they make *count_primes* faster? Don't test this yet. Write your guess; exercises 01–03 will prove you right or wrong.
