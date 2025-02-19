
from __future__ import annotations
from .step import Step
from ..pipeline_input import PipelineInput
from ...graph.dataset import DaylightDataset
    
class DataLoadStep(Step):
    
    @classmethod
    def _run(cls, inp:PipelineInput)->PipelineInput:
        d = DaylightDataset("../graph")
        _ = d.process()
        return PipelineInput(d)
        