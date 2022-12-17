# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# nine fourty
# nine fourty nine: have dp on paper
# spend too long thinking about MQs for next_by_job
# realize it's a trivial two-pointer task
# ten thirty seven: done (unoptimized slightly)?
# ten thirty nine: probably optimized, but leetcode is down or something
# oh god and I'm losing packets

from collections import deque
from dataclasses import dataclass
from itertools import starmap


@dataclass(frozen=True)
class Job:
    start: float
    end: float
    profit: float

    def conflicts(self, other):
        first, second = sorted([self, other], key=lambda j: j.start)
        return first.start <= second.start < first.end


def get_next_by_job(jobs):
    sorted_by_start = jobs  # sorted(jobs, key=lambda j: j.start)
    sorted_by_end = sorted(jobs, key=lambda j: j.end)
    next_by_job = {}
    s = 0
    e = 0
    while e < len(jobs) and s < len(jobs):
        js, je = sorted_by_start[s], sorted_by_end[e]
        if js is je or js.conflicts(je):
            s += 1
            continue
        next_by_job[je] = s
        e += 1
    return next_by_job


def max_profit(starts, ends, profits):
    jobs = list(starmap(Job, zip(starts, ends, profits)))
    jobs.sort(key=lambda j: j.start)
    next_by_job = get_next_by_job(jobs)

    def dp(i):
        if i >= len(jobs):
            return 0
        profit_with_job = jobs[i].profit

        next_job_index = next_by_job.get(jobs[i])
        if next_job_index is not None:
            profit_with_job += dp(next_job_index)

        return max(profit_with_job, dp(i + 1))

    return dp(0)


startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
print(max_profit(startTime, endTime, profit))
print()

startTime = [1, 2, 3, 4, 6]
endTime = [3, 5, 10, 6, 9]
profit = [20, 20, 100, 70, 60]
print(max_profit(startTime, endTime, profit))
