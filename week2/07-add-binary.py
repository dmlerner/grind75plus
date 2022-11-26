# https://leetcode.com/problems/add-binary/
from itertools import zip_longest

def reversed_int_generator(bitstring):
    for b in reversed(bitstring):
        yield int(b)

def add_binary(a, b):
    carry = 0
    sum_binary_reversed = []
    addends = (a, b)
    for bits in zip_longest(*map(reversed_int_generator, addends), fillvalue=0):
        bit_sum = sum(bits) + carry
        sum_bit, carry = bit_sum & 1, (bit_sum & 2) // 2
        sum_binary_reversed.append(sum_bit)

    if carry:
        sum_binary_reversed.append(carry)

    return ''.join(map(str, reversed(sum_binary_reversed)))

def add_binary2(a, b):
    a = list(map(int, a))
    b = list(map(int, b))
    carry = 0
    i = -1
    sum_binary_reversed = []
    while True:
        try:
            bit_sum = a[i] + b[i] + carry
            sum_bit, carry = bit_sum & 1, (bit_sum & 2) // 2
            sum_binary_reversed.append(sum_bit)
            i -= 1
        except IndexError:
            break

    while True:
        try:
            bit_sum = a[i] + carry
            sum_bit, carry = bit_sum & 1, (bit_sum & 2) // 2
            sum_binary_reversed.append(sum_bit)
            i -= 1
        except IndexError:
            break
    while True:
        try:
            bit_sum = b[i] + carry
            sum_bit, carry = bit_sum & 1, (bit_sum & 2) // 2
            sum_binary_reversed.append(sum_bit)
            i -= 1
        except IndexError:
            break

    if carry:
        sum_binary_reversed.append(carry)

    return ''.join(map(str, reversed(sum_binary_reversed)))

print(add_binary('11', '1'))
