from __future__ import annotations
from ..utils.extended_enum import ExtendedEnum



class RoomPropsEnum(ExtendedEnum):
    """
    Enumerator listing available and relevant room properties.

    How to use:

    $ RoomPropsEnum.AREA.value  # expected to give "Area"
    """
    AREA = "Area"
    HEIGHT = "Height"   

class WallPropsEnum(ExtendedEnum):
    """
    Enumerator listing available and relevant wall properties.

    How to use:

    $ WallPropsEnum.WIDTH.value  # expected to give "Width"
    """
    HEIGHT = "Height"
    LENGTH = "Length"   
    THICKNESS = "Thickness"
    MATERIAL = "Material"
    REFLECTIVITY = "Reflectivity"

class WindowPropsEnum(ExtendedEnum):
    """
    Enumerator listing available and relevant window properties.

    How to use:

    $ WindowPropsEnum.TRANSMITTANCE.value  # expected to give "Transmittance"
    """
    WIDTH = "Width"
    HEIGHT = "Height"   
    THICKNESS = "Thickness"
    MATERIAL = "Material"
    TRANSMITTANCE = "Transmitance"
    RATIO = "Frame Ratio"
    VECTORS = "Vectors"

class SlabPropsEnum(ExtendedEnum):
    """
    Enumerator listing available and relevant floor and ceiling properties.

    How to use:

    $ SlabPropsEnum.AREA.value  # expected to give "Area"
    """

    AREA = "Area"
    MATERIAL = "Material"
    REFLECTIVITY = "Reflectivity"

class EdgePropsEnum(ExtendedEnum):
    """
    Enumerator listing available and relevant edge properties.

    How to use:

    $ EdgePropsEnum.AREA.value  # expected to give "from"
    """

    FROM = "from"
    TO = "to"
