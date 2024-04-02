import copy

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x, y, k, cnt):
    # print(x, y, k, cnt)
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if visited[nx][ny] : continue
        if graph[nx][ny] < graph[x][y]:
            visited[nx][ny] = 1
            dfs(nx, ny, k, cnt + 1)
            visited[nx][ny] = 0
        elif graph[nx][ny] - K < graph[x][y] and k == 1 : #등산로를 깎는다.
            tmp = graph[nx][ny]
            while graph[nx][ny] >= graph[x][y]:
                graph[nx][ny] -= 1
            if graph[nx][ny] < 0 : graph[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, 0, cnt + 1)
            visited[nx][ny] = 0
            graph[nx][ny] = tmp


T = int(input())

for tc in range(1, T+1):
    ans = 1
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    graph2 = [[0] * N for _ in range(N)]

    maxVal = 0
    for i in range(N):
        maxVal = max(max(graph[i]), maxVal)
        for j in range(N):
            graph2[i][j] = graph[i][j]

    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] == maxVal:
                visited = [[0] * N for _ in range(N)]
                visited[i][j] = 1
                dfs(i, j, 1, 1)
                for l in range(N):
                    for r in range(N):
                        graph[l][r] = graph2[l][r]
                for v in visited:
                    ans = max(max(v), ans)

    print("#{} {}".format(tc, ans))