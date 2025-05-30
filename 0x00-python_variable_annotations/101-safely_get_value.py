#!/usr/bin/env python3
"""Safely get a value from a mapping with proper type annotations."""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Return value from dict by key if present, else return default."""
    if key in dct:
        return dct[key]
    else:
        return default

