from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    current_w = 0
    q = deque()

    while len(truck_weights) > 0 or q:
        if q:
            truck = q.popleft()
            if time == truck[1]:
                current_w -= truck[0]
            else:
                q.appendleft(truck)
        if truck_weights :
            if current_w + truck_weights[0] <= weight:
                q.append([truck_weights[0], time + bridge_length])
                current_w += truck_weights[0]
                del truck_weights[0]

        time += 1
    return time