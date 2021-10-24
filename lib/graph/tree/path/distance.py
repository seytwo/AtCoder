from lib.graph.tree.distance.lca import get_distance
def is_on_path(height, doubling, i, j, k):
  ik = get_distance(height, doubling, i, k)
  kj = get_distance(height, doubling, k, j)
  ij = get_distance(height, doubling, i, j)
  return ik+kj == ij
