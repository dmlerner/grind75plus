# https://leetcode.com/problems/design-in-memory-file-system/
# 8:00
# 9:09 passes
"""
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.

void mkdir(String path) Makes a new directory according to the given path.
The given directory path does not exist.
If the middle directories in the path do not exist, you should create them as well.

void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.

String readContentFromFile(String filePath) Returns the content in the file at filePath.
"""

from david import show


class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinarySearchTree(value)

    def in_order(self):
        if self.value is None:
            return
        if self.left:
            yield from self.left.in_order()
        yield self.value
        if self.right:
            yield from self.right.in_order()

    def __repr__(self):
        return "BST(" + str(self.value) + ")"


class Inode:
    def __init__(self, path_tail, is_directory):
        self.path_tail = path_tail  # last element of path
        self.is_directory = is_directory
        self.children = None
        self.child_by_path_tail = {}
        self.contents = []

    def add(self, path_tail, is_directory):
        child = Inode(path_tail, is_directory)
        if self.children is None:
            self.children = BinarySearchTree(child)
        else:
            self.children.add(child)
        self.child_by_path_tail[path_tail] = child

    def __le__(self, other):
        assert isinstance(other, Inode)
        return self.path_tail < other.path_tail

    def __repr__(self):
        return "Inode(" + str(self.path_tail) + ")"

    # @show
    def ls(self, parts, i):
        assert parts[i] == self.path_tail
        if i == len(parts) - 1:
            if self.is_directory:
                if not self.children:
                    return []
                return list(c.path_tail for c in self.children.in_order())
            return [self.path_tail]
        else:
            return self.child_by_path_tail[parts[i + 1]].ls(parts, i + 1)

    def mk(self, parts, i, is_directory):
        assert parts[i] == self.path_tail
        if i == len(parts) - 1:
            return self
        terminal = i == len(parts) - 2
        if parts[i + 1] not in self.child_by_path_tail:
            self.add(parts[i + 1], not terminal or is_directory)
        return self.child_by_path_tail[parts[i + 1]].mk(parts, i + 1, is_directory)

    def read_contents(self):
        assert not self.is_directory
        return "".join(self.contents)

    def add_content(self, content):
        assert not self.is_directory
        self.contents.append(content)


class FileSystem:
    @staticmethod
    def parse(path):
        parsed = ["/"]
        assert path[0] == "/"
        tail = path[1:].split("/")
        if tail != [""]:
            parsed += tail
        return parsed

    def __init__(self):
        self.fs = Inode("/", True)

    # @show
    def ls(self, path):
        parts = FileSystem.parse(path)
        return self.fs.ls(parts, 0)

    def mkdir(self, path):
        parts = FileSystem.parse(path)
        self.fs.mk(parts, 0, True)

    def addContentToFile(self, filePath, content):
        parts = FileSystem.parse(filePath)
        self.fs.mk(parts, 0, False).add_content(content)

    def readContentFromFile(self, filePath):
        parts = FileSystem.parse(filePath)
        return self.fs.mk(parts, 0, False).read_contents()

    def __repr__(self):
        return "FileSystem(" + repr(self.fs) + ")"




def test(commands, args, expects):
    verify(len(set(map(len, (commands, args, expects)))), 1)
    for command, arg, expect in zip(commands, args, expects):
        print("testing", command, arg, expect)
        match command:
            case "FileSystem":
                fs = FileSystem()
            case "ls":
                verify(fs.ls(*arg), expect)
            case "mkdir":
                verify(fs.mkdir(*arg), expect)
            case "addContentToFile":
                verify(fs.addContentToFile(*arg), expect)
            case "readContentFromFile":
                verify(fs.readContentFromFile(*arg), expect)


def verify(a, b):
    if a != b:
        print("fail", a, b)
        assert False

assert FileSystem.parse("/") == ["/"]
assert FileSystem.parse("/a") == ["/", "a"]

test(
    [
        "FileSystem",
        "ls",
        "mkdir",
        "addContentToFile",
        "ls",
        "readContentFromFile",
    ],
    [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]],
    [None, [], None, None, ["a"], "hello"],
)
"""

inode = Inode('/', True)
inode.add('foo', False)
inode.add('bar', False)
print(vars(inode))

fs = FileSystem()
fs.mkdir('/a/b/c')
ls = fs.ls('/a/b/c')
print(f'{ls=}')
assert ls == []
ls = fs.ls('/a/b')
print(f'{ls=}')
assert ls == ['c']

fs.mkdir('/a/b/d')
ls = fs.ls('/a/b/c')
print(f'{ls=}')
assert ls == []
ls = fs.ls('/a/b')
print(f'{ls=}')
assert ls == ['c', 'd']
"""
