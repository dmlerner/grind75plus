# https://leetcode.com/problems/first-missing-positive/
# 11:11
# 11:27

# requires linear time and constant extra space

def first_missing_positive(numbers):
    def swap(i, j):
        if numbers[i] == numbers[j]:
            return False
        numbers[i], numbers[j] = numbers[j], numbers[i]
        return True

    def get_target_position(num):
        return num - 1

    for i in range(len(numbers)):
        while True:
            target_position = get_target_position(numbers[i])
            if i != target_position and 0 <= target_position < len(numbers):
                if not swap(i, target_position):
                    break
            else:
                break

    for i, n in enumerate(numbers):
        if n != i + 1:
            return i + 1
    return len(numbers) + 1

nums = [3,4,-1,1]
nums = [1,1]
print(first_missing_positive(nums))
