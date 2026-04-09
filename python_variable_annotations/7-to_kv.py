#!/usr/bin/env python3

"""
Function that return tupple with k (str) and squared of v
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """return tupple with k (str) and result of squared of v

    Args:
        k (str): String
        v (typing.Union[int, float]): Number to squared

    Returns:
        typing.Tuple[str, float]: Tupple of string and squared of v
    """

    return (k, v * v)
