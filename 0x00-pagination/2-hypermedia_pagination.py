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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing
        the following key-value pairs
        """

        data_dict = {}
        data_dict['page_size'] = len(self.get_page(page, page_size))
        data_dict['page'] = page
        data_dict['data'] = self.get_page(page, page_size)
        total_pages = (len(self.__dataset) + page_size - 1) // page_size
        if total_pages <= page + 1:
            next_page = None
        else:
            next_page = page + 1
        data_dict['next_page'] = next_page
        if page - 1 < 1:
            prev_page = None
        else:
            prev_page = page - 1
        data_dict['prev_page'] = prev_page
        data_dict['total_pages'] = total_pages
        return data_dict
