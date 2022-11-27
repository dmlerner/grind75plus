# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# two twenty five - two twenty nine

from itertools import product

def letters(i):
    match int(i):
        case 2:
            return 'abc'
        case 3:
            return 'def'
        case 4:
            return 'ghi'
        case 5:
            return 'jkl'
        case 6:
            return 'mno'
        case 7:
            return 'pqrs'
        case 8:
            return 'tuv'
        case 9:
            return 'wxyz'

def get_combinations(phone_number_str):
    combinations = [""]
    for digit in phone_number_str:
        new_combinations = []
        for combination, letter in product(combinations, letters(digit)):
            new_combinations.append(combination + letter)
        combinations = new_combinations
    return combinations

s = '23'

print(get_combinations(s))
