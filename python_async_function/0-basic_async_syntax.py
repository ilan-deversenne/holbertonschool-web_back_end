#!/usr/bin/env python3

"""
Asyncio wait random delay with a max delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait random delay with a max delay

    Args:
        max_delay (int, optional): Wait time (delay). Defaults to 10.

    Returns:
        float: Delay
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
