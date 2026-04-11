#!/usr/bin/env python3

"""
Measure runtime of async_comprehension
"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime of async_comprehension

    Returns:
        float: Runtime
    """
    started_at: float = time()

    # awaitable asyncio.gather(*aws, return_exceptions=False)
    await asyncio.gather(*[async_comprehension() for i in range(4)])

    ended_at: float = time()

    return ended_at - started_at
