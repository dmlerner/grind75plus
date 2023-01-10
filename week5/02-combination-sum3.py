# ten thirty four
# ten fifty one


def combination_sum(nums, target):
    combinations = []

    def dfs(combination, i, target):
        if target == 0:
            combinations.append(combination)
            return
        if target < 0:
            return
        for i in range(i, len(nums)):
            dfs(combination + (nums[i],), i, target - nums[i])

    dfs((), 0, target)
    return combinations


nums = [2, 3, 6, 7]
target = 7
combs = combination_sum(nums, target)
print(f"{combs=}")
