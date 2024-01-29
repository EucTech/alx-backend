#!/usr/bin/env python3
""" a function named index_range that takes two integer
arguments page and page_size"""


import csv
import math
from typing import List


def index_range(page, page_size):
    """index range function"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """page dataset"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)

        assert page > 0
        assert page_size > 0

        data = self.dataset()

        try:
            indexing = index_range(page, page_size)
            return data[indexing[0]:indexing[1]]
        except IndexException as e:
            return []
