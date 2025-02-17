from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class Node:
  id: int
  category: int
  vector: tuple[int]

  @property
  def out(self)->tuple[int]:
    return np.pad(np.array([self.category, *self.vector]), (0, 7-len(self.vector)-1), 'constant', constant_values=(0)).astype(np.float32)