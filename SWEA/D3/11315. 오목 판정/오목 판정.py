t = int(input())
def dfs(level, x, y, dir):
    global key
    if level >= 4:
        key = True
        return
    if x+1 < n and graph[x+1][y] == 'o': # 1
        if level == 0:
            dfs(level + 1, x+1, y, 1)
        elif dir == 1:
            dfs(level + 1, x + 1, y, 1)
    if y+1 < n and graph[x][y+1] == 'o': # 2
        if level == 0:
            dfs(level + 1, x, y+1, 2)
        elif dir == 2:
            dfs(level + 1, x, y + 1, 2)
    if x+1 < n and y+1 < n and graph[x+1][y+1] == 'o': # 3
        if level == 0:
            dfs(level + 1, x+1,y+1, 3 )
        elif dir == 3:
            dfs(level + 1, x + 1, y + 1, 3)
    if x+1 < n and y-1 >= 0 and graph[x+1][y-1]=='o': # 4
        if level == 0:
            dfs(level + 1, x+1, y-1 , 4)
        elif dir == 4:
            dfs(level + 1, x + 1, y - 1, 4)

for tc in range(1, t + 1):
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    key = False
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'o':
                dfs(0, i, j, 0)
            if key:
                break
        if key:
            break
    if key:
        print('#{} {}'.format(tc, "YES"))
    else:
        print('#{} {}'.format(tc, "NO"))
