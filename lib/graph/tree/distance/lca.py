# https://atcoder.jp/contests/abc014/tasks/abc014_4
from lib.graph.tree.lca.doubling import get_lca
def get_distance(height, doubling, i, j):
  '''頂点iと頂点jの距離を計算'''
  k = get_lca(height, doubling, i, j)
  return height[i]+height[j]-2*height[k]
