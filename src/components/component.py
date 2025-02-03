from __future__ import annotations
from dataclasses import dataclass

from .connection_graph import ConnectionGraph

@dataclass(frozen=True)
class Component:
    """
    Object containing a single component with all its elements. Parent class for all the components

    How to use:

    r = Component(id="2342")
    """
    id: str