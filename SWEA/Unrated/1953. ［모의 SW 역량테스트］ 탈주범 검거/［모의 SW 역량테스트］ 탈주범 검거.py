from collections import deque

type_x = [[], [-1,1,0,0], [-1,1], [0,0], [-1,0], [1,0], [1,0], [-1,0]]
type_y = [[], [0,0,1,-1], [0,0], [1,-1], [0,1], [0,1], [0,-1], [0,-1]]


def directionCheck(x, y, target):
    target_x = type_x[target]
    target_y = type_y[target]
    if x == 1 or x == -1:
        nx = -x
        if nx in target_x:
            return True
    elif y == 1 or y == -1:
        ny = -y
        if ny in target_y:
            return True
    return False


def bfs(x,y):
    global ans
    q = deque()
    q.append((x,y,1))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    while q:
        x, y, t = q.popleft()
        type = graph[x][y]
        for i in range(len(type_x[type])):
            nx = x + type_x[type][i]
            ny = y + type_y[type][i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or t > l: continue
            if directionCheck(type_x[type][i], type_y[type][i], graph[nx][ny])and not visited[nx][ny] and graph[nx][ny] != 0 and t+1 <= l:
                q.append((nx, ny, t+1))
                visited[nx][ny] = 1
                ans += 1

T = int(input())
for tc in range(1, T+1):
    ans = 1
    n,m,r,c,l = map(int,input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    bfs(r,c)

    print('#{} {}'.format(tc, ans))