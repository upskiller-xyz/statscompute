from __future__ import annotations
from dataclasses import dataclass

from .bbox import Bbox
from .component import Component
from .coordinate import Coordinate
from .window import Window
from ..cp.slab_props import SlabProps


@dataclass(frozen=True)
class Slab(Component):
    """
    Object containing a single slab (a floor or a ceiling).

    How to use:

    w = Slab("", center=Coordinate(0,0,0), bb=Bbox(6000,2000, 100), 
            props=SlabProps("concrete", 0.2, 22.2))
    """
    id: str
    center: Coordinate
    bb: Bbox
    props: SlabProps