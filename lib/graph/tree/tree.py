from lib.graph.graph import Graph
class Tree(Graph):
  def __init__(self, edges:list, root:int)->None:
    N = len(edges)+1
    super().__init__(N, edges)
    self.root = root
    self.parent = self.get_parents()
    self.children = self.get_children()
    return
  def get_parents(self):
    parent = [None]*self.N
    used = set([self.root])
    nodes = [self.root]
    while len(nodes) != 0:
      i = nodes.pop()
      for j in self.adjacents[i]:
        if j in used:
          continue
        parent[j] = i
        used.add(j)
        nodes.append(j)
    return parent
  def get_children(self):
    children = [ set() for _ in range(self.N) ]
    for (i, j) in enumerate(self.parent):
      if j is None:
        continue
      children[j].add(i)
    return children

def get_heights(tree:Tree)->list:
  '''高さを取得'''
  height = [None]*tree.N
  nodes = [(tree.root, 0)]
  while len(nodes) != 0:
    (i, h) = nodes.pop()
    height[i] = h
    for j in tree.children[i]:
      nodes.append((j, h+1))
  return height
