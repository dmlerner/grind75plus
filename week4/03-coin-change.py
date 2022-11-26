# https://leetcode.com/problems/coin-change/
# one fourty four two twelve
# extra optimizing killed @cache!
# didn't need second dfs argument
# but it may have sped things up
# certainly costs memory
from david import show

IMPOSSIBLE = float("inf")
from functools import cache


def fewest_coins(coins, amount):
    coins.sort(reverse=True)
    record = IMPOSSIBLE

    @cache
    # @show
    def dfs(amount, first):
        nonlocal record
        if amount == 0:
            return 0
        if amount < 0:
            return IMPOSSIBLE
        if first >= len(coins):
            return IMPOSSIBLE
        # if using == record:
        #     return IMPOSSIBLE

        coins_used = min(
            1 + dfs(amount - coins[first], first),
            1 + dfs(amount - coins[first], first + 1),
            dfs(amount, first + 1),
        )
        record = min(record, coins_used)
        return coins_used

    coins_used = dfs(amount, 0)
    if coins_used == IMPOSSIBLE:
        return -1
    return coins_used


coins = [3, 7, 405, 436]
amount = 8839
print(fewest_coins(coins, amount))
