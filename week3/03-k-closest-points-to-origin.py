# https://leetcode.com/problems/k-closest-points-to-origin/
# three ten - three twenty nine (using heap)
# three thirty - three fourty one (using sorted list)

import heapq


class Pt:
    def __init__(self, pt):
        x, y = pt
        self.x = x
        self.y = y

    def dist(self):
        return self.x**2 + self.y**2

    def as_list(self):
        return [self.x, self.y]

    def __lt__(self, o):
        return self.dist() > o.dist()

    def __repr__(self):
        return "(" + ", ".join(map(str, (self.x, self.y, self.dist()))) + ")"


def get_k_closest(points, k):
    points = list(map(Pt, points))
    k_closest = points[:k]
    heapq.heapify(k_closest)
    for point in points[k:]:  # n
        if point.dist() < k_closest[0].dist():
            heapq.heapreplace(k_closest, point)  # lg k
    # return k_closest
    return list(map(Pt.as_list, k_closest))


def dist(pt):
    return pt[0] ** 2 + pt[1] ** 2


import bisect


def get_k_closest2(points, k):
    k_closest = points[:k]
    k_closest.sort(key=dist)
    worst_dist = max(map(dist, k_closest))
    for point in points[k:]:  # n
        if dist(point) < worst_dist:
            bisect.insort(k_closest, point, key=dist)  # k
            del k_closest[-1]
            worst_dist = dist(k_closest[-1])
    return k_closest


from david import show
import random

# q = 0
# @show
def quick_select(points, k, i=None, j=None):
    # global q
    # q += 1
    # if q > 10:
    #     print('inf recursion')
    #     return
    i = 0 if i is None else i
    j = len(points) - 1 if j is None else j
    if i >= j:
        return
    pivot_index = random.randint(i, j)
    new_pivot_index = partition(points, i, j, pivot_index)
    quick_select(points, k, i, new_pivot_index - 1)
    if k > new_pivot_index:
        quick_select(points, k, new_pivot_index + 1, j)
    return points[:k]


# @show
def partition(points, i, j, pivot_index):
    # breakpoint()
    pivot = points[pivot_index]
    pivot_dist = dist(pivot)
    active = i
    points[j], points[pivot_index] = points[pivot_index], points[j]
    _j = j
    j -= 1
    while i < j:
        if dist(points[active]) <= pivot_dist:
            points[i], points[active] = points[active], points[i]
            i += 1
        else:
            points[j], points[active] = points[active], points[j]
            j -= 1
    # points[_j], points[i] = points[i], points[_j]
    return i


k = 2
# pts = [[-95,76],[17,7],[-55,-58],[53,20],[-69,-8],[-57,87],[-2,-42],[-10,-87],[-36,-57],[97,-39],[97,49]]
pts = [[1, 3], [-2, 2], [2, -2]]
pts = [[1, 3], [-2, 2]]
pts = [[3, 3], [5, -1], [-2, 4]]
k = 2
s = None
random.seed(5422)
# breakpoint()
print(quick_select(pts, k))
