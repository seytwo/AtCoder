# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A
from lib.array.range.segtree import SegmentTree
class RMQ(SegmentTree):
  def __init__(self, N:int)->None:
    INF:float = float("inf")
    aggregate = min
    super().__init__(N, INF, aggregate)
    return
