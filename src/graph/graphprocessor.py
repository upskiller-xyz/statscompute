from .graphparser import GraphParser
from .node import Node
from .edge import Edge


temp = {
    "wall": 0,
    "window": 1,
    "floor": 2,
    "ceiling":3,
    "balcony":4
    }

class GraphProcessor:

  @classmethod
  def run(cls, graph:dict):
    return cls._run(graph)

  @classmethod
  def _run(cls, graph:dict):
    return cls._run(graph)

  @classmethod
  def _node_dict(cls, graph:dict):
    
    return {n: i for i,n in enumerate(GraphParser.get_nodes(graph).keys())}

  @classmethod
  def edgify(cls, graph:dict, nodes:dict[str, int]=[])->list[Edge]:
    if not nodes:
      nodes = cls._node_dict(graph)
      
    _edges = [GraphParser.get_edge(e) for e in GraphParser.get_edges(graph)]
    
    return [Edge(nodes[e.start], nodes[e.end]) for e in _edges 
            if e.start in nodes and e.end in nodes]

  @classmethod
  def nodify(cls, graph:dict, nodes:dict[str, int]=[])->list[Node]:
    if not nodes:
      nodes = cls._node_dict(graph)
      
    return [GraphParser.get_node(nodes[k], temp[k.split("_")[0].lower()], v) 
    for k, v in GraphParser.get_nodes(graph).items() 
    if not k.lower().startswith("room")]
    