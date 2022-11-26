# https://leetcode.com/problems/contains-duplicate/
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
