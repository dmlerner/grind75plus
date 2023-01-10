# https://leetcode.com/problems/merge-intervals/
# twelve fifty two - twelve fifty nine
# could use interval tree
def merge_all(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if overlaps(interval, merged[-1]):
            merged[-1] = merge(interval, merged[-1])
        else:
            merged.append(interval)
    return merged


def overlaps(a, b):
    if a[0] > b[0]:
        return overlaps(b, a)
    return b[0] <= a[1]


def merge(a, b):
    if a[0] > b[0]:
        return merge(b, a)
    return [a[0], max(a[1], b[1])]
