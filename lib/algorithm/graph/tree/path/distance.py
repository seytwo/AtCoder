from lib.datastructure.graph.tree.tree import Tree
from lib.algorithm.graph.tree.distance.lca import Distance
class Path(Distance):
  def __init__(self, tree:Tree)->None:
    super().__init__(tree)
    return
  def is_on_path(self, i:int, j:int, k:int):
    ik = self.get(i, k)
    kj = self.get(k, j)
    ij = self.get(i, j)
    return ik+kj == ij
