import sys
input = sys.stdin.readline
def play():  # 플레이 시켜서 i번 세로선의 결과가 i인지 체크
    for start in range(N):  # 1번 세로선, 2번 세로선, 3번 세로선
        y = start
        for j in range(H):  # 가로선
            if graph[j][y]:
                y = y + 1
            elif y - 1 >= 0 and graph[j][y - 1]:
                y = y - 1
        if y != start:
            return False
    return True


def dfs(line, x, y):
    global ans
    if line > 3 or line > ans:
        return;
    if play():
        ans = min(line, ans)
        return
    for i in range(x, H):  # 세로
        if i == x:
            now = y  # 이전에 봤던 곳 이어서 보기 위해
        else:
            now = 0
        for j in range(now, N - 1):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(line + 1, i, j + 2)
                graph[i][j] = 0

N, M, H = map(int, input().split())  # 세로, 가로, 세로선마다 놓을 수 있는 가로선 개수 H
if M == 0:
    print(0)
    exit(0)
graph = [[0] * N for _ in range(H)]
ans = 4
lineCnt = [0] * M
for i in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
dfs(0, 0, 0)
print(ans if ans < 4 else -1)