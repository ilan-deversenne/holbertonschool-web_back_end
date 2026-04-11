#!/usr/bin/env python3

"""
Function that measure time of wait_n coroutines execution
"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int):
    """Measure time

    Args:
        n (int): Number of coroutines for wait_n
        max_delay (int): Max delay for wait_n

    Returns:
        int: Time
    """
    start_at: int = time()
    run(wait_n(n, max_delay))
    end_at: int = time()

    return (end_at - start_at) / n
