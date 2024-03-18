from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    x = 0
    y = 0
    visited = [[100000000] * n for _ in range(n)]
    visited[0][0] = graph[0][0]
    # heapq.heappush(hq, (-graph[x][y], x, y))
    q.append((x, y))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[x][y] + graph[nx][ny] < visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + graph[nx][ny]
                q.append((nx, ny))


    return visited[n-1][n-1]

cnt = 1
while True:
    n = int(input())
    if n == 0: break
    graph = [list(map(int, input().split())) for _ in range(n)]
    print("Problem", cnt, end = "")
    print(":", bfs())
    cnt += 1