# https://atcoder.jp/contests/abc167/tasks/abc167_d

def get_doubling(next, M):
  '''2^M個先までのダブリング配列を取得'''
  N = len(next)
  doubling = [ [ next[i] for _ in range(M) ] for i in range(N) ]
  for k in range(1, M):
    for i in range(N):
      j = doubling[i][k-1]
      doubling[i][k] = doubling[j][k-1]
  return doubling

def get_knext(doubling, i, d):
  '''頂点iのd個先の頂点を取得'''
  k = 0
  while d > 0:
    if d&1 == 1:
      i = doubling[i][k]
    d = d>>1
    k += 1
  return i
