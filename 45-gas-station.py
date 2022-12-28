# https://leetcode.com/problems/gas-station/
# 7:47
# 8:15 well I'm stumped.
# done for the night
from itertools import accumulate as acc
from operator import add

def accumulate(arr):
    return list(acc(arr, add))
print(accumulate([2, 3, 4]))


def find_starting_station(gas, cost):
    # a_g[i] = total gas picked up from stations [0, i]
    accumulated_gas = accumulate(gas)
    accumulated_cost = accumulate(cost)
    # useful because it tells us how much gas you pick up on interval [i, j]
    # wrapping around if i > j or i-1 < 0
    # gas_between(i, j) = accumulated_gas[j] - accumulated_gas[i-1]
