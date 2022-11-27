# https://leetcode.com/problems/partition-equal-subset-sum/
# seven thirty eight - seven fourty three (provisionally)
# appears correct, but DLE (fourty seven)
# even with caching!
# seven fifty two - marginally under time limit
# lower fan out is a good thing. 6.5 s -> 2.7s

from collections import Counter
from functools import cache

def remove_duplicates(nums):
    without_duplicates = []
    c = Counter(nums)
    for num, count in c.items():
        if count % 2:
            without_duplicates.append(num)
    return without_duplicates

def can_partition(nums, do_remove_duplicates=False):
    if do_remove_duplicates and can_partition(remove_duplicates(nums), False):
        return True
    s = sum(nums)
    if s % 2:
        return False
    target = s/2
    # optional
    nums.sort(reverse=True)
    return can_subset_sum(nums, target)

def can_subset_sum(nums, target):
    @cache
    def dfs(i, target):
        # can we sum to target using num[i:]?
        if i >= len(nums):
            return False
        if target < 0:
            return False
        if target == 0:
            return True
        if dfs(i+1, target) or dfs(i+1, target-nums[i]):
           return True
        return False
        # for j in range(i, len(nums)):
        #     # the next num I actually use is num[j]
        #     new_target = target - nums[j]
        #     if dfs(j+1, new_target):
        #         return True
        # return False
    return dfs(0, target)


import time
nums = [1, 5, 11, 5]
nums = [4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,12,12,12,12,12,12,12,12,16,16,16,16,16,16,16,16,20,20,20,20,20,20,20,20,24,24,24,24,24,24,24,24,28,28,28,28,28,28,28,28,32,32,32,32,32,32,32,32,36,36,36,36,36,36,36,36,40,40,40,40,40,40,40,40,44,44,44,44,44,44,44,44,48,48,48,48,48,48,48,48,52,52,52,52,52,52,52,52,56,56,56,56,56,56,56,56,60,60,60,60,60,60,60,60,64,64,64,64,64,64,64,64,68,68,68,68,68,68,68,68,72,72,72,72,72,72,72,72,76,76,76,76,76,76,76,76,80,80,80,80,80,80,80,80,84,84,84,84,84,84,84,84,88,88,88,88,88,88,88,88,92,92,92,92,92,92,92,92,96,96,96,96,96,96,96,96,97,99]
s = time.time()
can_partition(nums, False)
e = time.time()
print(e - s)
