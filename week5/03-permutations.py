# https://leetcode.com/problems/permutations/
# ten fifty five
# eleven twenty four
from david import show

def get_permutations(nums):
    n = len(nums)
    permutations = []
    # set the first unused position to every unused index
    def dfs(permutation, unused):
        if not unused:
            permutations.append([nums[p] for p in permutation])
            return
        first_none_index = permutation.index(None)
        for index in unused:
            permutation[first_none_index] = index
            dfs(permutation, unused - {index})
            permutation[first_none_index] = None
    dfs([None]*len(nums), set(range(n)))
    return permutations

def get_permutations2(nums):
    n = len(nums)
    permutations = []
    # set every unused position to the first unused index
    def dfs(permutation, i):
        if i >= len(nums):
            permutations.append([nums[p] for p in permutation])
            return
        for j in range(n):
            if permutation[j] is None:
                permutation[j] = i
                dfs(permutation, i+1)
                permutation[j] = None
    dfs([None]*len(nums), 0)
    return permutations

print(get_permutations2([9, 3, 7]))
