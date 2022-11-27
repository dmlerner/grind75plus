# https://leetcode.com/problems/container-with-most-water/
# one oh three - two twenty three but uh, something
# TODO: redo in one pass

class MQ(list):
    def append(self, x):
        if self and x[0] <= self[-1][0]:
            return
        super().append(x)


def most_water(heights):
    right = MQ()
    for (i, h) in reversed(list(enumerate(heights))):
        right.append((h, i))
    left = MQ()
    for (i, h) in enumerate(heights):
        left.append((h, i))


    l = 0
    r = 0
    max_area = 0
    while l < len(left) and r < len(right):
        hl, il = left[l] # 0, 1; 1, 8
        hr, ir = right[r] # 8, 7
        w = ir - il # 8
        h = min(hl, hr) # 8
        max_area = max(max_area, w*h) # 9; 64

        if hl <= hr:
            l += 1 # l = 1
        if hl >= hr:
            r += 1

    return max_area

heights = [1,8,6,2,5,4,8,3,7]
mw = most_water(heights)
