# https://leetcode.com/problems/sort-colors/
# three oh six
# three thirty

def show(colors, next_zero, active, next_two):
    out = []
    for i, c in enumerate(colors):
        o = ""
        c = str(c)
        if i == next_zero:
            o += "Z"
        if i == active:
            o += "A"
        if i == next_two:
            o += "T"
        o += f'({c})'
        out.append(o)
    max_len = 5#max(map(len, out))
    out = [(' '*max_len + o)[-max_len:] for o in out]
    print(', '.join(map(str, out)))

def sort_colors(colors):
    def swap(i, j):
        colors[i], colors[j] = colors[j], colors[i]

    next_zero = 0
    active = 0
    next_two = len(colors) - 1
    while active <= next_two:
        show(colors, next_zero, active, next_two)
        c = colors[active]
        if c == 0:
            swap(active, next_zero)
            next_zero += 1
            active += 1
            # if active < next_zero:
            #     active += 1
        elif c == 2:
            swap(active, next_two)
            next_two -= 1
            # if active > next_two:
            #     active -= 1
        else:
            active += 1

import random
# random.seed(1234)
colors = list(random.randint(0, 2) for i in range(7))
# colors = [0,1,1,2,0,1,0]
print(colors)
sort_colors(colors)
print(colors)

