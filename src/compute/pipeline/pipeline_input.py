from __future__ import annotations
from dataclasses import dataclass
import torch
from torch_geometric.loader import DataLoader
from ...graph.dataset import DaylightDataset
from .steps.model import ModelInput

@dataclass(frozen=True)
class PipelineInput:
    dataset: DaylightDataset
    train: DataLoader
    val: DataLoader
    model: ModelInput