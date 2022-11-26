# nine fifty four
# ten thirty two

def filter_nodes(start, get_neighbors, predicate):
    nodes = []
    def dfs(node):
        match predicate(node):
            case True:
                nodes.append(node)
            case False:
                for neighbor in get_neighbors(node):
                    dfs(neighbor)
    dfs(start)
    return nodes

def combination_sum(nums, target):
    nums = tuple(sorted(nums))
    def get_neighbor_combinations(combination):
        s = sum(combination)
        for num in nums:
            if combination and num < combination[-1]:
                continue
            if num + s <= target:
                yield combination + (num,)

    def pred(combination):
        return sum(combination) == target
    filtered = filter_nodes((), get_neighbor_combinations, pred)
    return filtered
    # print(f'{filtered=}')
    # return [f[1] for f in filtered]

# breakpoint()
nums = [2, 3, 6, 7]
target = 7
# (4, 2,1), 3
combs = combination_sum(nums, target)
print(f'{combs=}')
