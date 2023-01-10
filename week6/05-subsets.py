# https://leetcode.com/problems/subsets/
# ten oh eight - ten twelve


def add_num(num, subsets):
    new_subsets = []
    for subset in subsets:
        new_subsets.append(subset + [num])
    return new_subsets


def get_subsets(nums):
    subsets = [[]]
    for num in nums:
        subsets.extend(add_num(num, subsets))
    return subsets
