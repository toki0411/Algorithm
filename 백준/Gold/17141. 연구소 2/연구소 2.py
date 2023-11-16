import copy
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus = []
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))
        elif graph[i][j] == 1: #벽일 경우
            visited[i][j] = -2
#-2 벽 -1 바이러스

def bfs():
    q = deque(); tool = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                q.append((i, j, 0))
            elif visited[i][j] == 0:
                tool = True
    if not tool:
        return 0
    visited2 = copy.deepcopy(visited)
    while q:
        x, y, t = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited2[nx][ny]==0:
                visited2[nx][ny] = t+1
                q.append((nx,ny,t+1))
    val = -1; flag = False
    # 바이러스가 다 퍼졌는지, 최소 시간을 체크
    for i in range(n):
        for j in range(n):
            if visited2[i][j] == 0:  # 다 퍼지지 않은 경우
                val = -1
                flag = True
                break
            elif visited2[i][j] == -1 or visited2[i][j] == -2:
                continue
            else:
                val = max(visited2[i][j], val)
        if flag:
            break


    return val

def virus_set(level, start):
    global ans, key
    if level == m:
        cnt = bfs()
        if cnt == -1:
            key = True
        else:
            ans = min(cnt, ans)
        return
    for i in range(start, len(virus)):
        x, y = virus[i]
        if visited[x][y] == 0:
            visited[x][y] = -1  #바이러스 두기
            virus_set(level + 1, i+1)
            visited[x][y] = 0
ans = 1e9
key = False
virus_set(0,0)
if key and ans == 1e9:
    print(-1)
else:
    print(ans)