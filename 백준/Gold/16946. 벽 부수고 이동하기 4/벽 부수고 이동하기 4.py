from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dist = [[1] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(fx, fy):
    q = deque()
    q.append((fx, fy))
    adjList = [(fx, fy)]
    visited[fx][fy] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                adjList.append((nx, ny))
                visited[nx][ny] = 1
                q.append((nx, ny))
    for i, j in adjList:
        dist[i][j] = adjList  # 모든 인접한 정점에 인접한 인덱스들을 넣어줌


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            zeroCnt = []
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
                if dist[nx][ny] not in zeroCnt and dist[nx][ny] != 1:
                    zeroCnt.append(dist[nx][ny])
            # print(i, j, zeroCnt)
            zeroCnt = list(map(lambda x:len(x), zeroCnt))

            print((sum(zeroCnt) + 1) % 10, end="")
        else:
            print(0, end="")
    print()