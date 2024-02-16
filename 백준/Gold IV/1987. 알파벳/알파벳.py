import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph=[list(input()) for _ in range(n)]

str = set()
str.add(graph[0][0])
ans = 0
def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < m and not graph[nx][ny] in str:  #체크
            str.add(graph[nx][ny])
            dfs(nx, ny, cnt +1)
            str.remove(graph[nx][ny])

dfs(0,0, 1)
print(ans)