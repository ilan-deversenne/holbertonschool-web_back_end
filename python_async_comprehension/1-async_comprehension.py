#!/usr/bin/env python3

"""
Get 10 random numbers from async_generator
"""

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Get 10 random numbers from async_generator

    Returns:
        typing.List[float]: List of 10 random numbers
    """
    return [gen async for gen in async_generator()]
