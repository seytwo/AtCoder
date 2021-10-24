def get_root(parent, c):
  '''根(親=c)のインデックスを取得'''
  for (i, j) in enumerate(parent):
    if j == c:
      return i
  raise ValueError()

def get_children(parent, root):
  '''子リストを取得'''
  N = len(parent)
  children = [ set() for _ in range(N) ]
  for (i, j) in enumerate(parent):
    if i == root:
      continue
    children[j].add(i)
  return children

def get_height(root, children):
  '''高さを取得'''
  N = len(children)
  height = [ None for _ in range(N) ]
  nodes = [(root, 0)]
  while len(nodes) != 0:
    (i, h) = nodes.pop()
    height[i] = h
    for j in children[i]:
      nodes.append((j, h+1))
  return height