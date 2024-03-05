import copy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(arr):
    max_val = 0
    q = deque()
    arr2 = arr

    for i in range(m):
        q.append((arr[i][0], arr[i][1], 0))
        visited[arr[i][0]][arr[i][1]] = 0

    while q:
        x, y, d = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny, visited[nx][ny]))
            elif graph[nx][ny] == 2 and visited[nx][ny] == '*':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny, visited[nx][ny]))
                arr2.append((nx, ny))


    for i in range(len(arr2)):
        visited[arr2[i][0]][arr2[i][1]] = '*'

    # print(visited)
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                return False
            elif visited[i][j] != '*' and visited[i][j] != '-' and graph[i][j] == 0:
                max_val = max(max_val, visited[i][j])
    return max_val


def dfs(cnt, start):
    global ans
    if cnt == m:
        for r in range(n):
            for c in range(n):
                visited[r][c] = visited2[r][c]
        key = bfs(case)
        if key != False:
            ans = min(key, ans)
        return

    for i in range(start, len(v)):
        case[cnt] = v[i]
        dfs(cnt + 1, i + 1)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
v = []
visited = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]
zeroFlag = False
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:  # 비활성 바이러스
            v.append((i, j))
            visited[i][j] = '*'
            visited2[i][j] = '*'
        elif graph[i][j] == 1:  # 벽
            visited[i][j] = '-'
            visited2[i][j] = '-'
        else:
            zeroFlag = True

case = [0] * m
ans = 100000000
dfs(0, 0)
if not zeroFlag:  # 빈 칸이 없어서 바이러스를 퍼뜨릴 필요가 없는 경우
    print(0)
elif ans == 100000000:  # 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우
    print(-1)
else:
    print(ans)