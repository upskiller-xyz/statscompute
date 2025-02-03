from __future__ import annotations
from dataclasses import dataclass

from .props import Props


@dataclass(frozen=True)
class WallProps(Props):
    """
    Object containing properties of a wall component.

    How to use:

    $ w = WallProps("concrete", 0.2)
    """
    material: str
    reflectivity: float