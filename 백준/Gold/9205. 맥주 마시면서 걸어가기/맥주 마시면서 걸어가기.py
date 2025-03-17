from collections import deque

T = int(input())

while T:
    n = int(input())
    hx, hy = map(int, input().split())
    q = deque()
    q.append([hx, hy])
    pList = []
    for i in range(n):
        px, py = map(int, input().split())
        pList.append([px, py])
    fx, fy = map(int, input().split())

    visited = [0] * n
    flag = False

    while q:
        x, y = q.popleft()
        if abs(x - fx) + abs(y - fy) <= 1000:
            flag = True
            break
        for i in range(n):
            px, py = pList[i][0], pList[i][1]
            if visited[i] == 0 and abs(x - px) + abs(y - py) <= 1000:
                q.append([px, py])
                visited[i] = 1
    if flag:
        print("happy")
    else:
        print("sad")
    T-=1