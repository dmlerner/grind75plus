"""
https://leetcode.com/problems/longest-consecutive-sequence/
11:39
11:47 idea
11:48 34/72 pass
12:03 69/72
"""
from david import sl, show


def show_dict(d):
    keys = list(d.keys())
    keys.sort()
    for k in keys:
        print(k, d[k])


def get_run(numbers, i):
    start = numbers[i]
    last = None
    while last is None or last == numbers[i] - 1:
        last = numbers[i]
        i += 1
    return start, last, i


def get_runs(numbers, i):
    numbers = numbers[: i + 1]
    numbers.sort()
    runs = []
    while i < len(numbers):
        start, last, i = get_run(numbers, i)
        runs.append((start, last))
    return runs


@show
def get_min_max_by_number(runs):
    min_by_number = {}
    max_by_number = {}
    for start, last in runs:
        for i in range(start, last + 1):
            min_by_number[i] = start
            max_by_number[i] = last
    return min_by_number, max_by_number


@show
def verify(numbers, i, min_by_number_actual, max_by_number_actual):
    min_by_number, max_by_number = get_min_max_by_number(get_runs(numbers, i))
    assert min_by_number == min_by_number_actual
    assert max_by_number == max_by_number_actual


def longest_consecutive(numbers):
    longest = 0
    max_by_number = {}
    min_by_number = {}
    for i, number in enumerate(numbers):
        # need to update min[number-1]'s min and max
        merge_down = number - 1 in min_by_number
        # need to update max[number+1]'s min and max
        merge_up = number + 1 in max_by_number
        min_by_number[number] = min_by_number.get(number - 1, number)
        max_by_number[number] = max_by_number.get(number + 1, number)

        if merge_down:
            max_by_number[min_by_number[number - 1]] = max_by_number[number]
        if merge_up:
            min_by_number[max_by_number[number + 1]] = min_by_number[number]

        verify(numbers, i, min_by_number, max_by_number)
        longest = max(longest, max_by_number[number] - min_by_number[number] + 1)
        sl()
        show_dict(min_by_number)
        show_dict(max_by_number)
    return longest


# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums = [-1, 9, -3, -6, 7, -8, -6, 2, 9, 2, 3, -2, 4, -1, 0, 6, 1, -9, 6, 8, 6, 5, 2]
nums = [
    -6,
    6,
    -9,
    -7,
    0,
    3,
    4,
    -2,
    2,
    -1,
    9,
    -9,
    5,
    -3,
    6,
    1,
    5,
    -1,
    -2,
    9,
    -9,
    -4,
    -6,
    -5,
    6,
    -1,
    3,
]
print(longest_consecutive(nums))
# 14
