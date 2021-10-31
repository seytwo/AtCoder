# https://atcoder.jp/contests/abc014/tasks/abc014_4
from lib.tree.tree import Tree
from lib.tree.lca.doubling import LCA
class Distance(LCA):
  def __init__(self, tree:Tree)->None:
      super().__init__(tree)
      return
  def get(self, i:int, j:int)->int:
    '''頂点iと頂点jの距離を計算'''
    k = super().get(i, j)
    return self.height[i]+self.height[j]-2*self.height[k]
    