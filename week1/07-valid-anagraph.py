from collections import Counter


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    shorter, longer = sorted((s, t), key=len)
    shorter_counts = Counter(shorter)
    for char in longer:
        if not shorter_counts[char]:
            return False
        shorter_counts[char] -= 1
    return True
