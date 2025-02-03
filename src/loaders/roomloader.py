from __future__ import annotations
from dataclasses import dataclass
import json

from .element_factory import ElementFactory
from ..components.component import Component
from ..components.coordinate import Coordinate
from ..components.slab import Slab
from ..components.wall import Wall
from ..components.window import Window
from ..components.room import Room
from ..nomenclature.element_enum import GraphElementEnum, ElementEnum
from ..utils.extended_enum import ExtendedEnum

class RoomLoader:


    @classmethod
    def run(cls, room:str)->Room:
        return cls._run(room)
    
    @classmethod
    def _run(cls, room:str)->Room:
        with open(room, "r") as f:
            r = json.load(f)
        id = room.split("/")[-1].split(".")[0]

        center = Coordinate(0,0,0)
        
        components = [ElementFactory.run(c, component, center) for c, component 
                      in r[GraphElementEnum.NODES.value].items() if "room" not in c.lower() and 
                                                                    "balcony" not in c.lower()]
        
        
        connections = r[GraphElementEnum.EDGES.value]
        return Room(id, connections, 
                    cls.component_by_type(components, Wall), 
                    cls.component_by_type(components, Window), 
                    cls.component_by_type(components, Slab)
                    )
    

    @classmethod
    def component_by_type(cls, components:Component, element_type:type)->list[Component]:
        return [c for c in components if isinstance(c, element_type)]
    
    