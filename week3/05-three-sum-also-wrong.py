# https://leetcode.com/problems/3sum/
# nine twenty five
# this one is wrong too
# there is no linear time solution
# get_next_larger is just impossible.

from collections import Counter

get_number = lambda num_and_count: num_and_count[0]
get_count = lambda num_and_count: num_and_count[1]


def get_sorted_with_counts(nums):
    sorted_nums = sorted(nums)
    sorted_with_counts = [[sorted_nums[0], 0]]
    for num in sorted_nums:
        if num == get_number(sorted_with_counts[-1]):
            sorted_with_counts[-1][1] += 1
        else:
            sorted_with_counts.append([num, 1])
    return sorted_with_counts


def is_valid(indices, swc):
    uses_of_number = Counter()
    if not all(map(lambda i: 0 <= i < len(swc), indices)):
        return False
    for number in get_numbers(indices, swc):
        uses_of_number[number] += 1

    for index in indices:
        number, count = swc[index]
        if uses_of_number[number] > count:
            return False
    return True


def get_numbers(indices, swc):
    # print(indices)
    return list(map(get_number, map(swc.__getitem__, indices)))


def get_next_larger(indices, swc):
    next_larger = indices[:]
    next_larger[0] += 1
    if not is_valid(next_larger, swc):
        next_larger[0] -= 1
        next_larger[1] += 1
    if is_valid(next_larger, swc):
        return next_larger


def get_next_smaller(indices, swc):
    next_smaller = indices[:]
    next_smaller[2] -= 1
    if is_valid(next_smaller, swc):
        return next_smaller


def three_sum(nums):
    # if len(nums) < 3:
    #     return []

    triples = []

    sorted_with_counts = get_sorted_with_counts(nums)
    i = 0
    j = 0 if get_count(sorted_with_counts[0]) > 1 else 1
    k = len(sorted_with_counts) - 1
    indices = [i, j, k]
    # try:
    #     assert is_valid(indices, sorted_with_counts)
    # except:
    #     return []

    while indices:
        s = sum(get_numbers(indices, sorted_with_counts))
        if s == 0:
            triples.append(list(get_numbers(indices, sorted_with_counts)))
            indices = get_next_larger(indices, sorted_with_counts)
        elif s < 0:
            indices = get_next_larger(indices, sorted_with_counts)
        else:
            indices = get_next_smaller(indices, sorted_with_counts)

    return triples


nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0]
# breakpoint()
# for i in distinct_sorted_iterator(nums, True):
#     # 1/0
ts = three_sum(nums)
print(ts)
