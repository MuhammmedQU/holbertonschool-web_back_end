#!/usr/bin/env python3
"""Module for task wait generator."""


import asyncio
import importlib
from typing import AsyncGenerator

wait_random = importlib.import_module("1-concurrent_coroutines").wait_random


async def task_wait_random(max_delay: int) -> AsyncGenerator[float, None]:
    """Return an async generator that yields a random delay"""
    delay = await wait_random(max_delay)
    yield delay


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """Return a list of delays from n random wait tasks"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task.__anext__()
        delays.append(delay)
    return delays
