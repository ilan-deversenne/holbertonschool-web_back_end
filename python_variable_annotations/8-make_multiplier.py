#!/usr/bin/env python3

"""
Multiplies a float by multiplier
"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Return function that multiply by multiplier

    Args:
        multiplier (float): Multiplier

    Returns:
        typing.Callable[[float], float]: Function that multiply by multiplier
    """

    return lambda n: n * multiplier
