from collections import defaultdict

# one fourty - one fourty three


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.terminal = False

    def insert(self, word):
        if not word:
            self.terminal = True
        else:
            self.children[word[0]].insert(word[1:])

    def search(self, word):
        if not word:
            return self.terminal
        return word[0] in self.children and self.children[word[0]].search(word[1:])

    def startsWith(self, prefix):
        if not prefix:
            return True
        return prefix[0] in self.children and self.children[prefix[0]].startsWith(
            prefix[1:]
        )
