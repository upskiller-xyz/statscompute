from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    """
    Object containing coordinates in 3D space. Z coordinate equals to 0 by default.

    How to use:

    r = Coordinate(x=0, y=0)
    """
    x: float
    y: float
    z: float = 0