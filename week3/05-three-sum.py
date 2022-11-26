# https://leetcode.com/problems/3sum/
# ten thirty-eight
# TODO try again

def get(numbers, l, h):
    return numbers[l], numbers[h]

def two_sum(numbers, target, low, high):
    # get all pairs of index whose numbers sum to target
    index_pairs = []
    move_low = move_high = False
    l = low
    h = high

    move_l = move_h = False
    while l != h and high > l and low < h:
        pair = get(numbers, l, h)
        s = sum(pair)
        if s == target:
            if get(numbers, *index_pairs[-1]) != pair:
                index_pairs.append((l, h))
            move_l = True
            move_h = True
        elif s < target:
            move_l = True
        else:
            move_h = True

        if move_l:
            l += 1
            while l < h and numbers[l] == numbers[l+1]:
                l += 1
            move_l = False
        if move_h:
            h -= 1
            while l < h and numbers[h] == numbers[h-1]:
                h -= 1
            move_h = False

    return index_pairs


nums = [2,7,11,15]
nums = [0,0,3,4]
target = 0
print(two_sum(nums, target, 0, len(nums)-1))
# three_sum(nums)



