from __future__ import annotations

from .modelinput import ModelInput
from ...earlystopping import EarlyStopping
from .modelbuild import ModelBuildStep


class ESBuildStep(ModelBuildStep):
    
    @classmethod
    def _run(cls, inp:ModelInput)->ModelInput:
        es = EarlyStopping(patience=50, min_delta=0.001)
        return ModelInput(inp.in_channels, inp.out_channels, 
                          inp.model, inp.optimizer, inp.criterion, es)