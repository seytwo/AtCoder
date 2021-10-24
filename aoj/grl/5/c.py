# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_C

N = int(input())
KC = [ list(map(int, input().split())) for _ in range(N) ]
Q = int(input())
UV = [ list(map(int, input().split())) for _ in range(Q) ]

K = [ kc[0] for kc in KC ]
C = [ kc[1:] for kc in KC ]

edges = []
for (i, c) in enumerate(C):
  for j in c:
    edges.append((i, j))

nodes = set(range(N))
for c in C:
  for i in c:
    nodes.remove(i)
root = list(nodes)[0]
  
from lib.graph.tree.tree import Tree
tree = Tree(edges, root)

from lib.graph.tree.lca.doubling import LCA
lca = LCA(tree)
results = [ lca.get(u, v) for (u, v) in UV ]
print("\n".join(map(str, results)))