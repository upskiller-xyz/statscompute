from __future__ import annotations
from dataclasses import dataclass
import os

from .roomloader import RoomLoader
from ..components.room import Room

class DatasetLoader:

    path = "dataset_20250130"

    @classmethod
    def run(cls, folder:str)->Room:
        return cls._run(folder)
    
    @classmethod
    def _run(cls, folder:str)->list[Room]:
        if not folder:
            folder = cls.path
        return [RoomLoader.run('{}/{}'.format(folder, x)) for x in os.listdir(folder) if x.endswith(".json")]