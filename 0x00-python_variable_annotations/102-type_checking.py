#!/usr/bin/env python3
"""Zoom an array by a factor and return a list with the zoomed elements."""

from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a zoomed-in version of the input list, multiplied by the factor."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

