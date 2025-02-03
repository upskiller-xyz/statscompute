from __future__ import annotations
from dataclasses import dataclass
from .statresult import StatResult
from ..components.room import Room
from .stat_enum import STATS

class StatCalculator:

    stats: list[STATS] = [x for x in STATS.get_members()]

    @classmethod
    def run(cls, dataset:list[Room])->list[StatResult]:
        return cls._run(dataset)
    
    @classmethod
    def _run(cls, dataset:list[Room])->list[StatResult]:
        return [cls._calc(s, dataset) for s in cls.stats]
    
    @classmethod
    def _calc(cls, s:STATS, dataset:list[Room])->StatResult:
        return s.value.run(dataset)