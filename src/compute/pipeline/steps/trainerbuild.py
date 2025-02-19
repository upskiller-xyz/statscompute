
from __future__ import annotations
from .step import Step
from ..pipeline_input import PipelineInput
from .model import ESBuildStep, CriterionBuildStep, OptimizerBuildStep, ModelBuildStep, ModelInput 
    
class TrainerBuildStep(Step):
    
    @classmethod
    def _run(cls, inp:PipelineInput)->PipelineInput:
        steps = [
            ModelBuildStep, CriterionBuildStep, 
            OptimizerBuildStep, ESBuildStep
        ]
        m = ModelInput(len(inp.dataset), 2)
        for step in steps:
            m = step.run(m)
            
        return PipelineInput(inp.dataset, inp.train_loader, inp.val_loader, m)
        