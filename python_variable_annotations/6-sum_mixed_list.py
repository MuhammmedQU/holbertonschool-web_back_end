#!/usr/bin/env python3
"""Module for sum_list function"""

from typing import List, Union


def sum_mixed_list(mxt_list: Union[List[float], List[int]]) -> float:
    """Return the sum of a list of floats"""
    return sum(mxt_list)
