#!/usr/bin/env python3

"""
Generate async that return 10 random numbers between 0 and 10
"""

import asyncio
import random
import typing


# Generator[YieldType, SendType, ReturnType]
async def async_generator() -> typing.Generator[float, None, None]:
    """Generate random numbers between 0 and 10 asynchronously

    Yields:
        float: Random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
