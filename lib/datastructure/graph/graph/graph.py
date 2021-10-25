class Graph:
  def __init__(self, N:int, edges:list, directed:bool=False)->None:
    self.N = N
    self.adjacents = self.get_adjecents(edges, directed)
    return
  def get_adjecents(self, edges:list, directed:bool=False)->list:
    adjacents = [ set() for _ in range(self.N) ]
    for (i, j) in edges:
      adjacents[i].add(j)
      if not directed:
        adjacents[j].add(i)
    return adjacents
