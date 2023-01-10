"""
https://leetcode.com/problems/find-the-duplicate-number/
11:53
11:57 admit that I can't use math
12:01 done
12:03 but oh wait I wasn't supposed to modify the array either??
12:16 read answer
"""


def swap(numbers, i, j):
    numbers[i], numbers[j] = numbers[j], numbers[i]


def find_duplicate(numbers):
    i = 0
    while i < len(numbers):
        while numbers[i] != i + 1:
            if numbers[i] == numbers[numbers[i] - 1]:
                break
            swap(numbers, i, numbers[i] - 1)
        i += 1
    return numbers[-1]


def floyd(numbers):
    slow = fast = numbers[0]

    start = True
    while start or slow != fast:
        print(slow, fast)
        start = False
        slow = numbers[slow]
        fast = numbers[numbers[fast]]

    print()
    print(slow, fast)
    print()

    slow = numbers[0]
    while slow != fast:
        slow = numbers[slow]
        fast = numbers[fast]
        # fast = numbers[numbers[fast]]
        print(slow, fast)
    return slow


print(floyd([4, 3, 1, 2, 3, 5]))
