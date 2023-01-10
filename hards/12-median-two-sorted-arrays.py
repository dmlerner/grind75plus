# https://leetcode.com/problems/median-of-two-sorted-arrays/
# 1:25 start
# 1:40 uh let's try typing
# 2:00 other than a gazillion off by ones that might be right
# 2:09 well it passes for get_zeroth_element...
# ha, leetcode has no official solution and the top user one describes it as notoriously full of obobs
from david import show, recursion_limit, show_locals

import bisect


@show
def median(xs, i, j):
    assert xs
    n = j - i + 1
    middle = (i + j) // 2
    show_locals()
    # breakpoint()
    if n % 2:
        return xs[middle]
    left_of_middle = max(0, middle - 1)
    right_of_middle = left_of_middle + 1
    return (xs[left_of_middle] + xs[right_of_middle]) / 2
    # return sum(xs[max(0, middle-1):middle+1])/2


# def median2(xs, ys):
#     # assume odd total length
#     xi = 0
#     xj = len(xs) - 1
#     yi = 0
#     yj = len(ys) - 1
#     target_index = (len(xs) + len(ys))//2

#     xs_median = median(xs)
#     y_insertion = bisect.bisect(xs_median, ys, yi, yj)
#     # keep either elements under xs_median in both, or over in both


def get_index_and_pivot(xs, xi, xj):
    index = (xj + xi) // 2
    return index, xs[index]


@recursion_limit
@show
def get_ith_element(xs, ys, xi, xj, yi, yj, i, n):
    # return merge_sorted(xs[xi:xj+1], ys[yi:yj+1])[i]
    # breakpoint()
    nx = xj - xi + 1
    ny = yj - yi + 1
    assert nx >= 0
    assert ny >= 0
    assert n == nx + ny

    if nx < ny:
        return get_ith_element(ys, xs, yi, yj, xi, xj, i, n)

    if ny == 0:
        return xs[xi + i]

    total_elements = nx + ny
    assert 0 <= i < total_elements

    if total_elements == 1:
        # TODO: needed?
        if nx:
            return xs[xi]
        return ys[yi]

    xs_pivot_index, xs_pivot = get_index_and_pivot(xs, xi, xj)

    # where would pivot of x go in y?
    # that is, the pivot of the part of x still in consideration; x[xi:xj+1]
    # ignore duplicate elements
    xs_pivot_y_insertion_index = bisect.bisect(ys, xs_pivot, yi, yj + 1)  # + yi
    ys_below_xs_pivot = xs_pivot_y_insertion_index - yi
    # true for odd or even
    xs_below_xs_pivot = xs_pivot_index - xi
    # have to subtract out pivot itself
    # not used
    xs_above_xs_pivot = nx - xs_below_xs_pivot - 1

    total_below_xs_pivot = xs_below_xs_pivot + ys_below_xs_pivot
    show_locals()
    if total_below_xs_pivot == i:
        return xs_pivot
    elif total_below_xs_pivot < i:
        return get_ith_element(
            xs,
            ys,
            xs_pivot_index + 1,
            xj,
            xs_pivot_y_insertion_index,
            yj,
            i - total_below_xs_pivot,
            total_elements - total_below_xs_pivot - 1,
        )
    else:
        return get_ith_element(
            xs,
            ys,
            xi,
            xs_pivot_index - 1,
            yi,
            xs_pivot_y_insertion_index - 1,
            i,
            total_below_xs_pivot,
        )


xs = 1, 2, 3, 4, 5, 9, 10
ys = 0, 8, 11
merged = list(sorted(xs + ys))
print(xs)
print(ys)
print(merged)
for i in range(len(xs) + len(ys)):
    # for i in (1,):
    actual = get_ith_element(
        xs, ys, 0, len(xs) - 1, 0, len(ys) - 1, i, len(xs) + len(ys)
    )
    expected = merged[i]
    print(i, actual, expected)
    assert actual == expected
    print(i, "passes!")
    print("." * 50)
    print()
