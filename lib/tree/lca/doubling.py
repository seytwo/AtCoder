# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_C
from lib.tree.tree import Tree
from lib.tree.height.height import get_height
from lib.unclassified.doubling import Doubling
class LCA(Doubling):
  def __init__(self, tree:Tree)->None:
    next:list = tree.parent.copy()
    next[tree.root] = tree.root
    super().__init__(next)
    self.height:list = get_height(tree)
    return
  def get(self, i:int, j:int)->int:
    '''頂点iと頂点jの最小共通先祖を取得'''
    (i, j) = self.sort_(i, j)
    i = self.balance_(i, j)
    if i == j:
      return i
    for k in reversed(range(self.M)):
      (i_, j_) = (self[i][k], self[j][k])
      (i, j) = (i_, j_) if i_ != j_ else (i, j)
    return self[i][0]
  def sort_(self, i:int, j:int)->tuple:
    return (i, j) if self.height[i] >= self.height[j] else (j, i)
  def balance_(self, i:int, j:int)->int:
    d:int = self.height[i]-self.height[j]
    return super().get(i, d)
