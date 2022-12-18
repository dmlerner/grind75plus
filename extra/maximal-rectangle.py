# https://leetcode.com/problems/maximal-rectangle/

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
                width = csr
            area = width * height
            max_area = max(max_area, area)

        mq.append(i)

    return max_area

def get_h(rectangle):
    R, C = len(rectangle), len(rectangle[0])
    h = [[0] * C for r in range(R)]
    for r in range(R):
        for c in range(C - 1, -1, -1):
            if rectangle[r][c] == '1':
                h[r][c] = 1
                try:
                    h[r][c] += h[r][c+1]
                except IndexError:
                    pass

    return h

def max_all_ones(rectangle):
    max_area = 0
    R, C = len(rectangle), len(rectangle[0])
    h = get_h(rectangle)
    print(h)

    for c in range(C):
        column = [h[r][c] for r in range(R)]
        # column = [c  if c != 1 else 0 for c in column]
        max_area = max(get_max_area(column), max_area)

    return max_area

rectangle = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(max_all_ones(rectangle))
