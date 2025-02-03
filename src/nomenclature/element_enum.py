from __future__ import annotations
from ..utils.extended_enum import ExtendedEnum


class ElementEnum(ExtendedEnum):
    WALL = "Wall"
    WINDOW = "Window"
    CEILING = "Ceiling"
    FLOOR = "Floor"
    ROOM = "Room"
    BALCONY = "Balcony"
    ALL = "_"

class GraphElementEnum(ExtendedEnum):
    NODES = "Nodes"
    EDGES = "Edges"