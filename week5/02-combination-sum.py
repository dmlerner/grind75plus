# https://leetcode.com/problems/combination-sum/
# eight fifteen
# choked. try again later. TODO

from david import show
from functools import cache


@show
def find_combinations(nums, target, i=0, prefix_combinations=None):
    prefix_combinations = prefix_combinations or []
    # invariant: target + sum(pc) == original target for any pc in prefix_combinations
    # invariant: all pc have same sum
    # nums = list(set(nums))
    if target == 0:
        return prefix_combinations
    if target < 0:
        return []
    if i == len(nums):
        return []

    used_i_target = target - nums[i]
    incremented_i = i + 1

    suffix_combinations = (
        find_combinations(
            nums, used_i_target, i, [pc + [nums[i]] for pc in prefix_combinations]
        )
        + find_combinations(
            nums,
            used_i_target,
            incremented_i,
            [pc + [nums[i]] for pc in prefix_combinations],
        )
        + find_combinations(nums, target, incremented_i, prefix_combinations)
    )
    combinations = []
    for s in suffix_combinations:
        for p in prefix_combinations:
            combinations.append(p + s)
    return combinations


nums = [2, 1]
target = 3
print(find_combinations(nums, target))
