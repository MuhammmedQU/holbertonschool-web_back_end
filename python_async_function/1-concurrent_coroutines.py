#!/usr/bin/env python3
"""Module that defines wait_n coroutine."""

import asyncio
from 0_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """Spawn wait_random n times and return delays in ascending order."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: list[float] = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
