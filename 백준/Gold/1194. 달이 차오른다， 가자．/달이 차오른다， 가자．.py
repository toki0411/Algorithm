from collections import deque

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[[0 for l in range(64)] for __ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
keyMap = {'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32}
doorMap = {'A': 1, 'B': 2, 'C': 4, 'D': 8, 'E': 16, 'F': 32}
def bfs(x, y):
    q = deque()
    q.append((x, y, 0, 0))
    visited[x][y][0] = 1
    while q:
        x, y, key, dis = q.popleft()

        if graph[x][y] == '1':
            return dis
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if not visited[nx][ny][key]:
                if graph[nx][ny] == '1' or graph[nx][ny] == '.':
                    visited[nx][ny][key] = 1
                    q.append((nx, ny, key, dis + 1))
                elif 'a' <= graph[nx][ny] <= 'f' : #열쇠
                    num = keyMap[graph[nx][ny]]
                    tmpKey = key | num
                    visited[nx][ny][tmpKey] = 1
                    q.append((nx, ny, tmpKey, dis + 1))

                elif 'A' <= graph[nx][ny] <= 'F' : #문
                    num = doorMap[graph[nx][ny]]
                    val = key & num
                    if val:
                        visited[nx][ny][key] = 1
                        q.append((nx, ny, key, dis + 1))
    return -1


for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            graph[i][j] = '.'
            print(bfs(i, j))