# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A

(N, Q) = map(int, input().split())
CXY:list = [ list(map(int, input().split())) for _ in range(Q) ]

from lib.segmenttree.segmenttree import SegmentTree
INF:float = 2**31-1
aggregate = min
st:SegmentTree = SegmentTree(N, INF, aggregate)

results:list = []
for (c, x, y) in CXY:
  if c == 0:
    st.set(y, x)
  elif c == 1:
    result:float = st.get(x, y+1)
    results.append(result)
print("\n".join(map(str, results)))
