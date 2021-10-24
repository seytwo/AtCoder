(N, K) = map(int, input().split())
A = list(map(lambda i: int(i)-1, input().split()))

import math
from lib.doubling.doubling import Doubling
next = A
M = int(math.log2(K))+1
doubling = Doubling(next, M)
result = doubling.get(0, K)
print(result+1)