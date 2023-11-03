
def dfs(x, y, cnt):
    if graph[x][y] == 'c':
        ans[x][y] = 0
        if  0<= y+1 < w and graph[x][y+1] == '.':
            dfs(x, y+1, cnt+1)
    else:
        ans[x][y] = cnt
        if 0 <= y+1 < w and graph[x][y+1] == '.':
            dfs(x, y+1, cnt+1)

h, w = map(int,input().split())
graph = [list(map(str,input()))for _ in range(h)]
ans = [[-1] * (w) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if graph[i][j] == 'c':
            dfs(i,j,0)
for i in range(len(ans)):
    for j in range(len(ans[0])):
        print(ans[i][j], end = ' ')
    print()
