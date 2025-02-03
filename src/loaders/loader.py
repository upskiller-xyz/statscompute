from __future__ import annotations
from dataclasses import dataclass
from uuid import uuid4

from ..components.component import Component

class Loader:

    @classmethod
    def run(cls, *args)->Component:
        return cls._run(args)
    
    @classmethod
    def _run(cls, *args)->Component:
        return Component(uuid4())