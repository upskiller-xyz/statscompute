from __future__ import annotations
import torch

from .encoder import GCNEncoder
from .decoder import GCNDecoder

class GraphAutoencoder(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels):
        super(GraphAutoencoder, self).__init__()
        self.encoder = GCNEncoder(in_channels, hidden_channels)
        self.decoder = GCNDecoder(hidden_channels, in_channels)

    def forward(self, x, edge_index):
        z = self.encoder(x, edge_index)
        return self.decoder(z, edge_index), z