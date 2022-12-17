# four ten
# try again
# four twenty two: incorrect
# four twenty nine: correct, except I didn't know I need to support multi-digit numbers
# four fourty five: works, in style. tokenizeeee

from david import show

def calculate(s):
    result = 0
    i = 0
    operation = None
    while i < len(s):
        c = s[i]
        i += 1
        if c in '+-':
            operation = c
        else:
            d = int(c)
            if operation == '+':
                result += d
            elif operation == '-':
                result -= d
            else:
                result = d
            operation = None
    return result

@show
def calculate_with_paren(s, i):
    result = 0
    j = i
    operation = None
    while j < len(s):
        c = s[j]
        j += 1
        if c in '+-':
            operation = c
        elif c == ')':
            break
        else:
            if c == '(':
                d, j = calculate_with_paren(s, j)
            else:
                d = int(c)

            if operation == '+':
                result += d
            elif operation == '-':
                result -= d
            else:
                result = d
            operation = None
    return result, j

def tokenize(s):
    token = []
    for c in s:
        if c == ' ':
            continue
        if c in '+-()':
            if token:
                yield ''.join(token)
            token = []
        elif token and token[-1] in '+-()':
            yield ''.join(token)
            token = []

        token.append(c)
    yield ''.join(token)

def calculate_multidigit(s):
    tokens = tokenize(s)
    def _calculate_multidigit():
        result = 0
        operation = None
        for token in tokens:

            if token in '+-':
                operation = token
            elif token == ')':
                break
            else:
                if token == '(':
                    d = _calculate_multidigit()
                else:
                    d = int(token)

                if operation == '+':
                    result += d
                elif operation == '-':
                    result -= d
                else:
                    result = d

                operation = None
        return result
    return _calculate_multidigit()





# s = '-1+4-8'
# calculated = calculate(s)
# print(calculated)
# assert calculated == -5


# #    0123456789012345678
# s = "(1+(4+5+2)-3)+(6+8)"
# calculated, _ = calculate_with_paren(s, 0)
# print(calculated, eval(s))
# assert calculated == eval(s)



#    01234567890123456789
s = "(1+(4+56+2)-3)+(6+8)"
calculated= calculate_multidigit(s)
print(calculated, eval(s))
assert calculated == eval(s)
