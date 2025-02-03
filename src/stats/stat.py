from __future__ import annotations
import numpy as np
from .statresult import StatResult


class Stat:
    """
    Object responsible for calculating specific metric.

    How to use:
    $ res = Stat.run(dataset)
    """
    @classmethod
    def run(cls, dataset)->StatResult:
        return cls._run(dataset)
    
    @classmethod
    def _run(cls, dataset)->StatResult:
        _result = cls._calc(dataset)
        return StatResult(np.mean(_result), np.max(_result), np.min(_result))
    
    @classmethod
    def _calc(cls, dataset)->StatResult:
        return [0]