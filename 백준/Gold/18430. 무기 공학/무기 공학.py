dx = [[0, 1], [0, -1], [-1, 0], [0, 1]]
dy = [[-1, 0], [-1, 0], [0, 1], [1, 0]]

def dfs(idx, cnt):
    global ans
    if idx == n * m :
        ans = max(cnt, ans)
        return
    x = idx // m
    y = idx % m
    if not visited[x][y]:
        for i in range(4):
            nx1 = x + dx[i][0]
            ny1 = y + dy[i][0]
            nx2 = x + dx[i][1]
            ny2 = y + dy[i][1]
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if not visited[nx1][ny1] and not visited[nx2][ny2]:
                    visited[nx1][ny1] = 1
                    visited[nx2][ny2] = 1
                    visited[x][y] = 1
                    dfs(idx + 1, cnt + graph[x][y] * 2 + graph[nx1][ny1] + graph[nx2][ny2])
                    #다음 좌표 설정
                    visited[nx1][ny1] = 0
                    visited[nx2][ny2] = 0
                    visited[x][y] = 0
    dfs(idx + 1, cnt )


n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0
visited = [[0] * m for _ in range(n)]

dfs(0, 0)

print(ans)
