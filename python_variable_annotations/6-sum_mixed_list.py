#!/usr/bin/env python3
"""Module for sum_list function"""

from typing import List, Union
import typing


def sum_mixed_list(mxt_list: Union[typing.List[float], typing.List[int]]) -> float:
    """Return the sum of a list of floats"""
    return sum(mxt_list)
