# https://atcoder.jp/contests/abc014/tasks/abc014_4
from lib.graph.tree.tree import Tree
from lib.graph.tree.lca.doubling import LCA
class Distance:
  def __init__(self, tree:Tree)->None:
    self.lca = LCA(tree)
    return
  def get(self, i:int, j:int)->int:
    '''頂点iと頂点jの距離を計算'''
    k = self.lca.get(i, j)
    return self.lca.height[i]+self.lca.height[j]-2*self.lca.height[k]
