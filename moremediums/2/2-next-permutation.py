# https://leetcode.com/problems/next-permutation/
# 8:37
# 8:44 idea on paper

def get_argmin(values):
    argmin, min = None, float('inf')
    for i, v in enumerate(values):
        if v < min:
            argmin = i
            min = v
    return argmin

def index_of_smallest_over(key, values, start_of_descending_tail):
    for i in reversed(range(start_of_descending_tail, len(values))):
        if values[i] > key:
            return i

def swap(i, j, values):
    values[i], values[j] = values[j], values[i]

def reverse_tail(i, values):
    j = len(values) - 1
    while i < j:
        swap(i, j, values)
        i += 1
        j -= 1

def get_start_of_descending_tail(values):
    n = len(values)
    for i in reversed(range(1, n)):
        if values[i-1] < values[i]:
            return i
    return 0

def next_permutation(values):
    # [4,3,6,5,2,1]
    # TODO: uniqueness
    start_of_descending_tail = get_start_of_descending_tail(values) # 2
    if start_of_descending_tail == 0:
        reverse_tail(0, values)
        return

    pre_tail = start_of_descending_tail - 1 # 1
    new_pre_tail = index_of_smallest_over(values[pre_tail], values, start_of_descending_tail) # 3
    swap(pre_tail, new_pre_tail, values) # [4,5,6,3,2,1]
    reverse_tail(start_of_descending_tail, values) # [4, 5, 1, 2, 3, 6]
    return values

print(next_permutation([4,3,6,5,5,2,1]))
print(next_permutation([3, 2, 1]))


