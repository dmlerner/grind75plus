# https://leetcode.com/problems/unique-paths/
# ten thiry seven - ten thirty eight
from math import comb
def u(m, n):
    total_moves = m - 1 + n - 1
    return comb(total_moves, m-1)
