# https://leetcode.com/problems/largest-rectangle-in-histogram/
# seven twenty five
# seven thirty three have something typed anyway...
# seven fourty seven this looks better
# seven fourty nine passes (forgot the mq can end up not empty)


def get_max_area(heights):
    heights.append(0)
    max_area = 0
    mq = []

    for i, h in enumerate(heights):
        while mq and h < heights[mq[-1]]:
            height_index = mq.pop()
            height = heights[height_index]
            # of height_index
            csr = i
            if mq:
                csl = mq[-1]
                width = csr - csl - 1
            else:
                # TODO? always true or just at first?
                width = csr
            area = width * height
            max_area = max(max_area, area)

        mq.append(i)

    return max_area


#          0,1,2,3,4,5
heights = [2, 1, 5, 6, 2, 3]
assert get_max_area(heights) == 10
