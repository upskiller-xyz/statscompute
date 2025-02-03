from __future__ import annotations
from dataclasses import dataclass
from uuid import uuid4

from ..nomenclature.element_enum import ElementEnum
from .loader import Loader

from .wallloader import WallLoader
from .windowloader import WindowLoader
from .slabloader import SlabLoader

from ..components.component import Component
from ..components.coordinate import Coordinate

class ElementFactory:
    """
    Object responsible for producing different components from the given content and the desired type.
    """

    _content:dict[str, str] = {
        ElementEnum.WALL: WallLoader,
        ElementEnum.WINDOW: WindowLoader,
        ElementEnum.FLOOR: SlabLoader,
        ElementEnum.CEILING: SlabLoader

    }
    _default = Loader

    @classmethod
    def _component_type(cls, element:str)->ElementEnum:
        """
        Method that gets component type from the component name.
        :param:
        element         name of the element, str
        return res      element type that this element corresponds to, ElementEnum
        """
        el = element.split("_")[0]
        return ElementEnum.from_name(el)

    @classmethod
    def run(cls, element: str | ElementEnum, 
            content:dict, 
            center:Coordinate, *args)->Component:
        """
        Method that produces a component from its input parameters.
        :param:
        element         name of the element or its type, str | ElementEnum
        content         parameters to construct the element from, dict
        center          initial placement of the element, Coordinate
        return res      produced component, Component
        """
        element_type = element
        if isinstance(element, str):
            element_type = cls._component_type(element)
        if isinstance(element, ElementEnum):
            element = uuid4()
        return cls._content.get(element_type, cls._default).run(element, content, center)