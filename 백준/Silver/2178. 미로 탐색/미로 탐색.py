import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())  #숫자 두 개 이상
graph = [list(map(int, ' '.join(input().split()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]
print(bfs(0,0))
