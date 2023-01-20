'''
https://leetcode.com/problems/find-k-closest-elements/
1:51
2:04 done
'''

from david import *
clean()

import bisect

def find_k_closest(values, k, x):
    insertion_index = bisect.bisect_left(values, x)
    # values[:insertion_index] are < x
    # values[insertion_index:] are >= x
    # the next value to be included that is >= x
    end = insertion_index
    # the next value to be included that is < x
    start = end - 1
    for i in range(k):
        if start < 0:
            return values[:k]
        else:
            start_value = values[start]

        try:
            end_value = values[end]
        except IndexError:
            return values[-k:]

        if abs(start_value - x) <= abs(end_value - x):
            start -= 1
        else:
            end += 1

    return values[start+1: end]

print(find_k_closest([1,2,3,4,5], 4, 3))
