import copy

n, m = map(int, input().split())
dir = [ [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],]
graph = [list(map(int, input().split())) for _ in range(n)]
cctv = []
# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def monitoring(graph, d, x, y):
    for i in d:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break;
            if graph[nx][ny] == 6:
                break;
            elif graph[nx][ny] == 0:
                graph[nx][ny] = -1  # 감시 했음

def dfs(depth, graph):
    global min_val;
    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += graph[i].count(0)
        min_val = min(min_val, cnt)
        return;

    temp = copy.deepcopy(graph)
    cctv_num, x, y = cctv[depth]
    for d in dir[cctv_num]:
        monitoring(temp, d, x, y)
        dfs(depth + 1, temp)
        temp = copy.deepcopy(graph)

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctv.append([graph[i][j], i, j])

min_val = int(1e9)
dfs(0, graph)
print(min_val)