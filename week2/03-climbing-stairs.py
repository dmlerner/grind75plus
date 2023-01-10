# https://leetcode.com/problems/climbing-stairs/
# 15:38-15:41 (recursive) 15:51 (iterative)
from functools import cache


@cache
def ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return ways(n - 1) + ways(n - 2)


def ways2(n):
    if n <= 1:
        return 1
    dp = 1, 1

    i = 2
    while i <= n:
        dp = dp[1], sum(dp)
        i += 1
    return dp[1]


for i in range(0, 30):
    print(i)
    print(ways(i), ways2(i))
    assert ways(i) == ways2(i)
