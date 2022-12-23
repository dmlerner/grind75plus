# https://leetcode.com/problems/palindrome-pairs/
# 9:22
# 9:51 handled happy path, buggy
# 10:02 handled happy path. todo: different length parts
# 12:22 134/136, 2 DLE

from david import *
from itertools import chain

WORD = '$'

class TrieNode(dict):
    def __init__(self):
        super().__init__()
        self.palindromic_continuations = None

    def get_palindromes(self):
        if self.palindromic_continuations:
            return self.palindromic_continuations
        self.palindromic_continuations = get_palindromes(self)
        return self.palindromic_continuations

    # def __repr__(self):
    #     return 'T(' + str(self.id) + '|' + super().__repr__() +')'


def build_trie(words):
    trie = TrieNode()
    for word in words:
        node = trie
        for c in word:
            node = node.setdefault(c, TrieNode())
        node[WORD] = word
    return trie

def get_palindromes(trie, prefix=None):
    prefix = prefix or []
    assert isinstance(trie, TrieNode)
    for letter in trie:
        if letter == WORD:
            if is_palindrome(prefix):
                yield trie[WORD]
            continue
        prefix.append(letter)
        yield from get_palindromes(trie[letter], prefix)
        prefix.pop()

def is_palindrome(word):
    if not word:
        return True
    middle = len(word)//2
    even = len(word)%2 == 0
    i = 0
    while True:
        try:
            if word[middle-i-even] != word[middle+i]:
                return False
        except IndexError:
            return True
        i += 1

assert not is_palindrome(['b', 'c'])

def find_pairs(words):
    forward_trie = build_trie(words)
    reverse_trie = build_trie(map(lambda x: x[::-1], words))
    index_by_word = { word: i for (i, word) in enumerate(words) }
    # simultaneously traversals
    # if hit end of word on one:
    #   and on other simultaneously, even pal
    #   and other will hit it in one more step, odd pal
    #   else, not pal

    def dfs(forward, reverse):
        assert isinstance(forward, TrieNode)
        assert isinstance(reverse, TrieNode)

        # If taking WORD from one, see if other continues palindromically

        # This is hacky and I should be able to just avoid it outright...
        # breakpoint()
        tmp = set()
        if WORD in reverse:
            reverse_index = index_by_word[reverse[WORD][::-1]]
            # TODO: cache
            for word in forward.get_palindromes():
                forward_index = index_by_word[word]
                tmp.add(tuple([forward_index, reverse_index]))
                yield [forward_index, reverse_index]

        if WORD in forward:
            forward_index = index_by_word[forward[WORD]]
            for word in reverse.get_palindromes():
                reverse_index = index_by_word[word[::-1]]
                if tuple([forward_index, reverse_index]) in tmp:
                    continue
                tmp.add(tuple([forward_index, reverse_index]))
                yield [forward_index, reverse_index]

        for letter in forward:
            if letter == WORD:
                forward_index = index_by_word[forward[WORD]]
                if WORD in reverse:
                    # even palindrome
                    if tuple([forward_index, index_by_word[reverse[WORD][::-1]]]) in tmp:
                        continue
                    yield [forward_index, index_by_word[reverse[WORD][::-1]]]

            elif letter in reverse:
                yield from dfs(forward[letter], reverse[letter])





    # return filter(lambda pair: pair[0]!=pair[1], chain(dfs(forward_trie, reverse_trie), dfs(reverse_trie, forward_trie)))
    return filter(lambda pair: pair[0]!=pair[1], dfs(forward_trie, reverse_trie))


# words = ["abcd","dcba","lls","s","sssll"]
words = ["a","abc","aba",""]
words = ["sssll", "s"]
words = ["a", "abc"]
with open('input.csv') as f:
    words = f.read().strip()
# t = build_trie(words)
# 1/0

# words = ["lls", "s"]
expected = [[0,1],[1,0],[3,2],[2,4]]
expected = [[0,3],[3,0],[2,3],[3,2]]
expected = []
# expected = [[1, 0]]
expected.sort()
# words = ["abcd","dcba","lls","s","sssll", ""]
# pairs = list(find_pairs(words))
# assert expected == pairs

# TODO: add case where pair[0] is longer than pair[1]
print(benchmark(lambda: list(find_pairs(words))))
