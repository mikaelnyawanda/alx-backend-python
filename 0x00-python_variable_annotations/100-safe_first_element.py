#!/usr/bin/env python3
"""Module for duck-typed function that returns the first element safely."""

from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence if it exists, else None."""
    if lst:
        return lst[0]
    else:
        return None

