# https://leetcode.com/problems/alien-dictionary/
# 2:50
# 3:13 maybe
# 3:15 no - I thought multiple solutions -> '', but that's only for 0 solutions.
# 3:18 124/127 pass
# 3:20 done

from itertools import pairwise
from collections import defaultdict


def get_ordered_pairs(words):
    for w1, w2 in pairwise(words):
        for (a, b) in zip(w1, w2):
            if a != b:
                yield a, b
                break
        else:
            if len(w1) > len(w2):
                raise ImpossibleException


def get_edges(words):
    predecessors_by_letter = defaultdict(set)
    successors_by_letter = defaultdict(set)
    for a, b in get_ordered_pairs(words):
        predecessors_by_letter[b].add(a)
        successors_by_letter[a].add(b)
    return predecessors_by_letter, successors_by_letter


class ImpossibleException(Exception):
    pass


def get_order(words):
    letters = set(letter for word in words for letter in word)
    predecessors_by_letter, successors_by_letter = get_edges(words)
    print(f"{predecessors_by_letter, =}")
    print(f"{successors_by_letter =}")
    frontier = set(filter(lambda letter: letter not in predecessors_by_letter, letters))
    while letters:
        print(f"{frontier =}")
        if not frontier:
            raise ImpossibleException
        next_letter = frontier.pop()
        letters.remove(next_letter)
        yield next_letter
        for letter in successors_by_letter[next_letter]:
            predecessors_by_letter[letter].remove(next_letter)
            if not predecessors_by_letter[letter]:
                frontier.add(letter)


def alien_order(words):
    try:
        return "".join(get_order(words))
    except ImpossibleException:
        return ""


# words = ["wrt","wrf","er","ett","rftt"]
words = ["zy", "zx"]
words = ["a", "b", "bb", "ba"]
words = ["abc", "ab"]
# print('ordered pairs', set(get_ordered_pairs(words)))
print("alien order", alien_order(words))
