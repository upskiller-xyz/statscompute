
from __future__ import annotations
import numpy as np
from torch_geometric.loader import DataLoader
from .step import Step
from ..pipeline_input import PipelineInput
from ...graph.dataset import DaylightDataset
    
class DataProcessStep(Step):
    batch = 100

    @classmethod
    def _split(cls, d:DaylightDataset)->tuple[DaylightDataset, DaylightDataset]:
        percent = np.ceil(len(d) * 0.8)
        dataset = d.shuffle()
        return (dataset[:percent], dataset[percent:])
    
    @classmethod
    def _run(cls, inp:PipelineInput)->PipelineInput:
        train_ds, val_ds = cls._split(inp.dataset)
        # print(f'Number of training graphs: {len(train_ds)}')
        # print(f'Number of test graphs: {len(val_ds)}')
        train_loader = DataLoader(train_ds, batch_size=cls.batch, shuffle=True)
        val_loader = DataLoader(val_ds, batch_size=cls.batch, shuffle=False)
        
        # for step, data in enumerate(train_loader):
        #     print(f'Number of graphs in the current batch: {data.num_graphs}')
        return PipelineInput(inp.dataset, train_loader, val_loader, None)
        