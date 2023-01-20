'''
https://leetcode.com/problems/contiguous-array/
12:42
1:08 maybe algorithm
1:12 implemented, 361/564 pass
1:14 edge case fixed, all pass
1:18 cleaner
'''

from david import clean

def findMaxLength(nums):
    max_length = 0

    min_index_by_delta = {0: -1}
    delta = 0

    for i, num in enumerate(nums):
        if num == 0:
            delta += 1
        else:
            delta -= 1
        if delta in min_index_by_delta:
            length = i - min_index_by_delta[delta]
            max_length = max(max_length, length)
        else:
            min_index_by_delta[delta] = i


    return max_length

clean()
