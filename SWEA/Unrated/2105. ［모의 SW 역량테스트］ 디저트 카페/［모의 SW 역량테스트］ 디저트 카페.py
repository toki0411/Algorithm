dx = [1,1,-1,-1]
dy = [1,-1,-1,1]
def dfs(d, x, y, dessert, ox, oy):
    global ans
    if x == ox and oy == y and d == 3:
        ans = max(len(dessert), ans)
        return
    if d+1 <= 3:
        nx = x + dx[d+1]
        ny = y + dy[d+1]
        if ox == nx and oy == ny and d+1 == 3:
            dfs(d+1, nx, ny, dessert, ox, oy)
        if nx >= 0 and ny >=0 and nx < n and ny < n and graph[nx][ny] not in dessert:
            dfs(d+1, nx, ny, dessert+[graph[nx][ny]], ox, oy)
    if d != -1:
        nx = x + dx[d]
        ny = y + dy[d]
        if ox == nx and oy == ny and d == 3:
            dfs(d, nx, ny, dessert, ox, oy)
        if nx >= 0 and ny >=0 and nx < n and ny < n and graph[nx][ny] not in dessert:
            dfs(d, nx, ny, dessert + [graph[nx][ny]], ox, oy)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ans = 1
    graph = [list(map(int, input().split()))for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dfs(-1, i, j, [graph[i][j]], i, j)
    print('#{} {}'.format(tc, ans if ans != 1 else -1))