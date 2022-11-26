# https://leetcode.com/problems/course-schedule/
# one oh eight - one thirty eight

from collections import defaultdict, deque

from itertools import repeat


def can_finish(num_courses, prereqs):
    courses_by_preq = defaultdict(set)
    unsatisfied_prereqs_by_course = dict(zip(range(num_courses), repeat(0)))
    for (course, prereq) in prereqs:
        courses_by_preq[prereq].add(course)
        unsatisfied_prereqs_by_course[course] += 1

    frontier = deque([])
    no_prereqs = {c for (c, nps) in unsatisfied_prereqs_by_course.items() if nps == 0}
    frontier.extend(no_prereqs)

    while frontier:
        active = frontier.popleft()
        for course in courses_by_preq[active]:
            unsatisfied_prereqs_by_course[course] -= 1
            if unsatisfied_prereqs_by_course[course] == 0:
                frontier.append(course)

    return sum(unsatisfied_prereqs_by_course.values()) == 0


prereqs = [[1, 0], [0, 1]]
prereqs = [[1, 0]]
prereqs = [[1, 4], [2, 4], [3, 1], [3, 2]]
print(can_finish(5, prereqs))
