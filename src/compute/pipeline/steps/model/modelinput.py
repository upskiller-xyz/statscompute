from __future__ import annotations
from dataclasses import dataclass
import torch

from ...earlystopping import EarlyStopping


@dataclass(frozen=True)
class ModelInput:
    in_channels: int
    out_channels: int = 2
    model:torch.nn.Module | None = None
    optimizer: any = None
    criterion: any = None
    stopping: EarlyStopping | None = None


    