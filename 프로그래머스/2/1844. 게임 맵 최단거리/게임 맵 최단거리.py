from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y,n,m, maps):
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    return maps[n-1][n-1]
def solution(maps):
    n = len(maps)
    m=len(maps[0])
    ans = bfs(0,0, n,m, maps)
    return ans if ans > 1 else -1