from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Bbox:
    """
    Object containing bounding box of an object.

    How to use:

    r = Bbox(width=0, height=0, length=0)
    """
    width: float = 0
    height: float = 0
    length: float = 0