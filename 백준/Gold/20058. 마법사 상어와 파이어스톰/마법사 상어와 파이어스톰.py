from collections import deque

n, q = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def rotate(x, y, c):
    graph2 = []
    for i in range(x, x + 2 ** c):
        arr = []
        for j in range(y, y + 2 ** c):
            arr.append(graph[i][j])
        graph2.append(arr)
    reversed_graph = graph2[::-1]
    rotated = list(zip(*reversed_graph))

    r = 0
    for i in range(x, x + 2 ** c):
        b = 0
        for j in range(y, y + 2 ** c):
            graph[i][j] = rotated[r][b]
            b += 1
        r += 1

def melt():  #녹을 얼음
    for i in range(len(melting)):
        x, y = melting[i]
        graph[x][y] -= 1

def bfs(xx, yy):
    ice = 1
    q = deque()
    q.append((xx,yy))
    visited[xx][yy] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= limit or ny >= limit:
                continue
            if graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                ice +=1

    return ice

graph = [list(map(int, input().split())) for _ in range(2 ** n)]
cmd = list(map(int, input().split()))
totalIce = 0
bigIce = 0
limit = 2**n
for c in cmd:
    if c != 0:
        for i in range(0, limit, 2**c):
            for j in range(0, limit, 2**c):
                rotate(i, j, c)

    melting = []
    for x in range(0, limit):
        for y in range(0, limit):
            cnt = 0
            if graph[x][y] <= 0: continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= limit or ny >= limit:
                    continue
                if graph[nx][ny] > 0 :
                    cnt += 1
            if cnt < 3:
                melting.append((x, y))
    melt()
for i in range(0, limit):
    totalIce += sum(graph[i])
visited = [[0] * limit for _ in range(limit)]
# print(graph)
for i in range(limit):
    for j in range(limit):
        if not visited[i][j] and graph[i][j]:
            bigIce = max(bfs(i, j), bigIce)


print(totalIce)
print(bigIce)