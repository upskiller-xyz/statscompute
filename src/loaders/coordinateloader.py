from __future__ import annotations
from dataclasses import dataclass
from uuid import uuid4

from ..components.coordinate import Coordinate
from ..nomenclature.props_enum import WallPropsEnum, WindowPropsEnum, SlabPropsEnum

class CoordinateLoader:

    _start = Coordinate(0,0,0)

    @classmethod
    def run(cls, room)->Coordinate:
        return cls._run(room)
    
    @classmethod
    def _run(cls, room)->Coordinate:
        x =0
        y = 0
        z = 0
        return Coordinate(x,y,z)
    

class WallCoordinateLoader:

    @classmethod
    def run(cls, wall, start)->Coordinate:
        return cls._run(wall, start)
    
    @classmethod
    def _run(cls, wall, start)->Coordinate:
        #TODO
        x = start.x + wall[WallPropsEnum.LENGTH.value] * 0.5
        y = start.y
        z = start.z
        return Coordinate(x,y,z)