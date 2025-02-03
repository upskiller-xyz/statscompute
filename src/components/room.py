from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

from .component import Component
from .connection_graph import ConnectionGraph

from .wall import Wall
from .window import Window
from .slab import Slab


@dataclass(frozen=True)
class Room(Component):
    """
    Object containing a single room with all its elements.

    How to use:

    r = Room(id="2342", graph={}, walls=[], windows=[], slabs=[])
    """
    id: str
    graph: ConnectionGraph
    walls: List[Wall] = field(default_factory=list)
    windows: List[Window] = field(default_factory=list)
    slabs: List[Slab] = field(default_factory=list)