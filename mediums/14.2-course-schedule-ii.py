"""
https://leetcode.com/problems/course-schedule-ii/
10:56
11:07 done
"""

from collections import defaultdict


def build_prereqs_by_course(prerequisites):
    prereqs_by_course = defaultdict(set)
    for course, prereq in prerequisites:
        prereqs_by_course[course].add(prereq)
    return prereqs_by_course


def find_order(num_courses, prerequisites):
    prereqs_by_course = build_prereqs_by_course(prerequisites)
    courses_by_prereq = build_prereqs_by_course(map(reversed, prerequisites))

    # n_prereqs_by_course = {
    #     course: len(prereqs_by_course.get(course, set())) for course in range(num_courses)
    # }

    order = []
    courses_without_prereqs = [course for course in range(num_courses) if not prereqs_by_course.get(course)]
    courses_without_prereqs_set = set(courses_without_prereqs)

    while courses_without_prereqs:
        course_without_prereqs = courses_without_prereqs.pop()
        courses_without_prereqs_set.remove(course_without_prereqs)

        order.append(course_without_prereqs)

        for course in courses_by_prereq[course_without_prereqs]:
            prereqs = prereqs_by_course[course]
            prereqs.remove(course_without_prereqs)
            if not prereqs:
                courses_without_prereqs.append(course)
                courses_without_prereqs_set.add(course)
            # n_prereqs_by_course[course] -= 1

    if len(order) == num_courses:
        return order
    return []


pre = [[1, 0], [0, 1], [0, 2], [1, 2]]
n = 3
# n = 100
# pre = [[i, j] for i in range(n) for j in range(i+1, n)]
# pre = []
print(pre)
print(find_order(n, pre))
