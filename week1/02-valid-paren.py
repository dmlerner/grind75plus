# https://leetcode.com/problems/valid-parentheses/
def is_valid(s):
    open_bracket_stack = []
    return (
        all(map(lambda bracket: is_valid_next_bracket(open_bracket_stack, bracket), s))
        and not open_bracket_stack
    )


def is_valid_next_bracket(open_bracket_stack, bracket):
    open_brackets = "[{("
    close_bracket_by_open_bracket = {"[": "]", "(": ")", "{": "}"}
    if bracket in open_brackets:
        open_bracket_stack.append(bracket)
    else:
        if not open_bracket_stack:
            return False

        correct_close_bracket = close_bracket_by_open_bracket[open_bracket_stack.pop()]
        if bracket != correct_close_bracket:
            return False
    return True


print(is_valid("()"))
