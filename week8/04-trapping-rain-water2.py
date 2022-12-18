# https://leetcode.com/problems/trapping-rain-water/description/
# eight oh one
# eight thirty six, mostly spent trying unsuccessfully to prove it


def calculate_trapped(heights):
    trapped = 0

    left = 0
    right = len(heights) - 1

    left_max = heights[left]
    right_max = heights[right]

    while left < right:
        fill_height = min(left_max, right_max)
        if heights[left] < heights[right]:
            # move the smaller pointer in
            left += 1
            # add water at its new position
            water_depth = max(0, fill_height - heights[left])

            left_max = max(left_max, heights[left])
        else:
            right -= 1
            water_depth = max(0, fill_height - heights[right])

            right_max = max(right_max, heights[right])
        trapped += water_depth

    return trapped


def pop_to_maintain_invariant(heights, mq, h):
    popped = None
    while mq and heights[mq[-1]] < h:
        popped = mq.pop()
    return popped


def calculate_trapped2(heights):
    # heights = [float('inf')]+heights
    trapped = 0
    # redo with linear storage stack approach
    index_mq = []  # non-strict monotonic decreasing
    for i, h in enumerate(heights):
        # TODO: rename to_fill
        to_fill_index = pop_to_maintain_invariant(heights, index_mq, h)
        if to_fill_index is not None:
            if index_mq:
                left_bound_index = index_mq[-1]
            else:
                left_bound_index = to_fill_index - 1
            # i is aka right_bound_index
            fill_height = min(h, heights[left_bound_index])
            water_depth = max(0, fill_height - heights[to_fill_index])
            width = i - left_bound_index - 1
            print(i, width, water_depth)
            trapped += width * water_depth
        index_mq.append(i)

    return trapped


heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
indices = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
heights = [2, 1, 1, 0, 1, 0, 1, 3, 2, 3]
print(calculate_trapped2(heights))
