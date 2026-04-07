#!/usr/bin/env python3
"""
Module for creating asyncio Tasks from coroutines.
"""
import asyncio
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[float]:
    """
    Create an asyncio.Task from the wait_random coroutine"""
    return asyncio.create_task(wait_random(max_delay))
