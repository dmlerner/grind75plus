# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# ten twenty six - thirty seven

def distinct_iterator(iterable, reverse):
    it = iterable
    if reverse:
        it = reversed(it)

    last = None
    for index, i in enumerate(it):
        if i == last:
            continue
        last = i
        index = index if not reverse else len(iterable) - index - 1
        yield index, i

def two_sum_ii(numbers, target):
    forward_it = distinct_iterator(numbers, False)
    reverse_it = distinct_iterator(numbers, True)

    low = next(forward_it)
    high = next(reverse_it)

    while low[0] != high[0]:
        s = low[1] + high[1]
        if s == target:
            return low[0]+1, high[0]+1
        if s < target:
            low = next(forward_it)
        else:
            high = next(reverse_it)


def main():
    numbers = 2,7,11,15
    target = 9
    ans = two_sum_ii(numbers, target)

if __name__ == '__main__':
    main()
