"""
https://leetcode.com/problems/longest-increasing-subsequence/
2:22
3:25 kill me
"""


def lenght_of_LIS(nums):
    chains = []
    # put each number in the longest chain we can add it to
    # each chain store as (head value, length)
    # start new chain only if can not go in any chain
    for i in range(len(nums) - 1, -1, -1):
        print(i, nums[i])
        # TODO: heap or do I need it at all? avoid all the sorting...
        chains.sort(key=lambda ab: -ab[1])
        for c, chain in enumerate(chains):
            if nums[i] < chain[0]:
                chains[c] = [nums[i], chain[1] + 1]
                break
        chains.append([nums[i], 1])
        print(chains)
        print()
    return max(l for (_, l) in chains)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [0, 1, 0, 3, 2, 3]
nums = [4, 1, 2, 3, 4, 1, 2, 3, 3, 4]
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
nums = [0, 1, 0, 3, 2, 3]
l = lenght_of_LIS(nums)
print()
print(nums)
print(l)

# official solution
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num

        return len(sub)
