import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
a = 0;
b = 0
for i in range(n):
    for k in range(n):
        if graph[i][k] == 9:
            a = i
            b = k

def bfs(x, y, babyShark):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = deque([(x, y)])
    visited[x][y] = 1
    temp = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] <= babyShark:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    if graph[nx][ny] < babyShark and graph[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))  #가장 위, 왼쪽 순서대로 정렬


cnt = 0
size = 2
ans = 0
while 1:
    fish = bfs(a, b, size)
    if len(fish) == 0:
        break
    
    nx, ny, dist = fish.pop()

    ans += dist
    
    graph[nx][ny] = 0
    graph[a][b] = 0
    #물고기 개수 up
    a, b = nx, ny
    cnt +=1
    if cnt == size:
        size+=1
        cnt = 0
print(ans)
