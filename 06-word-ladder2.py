from david import show
class Trie:
    def __init__(self, letter, parent=None):
        self.letter = letter # should not be needed, just for debugging
        self.parent = parent
        self.suffix_by_first = {}

    def add(self, word):
        if not word:
            return
        first, suffix = word[0], word[1:]
        if first not in self.suffix_by_first:
            self.suffix_by_first[first] = Trie(first, self)
        self.suffix_by_first[first].add(suffix)

    def get_last(self, word):
        assert isinstance(word, str)
        ''' returns the Trie (rooted at self) whose letter is word[-1] '''
        if not word:
            return self

        first, suffix = word[0], word[1:]
        if first not in self.suffix_by_first:
            return
        return self.suffix_by_first[first].get_last(suffix)

    def __iter__(self):
        yield from self.suffix_by_first.values()

    def __len__(self):
        return len(self.suffix_by_first)

    def __repr__(self):
        children = '[' + ','.join(map(str, self)) + ']' if len(self) else ''
        return self.letter + children

    def __contains__(self, word):
        if not word:
            return True
        first, suffix = word[0], word[1:]
        if first not in self.suffix_by_first:
            return False
        return suffix in self.suffix_by_first[first]



def build_dictionary(words):
    dictionary = Trie('^')
    for word in words:
        dictionary.add(word)
    return dictionary

def test_build_dictionary():
    d = build_dictionary(wordList)

    assert d.letter == '^'

    s = str(d)
    assert s == '^[h[o[t]],d[o[t,g]],l[o[t,g]],c[o[g]]]'

    h_last = d.get_last('h')
    assert h_last
    assert h_last.letter == 'h'
    assert len(h_last) == 1
    print()

    do_last = d.get_last('do')
    assert do_last
    assert do_last.letter == 'o'
    assert len(do_last) == 2
    print()
    assert do_last.parent is d.get_last('d')
    assert do_last.parent.letter == 'd'
    assert do_last.parent.parent.letter == '^'
    assert do_last.parent.parent.parent is None

    assert 'hot' in d
    assert 'ho' in d # assume all words are terminal
    assert 'o' not in d

    print('build_dictionary passes')

def test_count_neighbors():
    d = build_dictionary(wordList)
    assert count_neighbors('hat', d) == 1
    assert count_neighbors('hot', d) == 2 # dot, lot; NOT hot
    assert count_neighbors('xxx', d) == 0
    assert count_neighbors('xx', d) == 0
    assert count_neighbors('xxxx', d) == 0
    print('test_count_neighbors passes')

def test_get_neighbors():
    d = build_dictionary(wordList)
    assert get_neighbors('hat', d) == ['hot']
    assert get_neighbors('hot', d) == ['dot', 'lot']
    assert get_neighbors('xxx', d) == []
    assert get_neighbors('xx', d) == []
    assert get_neighbors('xxxx', d) == []
    print('test_get_neighbors passes')

def count_neighbors(word, dictionary, max_dist=1):
    if max_dist < 0:
        return 0
    if max_dist == 0:
        return word in dictionary

    count = 0

    for letter, child in dictionary.suffix_by_first.items():

        subproblem_max_dist = max_dist
        if letter != word[0]:
            subproblem_max_dist -= 1

        count += count_neighbors(word[1:], child, subproblem_max_dist)

    return count

def get_neighbors(word, dictionary, max_dist=1):
    if max_dist < 0:
        return []
    if max_dist == 0:
        if word in dictionary:
            return [word]
        else:
            return []

    neighbors = []

    for letter, child in dictionary.suffix_by_first.items():

        subproblem_max_dist = max_dist
        if letter != word[0]:
            subproblem_max_dist -= 1

        for neighbor in get_neighbors(word[1:], child, subproblem_max_dist):
            neighbors.append(letter + neighbor)

    return neighbors

wordList = ["hot","dot","dog","lot","log","cog"]
test_build_dictionary()
test_count_neighbors()
test_get_neighbors()
