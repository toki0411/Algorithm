dx = [-1,1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    global ans
    if graph[x][y] == 3:
        ans = 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < 16 and 0<= ny < 16 and not visited[nx][ny] and graph[nx][ny] == 0 or graph[nx][ny] == 3:
            visited[nx][ny] = 1
            dfs(nx, ny)
            visited[nx][ny] = 0

for tc in range(1, 11):
    t = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    ans = 0
    visited = [[0] * 16 for _ in range(16)]
    dfs(1,1)

    print('#{} {}'.format(t, ans))
