# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_C

N = int(input())
KC = [ list(map(int, input().split())) for _ in range(N) ]
Q = int(input())
UV = [ list(map(int, input().split())) for _ in range(Q) ]

K = [ kc[0] for kc in KC ]
C = [ kc[1:] for kc in KC ]

parent = [ -1 for _ in range(N) ]
for i in range(N):
  for j in C[i]:
    parent[j] = i

from lib.graph.tree.tree import get_root, get_children, get_height
root = get_root(parent, -1)
children = get_children(parent, root)
height = get_height(root, children)

import math
from lib.doubling.doubling import initialize
M = int(math.log2(N))+1
doubling = initialize(parent, M)

from lib.graph.tree.lca.doubling import query
results = [ str(query(height, doubling, u, v)) for (u, v) in UV ]
print("\n".join(results))