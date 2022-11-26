# https://leetcode.com/problems/search-in-rotated-sorted-array/
# seven twenty seven
# almost working at seven thirty six
# working at eight oh eight
# thirty nine minutes: worth redoing


def find_rotation_index(nums):
    if nums[0] <= nums[-1]:
        return 0

    low = 0
    high = len(nums) - 1
    # invariant: [low, high] contains index of original min value
    while low < high:
        mid_index = (low + high) // 2
        mid_value = nums[mid_index]

        if mid_value >= nums[0]:
            # mid index is before rotation point
            low = mid_index + 1
        else:
            assert mid_value < nums[0]
            # mid index is after rotation point
            high = mid_index
    return low


def find_in_rotated(nums, target):
    original_min_index = find_rotation_index(nums)
    if target < nums[0]:
        return find(nums, original_min_index, len(nums) - 1, target)
    return find(nums, 0, original_min_index - 1, target)
    # return find(nums, 0, max(original_min_index-1, 0), target)


def find(nums, low, high, target):
    if high == -1:
        high += len(nums)
    assert 0 <= low <= high
    while low <= high:
        mid_index = (low + high) // 2
        mid_value = nums[mid_index]
        if mid_value == target:
            return mid_index
        if mid_value > target:
            high = mid_index - 1
        else:
            low = mid_index + 1
    return -1


nums = [1, 3, 5]
target = 5
index = find_in_rotated(nums, target)
# print(index)
assert index == 2

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
index = find_in_rotated(nums, target)
# print(index)
assert index == 4

nums = [1, 3]
target = 3
index = find_in_rotated(nums, target)
# print(index)
assert index == 1
