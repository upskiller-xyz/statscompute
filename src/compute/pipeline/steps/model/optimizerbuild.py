from __future__ import annotations
import torch
from .modelinput import ModelInput
from .modelubild import ModelBuildStep


class OptimizerBuildStep(ModelBuildStep):
    
    @classmethod
    def _run(cls, inp:ModelInput)->ModelInput:
        opt = torch.optim.Adam(inp.model.parameters(), lr=0.01)
        return ModelInput(inp.in_channels, inp.out_channels, 
                          inp.model, opt)
    