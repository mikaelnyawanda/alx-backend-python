#!/usr/bin/env python3
"""Module for a function that returns a multiplier function."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier."""
    return lambda x: x * multiplier

