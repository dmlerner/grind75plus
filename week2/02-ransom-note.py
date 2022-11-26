# https://leetcode.com/problems/ransom-note/
# 3:34 - 3:36
from collections import Counter

def can_construct(note, magazine):
    note_counts = Counter(note)
    magazine_counts = Counter(magazine)
    for letter in note_counts:
        if magazine_counts[letter] < note_counts[letter]:
            return False
    return True

def can_construct2(note, magazine):
    note_counts = Counter(note)
    magazine_counts = Counter(magazine)
    return not any(map(lambda letter: magazine_counts[letter] < note_counts[letter], note_counts))
