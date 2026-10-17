# Exercise 06 (capstone): A concurrent port checker

## The problem

This is a real sysadmin tool: given a list of `host:port` targets (SSH on your VMs, DNS on your
BIND server, a web app), report which ones are reachable. A dead host doesn't answer: you wait
for the full timeout. With 50 targets and a 2-second timeout, a sequential checker can take
**100 seconds**. That's unusable for monitoring.

## The rules this time

- **No prescribed approach.** You've used threads, processes and asyncio. Pick one.
- You must **defend your choice** in `DECISION.md`: bottleneck, alternatives, measurements.
- No new hints about *which* tool to use. `HINTS.md` only helps with the networking parts.

## Build

### 1. `check_many(targets, timeout)` in `checker.py`

The contract is in the docstring. In short: a dict `"host:port" -> bool` for every target,
concurrent, never crashes on a bad host.

Networking building blocks (pick what fits your approach):
- blocking: [`socket.create_connection`](https://docs.python.org/3/library/socket.html#socket.create_connection)
- asyncio: [`asyncio.open_connection`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection) + [`asyncio.wait_for`](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for)

Whatever you open, **close it**.

### 2. The CLI in `__main__.py`

CLI spec:

```bash
python -m exercises.ex06_port_checker targets.txt --timeout 1
```

- reads targets from the file (format: see `targets.example.txt`; skip blanks and `#` comments)
- prints one line per target, `UP` or `DOWN`, plus a summary line and the total time taken
- exit code `0` if everything is up, `1` if anything is down (so it could run from cron or a CI job)
- a malformed line like `nonsense` should produce a clear error message, not a traceback

## Check and run

```bash
pytest tests/test_ex06_port_checker.py -v
cp exercises/ex06_port_checker/targets.example.txt targets.txt   # then edit it for your lab
python -m exercises.ex06_port_checker targets.txt --timeout 1
echo $?
```

Point it at your real lab: your VMs' SSH, your DNS servers on port 53, something that's turned off.
Stop a service with `systemctl stop` and watch it flip to DOWN.

## Explain

Fill in `DECISION.md`. Then in `LEARNING_LOG.md`: what was harder than you expected?

## Stretch

- Add a `--concurrency N` limit.
- Add `--json` output so other programs can consume the results.
- Measure the difference between "connection refused" and "timeout" targets. Why are they so different in speed? (Think about what a closed port vs. a firewall `DROP` rule actually sends back.)
