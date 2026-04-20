#!/usr/bin/env python3

import csv
import math
from typing import List


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

    def index_range(self, page: int, page_size: int) -> tuple:
        """Rage index for pagination

        Args:
            page (int): Page
            page_size (int): Size page

        Returns:
            tuple: Tuple of start index & end index
        """

        assert (type(page_size) is int)
        assert (type(page) is int)
        assert (page_size > 0)
        assert (page > 0)

        return ((page - 1) * page_size, page * page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page

        Args:
            page (int, optional): Page. Defaults to 1.
            page_size (int, optional): Page size. Defaults to 10.

        Returns:
            List[List]: List of related page contents
        """

        index_range = self.index_range(page, page_size)
        return self.dataset()[index_range[0]:index_range[1]]
