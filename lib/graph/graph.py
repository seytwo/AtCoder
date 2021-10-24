def get_adjecents(N, edges, directed=False):
  '''隣接頂点リストを取得'''
  adjacents = [ set() for _ in range(N) ]
  for (i, j) in edges:
    adjacents[i].add(j)
    if not directed:
      adjacents[j].add(i)
  return adjacents
  
def get_weight(edges, weights):
  '''隣接頂点の組から重みを取得する辞書を作成'''
  return { (i, j) : w for ((i, j), w) in zip(edges, weights) }