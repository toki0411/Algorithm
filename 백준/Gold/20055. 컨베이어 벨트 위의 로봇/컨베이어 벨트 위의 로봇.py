from collections import deque
N, K = map(int, input().split())
dur = list(map(int, input().split()))
robot = []
def offload():
    idx = 0
    while idx < len(robot):
        if robot[idx] == N-1:
            del robot[idx]
        else:
            idx +=1

def landing():
    if check(0):
        robot.append(0)
        dur[0] -= 1
def robotMove():
    for i in range(len(robot)):
        next = robot[i] + 1
        if robot[i] + 1 == 2*N:
            next = 0
        if dur[next] > 0 and check(next):
            robot[i] = next
            dur[next] -= 1
    offload()

def check(next):
    for r in robot:
        if r == next:
            return False
    return True

level = 0
dur = deque(dur)
while True:
    level += 1
    dur.rotate(1)  #1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    for i in range(len(robot)):
        robot[i] += 1
        if robot[i] == 2*N:
            robot[i] = 0
    offload()
    if len(robot) > 0:  #2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        robotMove()

    if dur[0] > 0:  #3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        landing()
    # print(dur, robot)
    cnt = 0
    for i in range(2*N):
        if dur[i] == 0:
            cnt += 1
    if cnt >= K:
        break

print(level)