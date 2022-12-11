# https://leetcode.com/problems/word-ladder/
# eight fourty nine
# nine oh eight: analyzed two algorithms
# nine twenty four: oh gosh my algorithm is borked, but salvagable
# nine thirty eight: oh god fuck yield
# nine fourty: that's about enough for tonight.
# definitely not getting the offer.
# I should probably not interview at 9pm.
# eight oh six (am)
# eight fifty five: passing Trie test, onto the alg...

class PrefixTrie:
    START = '^'
    def __init__(self, letter):
        self.letter = letter
        self.children_by_letter = {}

    def add(self, word):
        assert word
        first = word[0]
        if first not in self.children_by_letter:
            self.children_by_letter[first] = PrefixTrie(first)
        self.children_by_letter[first]._add(word)

    def _add(self, word):
        if not word:
            return

        first, rest = word[0], word[1:] # splat magic?
        assert first == self.letter
        if not rest:
            return
        second = rest[0]

        if second not in self.children_by_letter:
            self.children_by_letter[second] = PrefixTrie(second)
        child = self.children_by_letter[second]
        child._add(rest)

    def __contains__(self, word):
        if not word:
            return True
        if not self.letter:
            return any(word in child for child in self)
        first, rest = word[0], word[1:]
        if first != self.letter:
            return False
        return any(rest in child for child in self)

    def __iter__(self):
        yield from self.children_by_letter.values()

    def __repr__(self):
        me = self.letter if self.letter is not None else 'Dictionary'
        children = '[' + ','.join(map(str, self.children_by_letter.values())) + ']' if self.children_by_letter else ''
        return me + children

    def get_last_letter_node(self, word):
        first, *rest = word
        if not self.letter:
            return self.children_by_letter[first].get_last_letter_node(word)

        if not rest:
            assert self.letter == first
            return self
        second = rest[0]
        return self.children_by_letter[second].get_last_letter_node(rest)



def unpack(x):
    return x[0:1], x[1:2], x[2:]

from dataclasses import dataclass

@dataclass
class State:
    # trie_node: 'PrefixTrie' = None
    word_index: int
    dist: int = 0

def test_trie():
    d = build_dictionary(wordList)
    assert 'hot' in d
    assert 'hat' not in d
    assert 'ot' not in d
    s = str(d)
    print(s)
    assert s == 'Dictionary[h[o[t]],d[o[t,g]],l[o[t,g]],c[o[g]]]'


def build_dictionary(word_list):
    dictionary = PrefixTrie(None)
    for word in word_list:
        dictionary.add(word)
    return dictionary

def get_neighbors(word, dictionary):
    neighbors = []
    for w in range(len(word)):
        prefix, letter, suffix = word[:w], word[w], word[w+1:]
        prefix_node = dictionary.get(prefix)

    for letter, child in dictionary.children_by_letter.items():
        if letter != word[w]:
            if child._contains(word[w+1:]):
                neighbors.append(word[:w] + letter + word[w+1:])

    def get_suffixes(w):
        out = []
        first, second, rest = unpack(word[w:]) # TODO: avoid slice repeatedly
        if not first:
            return ['']
        # first followed by all possible recursive suffixes
        out.extend([[first] + suffix for suffix in get_suffixes(w+1)])
        # !first followed by word[1:] if that is valid, for each !first

    if first in dictionary:
        pass

def test_get_neighbors():
    neighbors = get_neighbors(beginWord, wordList)
    assert neighbors == ["hot"]


def ladder_length(begin_word, end_word, word_list):
    word_list = filter(lambda word: len(word) == len(begin_word), word_list)
    dictionary = build_dictionary(word_list)
    print(dictionary)
    stack = []

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
test_trie()
test_get_neighbors()
# assert ladder_length(beginWord, endWord, wordList) == 5
