from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, limit):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    cnt = 0
    if graph[x][y] == 1:
        cnt += 1
    q.append((x, y, 1))
    visited[x][y] = 1
    while q:
        x, y, area = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if not visited[nx][ny] and area+1 <= limit:
                if graph[nx][ny] == 1:
                    cnt += 1
                visited[nx][ny] = 1
                q.append((nx, ny, area + 1))
    # print(cnt)
    return cnt

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    houseCnt = 0
    graph = [list(map(int, input().split())) for _ in range(n)]
    for k in range(1, n+2):
        price = k * k + (k - 1) * (k - 1)
        for i in range(n):
            for j in range(n):
                tmp = bfs(i, j, k)
                # print(tmp)
                if tmp * m - price >= 0 and tmp > houseCnt:
                    # print(tmp, tmp * m - price)
                    houseCnt = tmp
    print('#{} {}'.format(tc, houseCnt))
