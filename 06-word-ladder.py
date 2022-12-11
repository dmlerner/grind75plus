# https://leetcode.com/problems/word-ladder/
# eight fourty nine
# nine oh eight: analyzed two algorithms
# nine twenty four: oh gosh my algorithm is borked, but salvagable
# nine thirty eight: oh god fuck yield
# nine fourty: that's about enough for tonight.
# definitely not getting the offer.
# I should probably not interview at 9pm.

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

from collections import defaultdict

class PrefixTrie:
    def __init__(self):
        self.children = {}# defaultdict(PrefixTrie) # first letter: suffix

    def add(self, word):
        if not word:
            return

        if word[0] not in self.children:
            self.children[word[0]] = PrefixTrie()
        self.children[word[0]].add(word[1:])

    def get_neighbors(self, word, d=1):
        if d == 0:
            return word in self

        if word[0] in self.children:
            yield from self.children[word[0]].get_neighbors(word[1:], d)
        for child in self.children.values():
            yield from child.get_neighbors(word[1:], d-1)
            # yield from (child.get_neighbors(word[1:]) for child in self.children.values())

    def get_neigbhors(self, word):
        for i in range(len(word)):
            if word[:i] in self:
                # go to bed



    def __iter__(self):
        yield from self.children

    def __in__(self, w):
        if not w:
            return True
        suffix_node = self.children.get(w[0])
        return suffix_node and w[1:] in suffix_node


def ladder_length(begin_word, end_word, word_list):
    dictionary = PrefixTrie()
    for word in word_list:
        dictionary.add(word)



assert ladder_length(beginWord, endWord, wordList) == 5
