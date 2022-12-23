# https://leetcode.com/problems/palindrome-pairs/
# 9:22
# 9:51 handled happy path, buggy
# 10:02 handled happy path. todo: different length parts

from david import *
from itertools import chain

WORD = '$'

class TrieNode(dict):
    nodes = []
    id = 0
    def __init__(self):
        super().__init__()
        self.id = TrieNode.id
        TrieNode.id += 1
        TrieNode.nodes.append(self)
        self.palindromic_continuations = None

    def __repr__(self):
        return 'T(' + str(self.id) + '|' + super().__repr__() +')'


def build_trie(words):
    trie = TrieNode()
    for word in words:
        node = trie
        for c in word:
            node = node.setdefault(c, TrieNode())
        node[WORD] = word
    return trie

@showlistify
def get_words(trie, prefix=None):
    prefix = prefix or []
    assert isinstance(trie, TrieNode)
    # if WORD in trie:
    #     yield prefix
    #     # yield trie[WORD]
    for letter in trie:
        if letter == WORD:
            yield prefix[:], trie[WORD]
            continue
        prefix.append(letter)
        yield from get_words(trie[letter], prefix)
        prefix.pop()

@showlistify
def get_palindromes(trie):
    for prefix, word in get_words(trie):
        if is_palindrome(prefix):
            yield word
    # yield from filter(lambda (prefix, is_palindrome, get_words(trie))

def is_palindrome(word):
    if not word:
        return True
    middle = len(word)//2
    even = len(word)%2 == 0
    i = middle
    while True:
        try:
            if word[middle-i-even] != word[middle+1]:
                return False
        except IndexError:
            return True
        i += 1

@showlistify
def find_pairs(words):
    forward_trie = build_trie(words)
    print(f'{forward_trie =}')
    reverse_trie = build_trie(map(lambda x: x[::-1], words))
    print(f'{reverse_trie =}')
    index_by_word = { word: i for (i, word) in enumerate(words) }
    # simultaneously traversals
    # if hit end of word on one:
    #   and on other simultaneously, even pal
    #   and other will hit it in one more step, odd pal
    #   else, not pal

    @showlistify
    def dfs(forward, reverse):
        assert isinstance(forward, TrieNode)
        assert isinstance(reverse, TrieNode)

        # If taking WORD from one, see if other continues palindromically
        sl()
        # breakpoint()
        if WORD in reverse:
            reverse_index = index_by_word[reverse[WORD][::-1]]
            # TODO: cache
            for word in get_palindromes(forward):
                forward_index = index_by_word[word]
                yield [forward_index, reverse_index]

        if WORD in forward:
            forward_index = index_by_word[forward[WORD]]
            # TODO: need to get palindromes of a child of reverse or something...
            # BUG: this gets full words
            for word in get_palindromes(reverse):
                reverse_index = index_by_word[word[::-1]]
                yield [forward_index, reverse_index]

        for letter in forward:
            if letter == WORD:
                forward_index = index_by_word[forward[WORD]]
                if WORD in reverse:
                    # even palindrome
                    print('found even')
                    yield [forward_index, index_by_word[reverse[WORD][::-1]]]
                # look for odd palindromes
                # TODO: optimize out loop?
                # this is probably a special case of continuing palindromically....
                # for middle_letter in reverse:
                #     if WORD in reverse[middle_letter]:
                #         # odd palindrome
                #         yield [forward_index, index_by_word[reverse[middle_letter][WORD][::-1]]]

            elif letter in reverse:
                yield from dfs(forward[letter], reverse[letter])





    # return filter(lambda pair: pair[0]!=pair[1], chain(dfs(forward_trie, reverse_trie), dfs(reverse_trie, forward_trie)))
    return filter(lambda pair: pair[0]!=pair[1], dfs(forward_trie, reverse_trie))



words = ["abcd","dcba","lls","s","sssll"]
# words = ["sssll", "s"]
# t = build_trie(words)
# print([prefix for prefix, word in get_words(t)])
# 1/0

# words = ["lls", "s"]
expected = [[0,1],[1,0],[3,2],[2,4]]
# expected = []
# expected = [[1, 0]]
expected.sort()
# words = ["abcd","dcba","lls","s","sssll", ""]
pairs = list(map(list, {tuple(p) for p in find_pairs(words)}))
pairs.sort()
expected
print(f'{expected=}')
pairs
print(f'{pairs=}')
print('expected', [(words[pair[0]], words[pair[1]]) for pair in expected])
print('pairs', [(words[pair[0]], words[pair[1]]) for pair in pairs])
assert expected == pairs

# TODO: add case where pair[0] is longer than pair[1]
