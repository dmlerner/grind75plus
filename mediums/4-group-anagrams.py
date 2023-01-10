# 1:17
# 1:22

from collections import Counter, defaultdict
from string import ascii_lowercase

index_by_letter = {letter: i for (i, letter) in enumerate(ascii_lowercase)}


def get_letter_counts(word):
    counts = [0] * 26
    count_by_letter = Counter(word)
    for letter, count in count_by_letter.items():
        counts[index_by_letter[letter]] = count
    return tuple(counts)


def group_anagrams(words):
    groups_by_counts = defaultdict(list)

    for w in words:
        groups_by_counts[get_letter_counts(w)].append(w)

    return list(groups_by_counts.values())


words = ["cat", "tac", "at"]
print(group_anagrams(words))
