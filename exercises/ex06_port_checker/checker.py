"""
Exercise 06 (capstone): a real concurrent TCP port checker.

Read exercises/ex06_port_checker/README.md first.
This time there's no prescribed approach: YOU choose, and you defend the
choice in DECISION.md.
"""

from __future__ import annotations


def check_many(targets: list[tuple[str, int]], timeout: float = 1.0) -> dict[str, bool]:
    """
    Check whether a TCP connection can be opened to each (host, port).

    Returns {"host:port": True/False} for EVERY target.
      True  -> something accepted the connection within `timeout` seconds
      False -> refused, timed out, unknown host, unreachable... anything else

    Must never raise because one target is bad.
    Must check targets CONCURRENTLY: 50 dead targets with timeout=1
    should take about 1 second, not 50.
    """
    # TODO: your code here
    raise NotImplementedError("Your turn! See README.md in this folder.")
