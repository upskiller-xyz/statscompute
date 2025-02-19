from dataclasses import dataclass

@dataclass(frozen=True)
class EdgeRaw:
  start: str
  end: str
  
@dataclass(frozen=True)
class Edge:
  start: int
  end: int

  @property
  def out(self)->list[int,int]:
    return [self.start, self.end]