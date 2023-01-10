# https://leetcode.com/problems/employee-free-time/
# 6:19
# 6:36 an idea

from david import show

import heapq
import bisect
from collections import namedtuple
from itertools import starmap


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"I({self.start}, {self.end})"

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, tuple) or isinstance(other, list):
            return self == Interval(*other)
        return self.start == other.start and self.end == other.end


def intersect(self, other):
    ts = max(self.start, other.start)
    te = min(self.end, other.end)
    if ts < te:
        return Interval(ts, te)


def to_intervals(time_pairs):
    return tuple(starmap(Interval, time_pairs))


def to_interval(time_pair):
    return Interval(*time_pair)


def get_first_free_interval_at_or_after(schedule, t):
    insertion_index = bisect.bisect(schedule, t, key=lambda interval: interval.start)
    if insertion_index == 0:
        return Interval(float("-inf"), schedule[0].start)

    last_before_index = insertion_index - 1

    if last_before_index == len(schedule) - 1:
        te = float("inf")
    else:
        te = schedule[last_before_index + 1].start

    ts = schedule[last_before_index].end
    return Interval(ts, te)


def get_first_free_interval_during(schedule, interval):
    first_free_interval_at_or_after = get_first_free_interval_at_or_after(
        schedule, interval.start
    )
    return intersect(first_free_interval_at_or_after, interval)


def _get_free_interval(schedules, candidate):
    for schedule in schedules:
        schedule_free_interval = get_first_free_interval_during(schedule, candidate)
        if schedule_free_interval is None:
            return False, Interval(
                get_first_free_interval_at_or_after(schedule, candidate.end).start,
                float("inf"),
            )
        candidate = schedule_free_interval
    return True, candidate


def get_free_interval(schedules, t):
    # find first common free interval starting not before t
    candidate = Interval(t, float("inf"))
    # it was cleaner having this method be recursive, but stack depth limits were a problem
    while True:
        found, new_candidate = _get_free_interval(schedules, candidate)
        if found:
            return new_candidate
        candidate = new_candidate


def get_common_free_times(schedules):
    t = float("-inf")
    while True:
        free_interval = get_free_interval(schedules, t)
        if free_interval.end == float("inf"):
            return
        if free_interval.start != float("-inf"):
            yield free_interval
        t = free_interval.end


assert get_first_free_interval_at_or_after(
    to_intervals([[1, 2], [5, 7]]), 1.5
) == Interval(2, 5)
assert get_first_free_interval_at_or_after(
    to_intervals([[1, 2], [5, 7]]), -3
) == Interval(float("-inf"), 1)

assert get_first_free_interval_during(
    to_intervals([[1, 2], [5, 7]]), to_interval([-10, 10])
) == Interval(-10, 1)
assert get_first_free_interval_during(
    to_intervals([[1, 2], [5, 7]]), to_interval([3, 6])
) == Interval(3, 5)
assert (
    get_first_free_interval_during(to_intervals([[1, 2], [5, 7]]), to_interval([5, 6]))
    is None
)

schedules = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
schedules = list(map(to_intervals, schedules))
assert tuple(get_common_free_times(schedules)) == to_intervals([[3, 4]])

schedules = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
"""
Help on built-in function bisect_right in module _bisect:

bisect_right(a, x, lo=0, hi=None, *, key=None)
    Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(i, x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
(END)
"""

from itertools import chain


class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        work = list(sorted(chain(*schedule), key=lambda x: x.start))
        result = []
        x = work[0]
        for y in work[1:]:
            if x.end < y.start:
                result.append(Interval(x.end, y.start))
                x = y
            elif y.end > x.end:
                x = y
        return result


import random
import time


def make_interval(min_val, max_val):
    assert min_val < max_val
    a, b = random.randint(min_val, max_val), random.randint(min_val, max_val)
    if a == b:
        return make_interval(min_val, max_val)
    return Interval(min(a, b), max(a, b))


def make_schedule(max_val, i):
    schedule = []
    times = [random.randint(0, max_val) for I in range(i * 3 + 6)]
    times.sort()
    I = 0
    while len(schedule) < i:
        schedule.append(Interval(times[I], times[I + 1]))
        I += 3
    assert len(schedule) == i
    return schedule


def make_intervals(e, i, max_val):
    return [make_schedule(max_val, i) for E in range(e)]


e = 500
i = 100000
max_val = 1000000000
schedule = make_intervals(e, i, max_val)

start = time.time()
s1 = Solution().employeeFreeTime(schedule)  # 35.7
stop = time.time()
dt1 = stop - start

start = time.time()
s2 = list(get_common_free_times(schedule))  # 1.80
stop = time.time()
dt2 = stop - start

speedup = dt1 / dt2  # 19.8

assert s1 == s2
