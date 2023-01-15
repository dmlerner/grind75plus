from __future__ import annotations

"""
12:26
"""

from collections import Counter


class Character:
    OPEN = "("
    CLOSE = ")"
    DIGIT = set(map(str, range(10)))
    LETTER = set("abcdefghijklmnopqrstuvwxyz")
    OPERATOR = set("*+-/^")


class Token:
    OPEN = "("
    CLOSE = ")"
    OPERATOR = "OPERATOR"
    # BINARY_OPERATOR = 'BINARY_OPERATOR'
    # UNARY_OPERATOR = 'UNARY_OPERATOR'
    CONSTANT = "CONSTANT"
    VARIABLE = "VARIABLE"

    @staticmethod
    def is_value(token):
        return token == Token.CONSTANT or token == Token.VARIABLE


def get_numeric_token(s, i):
    assert s[i] in Character.DIGIT
    digits = []
    while i < len(s) and s[i] in Character.DIGIT:
        digits.append(s[i])
        i += 1
    digits = int("".join(digits))
    return digits, i


def get_alpha_token(s, i):
    assert s[i] in Character.LETTER
    letters = []
    while i < len(s) and s[i] in Character.LETTER:
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
        case c if c in Character.OPERATOR:
            token_type, token = Token.OPERATOR, c
            i += 1
        case c if c in Character.DIGIT:
            token, i = get_numeric_token(s, i)
            token_type = Token.CONSTANT
        case c if c in Character.LETTER:
            token, i = get_alpha_token(s, i)
            token_type = Token.VARIABLE
        case _:
            raise Exception

    yield token_type, token
    yield from tokenize(s, i)


from dataclasses import dataclass, field
from david import show, sl, clean
from enum import StrEnum

# TODO; consider StrEnum for Character/Token
SymbolType = StrEnum("SymbolType", "OPERATOR VALUE GROUPING".split())


@dataclass
class Symbol:
    value: str = None
    symbol_type: SymbolType = None

    def __post_init__(self):
        self.symbol_type = self.__class__.symbol_type

    def priority(self):
        return self.symbol_type

    def is_higher_priority_than(self, other):
        assert isinstance(other, Symbol)
        if type(self) == type(other):
            return self.priority() > other.priority()
        return Symbol.priority(self) > Symbol.priority(other)
    def repr(self):
        cname = str(self.__class__)
        start = cname.index('.')+1
        len = 2
        cname = cname[start: start+len] + ' '
        return '{'+cname+str(self.value)+'}'
    def __repr__(self):
        return self.repr()


@dataclass
class Grouping(Symbol):
    symbol_type = SymbolType.GROUPING

    def __repr__(self):
        return self.repr()


import operator


@dataclass
class Operator(Symbol):
    # TODO: support other arities
    # for now, assume binary operators only
    arity: int = 2
    symbol_type = SymbolType.OPERATOR

    priority_by_operation = {"^": 2, "*": 1, "/": 1, "+": 0, "-": 0}
    operator_by_operation = {
        "^": operator.pow,
        "*": operator.mul,
        "/": operator.truediv,
        "+": operator.add,
        "-": operator.sub,
    }

    def evaluate(self, operands):
        # TODO: support Variables
        assert all(isinstance(operand, Constant) for operand in operands)
        assert len(operands) == self.arity
        operand_values = (operand.get_value() for operand in operands)
        # TODO: support returning Variable
        return Value(Operator.operator_by_operation[self.value](*operand_values))

    def priority(self):
        return Operator.priority_by_operation[self.value]

    def __repr__(self):
        return self.repr()


@dataclass
class Value(Symbol):
    def __repr__(self):
        return self.repr()

    symbol_type = SymbolType.VALUE

    def get_value(self):
        return float(self.value)


@dataclass
class Variable(Value):
    def __repr__(self):
        return self.repr()

    pass


@dataclass
class Constant(Value):
    def __repr__(self):
        return self.repr()

    pass


# TODO: consider (unary) identity operation so everything is in operations?
@dataclass
class TreeNode:
    symbol: Symbol = None
    children: list[TreeNode] = field(default_factory=list)
    root_id: int = None

    def __post_init__(self):
        assert self.symbol is None or isinstance(self.symbol, Symbol)

    @show
    def get_simplified(self):
        if self.symbol is None:
            assert TreeNode.root_id is None or TreeNode.root_id == id(self)
            root_id = id(self)
            return self.children[0].get_simplified()
        assert isinstance(self.symbol, Symbol)
        if isinstance(self.symbol, Value):
            return self
        if isinstance(self.symbol, Grouping):
            assert len(self.children) == 1
            return self.children[0]
        if isinstance(self.symbol, Operator):
            simplified_children_symbols = [
                child.get_simplified().symbol for child in self.children
            ]
            return TreeNode(self.symbol.evaluate(simplified_children_symbols))

    def __repr__(self):
        recursed = "".join(map(str, self.children))
        return f"T[{self.symbol}|({recursed})]"

    def simplify(self):
        match self.token_type:
            case Token.OPEN:
                pass
            # TODO: try this syntax
            # case t if Token.is_value(t)
            case Token.CONSTANT | Token.VARIABLE:
                assert not self.children
                return self.token
            case Token.OPERATOR:
                assert self.children
                match self.token:
                    case "-":
                        if len(self.children) == 1:
                            return -self.children[0].simplify()
                        return

    def is_higher_priority_than(self, other):
        if self.symbol is None:
            return False
        assert other.symbol is not None
        return self.symbol.is_higher_priority_than(other.symbol)


def build_tree(s):
    root = TreeNode()
    ancestors = [root]
    constructor_by_token_type = {
        Token.OPEN: Grouping,
        Token.CONSTANT: Constant,
        Token.VARIABLE: Variable,
        Token.OPERATOR: Operator,
    }

    for (token_type, token) in tokenize(s):
        print(token_type, token)
        active = ancestors[-1]
        constructor = constructor_by_token_type.get(token_type)
        node = TreeNode(constructor(token))
        # TODO: Can I make priority replace the per token type logic?
        match token_type:
            case Token.OPEN:
                active.children.append(node)
                ancestors.append(node)
            case Token.CLOSE:
                ancestors.pop()
            # case [Token.CONSTANT | Token.VARIABLE, t]:
            case Token.CONSTANT | Token.VARIABLE:
                active.children.append(node)
                ancestors.append(node)
            case Token.OPERATOR:
                # have to walk from root downward
                # stop at first operator of higher priority
                # for at least ^, continue past equal priority
                # so that a^b^c = a^(b^c)
                # find the first strictly higher priority ancestor
                # it is the left operand
                # if none,
                operator = node
                for i, ancestor in enumerate(ancestors):
                    if ancestor.is_higher_priority_than(operator):
                        break
                left_operand = ancestors[i - 1].children[-1]
                assert ancestor is left_operand
                ancestors[i - 1].children[-1] = operator
                operator.children.append(left_operand)
                ancestors[-1] = operator
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


expression = "1+2+3"
expression = "1+2*3"
expression = "1"
expression = "1+1"
t = build_tree(expression)
print(t)
print(t.children[0])
print(t.children[0].children[0])
print(t.children[0].children[1])
print('.'*20)
print("=", t.get_simplified().symbol.get_value())
