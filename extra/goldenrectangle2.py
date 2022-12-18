# eight thirty eight
# eight fourty eight might work
# eight fifty: appears to

# copied from 8.10
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
    h = [[1] * C for r in range(R)]
    for r in range(R):
        for c in range(C - 2, -1, -1):
            if rectangle[r][c + 1] > rectangle[r][c]:
                h[r][c] = h[r][c + 1] + 1
    return h

def max_golden_rectangle_area(rectangle):
    """
    width >= 2 ascending within rows
    """
    max_area = 0
    R, C = len(rectangle), len(rectangle[0])
    h = get_h(rectangle)

    for c in range(C):
        column = [h[r][c] for r in range(R)]
        column = [c  if c != 1 else 0 for c in column]
        max_area = max(get_max_area(column), max_area)

    return max_area


def naive(matrix):
    # breakpoint()

    R, C = len(matrix), len(matrix[0])
    def f(r1, c1, w, h):
        # if (r1, c1, w, h) == (0, 2, 2, 1):
        #     breakpoint()
        for c2 in range(max(1, c1), c1+w):
            for r2 in range(r1, min(r1+h, R)):
                if matrix[r2][c2] >= matrix[r2][c2-1]:
                    return 0
        return w * h

    largest = 0
    for r1 in range(R):
        for c1 in range(C):
            for w in range(2, C-r1-1):
                for h in range(1, R):
                    _f = f(r1, c1, w, h)
                    if _f >= 2:
                        print(r1, c1, w, h, _f)
                    largest = max(largest, _f)
    return largest

from random import randint, seed

def show_rect(r):
    for row in r:
        row = [h if h != 1 else 0 for h in row]
        print(''.join(map(str, row)))

seed(1234)
def test():
    for i in range(10000):
        print(f'{i=}')
        R, C = randint(1, 9), randint(1, 9)
        R, C = 3,3
        x = rectangle = [[randint(1, 9) for c in range(C)] for r in range(R)]
        n, m = naive(rectangle), max_golden_rectangle_area(rectangle)
        if n != m:
            # print(R, C)
            # print(rectangle)
            print('fail')
            print('naive: ', n)
            print('me   : ', m)
            print()
            print('rectangle: ')
            show_rect(rectangle)
            print()
            print('h        : ')
            print(get_h(rectangle))
            show_rect(get_h(rectangle))
            break

rectangle = list(map(lambda x: [int(c) for c in x], ['2347123','3964217']))
rectangle = [[2,3,4,7,1,2,3], [3,9,6,4,2,1,7]]
want = [[4,3,2,1,3,2,1],[2,1,1,1,1,2,1]]
h = get_h(rectangle)
show_rect(rectangle)
print()
show_rect(h)
print()
show_rect(want)
assert h == want
print('get_h passes')
print('.'*50)
print()
assert max_golden_rectangle_area(rectangle) == 4
print('my test case passes')
print('.'*50)
print()

test()
