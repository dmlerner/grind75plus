# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# eleven fourty one - eleven fifty (?)

import operator


def is_operator(t):
    return t in "+-/*"


def get_operator(t):
    op = {
        "+": operator.add,
        "-": operator.sub,
        "/": lambda a, b: int(a / b),
        "*": operator.mul,
    }[t]

    def _operator(a, b):
        return op(int(a), int(b))

    return _operator


def eval_rpn(tokens):
    stack = []
    for t in tokens:
        if is_operator(t):
            operands = stack[-2:]
            del stack[-2:]
            stack.append(get_operator(t)(*operands))
        else:
            stack.append(t)
    return stack[-1]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(eval_rpn(tokens))
