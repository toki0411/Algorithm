import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sys = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [list(input()) for _  in range(n)]
visited = [[[0 for l in range(k+1)] for _ in range(m)] for __ in range(n)]  #열, 행, 층

def bfs():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1
    while q:
        x, y, wb = q.popleft()
        if x == n-1 and y == m-1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[nx][ny][wb] and graph[nx][ny] == '0':
                visited[nx][ny][wb] = visited[x][y][wb] + 1
                q.append([nx, ny, wb])
            elif graph[nx][ny] == '1' and wb + 1 <= k and not visited[nx][ny][wb + 1]:
                visited[nx][ny][wb+1] = visited[x][y][wb] + 1
                q.append([nx, ny, wb+1])

bfs()
arr = visited[n-1][m-1]
arr.sort()
for a in arr:
    if a != 0:
        print(a)
        exit(0)
print(-1)