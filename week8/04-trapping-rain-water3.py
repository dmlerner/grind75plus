# https://leetcode.com/problems/trapping-rain-water/
# seven fifty two
# eight oh one: I think I remember: descending mq
# eight oh four: typed up
# eight seventeen: ah right, this is the horizontal approach
# eight nineteen: passes
# let's try the vertical approach too.
# eight thirty four: works

def calculate_rain_horizontal(heights):
    rain = 0
    mq = []
    for i, h in enumerate(heights):
        while mq and h > heights[mq[-1]]:
            # fill with water
            popped = mq.pop()
            if not mq:
                # nothing taller before it, so can't store water
                continue

            height = min(heights[mq[-1]], h)
            depth = height - heights[popped]
            if depth <= 0:
                continue

            width = i - mq[-1] - 1
            rain += depth * width

        mq.append(i)
    return rain

def calculate_rain_vertical(heights):
    l = 0
    r = len(heights) - 1
    left_max = right_max = 0
    rain = 0
    while l <= r:
        height = min(left_max, right_max)
        #if heights[l] <= heights[r]:
        if left_max <= right_max:
            left_max = max(left_max, heights[l])
            location_to_fill = l
            l += 1
        else:
            right_max = max(right_max, heights[r])
            location_to_fill = r
            r -= 1

        depth = height - heights[location_to_fill]
        if depth > 0:
            rain += depth
    return rain


#          0,1,2,3,4,5,6,7,8,9,0,1
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
rain = calculate_rain_vertical(heights)
print(rain)



