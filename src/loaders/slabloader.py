from __future__ import annotations
from dataclasses import dataclass
import json
from uuid import uuid4

from ..components.coordinate import Coordinate
from ..components.bbox import Bbox
from ..components.slab import Slab

from ..cp.slab_props import SlabProps

from ..nomenclature.props_enum import SlabPropsEnum

class SlabLoader:

    @classmethod
    def run(cls, id:str, w:dict, center:Coordinate)->Slab:
        return cls._run(id, w, center)
    
    @classmethod
    def _run(cls,id:str,  w:dict, center:Coordinate)->Slab:
        props = SlabProps(w[SlabPropsEnum.MATERIAL.value], 
                          float(w[SlabPropsEnum.REFLECTIVITY.value]), 
                          float(w[SlabPropsEnum.AREA.value]))
        bb = Bbox(0,0,0)
        return Slab(id, center, bb, props)