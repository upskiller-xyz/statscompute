from __future__ import annotations

from ..components.coordinate import Coordinate
from ..components.bbox import Bbox
from ..components.wall import Wall
from ..cp.wall_props import WallProps
from ..nomenclature.props_enum import WallPropsEnum


class WallLoader:

    path = "dataset_20250130/test_generation/{}.json"

    @classmethod
    def run(cls, id:str, wall:dict, center:Coordinate)->Wall:
        return cls._run(id, wall, center)
    
    @classmethod
    def _run(cls, id:str, wall:dict, center:Coordinate)->Wall:
        
        bb = Bbox(float(wall[WallPropsEnum.THICKNESS.value]),
                  float(wall[WallPropsEnum.HEIGHT.value]),
                  float(wall[WallPropsEnum.LENGTH.value]))
        props = WallProps(wall[WallPropsEnum.MATERIAL.value], 
                          float(wall[WallPropsEnum.REFLECTIVITY.value]))
        # windows = []
        return Wall(id, center, bb, props)