# https://leetcode.com/problems/two-sum/


def f(nums, target):
    seen_num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen_num_to_index:
            return seen_num_to_index[complement], index
        seen_num_to_index[num] = index
