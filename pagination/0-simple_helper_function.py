#!/usr/bin/env python3

"""
Pagination index helper
"""

def index_range(page: int, page_size: int) -> tuple:
    """Rage index for pagination

    Args:
        page (int): Page
        page_size (int): Size page

    Returns:
        tuple: Tuple of start index & end index
    """

    return ((page - 1) * page_size, page * page_size)
