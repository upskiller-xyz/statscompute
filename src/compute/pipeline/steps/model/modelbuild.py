from __future__ import annotations
from ..step import Step
from .modelinput import ModelInput
from ...autoencoder import GraphAutoencoder


class ModelBuildStep(Step):
    @classmethod
    def run(cls, inp:ModelInput)->ModelInput:
        return cls._run(inp)
    
    @classmethod
    def _run(cls, inp:ModelInput)->ModelInput:
        m = GraphAutoencoder(inp.in_channels, inp.out_channels)
        return ModelInput(inp.in_channels, inp.out_channels, m)
    
