from david import show, count_calls
from collections import deque, defaultdict

class Trie:
    def __hash__(self):
        return hash(id(self))

    def __init__(self, letter, parent=None):
        self.letter = letter  # should not be needed, just for debugging
        self.parent = parent
        self.suffix_by_first = {}
        self.terminal = False

    def add(self, word, i=0):
        if i >= len(word):
            self.terminal = True
            return
        first = word[i]
        if first not in self.suffix_by_first:
            self.suffix_by_first[first] = Trie(first, self)
        self.suffix_by_first[first].add(word, i+1)

    @show
    def get_last(self, word, i=0):
        """ returns the Trie (rooted at self) whose letter is word[-1] """
        if i >= len(word):
            return self
        first = word[i]

        if first not in self.suffix_by_first:
            return
        return self.suffix_by_first[first].get_last(word, i+1)

    def __iter__(self):
        yield from self.suffix_by_first.values()

    def __len__(self):
        return len(self.suffix_by_first)

    def __repr__(self):
        children = "[" + ",".join(map(str, self)) + "]" if len(self) else ""
        return self.letter + children

    @show
    def __contains__(self, word):
        return self._contains(word, 0)

    @show
    def _contains(self, word, i):
        if i >= len(word):
            return self.terminal
        first = word[i]
        if first not in self.suffix_by_first:
            return False
        return self.suffix_by_first[first]._contains(word, i+1)

    def get_word(self):
        # TODO: avoid quadratic
        if self.parent is None:
            return ""
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
    dictionary = Trie("^")
    for word in words:
        dictionary.add(word)
    return dictionary


def count_neighbors(word, dictionary, max_dist=1):
    # Don't care enough to use iter; was just for experimenting.
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
    # Don't care enough to use iter; was just for experimenting.
    """inefficient but I believe working"""
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
def neighbor_generator(word, dictionary, max_dist=1, i=0):
    assert isinstance(word, str)
    assert isinstance(dictionary, Trie)
    if i >= len(word):
        # assert False # ?
        return
    if max_dist == 0:
        last_word = dictionary.get_last(word, i)
        if last_word is not None:
            yield last_word
        return
    print(f'{max_dist =}')
    assert max_dist > 0

    ofirst = word[i]
        # ofirst, suffix = next(word), word
        # print(f'{ofirst =}')
        # print('suffix',end='= ')
        # suffix = showiter(suffix)
    # except StopIteration:
        # assert False
        # return

    # # TODO:  avoid string slicing; use iter(word)?
    # suffix = word[1:]
    for first, child in dictionary.suffix_by_first.items():
        print(f'{first =}')
        print(f'{child =}')
        subproblem_max_dist = max_dist
        if first != ofirst:
            # I would think this would let me lose the 'return' above...
            # if max_dist == 0:
            #     continue
            subproblem_max_dist -= 1
        yield from neighbor_generator(word, child, subproblem_max_dist, i+1)


# @show
def bfs_generator(word, dictionary):
    assert isinstance(word, str)
    frontier = deque([word])
    dist_by_word = {word: 1}  # problem wants node count, not edge
    visited = set()
    while frontier:
        print('!frontier=', frontier)
        active = frontier.popleft()
        print('!active=', active)
        assert isinstance(active, str)
        # TODO: optimize out the get_word
        for neighbor in neighbor_generator(active, dictionary):
            assert isinstance(neighbor, Trie)
            assert neighbor is not None
            if neighbor not in visited:
                neighbor_word = neighbor.get_word()
                print(f'{neighbor_word =}')
                dist_by_word[neighbor_word] = dist_by_word[active] + 1
                print('!', f'{dist_by_word=}')
                visited.add(neighbor)
                yield dist_by_word[neighbor_word], neighbor
                frontier.append(neighbor_word)
            else:
                print('!aready visited=', neighbor, neighbor.get_word())


def ladder_length(start, end, word_list):
    d = build_dictionary(word_list)
    target_node = d.get_last(end)
    print(f'{target_node.get_word() =}')
    for (dist, last_word_node) in bfs_generator(start, d):
        print('!!', dist, last_word_node.get_word())
        if last_word_node is target_node:
            return dist
    return 0


def test_build_dictionary():
    d = build_dictionary(wordList)

    assert d.letter == "^"

    s = str(d)
    assert s == "^[h[o[t]],d[o[t,g]],l[o[t,g]],c[o[g]]]"

    h_last = d.get_last("h")
    assert h_last
    assert h_last.letter == "h"
    assert len(h_last) == 1

    do_last = d.get_last("do")
    assert do_last
    assert do_last.letter == "o"
    assert len(do_last) == 2
    assert do_last.parent is d.get_last("d")
    assert do_last.parent.letter == "d"
    assert do_last.parent.parent.letter == "^"
    assert do_last.parent.parent.parent is None
    print("test_build_dictionary passes")
    print()

def test_contains():
    d = build_dictionary(wordList)

    assert "hot" in d
    assert "ho" not in d
    assert "o" not in d

    print("test_contains passes")
    print()


