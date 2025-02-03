from __future__ import annotations
from dataclasses import dataclass

@dataclass
class StatResult:
    """
    Interface containing metrics for a specific stat control.

    How to use:
    $ res = StatResult(12, 0, 0)
    $ res.mean  # expected to print 12
    $ res = StatResult.empty()
    $ res.mean  # expected to print 0
    """
    mean: float
    max: float
    min: float

    @classmethod
    def empty(cls)->StatResult:
        """
        Method producing an empty instance of StatResult.

        How to use:
        
        $ res = StatResult.empty()
        $ res.mean  # expected to print 0
        """
        return StatResult(0,0,0)