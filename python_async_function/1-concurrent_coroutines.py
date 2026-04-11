#!/usr/bin/env python3

"""
Function to create coroutines for wait_random
"""

import asyncio
import typing

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Create n coroutines for wait_random

    Args:
        n (int): Number of coroutines
        max_delay (int): Max delay for wait_random

    Returns:
        typing.List: List with delays
    """
    tasks: list = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
