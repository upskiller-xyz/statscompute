
from __future__ import annotations
from ..pipeline_input import PipelineInput

class Step:
    @classmethod
    def run(cls, inp:PipelineInput)->PipelineInput:
        return cls._run(inp)
    
    @classmethod
    def _run(cls, inp:PipelineInput)->PipelineInput:
        return inp
    