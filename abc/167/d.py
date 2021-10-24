# https://atcoder.jp/contests/abc167/tasks/abc167_d

(N, K) = map(int, input().split())
A = list(map(lambda i: int(i)-1, input().split()))

import math
from lib.doubling.doubling import get_doubling, get_knext
M = int(math.log2(K))+1
doubling = get_doubling(A, M)
result = get_knext(doubling, 0, K)
print(result+1)