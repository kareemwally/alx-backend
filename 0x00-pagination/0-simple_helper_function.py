#!/usr/bin/env python3
"""
module that has one function to calculate the range of data paer page
"""


def index_range(page, page_size):
    """
    a simple function to return a tuple of start, end indexes
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return tuple(start_index, end_index)
