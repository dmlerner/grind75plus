"""
https://leetcode.com/problems/decode-string/
8:05
8:11 _decode works for flat
8:24 I should probably parse R->L
and also stop leetcoding for the night...
8:09 the next night
8:40 ok I should stop just reading https://en.wikipedia.org/wiki/Left_recursion#:~:text=7%20External%20links-,Definition,itself%20as%20the%20leftmost%20symbol.
9:00 passes and that's almost pretty!
9:10 well that's gorgeous
9:21 oh god it's so beautiful
"""


class Token:
    OPEN = "["
    CLOSE = "]"
    DIGITS = set(map(str, range(10)))
    CHARACTERS = set("abcdefghijklmnopqrstuvwxyz")


def get_repeat_token(s, i):
    assert s[i] in Token.DIGITS
    digit = []
    while i < len(s) and s[i] in Token.DIGITS:
        digit.append(s[i])
        i += 1
    digit = int("".join(digit))
    return Token.DIGITS, digit, i


def get_letters_token(s, i):
    assert s[i] in Token.CHARACTERS
    letters = []
    while i < len(s) and s[i] in Token.CHARACTERS:
        letters.append(s[i])
        i += 1
    return Token.CHARACTERS, "".join(letters), i


def tokenize(s, i=0):
    if i == len(s):
        return

    match s[i]:
        case Token.OPEN:
            token_type, token = Token.OPEN, None
            i += 1
        case Token.CLOSE:
            token_type, token = Token.CLOSE, None
            i += 1
        case c if c in Token.DIGITS:
            token_type, token, i = get_repeat_token(s, i)
        case c if c in Token.CHARACTERS:
            token_type, token, i = get_letters_token(s, i)
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


def decode_from_tokens(s):
    multipliers = []
    expressions = [[]]
    for (token_type, token) in tokenize(s):
        match token_type:
            case Token.OPEN:
                expressions.append([])
            case Token.CLOSE:
                expression = expressions.pop()
                multiplier = multipliers.pop()
                multiplied_expression = multiplier * expression
                expressions[-1].append(multiplied_expression)
            case Token.CHARACTERS:
                expressions[-1].append(token)
            case Token.DIGITS:
                multipliers.append(token)
    return "".join(flatten(expressions))


s = "3[a]2[bc]"
s = "3[ab2[cd]]"
s = "2[abc]3[cd]ef"
expect = 3 * "abcdcd"
expect = "abcdcdabcdcdabcdcd"
expect = "abcabccdcdcdef"
print(list(tokenize(s)))
print()
decoded = decode_from_tokens(s)
print(decoded, decoded == expect)
