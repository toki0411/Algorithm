import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)
def dfs(x, y):
    global safe
    visited[x][y] = 1
    cycle.append([x,y])
    nowX = x
    nowY = y
    if graph[x][y] == 'D' and x < n-1:  #down
        nowX += 1
    elif graph[x][y] == 'L' and y > 0:  #left
        nowY -= 1
    elif graph[x][y] == 'R' and y < m-1:  #right
        nowY += 1
    elif graph[x][y] == 'U' and x > 0 :  #up
        nowX -= 1

    if visited[nowX][nowY]:
        if [nowX, nowY] in cycle:
            safe += 1
    else:
        dfs(nowX, nowY)

n, m = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
graph = []
safe = 0
for _ in range(n):
    l = list(input())
    graph.append(l)
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cycle = []
            dfs(i, j)

print(safe)