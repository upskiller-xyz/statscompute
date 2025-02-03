from __future__ import annotations


from ..components.coordinate import Coordinate
from ..components.bbox import Bbox
from ..components.window import Window

from ..cp.window_props import WindowProps

from ..nomenclature.props_enum import WindowPropsEnum

class WindowLoader:

    path = "dataset_20250130/test_generation/{}.json"

    @classmethod
    def run(cls, id:str, w:dict, center:Coordinate)->Window:
        return cls._run(id, w, center)
    
    @classmethod
    def _run(cls,id:str, w:dict, center:Coordinate)->Window:
        
        bb = Bbox(float(w[WindowPropsEnum.THICKNESS.value]),
                  float(w[WindowPropsEnum.HEIGHT.value]),
                  float(w[WindowPropsEnum.WIDTH.value]))
        props = WindowProps(w[WindowPropsEnum.MATERIAL.value], 
                            float(w[WindowPropsEnum.TRANSMITTANCE.value]),
                            float(w[WindowPropsEnum.RATIO.value])
                            # w[WindowPropsEnum.VECTORS.value]
                            )
        # windows = []
        return Window(id, center, bb, props)