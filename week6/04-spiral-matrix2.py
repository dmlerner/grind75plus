# nine oh seven - nine twenty five

RIGHT, DOWN, LEFT, UP = range(4)

def get_next_position(r, c, direction, undo=False):
    undo_sign = -1 if undo else 1
    if direction == RIGHT:
        c += undo_sign
    elif direction == DOWN:
        r += undo_sign
    elif direction == LEFT:
        c -= undo_sign
    elif direction == UP:
        r -= undo_sign
    return r, c

def to_spiral(mat):
    r = 0
    c = -1
    direction = RIGHT
    unused = len(mat)*len(mat[0])

    while unused:
        r, c = get_next_position(r, c, direction)

        if (v := get(mat, r, c)) is None:
            r, c = get_next_position(r, c, direction, True)
            direction = (direction + 1)%4
        else:
            mat[r][c] = None
            yield v
            unused -= 1

def get(mat, r, c):
    if not 0 <= r < len(mat):
        return
    if not 0 <= c < len(mat[0]):
        return
    return mat[r][c]

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print("\n".join(map(str, mat)))
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
expected = [1,2,3,4,8,12,11,10,9,5,6,7]
print(f"{expected=}")
actual = list(to_spiral(mat))
print(f"{actual=}")
assert actual == expected
