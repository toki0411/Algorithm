import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[0] * 4 for _ in range(4)]
ans = 0
for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(0, 8, 2):
        a = arr[j]  # 물고기의 번호
        b = arr[j + 1] -1 # 물고기의 방향
        graph[i][j // 2] = [a, b]

def dfs(x, y, score, graph):
    global ans
    score += graph[x][y][0]
    ans = max(score, ans)
    graph[x][y][0] = 0

    # 물고기들이 이동한다.
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for i in range(4):
            for j in range(4):
                if graph[i][j][0] == f:
                    f_x = i; f_y = j
                    break
        if f_x == -1 and f_y == -1:continue
        dir = graph[f_x][f_y][1]

        # 방향 결정 - 이동가능할 때까지 반시계 방향으로 45도씩 최대 한 바퀴까지 회전
        for i in range(8):
            ndir = (dir + i) % 8
            nx = f_x + dx[ndir]
            ny = f_y + dy[ndir]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == x and ny == y):
                continue
            graph[f_x][f_y][1] = ndir
            graph[f_x][f_y], graph[nx][ny] = graph[nx][ny], graph[f_x][f_y]
            break

    # 상어가 이동한다.
    sDir = graph[x][y][1]
    for i in range(1, 5):
        nx = x + dx[sDir] * i
        ny = y + dy[sDir] * i
        if (0 <= nx < 4 and 0 <= ny < 4) and graph[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(graph))
dfs(0, 0, 0, graph)
print(ans)