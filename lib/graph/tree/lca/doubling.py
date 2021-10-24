def sort(height, i, j):
  '''高さ順に頂点iと頂点jを並び替え'''
  return (i, j) if height[i] >= height[j] else (j, i)

import lib.doubling.doubling as dbl
def balance(height, doubling, i, j):
  '''頂点iを頂点jと同じ高さまで上げる'''
  d = height[i]-height[j]
  return dbl.query(doubling, i, d)
  
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_C
def query(height, doubling, i, j):
  '''頂点iと頂点jの最小共通先祖を取得'''
  (i, j) = sort(height, i, j)
  i = balance(height, doubling, i, j)
  if i == j:
    return i
  M = len(doubling[0])
  for k in reversed(range(M)):
    (i_, j_) = (doubling[i][k], doubling[j][k])
    (i, j) = (i_, j_) if i_ != j_ else (i, j)
  return doubling[i][0]