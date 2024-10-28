#!/usr/bin/env python3
"""
simple module to extract the right pages from the CSV file
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    a simple function to return a tuple of start, end indexes
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return tuple((start_index, end_index))


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
        """
        using the index_ange function to get the right rows of the
        csv file
        """
        assert isinstance(page, int) and page > 0, \
            "page should be intger greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size should be intger greater than 0"
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start:end] if start < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returning the info dictionary of the pages
        """
        assert isinstance(page, int) and page > 0, \
            "page should be intger greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size should be intger greater than 0"
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages}
