# https://leetcode.com/problems/insert-interval/
# twelve oh five

from itertools import islice, chain


def find_first_index_gte(values, new_value):
    lower_bound = 0
    upper_bound = len(values)  # intentionally one past array bound

    while lower_bound != upper_bound:
        middle_index = (lower_bound + upper_bound) // 2
        middle_value = values[middle_index]

        if middle_value < new_value:
            lower_bound = middle_index + 1
        # elif middle_value >= new_value:
        else:
            upper_bound = middle_index

    return lower_bound


def overlaps(int1, int2):
    if int1[0] > int2[0]:
        return overlaps(int2, int1)
    return int1[0] <= int2[0] <= int1[1]


def merge(int1, int2):
    starts = int1[0], int2[0]
    stops = int1[1], int2[1]
    return [min(starts), max(stops)]


def insert(intervals, new_interval):
    new_interval_index = find_first_index_gte(intervals, new_interval)
    tail = intervals[new_interval_index:]
    del intervals[new_interval_index:]
    tail = iter(tail)

    if intervals and overlaps(new_interval, intervals[-1]):
        intervals[-1] = merge(new_interval, intervals[-1])
    else:
        intervals.append(new_interval)

    for interval in tail:
        if overlaps(interval, intervals[-1]):
            intervals[-1] = merge(interval, intervals[-1])
        else:
            intervals.append(interval)
            break
    intervals.extend(tail)

    return intervals


intervals = [[0, 3], [9, 12]]
print(f"{intervals=}")
new_interval = [7, 16]
print(f"{new_interval=}")
print(insert(intervals, new_interval))
