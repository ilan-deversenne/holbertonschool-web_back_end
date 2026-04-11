#!/usr/bin/env python3

"""
Create asyncio task for wait_random with task_wait_random
"""

import asyncio
import typing

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Create n coroutines for task_wait_random

    Args:
        n (int): Number of coroutines
        max_delay (int): Max delay for task_wait_random

    Returns:
        typing.List: List with delays
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
