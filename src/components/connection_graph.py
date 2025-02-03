from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Connection:
    """
    Object containing relationships of one node with others in the graph.

    How to use:

    r = Connection(node_name="Wall_001", connected=["Wall_002", "Wall_004"])
    """
    node_name: str
    connected: list[str]

@dataclass(frozen=True)
class ConnectionGraph:
    """
    Object containing connections within the graph.

    How to use:

    r = ConnectionGraph(connections=[])
    """
    connections: list[Connection]