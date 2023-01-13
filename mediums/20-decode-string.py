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
"""

DIGITS = set(map(str, range(10)))
CHARACTERS = set("abcdefghijklmnopqrstuvwxyz")


class Token:
    OPEN = "["
    CLOSE = "]"
    LETTERS = "LETTERS"
    REPEAT = "REPEAT"


def get_repeat_token(s, i):
    assert s[i] in DIGITS
    digit = []
    while i < len(s) and s[i] in DIGITS:
        digit.append(s[i])
        i += 1
    digit = int("".join(digit))
    return Token.REPEAT, digit, i


def get_letters_token(s, i):
    assert s[i] in CHARACTERS
    letters = []
    while i < len(s) and s[i] in CHARACTERS:
        letters.append(s[i])
        i += 1
    return Token.LETTERS, "".join(letters), i


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
        case c if c in DIGITS:
            token_type, token, i = get_repeat_token(s, i)
        case c if c in CHARACTERS:
            token_type, token, i = get_letters_token(s, i)
        case _:
            raise Exception

    yield token_type, token
    yield from tokenize(s, i)


def decode_from_tokens(s):
    multipliers = []
    expressions = [[]]
    for (token_type, token) in tokenize(s):
        match token_type:
            case Token.OPEN:
                expressions.append([])
            case Token.CLOSE:
                # expression = "".join(expressions.pop())
                expression = expressions.pop()
                multiplier = multipliers.pop()
                multiplied_expression = multiplier * expression
                expressions[-1].append(multiplied_expression)
            case Token.LETTERS:
                expressions[-1].append(token)
            case Token.REPEAT:
                multipliers.append(token)
    return "".join(expressions.pop())


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
