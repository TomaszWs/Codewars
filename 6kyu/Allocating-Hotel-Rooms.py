# Task
#
# Allocate customers to hotel rooms based on their arrival and departure days.
# Each customer wants their own room, so two customers can stay in the same
# room only if the departure day of the first customer is earlier than the
# arrival day of the second customer. The number of rooms used should be
# minimized.
# Input
#
# A list or array of n customers, 1 ≤ n ≤ 1000. Each customer is represented
# by (arrival_day, departure_day), which are positive integers satisfying
# arrival_day ≤ departure_day.
# Output
#
# A list or array of size n, where element i indicates the room that customer
# i was allocated. Rooms are numbered 1,2, ..., k for some 1 ≤ k ≤ n. Any
# allocation that minimizes the number of rooms k is a valid solution.
# Example:
#
# Suppose customers is [(1,5), (2,4), (6,8), (7,7)].
# Clearly customers 1 and 2 cannot get the same room. Customer 3 can use the
# same room as either of them, because they both leave before customer
# 3 arrives. Then customer 4 can be given the other room.
# So any of [1,2,1,2], [1,2,2,1], [2,1,2,1], [2,1,1,2] is a valid solution.
#
# NOTE: The list of customers is not necessarily ordered by arrival_time.
# Source: CSES
# Related kata:
#
# Minimum number of taxis is a harder version, because the lists are bigger.
#
# The Hotel with Infinite Rooms
# Is room reserved?


import heapq


def allocate_rooms(customers):
    customers = sorted(enumerate(customers), key=lambda x: x[1][0])
    min_heap = []
    allocation = [0] * len(customers)
    room_count = 0
    for index, (arrival, departure) in customers:
        if min_heap and min_heap[0][0] < arrival:
            _, room_id = heapq.heappop(min_heap)
        else:
            room_count += 1
            room_id = room_count
        allocation[index] = room_id
        heapq.heappush(min_heap, (departure, room_id))
    return allocation


if __name__ == "__main__":
    print(allocate_rooms([(1, 5), (2, 4), (6, 8), (7, 7)]))


# Best solutions:


def allocate_rooms(customers):
    res = [0] * len(customers)
    dep = [0] * len(customers)
    for i, (a, d) in sorted(enumerate(customers), key=lambda x: x[1]):
        n = next(r for r, d in enumerate(dep) if d < a)
        dep[n] = d
        res[i] = n + 1
    return res


import heapq


def allocate_rooms(customers):
    rooms, h, res = 0, [], [0] * len(customers)
    for i, (a, b) in sorted(enumerate(customers), key=lambda p: p[1]):
        if not h or h[0][0] >= a:
            rooms += 1
            res[i] = rooms
            heapq.heappush(h, (b, rooms))
        else:
            res[i] = h[0][1]
            heapq.heappushpop(h, (b, h[0][1]))
    return res


def allocate_rooms(customers):
    res, cur = [-1] * len(customers), []

    for k, (arr, dep) in sorted(enumerate(customers), key=lambda x: x[1]):
        mn_val, mn_ind = arr, -1
        for j, c in enumerate(cur):
            if c < mn_val:
                mn_val, mn_ind = c, j

        if mn_ind > -1:
            res[k] = mn_ind + 1
            cur[mn_ind] = dep
        else:
            cur.append(dep)
            res[k] = len(cur)

    return res
