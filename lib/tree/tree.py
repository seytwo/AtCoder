from lib.graph.graph import Graph
class Tree(Graph):
  def __init__(self, edges:list, root:int) -> None:
    N:int = len(edges)+1
    super().__init__(N, edges)
    self.root:int = root
    self.parent:list = [None]*N
    self.children:list = [ set() for _ in range(N) ]
    queue = [root]
    used = set()
    while len(queue) != 0:
      i = queue.pop()
      used.add(i)
      for j in self[i]:
        if j in used:
          continue
        self.parent[j] = i
        self.children[i].add(j)
        queue.append(j)
    return
