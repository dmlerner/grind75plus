from __future__ import annotations

"""
https://leetcode.com/problems/number-of-atoms/
12:44
"""

from collections import Counter


class Character:
    OPEN = "("
    CLOSE = ")"
    DIGIT = set(map(str, range(10)))
    LOWERCASE = set("abcdefghijklmnopqrstuvwxyz")
    UPPERCASE = set("abcdefghijklmnopqrstuvwxyz".upper())


class Token:
    OPEN = "("
    CLOSE = ")"
    ATOM = "atom"
    SUBSCRIPT = "subscript"
    # COEFFICIENT = 'coefficient'


def get_numeric_token(s, i):
    assert s[i] in Character.DIGIT
    digits = []
    while i < len(s) and s[i] in Character.DIGIT:
        digits.append(s[i])
        i += 1
    digits = int("".join(digits))
    return digits, i


def get_alpha_token(s, i):
    assert s[i] in Character.UPPERCASE
    letters = [s[i]]
    i += 1
    while i < len(s) and s[i] in Character.LOWERCASE:
        letters.append(s[i])
        i += 1
    return "".join(letters), i


def tokenize(s, i=0):
    if i == len(s):
        return

    match s[i]:
        case Character.OPEN:
            token_type, token = Token.OPEN, None
            i += 1
        case Character.CLOSE:
            token_type, token = Token.CLOSE, None
            i += 1
        case c if c in Character.DIGIT:
            token, i = get_numeric_token(s, i)
            token_type = Token.SUBSCRIPT
        case c if c in Character.UPPERCASE:
            token, i = get_alpha_token(s, i)
            token_type = Token.ATOM
        case _:
            raise Exception

    yield token_type, token
    yield from tokenize(s, i)


def flatten(lists):
    for element in lists:
        if isinstance(element, list):
            yield from flatten(element)
        else:
            yield element


from dataclasses import dataclass, field
from david import show, sl, clean


@dataclass  # (frozen=True)
class TreeNode:
    atom: str = None
    multiplier: int = 1
    children: list[TreeNode] = field(default_factory=list)

    def __repr__(self):
        recursed = "".join(map(str, self.children))
        return f"T[{self.atom}|{self.multiplier}|({recursed})]"

    @show
    def get_counts(self):
        if not self.children:
            if self.atom:
                return Counter({self.atom: self.multiplier})
            return Counter({})
        if self.multiplier != 1:
            for child in self.children:
                child.multiplier *= self.multiplier
        return sum((child.get_counts() for child in self.children), Counter())


def build_tree(s):
    root = TreeNode()
    ancestors = [root]
    for (token_type, token) in tokenize(s):
        print(token_type, token)
        active = ancestors[-1]
        match token_type:
            case Token.OPEN:
                child = TreeNode()
                active.children.append(child)
                ancestors.append(child)
            case Token.CLOSE:
                ancestors.pop()
            case Token.ATOM:
                child = TreeNode(token)
                active.children.append(child)
            case Token.SUBSCRIPT:
                assert active.children[-1].multiplier == 1
                active.children[-1].multiplier = token
        sl()

    return root


def count(formula):
    formula_tree = build_tree(formula)
    return formula_tree.get_counts()


def verify(actual, expected):
    if actual != expected:
        print("...")
        sl()
        assert False


def show_counts(formula):
    counts = count(formula)
    atoms = sorted(counts.keys())
    out = []
    for atom in atoms:
        out.append(atom)
        if counts[atom] > 1:
            out.append(counts[atom])
    return "".join(map(str, out))


formula = "K4(ON(SO3)2)2"
formula = "K4"
# assert count(formula) == {'K': 4}
# 1/0
# formula = "(K4)2"
# assert count(formula) == {'K': 8}
# 1/0
formula = "(K4)2X"
expected = {"K": 8, "X": 1}
formula = "(((K4)2)3J2)10"
expected = {"K": 240, "J": 20}
formula = "CH3OOH"
expected = {"C": 1, "H": 4, "O": 2}
verify(count(formula), expected)
