from lib.tree.tree import Tree
def get_height(tree:Tree)->list:
  height = [None]*tree.N
  queue:list = [(tree.root, 0)]
  while len(queue) != 0:
    (i, h) = queue.pop()
    height[i] = h
    for j in tree.children[i]:
      queue.append((j, h+1))
  return height
