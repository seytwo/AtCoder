import math
class SegmentTree(list):
  def __init__(self, N:int, INF:float, aggregate)->None:
    N:int = 2**(int(math.log2(N))+1)
    iterable:list = [INF]*(2*N-1)
    super().__init__(iterable)
    self.N:int = N
    self.INF:float = INF
    self.aggregate = aggregate
    return
  def set(self, value:float, i:int)->None:
    i += self.N-1
    self[i] = value
    while i > 0:
      i:int = self.parent_(i)
      (l, r) = self.children_(i)
      (l, r) = (self[l], self[r])
      self[i] = self.aggregate(l, r)
    return
  def get(self, l:int, r:int)->float:
    return self.get_(l, r, 0, self.N, 0)
  def get_(self, l:int, r:int, i:int, j:int, k:int)->float:
    if (j <= l) or (r <= i):
      return self.INF
    if (l <= i) and (j <= r):
      return self[k]
    c:int = (i+j)//2
    (kl, kr) = self.children_(k)
    i:float = self.get_(l, r, i, c, kl)
    j:float = self.get_(l, r, c, j, kr)
    return self.aggregate(i, j)
  def children_(self, i:int)->tuple:
    return (self.left_(i), self.right_(i))
  def left_(self, i:int)->int:
    return 2*i+1
  def right_(self, i:int)->int:
    return 2*i+2
  def parent_(self, i:int)->int:
    return (i-1)//2
    