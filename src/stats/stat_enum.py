from ..utils.extended_enum import ExtendedEnum

from . import stats


class STATS(ExtendedEnum):

    WALL_AMOUNT= stats.WallAmountStat
    WINDOW_AMOUNT= stats.WindowAmountStat
    SLAB_AMOUNT= stats.SlabAmountStat
    ROOM_AREA = stats.RoomAreaStat



