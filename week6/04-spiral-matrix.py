# https://leetcode.com/problems/spiral-matrix/
# eight thirty
# TODO: try again

# def get_row(mat, r, c, n):
#     r = r % len(mat)
#     c = c % len(mat[0])
#     return mat[r][c:c+n]
# def get_col(mat, r, c, n):
#     r = r % len(mat)
#     c = c % len(mat[0])
#     return [mat[R][c] for R in range(r,r+n)]


def get_row(mat, r, c1, c2):
    return mat[r][c1:c2]


def get_col(mat, c, r1, r2):
    return [mat[ri][c] for ri in range(r1, r2)]


def to_spiral(mat):
    spiral = []
    spiral.extend(mat[0])
    R, C = len(mat), len(mat[0])
    i = 0
    while True:
        layer = [
            get_col(mat, C - 1 - i, 1 + i, R - i),  # right downward
            reversed(get_row(mat, R - 1 - i, i, C - 1 - i)),  # bottom leftward
            reversed(get_col(mat, i, 1 + i, R - 1 - i)),  # left upward
            get_row(mat, 1 + i, 1 + i, C - 1 - i), # top rightwrad
        ]  # top rightward
        for l in layer:
            spiral.extend(l)
        if not all(layer):
            return spiral
        i += 1

    # size = len(mat) - 1
    # depth = 0
    # while size > 0:

    #     get_col(mat, 1+depth, -1-depth, size) # right downward
    #     get_row(mat, -1-depth, -2, size) # bottom leftward
    #     size -= 1

    #     get_col(mat, -2, 0, size) # left upward
    #     get_row(mat, 1, 1, size) # top rightward
    #     size -= 1

    #     depth += 1


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print("\n".join(map(str, mat)))
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
expected = [1,2,3,4,8,12,11,10,9,5,6,7]
print(f"{expected=}")
actual = to_spiral(mat)
print(f"{actual=}")
assert actual == expected
