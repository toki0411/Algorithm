def dfs(V):
    x, y, command = V
    global cnt
    if x == n - 1 and y == n - 1:
        cnt += 1
        return

    # 대각선 (현재 가로, 세로, 대각선이든 모든 경우에 가능)
    if x + 1 < n and y + 1 < n and graph[x + 1][y + 1] == 0 and graph[x + 1][y] == 0 and graph[x][y + 1] == 0:  # 대각선
        dfs((x + 1, y + 1, 2))

    if command == 0 or command == 2:  # 가로
        if y + 1 < n and graph[x][y + 1] == 0:  # 가로
            dfs((x, y + 1, 0))

    if command == 1 or command == 2:  # 세로
        if x + 1 < n and graph[x + 1][y] == 0:  # 세로
            dfs((x + 1, y, 1))

n = int(input())
graph = [[] for _ in range(n)]
cnt = 0
# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))
dfs((0, 1, 0))
print(cnt)
