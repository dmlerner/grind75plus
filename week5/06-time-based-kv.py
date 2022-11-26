# https://leetcode.com/problems/time-based-key-value-store/
# one twenty - one thirty two (random time supported)
# one thirty six - one fourty two (monotonic time)

from collections import defaultdict

def find(values, timestamp):
    ans = None
    low = 0
    high = len(values) - 1
    while low <= high:
        middle_index = (low + high)//2
        middle_timestamp, middle_value = values[middle_index]
        if middle_timestamp == timestamp:
            return middle_value
        if middle_timestamp > timestamp:
            high = middle_index - 1
        else:
            low = middle_index + 1
            ans = middle_value
    return ans or ""


class TimeMap:
    def __init__(self):
        self.values_by_key = defaultdict(list)

    def set(self, k, v, timestamp):
        self.values_by_key[k].append((timestamp, v))

    def get(self, k, timestamp):
        values = self.values_by_key[k]
        if not values:
            return ""
        return find(values, timestamp)
