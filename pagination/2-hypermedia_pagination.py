#!/usr/bin/env python3

"""
Simple pagination
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Rage index for pagination

    Args:
        page (int): Page
        page_size (int): Size page

    Returns:
        tuple: Tuple of start index & end index
    """

    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page

        Args:
            page (int, optional): Page. Defaults to 1.
            page_size (int, optional): Page size. Defaults to 10.

        Returns:
            List[List]: List of related page contents
        """

        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(page, int) and page > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        return data[start:end] if start < len(data) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get hypermedia of page

        Args:
            page (int, optional): Page. Defaults to 1.
            page_size (int, optional): Page size. Defaults to 10.

        Returns:
            dict: Hypermedia of page
        """

        pages = self.get_page(page, page_size)
        data_size = len(self.__dataset)
        max_pages = page * page_size

        return {
            'page_size': page_size,
            'page': page if max_pages < data_size else 0,
            'data': pages,
            'next_page': page + 1 if max_pages + 1 < data_size else None,
            'prev_page': page - 1 if page - 1 > 0 else max_pages,
            'total_pages': math.ceil(data_size / page_size)
        }
