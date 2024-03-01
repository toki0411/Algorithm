from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    val = 0
    q = deque()
    q.append((x, y, 1))

    while q:
        x, y, d = q.popleft()
        val = max(d, val)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if graph[nx][ny] < graph[x][y]:
                q.append((nx, ny, d+1))

    return val

T = int(input())
for tc in range(1, T + 1):
    ans = 0
    n, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    max_val = max(map(max, graph))
    maximum = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == max_val:
                maximum.append((i, j))

    for k in range(K+1):
        for i in range(n):
            for j in range(n):
                if graph[i][j] - k < 0:
                    continue
                else:
                    graph[i][j] -= k
                for l in range(len(maximum)):
                    v= bfs(maximum[l][0], maximum[l][1])
                    ans = max(ans, v)
                graph[i][j] += k

    print('#{} {}'.format(tc, ans))
