import torch
from torch_geometric.loader import DataLoader
from ..graph.dataset import DaylightDataset
from .pipeline.steps.model.modelinput import ModelInput

class Trainer:

    @classmethod
    def train(cls, model:torch.nn.Module, b:DaylightDataset, optimizer, criterion):
        model.train()
        optimizer.zero_grad()

        out, z = model(b.x, b.edge_index)
        loss = criterion(out, b.x)
        loss.backward()
        optimizer.step()
        return loss.item()
    
    @classmethod
    def test(cls, model:torch.nn.Module, loader:DataLoader, criterion):
        model.eval()
        loss = None
        for data in loader:
            out, _ = model(data.x, data.edge_index)  
            loss = criterion(out, data.x)
        return loss
    
    @classmethod
    def run(cls, m:ModelInput):
        epoch = 0
        while not m.early_stopping.early_stop:
            train_losses = [cls.train(m.model, b, m.optimizer, m.criterion) for b in m.train_loader]
            val_loss = cls.test(m.model, m.val_loader, m.criterion)
            if (epoch % 10 ==0):
                print(f'Epoch {epoch+1}, Train loss: {train_losses.sum()/len(m.train_loader)} Loss: {val_loss}')
        print('Training complete.')
        return m