# https://leetcode.com/problems/bus-routes/
# 3:25
# 3:34 idea
# 3:48 20/46 pass
# 3:52 43/46 pass
# 3:53 done

from collections import defaultdict, deque

def count_busses(routes, source_stop, target_stop):
    if source_stop == target_stop:
        return 0

    route_numbers_by_stop = defaultdict(set)
    for r, route in enumerate(routes):
        for stop in route:
            route_numbers_by_stop[stop].add(r)

    source_routes = route_numbers_by_stop[source_stop]
    if route_numbers_by_stop[target_stop].intersection(route_numbers_by_stop[source_stop]):
        return 1

    connected_route_numbers_by_number = defaultdict(set)
    for stop in route_numbers_by_stop:
        for r1 in route_numbers_by_stop[stop]:
            for r2 in route_numbers_by_stop[stop]:
                connected_route_numbers_by_number[r1].add(r2)
                connected_route_numbers_by_number[r2].add(r1)


    frontier = deque(source_routes)
    distance_by_route = {r: 1 for r in source_routes}
    while frontier:
        next_route = frontier.pop()
        for connected_route in connected_route_numbers_by_number[next_route]:
            if connected_route not in distance_by_route:
                distance_by_route[connected_route] = distance_by_route[next_route] + 1
                if connected_route in route_numbers_by_stop[target_stop]:
                    return distance_by_route[connected_route]
                frontier.append(connected_route)
    return -1



routes = [[2],[2,8]]
source = 2
target = 8

c = count_busses(routes, source, target)
print(c)
assert c == 1
