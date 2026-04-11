#!/usr/bin/env python3

"""
Generate async that return 10 random numbers between 0 and 10
"""

from random import uniform
from asyncio import sleep


async def async_generator():
    """Generate random numbers between 0 and 10 asynchronously

    Yields:
        float: Random number between 0 and 10
    """
    for i in range(10):
        await sleep(1)
        yield uniform(0, 10)
