# https://atcoder.jp/contests/abc167/tasks/abc167_d
import math
class Doubling(list):
  def __init__(self, next:list, M:int=None)->None:
    N:int = len(next)
    M:int = int(math.log2(N))+1 if M is None else M
    iterable:list = [ [ next[i] for _ in range(M) ] for i in range(N) ]
    for k in range(1, M):
      for i in range(N):
        j = iterable[i][k-1]
        iterable[i][k] = iterable[j][k-1]
    super().__init__(iterable)
    self.M:int = M
    return
  def get(self, i:int, d:int)->int:
    '''要素iのd個先の要素を取得'''
    k:int = 0
    while d > 0:
      if d&1 == 1:
        i = self[i][k]
      d = d>>1
      k += 1
    return i
