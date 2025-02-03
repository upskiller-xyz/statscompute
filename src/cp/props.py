from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Props:
    """
    Object containing properties of a generic component.

    How to use:

    $ w = Props("Concrete")
    """
    material: str