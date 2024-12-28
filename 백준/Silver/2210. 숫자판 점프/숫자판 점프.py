s = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(cnt, str, x, y):
    if cnt == 6:
        tmp = ''.join(str)
        if tmp not in s:
            s.add(tmp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
            continue
        dfs(cnt + 1, str + [graph[nx][ny]], nx, ny)

graph = [list(input().split()) for _ in range(5)]
for i in range(5):
    for j in range(5):
        dfs(0, [], i, j)
print(len(s))