# https://leetcode.com/problems/product-of-array-except-self/
# two nineteen - two twenty six


from itertools import accumulate, starmap
from operator import mul


def product_except_self(nums):
    prefix_products = list(accumulate(nums, mul))
    suffix_products = list(reversed(list(accumulate(reversed(nums), mul))))
    products = [suffix_products[1]]
    products.extend(starmap(mul, zip(prefix_products, suffix_products[2:])))
    products.append(prefix_products[-2])
    return products
