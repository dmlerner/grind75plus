# https://leetcode.com/problems/majority-element/
def majority(nums):
    a = b = None
    a_count = b_count = 0
    for i in nums:
        if a_count == 0:
            a = i
        elif b_count == 0:
            b = i

        if i == a:
            a_count += 1
        elif i == b:
            b_count += 1
        else:
            a_count -= 1
            b_count -= 1

    return a if a_count > b_count else b


def majority2(nums):
    m = None
    count = 0
    for i in nums:
        if count == 0:
            m = i

        if i == m:
            count += 1
        else:
            count -= 1
    return m


print(majority2((3, 2, 3)))
