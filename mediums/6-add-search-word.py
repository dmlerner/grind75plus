# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# 6:20
# 6:31 14/29 (DLE)
# 6:31 18/29
# 6:45 passes (but barely)
"""
do faster recursion first!
don't cache search - adding changes its answer
"""

from david import show

from functools import cache


class WordDictionary:
    WILDCARD = "."
    WORD_MARKER = "$"

    def __init__(self):
        self.word_trie = {}

    @cache
    def addWord(self, word):
        assert "." not in word
        active = self.word_trie
        for letter in word:
            active = active.setdefault(letter, {})
        active[WordDictionary.WORD_MARKER] = word

    def search(self, word):
        def find_suffix(i, trie):
            if i == len(word):
                return WordDictionary.WORD_MARKER in trie
            if word[i] in trie and find_suffix(i + 1, trie[word[i]]):
                return True
            if word[i] == WordDictionary.WILDCARD:
                if any(
                    find_suffix(i + 1, trie[letter])
                    for letter in trie
                    if letter != WordDictionary.WORD_MARKER
                ):
                    return True
            return False

        return find_suffix(0, self.word_trie)


# wd = WordDictionary()
# wd.addWord("bad")
# wd.addWord("dad")
# wd.addWord("mad")
# assert not wd.search("pad")
# assert wd.search(".ad")

wd = WordDictionary()
expected = [
    None,
    None,
    None,
    None,
    None,
    False,
    False,
    None,
    True,
    True,
    False,
    False,
    True,
    False,
]
ret = []
actions = [
    "WordDictionary",
    "addWord",
    "addWord",
    "addWord",
    "addWord",
    "search",
    "search",
    "addWord",
    "search",
    "search",
    "search",
    "search",
    "search",
    "search",
]
args = [
    [],
    ["at"],
    ["and"],
    ["an"],
    ["add"],
    ["a"],
    [".at"],
    ["bat"],
    [".at"],
    ["an."],
    ["a.d."],
    ["b."],
    ["a.d"],
    ["."],
]
for action, arg, ex in zip(actions, args, expected):
    print()
    if action == "WordDictionary":
        continue
    elif action == "addWord":
        fn = wd.addWord
    elif action == "search":
        fn = wd.search
    else:
        print(action)
    ret = fn(*arg)
    if ret != ex:
        print(action, arg, ex, ret)
        assert False
