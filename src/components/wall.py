from __future__ import annotations
from dataclasses import dataclass

from .bbox import Bbox
from .component import Component
from .coordinate import Coordinate
from ..cp.wall_props import WallProps


@dataclass(frozen=True)
class Wall(Component):
    """
    Object containing a single wall.

    How to use:

    w = Wall("", center=Coordinate(0,0,0), bb=Bbox(600,20, 1000), 
            props=WallProps("concrete", 0.2), windows=[])
    """
    id: str
    center: Coordinate
    bb: Bbox
    props: WallProps
#     windows: list[Window] = []