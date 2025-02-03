from __future__ import annotations
from dataclasses import dataclass

from .bbox import Bbox
from .component import Component
from .coordinate import Coordinate

from ..cp.window_props import WindowProps




@dataclass(frozen=True)
class Window(Component):
    """
    Object containing a single room with all its elements.

    How to use:

    $ w = Window("", center=Coordinate(0,0,0), bb=Bbox(600,20, 1000), props=WindowProps("glass", 0.2,0.2,[[0,0,0]]))
    """
    id: str
    center: Coordinate
    bb: Bbox
    props: WindowProps