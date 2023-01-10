# https://leetcode.com/problems/binary-search/
def binary_search(values, target):
    return _binary_search(values, target, 0, len(values) - 1)


def _binary_search(values, target, lower_bound, upper_bound):
    if lower_bound > upper_bound:
        return -1

    middle = (lower_bound + upper_bound) // 2
    middle_value = values[middle]
    if target == middle_value:
        return middle

    if target < middle_value:
        upper_bound = middle - 1
    elif target > middle_value:
        lower_bound = middle + 1

    return _binary_search(values, target, lower_bound, upper_bound)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target)
