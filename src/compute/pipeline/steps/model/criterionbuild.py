from __future__ import annotations
import torch

from .modelinput import ModelInput
from ...earlystopping import EarlyStopping
from .modelbuild import ModelBuildStep


class CriterionBuildStep(ModelBuildStep):
    
    @classmethod
    def _run(cls, inp:ModelInput)->ModelInput:
        cr = torch.nn.MSELoss()
        return ModelInput(inp.in_channels, inp.out_channels, 
                          inp.model, inp.optimizer, cr)
    