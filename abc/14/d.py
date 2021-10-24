# https://atcoder.jp/contests/abc014/tasks/abc014_4

N = int(input())
XY = [ list(map(lambda i: int(i)-1, input().split())) for _ in range(N-1) ]
Q = int(input())
AB = [ list(map(lambda i: int(i)-1, input().split())) for _ in range(Q) ]

from lib.graph.tree.tree import Tree
edges = XY
root = 0
tree = Tree(edges, root)

from lib.graph.tree.distance.lca import Distance
distance = Distance(tree)
results = [ distance.get(a, b)+1 for (a, b) in AB ]
print("\n".join(map(str, results)))