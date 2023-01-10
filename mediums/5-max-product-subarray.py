# https://leetcode.com/problems/maximum-product-subarray/
# 10:40
from david import *


def split_by_zeros(values):
    split = []
    for v in values:
        if v == 0:
            return split
        split.append(v)

        # if v == 0:
        #     # if product is None:
        #     #     assert False
        #     #     product = 0
        #     #     continue
        #     if product < 0:
        #         product /= -min(map(abs, (product_to_first_negative, product_from_last_negative)))
        #     max_product = max(product, max_product)

        #     product = 1
        #     negatives = 0
        #     product_to_first_negative = 1
        #     product_from_last_negative = 1


def _get_max_product(values):
    max_product = float("-inf")
    product = 1
    # max_element = max_product

    # inclusive
    product_to_first_negative = 1
    product_from_last_negative = 1

    for v in values:
        # max_element = max(max_element, v)
        product *= v
        if v < 0:
            if product_from_last_negative == 1:
                product_to_first_negative *= v
            product_from_last_negative = v
        else:
            # v > 0
            if product_from_last_negative == 1:
                product_to_first_negative *= v
            else:
                product_from_last_negative *= v

        # sl()

    if product < 0:
        product /= -min(
            map(abs, (product_to_first_negative, product_from_last_negative))
        )
    max_product = max(product, max_product)

    # sl()

    # if max_element < 0:
    #     return max_element
    return int(max_product)


# nums = 0, 2, 3, 0
# nums = -2, 0, -1
# nums = 0, 2, 3, -2, 4, 0
nums = 2, 3, -2, 4
nums = -3, -1, -1
nums = (-2,)
print(get_max_product(nums))
