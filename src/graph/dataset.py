import json
import numpy as np
import os
import torch
from torch_geometric.data import InMemoryDataset, Data

from .graphprocessor import GraphProcessor


class DaylightDataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None, pre_filter=None):
        super().__init__(root, transform, pre_transform, pre_filter)
        self.load(self.processed_paths[0])
        # For PyG<2.4:
        # self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self):
        return os.listdir('{}/{}'.format(self.root, "json"))[:2000]

    @property
    def processed_file_names(self):
        return ['data.pt']

    def getData(self, graph):
      edge_index = torch.from_numpy(np.array([n.out for n in GraphProcessor.edgify(graph)]))
      nds = np.array([n.out for n in GraphProcessor.nodify(graph)])
      nds = nds / np.max(nds, axis=0)

      x = torch.from_numpy(nds.astype(np.float32))

      return Data(x=x, edge_index=edge_index.T)

    def load_graph(self, fname):
      
      with open(fname, "r") as f:
        g = json.load(f)
      return g


    def process(self):
        # Read data into huge `Data` list.
        data_list = [self.getData(self.load_graph('{}/{}/{}'.format(self.root, "json", g))) for g in self.raw_file_names]

        if self.pre_filter is not None:
            data_list = [data for data in data_list if self.pre_filter(data)]

        if self.pre_transform is not None:
            data_list = [self.pre_transform(data) for data in data_list]

        self.save(data_list, self.processed_paths[0])
        return data_list
        # For PyG<2.4:
        # torch.save(self.collate(data_list), self.processed_paths[0])