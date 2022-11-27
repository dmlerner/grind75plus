class BiIterator:
    def __init__(self, iterable, n):
        self.length = n
        self.iterable = iterable
        self.forward_iter = iter(iterable)
        self.reversed_iter = iter(reversed(iterable))

    def next_from(self, it):
        if not self.length:
            raise StopIteration
        self.length -= 1
        return next(it)


    def front(self):
        return self.next_from(self.forward_iter)

    def back(self):
        return self.next_from(self.reversed_iter)

class BiIterator:
    def __init__(self, n, forward_iter, reverse_iter):
        self.length = n
        self.forward_iter = forward_iter
        self.reverse_iter = reverse_iter

    def next_from(self, it):
        if not self.length:
            raise StopIteration
        self.length -= 1
        yield next(it)

    def __iter__(self):
        yield from self.next_from(self.forward_iter)

    def __reversed__(self):
        yield from self.next_from(self.reverse_iter)

def get_dimensions(mat):
    return len(mat), len(mat[0])

def get_row_iterator(mat, r, reverse):
    R, C = get_dimensions(mat)
    cols = range(C)
    if reverse:
        cols = reversed(cols)
    for col in cols:
        yield mat[r][col]

def get_row_iterators(mat, r):
    return (get_row_iterator(mat, r, x) for x in (False, True))

def get_col_iterator(mat, c, reverse):
    R, C = get_dimensions(mat)
    rows = range(R)
    if reverse:
        rows = reversed(rows)
    for row in rows:
        yield mat[row][c]

def get_col_iterators(mat, c):
    return (get_col_iterator(mat, c, x) for x in (False, True))


def to_spiral(mat):
    R, C = get_dimensions(mat)
    row_iterators = [BiIterator(C, *get_row_iterators(mat, r)) for r in range(R)]
    col_iterators = [BiIterator(R, *get_col_iterators(mat, c)) for c in range(C)]
    n = R*C
    for idx, i in enumerate(row_iterators[0]):
        yield i

        for c in col_iterators:


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
to_spiral(mat)
