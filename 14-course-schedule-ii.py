"""
https://leetcode.com/problems/course-schedule-ii/
8:12
8:28 oh god I feel stupid
8:42 heap approach might work but is ugly
8:48 works and is pretty
"""

from collections import defaultdict
import heapq


def build_prereqs_by_course(prerequisites):
    prereqs_by_course = defaultdict(set)
    for course, prereq in prerequisites:
        prereqs_by_course[course].add(prereq)
    return prereqs_by_course

class NoSuchOrderException(Exception): pass

def pop_min(heap, n_prereqs_by_course):
    while heap:
        n_prereqs, prereq = heapq.heappop(heap)
        if n_prereqs == n_prereqs_by_course[prereq]:
            if n_prereqs == 0:
                return prereq
            else:
                break
    raise NoSuchOrderException


def find_order(num_courses, prerequisites):
    prereqs_by_course = build_prereqs_by_course(prerequisites)
    courses_by_prereq = build_prereqs_by_course(map(reversed, prerequisites))

    n_prereqs_by_course = {
        course: len(prereqs_by_course.get(course, set())) for course in range(num_courses)
    }
    heap = [(n, c) for (c, n) in n_prereqs_by_course.items()]
    heapq.heapify(heap)

    order = []

    while heap and len(order) < num_courses:
        try:
            prereq = pop_min(heap, n_prereqs_by_course)
        except NoSuchOrderException:
            return []

        order.append(prereq)

        for course in courses_by_prereq[prereq]:
            prereqs = prereqs_by_course[course]
            prereqs.remove(prereq)
            n_prereqs_by_course[course] -= 1
            heapq.heappush(heap, (len(prereqs), course))

    return order


pre = [[1, 0]]
