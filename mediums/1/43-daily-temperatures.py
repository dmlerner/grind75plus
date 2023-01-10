# https://leetcode.com/problems/daily-temperatures/
# 7:23
# 7:30 done?
# one minor error, sweet.
# take that, mqs.


def get_days_until_warmer(temps):
    days_until_warmer = [0] * len(temps)
    stack = []

    for day, temp in enumerate(temps):

        while stack and temp > temps[stack[-1]]:
            popped_day = stack.pop()
            days_until_warmer[popped_day] = day - popped_day

        stack.append(day)

    return days_until_warmer


temps = [73, 74, 75, 71, 69, 72, 76, 73]
duw = get_days_until_warmer(temps)
print(duw)
