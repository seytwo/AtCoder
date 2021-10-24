# https://atcoder.jp/contests/abc167/tasks/abc167_d
import math
class Doubling(list):
  def __init__(self, next, M=None):
    N = len(next)
    self.M = int(math.log2(N))+1 if M is None else M
    iterable = [ [ next[i] for _ in range(self.M) ] for i in range(N) ]
    for k in range(1, self.M):
      for i in range(N):
        j = iterable[i][k-1]
        iterable[i][k] = iterable[j][k-1]
    super().__init__(iterable)
    return
  def get(self, i, d):
    '''要素iのd個先の要素を取得'''
    k = 0
    while d > 0:
      if d&1 == 1:
        i = self[i][k]
      d = d>>1
      k += 1
    return i
