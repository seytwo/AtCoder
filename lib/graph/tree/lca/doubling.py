# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_C
from lib.graph.tree.tree import Tree, get_heights
from lib.doubling.doubling import Doubling
class LCA:
  def __init__(self, tree:Tree)->None:
    parent = tree.parent.copy()
    parent[tree.root] = tree.root
    self.doubling = Doubling(parent)
    self.height = get_heights(tree)
    return
  def get(self, i:int, j:int):
    '''頂点iと頂点jの最小共通先祖を取得'''
    (i, j) = self.sort_(i, j)
    i = self.balance_(i, j)
    if i == j:
      return i
    for k in reversed(range(self.doubling.M)):
      (i_, j_) = (self.doubling[i][k], self.doubling[j][k])
      (i, j) = (i_, j_) if i_ != j_ else (i, j)
    return self.doubling[i][0]
  def sort_(self, i, j):
    return (i, j) if self.height[i] >= self.height[j] else (j, i)
  def balance_(self, i, j):
    d = self.height[i]-self.height[j]
    return self.doubling.get(i, d)
