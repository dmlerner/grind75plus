# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit(prices):
    max_price_after = float('-inf')
    max_profit = 0
    for p in reversed(prices):
        max_profit = max(max_profit, max_price_after - p)
        max_price_after = max(max_price_after, p)
    return max_profit

prices = 7,6,4,3,1
print(max_profit(prices))
