#!/usr/bin/env python3
"""Module for creating a task from wait_random."""

import asyncio
from 0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return a Task wrapping wait_random."""
    return asyncio.create_task(wait_random(max_delay))
