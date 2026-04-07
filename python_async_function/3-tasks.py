#!/usr/bin/env python3
"""Module for task wait generator."""

import asyncio
import importlib
from typing import AsyncGenerator

wait_random = importlib.import_module("0-basic_async_syntax").wait_random


async def task_wait_random(max_delay: int) -> AsyncGenerator[float, None]:
    """Return an async generator that yields a random delay."""
    delay = await wait_random(max_delay)
    yield delay


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """Return a list of delays from n random wait tasks."""
    tasks = [
        asyncio.create_task(task_wait_random(max_delay).__anext__())
        for _ in range(n)
    ]

    delays: list[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
