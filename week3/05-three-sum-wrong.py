# The bug here is that if there are repeats,
# two iterators could share a value per problem statement
# but I don't allow it


def distinct_sorted_iterator(iterable, reverse):
    # assumes sorted
    n = len(iterable)
    if reverse:
        iterable = reversed(iterable)

    iterator = iter(iterable)

    last = None
    for index, i in enumerate(iterator):
        if i != last:
            last = i
            index = index if not reverse else (n - index - 1)
            yield index, i


def three_sum(nums):
    if len(nums) < 3:
        return []

    nums.sort()

    triples = []

    i_iter = distinct_sorted_iterator(nums, False)
    j_iter = distinct_sorted_iterator(nums, False)
    next(j_iter)
    k_iter = distinct_sorted_iterator(nums, True)
    iters = i_iter, j_iter, k_iter

    # invariant: i < j < k
    # invariant: nums[i] != nums[i-1]
    # invariant: nums[j] != nums[j-1]
    # invariant: nums[k] != nums[k+1]

    get_index = lambda index_and_number: index_and_number[0]
    get_number = lambda index_and_number: index_and_number[1]

    candidate = list(map(next, iters))

    def f(candidate):
        return get_index(candidate[1]) != get_index(candidate[2])

    while f(candidate):
        candidate_sum = sum(map(get_number, candidate))
        if candidate_sum <= 0:
            if candidate_sum == 0:
                triples.append(list(map(get_number, candidate)))
            i, j, k = map(get_index, candidate)
            candidate[0] = next(i_iter)
            if get_index(candidate[0]) == j:
                candidate[1] = next(j_iter)
                if get_index(candidate[1]) == k:
                    break
        else:
            candidate[2] = next(k_iter)

    return triples
