# Hints

Open **one level at a time**, and only after you've tried for a while.
Level 1 is a nudge, level 2 names the tools, level 3 is the plan in plain words (still no code).

---

## Exercise 00: baseline

<details><summary>Level 1</summary>

You need somewhere to collect results, and a way to visit each item once.
</details>

<details><summary>Level 2</summary>

A `for` loop with `append`, or a list comprehension. Both are fine; write it the way you'd explain it out loud.
</details>

---

## Exercise 01: threads

<details><summary>Level 1: the "threads can't return values" puzzle</summary>

A thread throws away whatever its target function returns. But threads **share memory** with the
code that started them. Is there an object you could create *before* starting the threads that every
thread can write into?
</details>

<details><summary>Level 2</summary>

- A list created in advance, the same length as `items`, filled with placeholders.
- Each thread needs to know **which slot** is its own. What does `enumerate()` give you?
- `func` doesn't know about slots. You'll need a small helper function (defined inside
  `run_with_threads`) that calls `func` and stores the result in the right place.
  That helper is the thread's `target`, and you pass its inputs with `args=(...)`.
</details>

<details><summary>Level 3: the plan</summary>

1. Make the results list with a placeholder per item.
2. Define a helper that takes (slot number, item), calls `func(item)`, stores the result in that slot.
3. **First loop:** for each item, create a thread for the helper, start it, remember it in a list.
4. **Second loop:** join every thread you remembered.
5. Return the results list.

Why two separate loops? If you can't answer that yet, do "break it on purpose" #3 in the README.
</details>

<details><summary>Stretch: limited workers</summary>

- Put `(slot, item)` pairs into a `queue.Queue`.
- Each worker thread loops: take a job with `get_nowait()`, and stop when it raises `queue.Empty`.
- Start exactly `workers` threads, then join them.
</details>

---

## Exercise 02: GIL experiment

<details><summary>Level 1</summary>

You already have `run_sequential` and `run_with_threads`. You're only adding the measurement around them.
</details>

<details><summary>Level 2</summary>

Copy the *shape* of `ex00_baseline/run.py`: a `with timed("label"):` block around each call.
</details>

---

## Exercise 03: processes

<details><summary>Level 1</summary>

Both executors are context managers (use `with`), and both have a `map` method that works like
the built-in `map`.
</details>

<details><summary>Level 2</summary>

- `Executor.map` returns an iterator, but the function must return a **list**.
- `map` already keeps the input order. Compare this to the work you did in ex01.
- `max_workers=None` gives the executor's default, so you can pass `workers` straight through.
</details>

<details><summary>Level 3: the plan</summary>

Open the pool with the right number of workers inside a `with` block, call `map(func, items)` on it,
turn the result into a list, return it. Both functions are about three lines.
</details>

---

## Exercise 04: race conditions

<details><summary>Level 1: hammer()</summary>

Same start-all-then-join-all pattern as ex01. The only difference is what each thread does:
not one call, but a loop of calls.
</details>

<details><summary>Level 1: SafeCounter</summary>

The bug happens when another thread sneaks in **between** step 1 and step 3. What if only one thread
at a time were allowed to be anywhere between those steps?
</details>

<details><summary>Level 2: SafeCounter</summary>

- Create one `threading.Lock()` per counter, in `__init__`, next to `self.value = 0`.
- A lock works as a context manager: `with self.<lock>:` and everything indented under it is protected.
- Ask yourself: which of the three steps must be inside? Do "break it on purpose" #1 to check your answer.
</details>

---

## Exercise 05: asyncio

<details><summary>Level 1</summary>

Calling `fake_server_check_async(host)` gives you a *coroutine object*: a paused piece of work that
hasn't started. You need something that takes **many** of those and runs them all together.
</details>

<details><summary>Level 2</summary>

- `asyncio.gather(*awaitables)` runs them concurrently and returns results **in the order given**.
  Note the `*`: it takes separate arguments, not a list.
- `gather` must be `await`ed, so it lives inside `check_all`.
- `asyncio.run(coroutine)` is the door from normal code into async code. It belongs in `run_with_asyncio`.
</details>

<details><summary>Level 3: the plan</summary>

`check_all`: build one coroutine per host (a generator expression works), pass them all to `gather`
with `*`, await it, return the list.
`run_with_asyncio`: hand `check_all(hosts)` to `asyncio.run` and return what it gives back.
</details>

<details><summary>Stretch: Semaphore</summary>

Create `asyncio.Semaphore(limit)`. Wrap each check in a small `async def` that does
`async with sem:` before awaiting the real check. Then gather the wrapped ones.
</details>

---

## Exercise 06: port checker

No hints about *which* concurrency approach to use. That decision is the exercise.
These hints only cover the networking.

<details><summary>Networking: blocking sockets</summary>

`socket.create_connection((host, port), timeout=timeout)` either returns a connected socket or raises.
Refused, timeout, DNS failure and unreachable networks all raise subclasses of `OSError`.
Use the socket in a `with` block so it gets closed.
</details>

<details><summary>Networking: asyncio</summary>

`asyncio.open_connection(host, port)` returns `(reader, writer)`. It has no timeout of its own:
wrap it in `asyncio.wait_for(..., timeout)`. Catch `OSError` and `asyncio.TimeoutError`.
Close with `writer.close()` then `await writer.wait_closed()`.
</details>

<details><summary>CLI</summary>

- `argparse`: one positional argument (the file) and one `--timeout` option with `type=float`.
- Parse a line with `line.rsplit(":", 1)`. Why `rsplit` and not `split`? (Think about IPv6 one day.)
- `sys.exit(0)` / `sys.exit(1)` sets the exit code. Check it with `echo $?`.
</details>
