from __future__ import annotations
from dataclasses import dataclass

from .props import Props


@dataclass(frozen=True)
class SlabProps(Props):
    """
    Object containing properties of a slab component (floor or ceiling).

    How to use:

    $ w = SlabProps("concrete", 0.2, 22.2)
    """
    material: str
    reflectivity: float
    area: float