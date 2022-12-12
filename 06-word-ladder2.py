from david import show, count_calls

class Trie:
    def __hash__(self):
        return hash(id(self))

    def __init__(self, letter, parent=None):
        self.letter = letter # should not be needed, just for debugging
        self.parent = parent
        self.suffix_by_first = {}
        self.terminal = False

    def add(self, word):
        if not word:
            self.terminal = True
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
            return self.terminal
        first, suffix = word[0], word[1:]
        if first not in self.suffix_by_first:
            return False
        return suffix in self.suffix_by_first[first]

    def get_word(self):
        if self.parent is None:
            return ''
        return self.parent.get_word() + self.letter


    def word_generator(self, prefix_list=None):
        # yield as a list of characters to avoid mutating strings
        prefix_list = prefix_list or []
        for first, suffix in self.suffix_by_first.items():
            prefix_list.append(first)
            yield from suffix.word_generator(prefix_list)
            prefix_list.pop()
        else:
            if prefix_list:
                yield prefix_list

    @count_calls
    def leaf_generator(self):
        for first, suffix in self.suffix_by_first.items():
            if suffix.terminal:
                yield suffix
            yield from suffix.leaf_generator()



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
    assert 'ho' not in d
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

def test_word_generator():
    d = build_dictionary(wordList)
    g = d.word_generator()
    a = next(g)
    assert ''.join(a) == 'hot'
    b = next(g)
    assert ''.join(a) == 'ho'
    assert ''.join(b) == 'ho'
    assert a is b
    print('test_word_generator passes')


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
    ''' inefficient but I believe working '''
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

@show
def neighbor_generator(word, dictionary, max_dist=1):
    assert isinstance(word, str)
    assert isinstance(dictionary, Trie)
    if max_dist == 0:
        last_word = dictionary.get_last(word)
        if last_word is not None:
            yield last_word
        return

    # TODO:  avoid string slicing; use iter(word)?
    suffix = word[1:]
    for first, child in dictionary.suffix_by_first.items():
        subproblem_max_dist = max_dist
        if first != word[0]:
            # I would think this would let me lose the 'return' above...
            # if max_dist == 0:
            #     continue
            subproblem_max_dist -= 1
        yield from neighbor_generator(suffix, child, subproblem_max_dist)


def test_leaf_generator():
    d = build_dictionary(wordList)
    g = d.leaf_generator()
    first = next(g)
    assert first.get_word() == 'hot'
    assert first is d.suffix_by_first['h'].suffix_by_first['o'].suffix_by_first['t']
    second = next(g)
    assert second.get_word() == 'dot'
    assert second is d.suffix_by_first['d'].suffix_by_first['o'].suffix_by_first['t']
    third = next(g)
    assert third.get_word() == 'dog'
    assert third is d.suffix_by_first['d'].suffix_by_first['o'].suffix_by_first['g']
    print('test_leaf_generator passes')

def test_leaf_generator_count():
    words = ['abcdefg', 'abcdefh']
    d = build_dictionary(words)
    d.leaf_generator.reset_call_count()
    g = d.leaf_generator()
    first = next(g)
    assert first.get_word() == 'abcdefg'
    assert first is d.suffix_by_first['a'].suffix_by_first['b'].suffix_by_first['c'].suffix_by_first['d'].suffix_by_first['e'].suffix_by_first['f'].suffix_by_first['g']
    second = next(g)
    assert second is d.suffix_by_first['a'].suffix_by_first['b'].suffix_by_first['c'].suffix_by_first['d'].suffix_by_first['e'].suffix_by_first['f'].suffix_by_first['h']
    assert first.parent is second.parent
    assert d.leaf_generator.call_count == len(words[0]) + 1
    print('test_leaf_generator passes')

def test_neighbor_generator():
    d = build_dictionary(wordList)
    g = neighbor_generator("hat", d, 1)
    first = next(g)
    assert first.get_word() == 'hot'
    assert first is d.suffix_by_first['h'].suffix_by_first['o'].suffix_by_first['t']
    try:
        second = next(g)
        assert False
    except StopIteration:
        pass
    print('test_neigbhor_generator passes')

from collections import deque
@show
def bfs_generator(word, dictionary):
    assert isinstance(word, str)
    frontier = deque([word])
    # TODO: hacky.
    # dictionary.dist = 0
    visited = set()
    while frontier:
        active = frontier.popleft()
        assert isinstance(active, str)
        # TODO: optimize out the get_word
        for neighbor in neighbor_generator(active, dictionary):
            print('neighbor', neighbor)
            assert neighbor is not None
            if neighbor not in visited:
                # neighbor.dist = active.dist + 1
                visited.add(neighbor)
                yield neighbor
                frontier.append(neighbor.get_word())

def test_bfs_generator():
    d = build_dictionary(wordList)
    g = bfs_generator("hat", d)
    first = next(g)
    assert first.get_word() == 'hot'
    assert first is d.suffix_by_first['h'].suffix_by_first['o'].suffix_by_first['t']
    second = next(g)
    assert second.get_word() == 'dot'
    assert second is d.suffix_by_first['d'].suffix_by_first['o'].suffix_by_first['t']
    print('test_bfs_generator passes')

def ladder_length(start, end, word_list):
    d = build_dictionary(word_list)
    target_node = d.get_last(end)
    print(target_node, target_node.get_word())
    for last_word_node in bfs_generator(start, d):
        print(last_word_node, last_word_node.get_word())
        if last_word_node is target_node:
            return last_word_node.dist
    return -1

def test_ladder_length():
    length = ladder_length("hat", "hot", wordList)
    print('!', length)
    assert length == 5


wordList = ["hot","dot","dog","lot","log","cog"]
# test_build_dictionary()
# test_count_neighbors()
# test_get_neighbors()
# test_word_generator()
# test_leaf_generator()
# test_leaf_generator_count()
# test_neighbor_generator()
# test_bfs_generator()
test_ladder_length()
