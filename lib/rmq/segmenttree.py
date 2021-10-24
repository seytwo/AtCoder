from lib.segmenttree.segmenttree import SegmentTree
class RMQ(SegmentTree):
  def __init__(self, N:int)->None:
    INF:float = float("inf")
    aggregate = min
    super().__init__(N, INF, aggregate)
    return