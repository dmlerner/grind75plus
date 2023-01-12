'''
https://leetcode.com/problems/rotate-array/
6:54
7:11 idea that I sure don't have a proof for off hand
7:15 implemented first pass
7:29 submit idea, 1/38 pass lol
7:31 use <=, now 28/38
7:32 k %= len(values), 38/38
This is a stupid fucking problem.
'''


def swap_chunks(values, i, j, k):
    ''' swap values[i:i+k] with values[j:j+k]'''
    for chunk_index in range(k):
        values[i+chunk_index], values[j+chunk_index] = values[j+chunk_index], values[i+chunk_index]

def rotate(values, k):
    k %= len(values)
    if k == 0:
        return
    n = len(values)
    i = 0
    j = n-k
    while i + k <= j:
        swap_chunks(values, i, n-k, k)
        i += k
    remainder = len(values) % k
    awkward = values[i: i + remainder]
    del values[i: i + remainder]
    values.extend(awkward)

values = list(range(8))
rotate(values, 2)
