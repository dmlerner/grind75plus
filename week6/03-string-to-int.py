# https://leetcode.com/problems/string-to-integer-atoi/
# eight oh seven - eight twenty
# this is a stupid problem. They have lots of invalid test cases, which they don't mention, so I didn't design for that at first.
# TODO: try again
"""
1. Read in and ignore any leading whitespace.

2. Check if the next character (if not already at the end of the string) is '-' or
'+'. Read this character in if it is either. This determines if the final result
is negative or positive respectively. Assume the result is positive if neither i
s present .

3. Read in next the characters until the next non-digit character or the end of the
input is reached. The rest of the string is ignored .

4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits
were read, then the integer is 0. Change the sign as necessary (from step 2) .

5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then c
lamp the integer so that it remains in the range. Specifically, integers less th
an -231 should be clamped to -231, and integers greater than 231 - 1 should be c
lamped to 231 - 1.

6. Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of th
e string after the digits.
"""


"""
whitespace *
(+|-)?
\d+
"""

DIGITS = "".join(map(str, range(10)))


def string_to_int(s):
    sign, digits = get_sign_and_digits(s)
    sign_multiplier = 1 if sign == "+" else -1
    integer = sign_multiplier * int("".join(digits))
    return min(max(-(2**31), integer), 2**31 - 1)


def get_sign_and_digits(s):
    i = 0
    sign = None
    digits = []

    while i < len(s):
        c = s[i]
        i += 1
        if c in DIGITS:
            if not sign:
                sign = "+"
            if digits or c != "0":
                digits.append(c)
            else:
                continue
        elif digits:
            break
        elif c == " ":
            pass
        elif c in "+-":
            assert not digits
            assert sign is None
            sign = c
        else:
            assert False

    sign = sign or "+"
    digits = digits or ["0"]

    return sign, digits


print(string_to_int("       00001234"))
