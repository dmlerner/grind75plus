# https://leetcode.com/problems/trapping-rain-water/
from david import show, recursion_limit
# two oh two

'''
index i may be the left edge of trapped rain
if h[i-1] < h[i]
if there is a run of equal h
use the right edge
h[i-2] == h[i-1] == h[i] -> h[i] is edge (no water)
h[i+1] gets some water
i.e.: if left slope is positive at i, left boundary at i, water at i+1

similarly on right, but reversed
index i may be the right edge of trapped rain
if h[i+1] > h[i]
if there is a run of equal h
use the left edge
h[i+2] == h[i+1] == h[i] -> h[i] is edge (no water)
h[i-1] gets some water
i.e.: if right slope is negative at i, right boundary at i, water at i-1

if edges are l and r
actual height is
min(h[l], h[r])

volume trapped is trickier
note getting total, not max in one region
'''


def get_left_bounds(heights):
    count = 0
    i = 1
    while i < len(heights):
        count += 1
        # if count > 10:
        #     break
        # print(i)
        if heights[i-1] < heights[i]:
            i = get_right_of_run(heights, i)
            yield i
        i += 1

def get_right_bound(heights, l):
    i = l+1
    while i < len(heights)-1:
        if heights[i] > heights[i+1]:#heights[i] > heights[l] or heights[i] == heights[l] and i != l:
            # if True or heights[i] > heights[i+1]:
            return i
        i += 1
    # return len(heights) - 1

def get_right_of_run(heights, i):
    h = heights[i]
    while heights[i] == h:
        i += 1
    return i - 1
    # for j in range(i+1, len(heights)):
    #     if heights[j] != heights[i]:
    #         return j - 1

def calculate_volume(heights):
    total = 0
    left_boundary = None
    right_boundary = None
    to_fill = []
    for i, h in enumerate(heights[1:]):
        if heights[i-1] < h:
            left_boundary = i
        if h < heights[i+1]:
            pass

def calculate_volume2(heights):
    total = 0
    for l in get_left_bounds(heights):
        r = get_right_bound(heights, l)
        print(l, r)

def compress(heights):
    i = 0
    while i < len(heights):
        size = get_run_size(heights, i)
        yield (i, size)
        i += size

def get_run_size(heights, i):
    size = 1
    for j in range(i+1, len(heights)):
        if heights[j] == heights[i]:
            size += 1
        else:
            break
    return size

@show
@recursion_limit(30)
def ascends(i):
    return i in range(1, len(heights)) and heights[i-1] < heights[i]
@show
@recursion_limit(30)
def descends(i):
    return i in range(len(heights)-1) and heights[i+1] < heights[i]

from itertools import count

# @show
# @recursion_limit(2)
@show
@recursion_limit()
def get_plateau(i):
    start = next(filter(descends, range(i, len(heights))))
    end = next(filter(ascends, range(start, len(heights))))
    return start, end


# def calculate_volume3(heights):
#     volume = 0
#     heights = [0] + heights + [0]
#     # left = 0
#     for (i1, s1), (i2, s2) in pairwise(compress(heights)):
#         h1, h2 = heights[i1], heights[i2]
#         print(i1, i2, s1, s2, h1, h2)
#         height = min(h1, h2)
#         for j in range(i1+s1, i2):
#             print(f'{j=}')
#             assert heights[j] < height
#             volume += height - heights[j]
#     return volume

def calculate_volume4():
    volume = 0
    i = 0
    left = None
    while i < len(heights):
        try:
            right, next_left = get_plateau(i)
            if left:
                h = min(heights[left], heights[right])
                for j in range(left+1, right):
                    volume += h - heights[j]
            left = next_left
            i = next_left+1 # TODO: fewer variables
        except StopIteration:
            return volume
    assert False
    return volume

def cheat():
    # chat.openai.com translated official c++ solution, wow
    ans = 0
    current = 0
    st = []
    while current < len(heights):
        while st and heights[current] > heights[st[-1]]:
            top = st[-1]
            st.pop()
            if not st:
                break
            distance = current - st[-1] - 1
            bounded_heights = min(heights[current], heights[st[-1]]) - heights[top]
            print(current, st[-1],heights[current], heights[st[-1]], heights[top])
            ans += distance * bounded_heights
        st.append(current)
        current += 1
    return ans




i       =  0,1,2,3,4,5,6,7,8,9,0,1
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(list(get_left_bounds(heights)))
# heights = [3, 3, 3, 2, 2, 1, 2, 2, 3, 3]
v = cheat()
print(v)
assert v == 6

# @recursion_limit()
# def f(n):
#     if n == 0:
#         return 0
#     return 1 + f(n-1)
# print(f(5))
# print(f(12))
