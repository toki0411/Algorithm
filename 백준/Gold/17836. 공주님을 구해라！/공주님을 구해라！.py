import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited = [[[10000000 for ___ in range(2)] for l in range(m)] for _ in range(n)]
    visited[0][0][0] = 0
    while q:
        x, y, g = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            # print(nx,ny)

            if g:  #칼 획득 후
                if visited[nx][ny][g] > visited[x][y][g] + 1 :
                    visited[nx][ny][g] = visited[x][y][g] + 1
                    q.append((nx, ny, g))
            else:
                if visited[nx][ny][0] > visited[x][y][0] + 1 and graph[nx][ny] == 0:
                    visited[nx][ny][g] = visited[x][y][g] + 1
                    q.append((nx, ny, g))
                elif visited[nx][ny][g] > visited[x][y][g] + 1 and graph[nx][ny] == 2:
                    visited[nx][ny][g] = visited[x][y][g] + 1
                    visited[nx][ny][1] = visited[x][y][g] + 1
                    q.append((nx, ny, 1))

    ans = min(visited[n-1][m-1])
    if ans == 10000000:
        return "Fail"
    elif ans > t:
        return "Fail"
    else:
        return ans

print(bfs())