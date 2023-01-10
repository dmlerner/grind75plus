# https://leetcode.com/problems/valid-palindrome/
from string import ascii_lowercase

VALID_CHARS = set(ascii_lowercase) | set(map(str, range(10)))


def is_valid_char(c):
    return c.lower() in VALID_CHARS


def is_valid(palindrome):
    i = 0
    j = len(palindrome) - 1
    while True:
        while i <= j and not is_valid_char(palindrome[i]):
            i += 1
        while i <= j and not is_valid_char(palindrome[j]):
            j -= 1
        if not i <= j:
            break
        if palindrome[i].lower() != palindrome[j].lower():
            return False
        i += 1
        j -= 1
    return True


def is_valid2(palindrome):
    return _is_valid2(list(palindrome), 0, len(palindrome) - 1)


def _is_valid2(chars, i, j):
    if not i < j:
        return True
    if not is_valid_char(chars[i]):
        return _is_valid2(chars, i + 1, j)
    if not is_valid_char(chars[j]):
        return _is_valid2(chars, i, j - 1)
    if chars[i].lower() != chars[j].lower():
        return False
    return _is_valid2(chars, i + 1, j - 1)


test_fn = is_valid2

assert test_fn("aba")
assert test_fn("ab.a")
assert test_fn("abb.a")
assert test_fn("a.a")

assert not test_fn("abac")
assert not test_fn("ab.ac")
assert not test_fn("abb.ac")
