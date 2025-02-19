
from .edge import Edge, EdgeRaw
from .node import Node

class GraphParser:
  @classmethod
  def get_nodes(cls, graph:dict):
    return {k:v for k,v in graph["Nodes"].items() if "room" not in k.lower()}

  @classmethod
  def get_edges(cls, graph:dict):
    return graph["Edges"]

  @classmethod
  def get_edge(cls, edge:dict)->EdgeRaw:
    return EdgeRaw(edge["from"], edge["to"])

  @classmethod
  def get_node(cls, id:int, cat:int, node:dict)->Node:
    node["Material"] = 0.2
    return Node(id, cat, [v for k,v in node.items() if k not in 
     ["Connectivity", "CentroidXY", "Vectors"]])
