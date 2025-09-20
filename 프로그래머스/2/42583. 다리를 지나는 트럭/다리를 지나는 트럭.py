from collections import deque
def solution(bridge_length, weight, truck_weights):
    q = deque()
    time = 0  #현재 시간
    idx = 0   #현재 트럭 인덱스 
    now = 0   #현재 다리에 올라간 무게 
    while True:
        #종료조건 
        if len(q) == 0 and idx >= len(truck_weights) :
            break
        time +=1 
        #내릴 수 있으면 내리기 
        if len(q) > 0 and time == q[0][1]:
            now -= q[0][0]
            q.popleft()
        #트럭이 다리에 올라갈 수 있으면 추가 
        if idx < len(truck_weights):
            if now + truck_weights[idx] <= weight:
                now += truck_weights[idx]
                q.append([truck_weights[idx], time + bridge_length])
                idx += 1
    return time