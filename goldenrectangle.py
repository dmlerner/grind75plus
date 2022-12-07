from david import show

def f(r1, c1, R, C):
    largest = 0
    height = 1
    while (r2 := r1 + height - 1) < R:
        width = 2
        while (c2 := c1 + width - 1) < C:
            if matrix[r2][c1] < matrix[r2][c2]:
                area = width * height
                largest = max(largest, area)
                width += 1
            else:
                break
        height += 1
    return largest

def naive(matrix):
    R, C = len(matrix), len(matrix[0])
    largest = 0
    for r1 in range(R):
        for c1 in range(C):
            largest = max(largest, f(r1, c1), R, C)
    return largest

def max_rectangle_in_hist(heights):
    pass

def mq(heights):
    # non strict increasing mq
    mq = []
    # first strictly smaller to the left; leftmost if a run of 'em
    fsl = [None]*len(heights)
    # first strictly smaller to the right
    # rightmost if a run of 'em
    # uh, surely I haven't implemented that for fsr
    fsr = [None]*len(heights)
    for i, h in enumerate(heights):
        # while the new height is too small, pop and update fsr
        while mq and h < heights[mq[-1]]:
            popped = mq.pop()
            fsr[popped] = i
        if mq:
            if heights[mq[-1]] == h:
                fsl[i] = fsl[mq[-1]]
            else:
                fsl[i] = mq[-1]
        mq.append(i)
    return fsl, fsr, mq

def compress(heights):
    ''' (i1 incl, i2 incl, h) '''
    # TODO: rewrite as generator
    compressed = []
    for i, h in enumerate(heights):
        if compressed and compressed[-1][-1] == h:
            compressed[-1][1] = i
        else:
            compressed.append([i,i,h])
    return compressed

# TODO: be more decoupled: work transparently, i.e. without thining about ranges. then fix up after.
def mq2(heights):
    compressed_heights = compress(heights)
    # print(f'{compressed_heights =}')
    mq = []
    fsl = [None]*len(heights)
    fsr = [None]*len(heights)
    fsr_todos = []
    for (i1, i2, h) in compressed_heights:
        # print('\n'.join(map(str, vars().items())))
        # breakpoint()
        while mq and h <= mq[-1][-1]: # while adding h would break strict monotonicity
            # print(i1, i2, h, mq)
            # assert h != mq[-1][-1]
            mqi1, mqi2, mqh = mq.pop()
            for i in range(mqi1,mqi2+1):
                fsr_todos.append(i)
            while fsr_todos:
                if h < heights[fsr_todos[-1]]:
                    fsr[fsr_todos.pop()] = i1
                else:
                    break

        if mq:
            for i in range(i1, i2+1):
                fsl[i] = mq[-1][0]
        mq.append([i1, i2, h])
    return fsl, fsr, mq

def get_fsl(heights):
    fsl = [None]*len(heights)
    for i, h in enumerate(heights):
        for j in range(i-1, -1, -1):
            if i - 1 >= 0 and heights[j] < h and (j == 0 or heights[j] != heights[j-1]):
                fsl[i] = j
                break
    return fsl

def get_fsr(heights):
    fsr = [None]*len(heights)
    for i, h in enumerate(heights):
        for j in range(i+1, len(heights)):
            if heights[j] < h and (j == len(heights)-1 or heights[j] != heights[j-1]):
                fsr[i] = j
                break
    return fsr

def verify(label, actual, expected, clean=str):
    if actual == expected:
        return
    print(label)
    print('actual:   ' + clean(actual))
    print('expected: ' + clean(expected))
    print()

clean = lambda x: str([str(x) if x is not None else '.' for x in x]).replace(',','').replace("'",'')

x = None

i =                [0,1,2,3,4,5,6,7,8]
h =                [0,1,2,2,3,3,2,2,1]
expect_fsl=        [x,0,1,1,2,2,1,1,0]
expect_fsr=        [x,x,8,8,6,6,8,8,x]
fsl, fsr, mq = mq2(h)

assert get_fsl(h) == expect_fsl
assert get_fsr(h) == expect_fsr
verify('fsl', fsl, get_fsl(h), clean)
verify('fsr', fsr, get_fsr(h), clean)
verify('mq', mq, [[0,0,0],[8,8,1]], clean)
