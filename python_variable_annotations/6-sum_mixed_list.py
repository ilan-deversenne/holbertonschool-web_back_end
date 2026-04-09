#!/usr/bin/env python3

"""
Function to sum a list of integers and floats
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Sum a list of integers and floats"""

    return sum(mxd_lst)
