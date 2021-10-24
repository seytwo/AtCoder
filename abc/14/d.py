N = int(input())
XY = [ list(map(lambda i: int(i)-1, input().split())) for _ in range(N-1) ]
Q = int(input())
AB = [ list(map(lambda i: int(i)-1, input().split())) for _ in range(Q) ]

from lib.graph.graph import get_adjecents
adjacents = get_adjecents(N, XY)

from lib.graph.tree.tree import get_parent, get_children, get_height
root = 0
parent = get_parent(adjacents, root)
children = get_children(parent, root)
height = get_height(root, children)

import math
from lib.doubling.doubling import get_doubling
parent[root] = root
M = int(math.log2(N))+1
doubling = get_doubling(parent, M)

from lib.graph.tree.distance.lca import get_distance
results = [ get_distance(height, doubling, a, b)+1 for (a, b) in AB ]
print("\n".join(map(str, results)))