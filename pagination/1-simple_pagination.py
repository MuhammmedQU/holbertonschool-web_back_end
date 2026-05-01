#!/usr/bin/env python3
"""Simple pagination module."""

import csv
from typing import List, Tuple

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize server."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]

            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1,
                 page_size: int = 10) -> List[List]:
        """Return a page of the dataset."""

        assert isinstance(page, int) and isinstance(page_size, int), "page and page_size must be integers"
        assert page > 0 and page_size > 0, "page and page_size must be positive integers"

        dataset = self.dataset()

        start, end = index_range(page, page_size)
        dataset = dataset[start:end]

        return dataset
