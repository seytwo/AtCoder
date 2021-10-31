# https://atcoder.jp/contests/abc167/tasks/abc167_d

(N, K) = map(int, input().split())
A = list(map(lambda i: int(i)-1, input().split()))

import math
from lib.unclassified.doubling import Doubling
M = int(math.log2(K))+1
doubling = Doubling(A, M)
result = doubling.get(0, K)
print(result+1)
