from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
pos = []  # 0의 좌표 모음
for i in range(n):  # 0의 좌표를 입력받는다.
    row = graph[i]
    for j in range(m):
        if row[j] == 0:
            pos.append([i, j])
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = 1
    kill = 1
    flag = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    flag = 1
                elif graph[nx][ny] == 2:
                    visited[nx][ny] = 1
                    kill += 1
                    q.append([nx, ny])

    return kill if not flag else -1
def game(turn):
    visited = [[0] * m for _ in range(n)]
    total_cnt = 0
    for x, y in turn:
        graph[x][y] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2 and not visited[i][j]:
                cnt = bfs(i, j, visited)
                if cnt != -1:
                    total_cnt += cnt
    for x, y in turn:
        graph[x][y] = 0
    return total_cnt

max_kill = 0
for turn in combinations(pos, 2):
    max_kill = max(max_kill, game(turn))
print(max_kill)
