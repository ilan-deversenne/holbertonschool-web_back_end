#!/usr/bin/env python3

"""
Annotations
"""

import typing


# Srry its for pycodestyle :(
def element_length(
    lst: typing.Iterable[typing.Sequence]
) -> typing.List[typing.Tuple[typing.Sequence, int]]:

    """Return length of elements

    Args:
        lst (typing.Iterable[typing.Sequence]): Iterable

    Returns:
        typing.List[typing.Tuple[typing.Sequence, int]]: List
    """

    return [(i, len(i)) for i in lst]
