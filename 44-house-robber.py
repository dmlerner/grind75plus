# https://leetcode.com/problems/house-robber/
# 7:34
# 7:37 done (@cache)
# 7:39 tested
# now for iterative...
# 7:45 done

from functools import cache

def max_theft(values):

    @cache
    def max_theft_starting_at(i):
        if i == len(values):
            return 0
        if i == len(values) - 1:
            return values[-1]
        return max(values[i] + max_theft_starting_at(i+2), max_theft_starting_at(i+1))

    return max_theft_starting_at(0)

def max_theft_iterative(values):
    max_from_two_later = 0
    max_from_one_later = values[-1]
    theft = max_from_one_later
    house = len(values) - 1
    while house > 0:
        house -= 1
        theft_robbing_house = values[house] + max_from_two_later
        theft_not_robbing_house = max_from_one_later
        theft = max(theft_robbing_house, theft_not_robbing_house)
        max_from_two_later, max_from_one_later = max_from_one_later, theft
    return theft

values = [1,2,3,1]
print(max_theft_iterative(values))


