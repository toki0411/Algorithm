from collections import deque
t = int(input())
def dfs(x, y):
    if abs(x-target_x) + abs(y - target_y) <= (20 * 50):
        visited[-1] = 1
        return
    for i in range(n):
        if visited[i]:
            continue
        nx, ny = store[i]
        distance = abs(x-nx) + abs(y-ny)
        if distance <= (20*50):
            visited[i] = 1
            dfs(nx,ny)
for tc in range(t):
    n = int(input()) #편의점 개수
    house_x, house_y = map(int,input().split())
    store = [list(map(int, input().split())) for _ in range(n)]
    target_x, target_y = map(int, input().split())
    visited = [0] * (n+1) # 집, 편의점, 축제장소
    # visited[0] = 1 # 집은 idx 0이고 방문처리한다.
    dfs(house_x, house_y)
    if not visited[-1]:
        print("sad")
    else:
        print("happy")

