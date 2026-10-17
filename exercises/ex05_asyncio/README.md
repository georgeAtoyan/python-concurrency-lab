# Exercise 05: asyncio

## The problem

Threads solved waiting in ex01. But each thread is a real OS thread: it has its own stack
(memory), and the OS must keep switching between all of them. 1,000 threads is heavy.
10,000 or 100,000 connections (a chat server, a crawler, a monitoring system for a big fleet)
and threads stop scaling. And every thread can still race with every other thread (ex04).

## The idea

Use **one** thread with an **event loop**. Each task runs until it reaches `await`
("I'm about to wait; wake me up when the answer arrives"), and the loop immediately runs
another task. Switching happens **only at `await`**: tasks cooperate instead of being
interrupted by the OS at random moments.

## Predict (LEARNING_LOG.md)

1. 1,000 hosts with 1,000 threads vs. with asyncio: which is faster, and by a lot or a little?
2. 10,000 hosts with asyncio: how long? (Max latency per host is 0.3 s.)
3. `bad_check` on just **10** hosts: how long? Read its code first.

## Build

In `runner.py`:

1. `check_all(hosts)`: run all checks concurrently on the event loop, results in order.
2. `run_with_asyncio(hosts)`: the bridge from normal code into async code.

Important to discover: calling an `async def` function **does not run it**. Try it in a Python shell:
`fake_server_check_async("x")`. What do you get back?

Read: [asyncio coroutines and tasks](https://docs.python.org/3/library/asyncio-task.html), especially `asyncio.run` and `asyncio.gather`.

## Check and run

```bash
pytest tests/test_ex05_asyncio.py -v
python -m exercises.ex05_asyncio.run
```

## Explain (LEARNING_LOG.md)

- What is the event loop doing while 10,000 checks are "in progress"? How can one thread wait on 10,000 things?
- Why did `bad_check` take as long as it did? What exactly does `time.sleep` do differently from `await asyncio.sleep`?
- Real-world translation: why can't you just use the `requests` library inside async code? What would you use instead?
- Why are race conditions like ex04's much rarer in asyncio code? (Hint: *where* can a task be switched out?)

## Stretch

Implement `check_all_limited(hosts, limit)` with `asyncio.Semaphore`. Real servers and firewalls
don't like 10,000 simultaneous connections from you. Measure how `limit` changes total time
and explain the formula you think it follows.
