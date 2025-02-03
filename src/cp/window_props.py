from __future__ import annotations
from dataclasses import dataclass

from .props import Props


@dataclass(frozen=True)
class WindowProps(Props):
    """
    Object containing properties of a window component.

    How to use:

    $ w = WindowProps("concrete", 0.2, 0.2, [[0,0,0]])
    """
    material: str
    transmittance: float
    ratio: float
    # vecs: list[list[float]]