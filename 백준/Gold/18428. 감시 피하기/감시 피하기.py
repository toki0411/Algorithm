import sys
from collections import deque

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    q = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'T':
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= N: break
                if graph[nx][ny] == 'O': break
                if graph[nx][ny] == 'S':
                    return False
    return True

def dfs(cnt):  #벽을 세울 조합 구함
    global ans
    if cnt == 3:
        if bfs():
            print("YES")
            exit(0)
        return
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                dfs(cnt + 1)
                graph[i][j] = 'X'
N = int(input())
graph = [list(input().split()) for _ in range(N)]
ans = 0
dfs(0)
print("NO")