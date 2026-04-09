#!/usr/bin/env python3

"""
Asyncio wait random delay with a max delay
"""

from random import uniform
from asyncio import sleep


async def wait_random(max_delay: float|int = 10) -> float:
    """Wait random delay with a max delay

    Args:
        max_delay (int, optional): Wait time (delay). Defaults to 10.

    Returns:
        float: Delay
    """
    delay: float = uniform(0, max_delay)
    await sleep(delay)

    return delay
