# https://leetcode.com/problems/maximum-subarray/
from itertools import islice


def max_subarray(nums):
    nums = iter(nums)
    best_sum = running_sum = next(nums)
    for num in nums:
        running_sum = max(running_sum + num, num)
        best_sum = max(best_sum, running_sum)
    return best_sum


print(max_subarray((1, 2, 3, 4)))
