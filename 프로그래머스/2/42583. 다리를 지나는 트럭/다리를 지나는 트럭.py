from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    now = 0
    current_weight = 0
    q = deque()
    while True:
        if now >= len(truck_weights) and len(q) == 0 :
            break
        time += 1
        if len(q) > 0 and q[0][1] == time:
            v = q.popleft()
            current_weight -= v[0]
        if now < len(truck_weights):
            if current_weight + truck_weights[now] <=weight:  # 추가
                q.append((truck_weights[now], time + bridge_length))
                current_weight += truck_weights[now]
                now += 1
    return time