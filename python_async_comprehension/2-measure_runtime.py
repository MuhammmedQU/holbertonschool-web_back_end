#!/usr/bin/env python3
"""Measure runtime for four parallel comprehensions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Execute async_comprehension four times in parallel"""
    start = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time.perf_counter()
    return end - start
