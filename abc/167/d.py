# https://atcoder.jp/contests/abc167/tasks/abc167_d

(N, K) = map(int, input().split())
A = list(map(lambda i: int(i)-1, input().split()))

import math
from lib.doubling.doubling import initialize, query
M = int(math.log2(K))+1
doubling = initialize(A, M)
result = query(doubling, 0, K)
print(result+1)