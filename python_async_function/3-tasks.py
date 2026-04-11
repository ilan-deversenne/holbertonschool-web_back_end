#!/usr/bin/env python3

"""
Create asyncio task for wait_random
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return asyncio task of wait_random

    Args:
        max_delay (int): Max delay

    Returns:
        asyncio.Task: Task
    """
    return asyncio.create_task(wait_random(max_delay))