def test_count_neighbors():
    d = build_dictionary(wordList)
    assert count_neighbors("hat", d) == 1
    assert count_neighbors("hot", d) == 2  # dot, lot; NOT hot
    assert count_neighbors("xxx", d) == 0
    assert count_neighbors("xx", d) == 0
    assert count_neighbors("xxxx", d) == 0
    print("test_count_neighbors passes")
    print()


def test_get_neighbors():
    d = build_dictionary(wordList)
    assert get_neighbors("hat", d) == ["hot"]
    assert get_neighbors("hot", d) == ["dot", "lot"]
    assert get_neighbors('dot') == ['hot', 'lot', 'dog']
    assert get_neighbors("xxx", d) == []
    assert get_neighbors("xx", d) == []
    assert get_neighbors("xxxx", d) == []
    print("test_get_neighbors passes")
    print()


def test_word_generator():
    d = build_dictionary(wordList)
    g = d.word_generator()
    a = next(g)
    assert "".join(a) == "hot"
    b = next(g)
    assert "".join(a) == "ho"
    assert "".join(b) == "ho"
    assert a is b
    print("test_word_generator passes")
    print()


def test_leaf_generator():
    d = build_dictionary(wordList)
    g = d.leaf_generator()
    first = next(g)
    assert first.get_word() == "hot"
    assert first is d.suffix_by_first["h"].suffix_by_first["o"].suffix_by_first["t"]
    second = next(g)
    assert second.get_word() == "dot"
    assert second is d.suffix_by_first["d"].suffix_by_first["o"].suffix_by_first["t"]
    third = next(g)
    assert third.get_word() == "dog"
    assert third is d.suffix_by_first["d"].suffix_by_first["o"].suffix_by_first["g"]
    print("test_leaf_generator passes")
    print()


def test_leaf_generator_count():
    words = ["abcdefg", "abcdefh"]
    d = build_dictionary(words)
    d.leaf_generator.reset_call_count()
    g = d.leaf_generator()
    first = next(g)
    assert first.get_word() == "abcdefg"
    assert (
        first
        is d.suffix_by_first["a"]
        .suffix_by_first["b"]
        .suffix_by_first["c"]
        .suffix_by_first["d"]
        .suffix_by_first["e"]
        .suffix_by_first["f"]
        .suffix_by_first["g"]
    )
    second = next(g)
    assert (
        second
        is d.suffix_by_first["a"]
        .suffix_by_first["b"]
        .suffix_by_first["c"]
        .suffix_by_first["d"]
        .suffix_by_first["e"]
        .suffix_by_first["f"]
        .suffix_by_first["h"]
    )
    assert first.parent is second.parent
    assert d.leaf_generator.call_count == len(words[0]) + 1
    print("test_leaf_generator_count passes")
    print()


def test_get_last():
    d = build_dictionary(wordList)
    hot_last = d.get_last('hot')
    assert hot_last is d.suffix_by_first["h"].suffix_by_first["o"].suffix_by_first["t"]
    assert hot_last.get_word() == 'hot'
    h_ot_last = d.suffix_by_first['h'].get_last('ot')
    assert h_ot_last is hot_last
    assert d.get_last('at') is None
    print("test_get_last passes")
    print()

def test_neighbor_generator():
    d = build_dictionary(wordList)
    g = neighbor_generator("hat", d, 1)
    first = next(g)
    assert first.get_word() == "hot"
    assert first is d.suffix_by_first["h"].suffix_by_first["o"].suffix_by_first["t"]
    try:
        # breakpoint()
        second = next(g)
        print(second)
        assert False
    except StopIteration:
        pass
    print("test_neigbhor_generator passes")
    print()

def test_neighbor_generator2():
    d = build_dictionary(wordList)
    g = neighbor_generator('dot', d, 1)
    neighbors = {n.get_word() for n in g}
    print(neighbors)
    assert neighbors == {'hot', 'lot', 'dog'}
    print("test_neigbhor_generator2 passes")
    print()


def test_bfs_generator():
    d = build_dictionary(wordList)
    g = bfs_generator("hat", d)
    first = next(g)
    assert first[0] == 2
    assert first[1].get_word() == "hot"
    assert first[1] is d.suffix_by_first["h"].suffix_by_first["o"].suffix_by_first["t"]
    second = next(g)
    assert second[0] == 3
    assert second[1].get_word() == "dot"
    assert second[1] is d.suffix_by_first["d"].suffix_by_first["o"].suffix_by_first["t"]
    print("test_bfs_generator passes")
    print()


def test_ladder_length():
    length = ladder_length("hit", "cog", wordList)
    print("!", length)
    # assert length == 5


wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# test_build_dictionary()
# test_contains()
# test_count_neighbors()
# test_get_neighbors()
# test_word_generator()
# test_leaf_generator()
# test_leaf_generator_count()
# test_get_last()
# test_neighbor_generator()
test_neighbor_generator2()
# test_bfs_generator()
# test_ladder_length()
