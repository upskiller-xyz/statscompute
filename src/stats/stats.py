from __future__ import annotations
from dataclasses import dataclass

from .stat import Stat
from .statresult import StatResult
from ..components.room import Room



class WallAmountStat(Stat):
    """
    Object responsible for calculating statistics of the amount of walls in the rooms
    present in the given dataset.

    How to use:

    $ res = WallAmountStat.run(dataset)
    """
    @classmethod
    def _calc(cls, dataset:list[Room])->StatResult:
        return [len(room.walls) for room in dataset]
    
class WindowAmountStat(Stat):
    """
    Object responsible for calculating statistics of the amount of windows in the rooms
    present in the given dataset.

    How to use:

    $ res = WindowAmountStat.run(dataset)
    """
    @classmethod
    def _calc(cls, dataset:list[Room])->StatResult:
        return [len(room.windows) for room in dataset]
    
class SlabAmountStat(Stat):
    """
    Object responsible for calculating statistics of the amount of slabs in the rooms
    present in the given dataset.

    How to use:

    $ res = CeilingAmountStat.run(dataset)
    """
    @classmethod
    def _calc(cls, dataset:list[Room])->StatResult:
        return [len(room.slabs) for room in dataset]
    
    
class RoomAreaStat(Stat):
    """
    Object responsible for calculating statistics of the area of the rooms
    present in the given dataset.

    How to use:

    $ res = RoomAreaStat.run(dataset)
    """
    @classmethod
    def _calc(cls, dataset:list[Room])->StatResult:
        return [room.slabs[0].props.area for room in dataset]