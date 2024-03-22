from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]
def bfs(xx, yy, zz):
    q = deque();
    q.append((xx,yy,zz))
    visited = [[[0 for _ in range(l)] for __ in range(c) ] for ___ in range(r)]
    visited[xx][yy][zz] = 0
    while q:
        x, y, z = q.popleft()
        # print(x, y, z)
        if graph[x][y][z] == 'E':
            return visited[x][y][z]
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= r or ny >= c or nz >= l: continue
            if graph[nx][ny][nz] != '#' and not visited[nx][ny][nz]:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                q.append((nx,ny,nz))
    return False
while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0: break
    else:
        graph = [[[0 for ll in range(l)] for _ in range(c)] for __ in range(r)]
        start = 0

        for li in range(l):
            for i in range(r):
                tmp = list(input())
                for j in range(c):
                    graph[i][j][li] = tmp[j]
                    if tmp[j] == 'S':
                        start = [i, j, li]
            input()
        ans = bfs(start[0], start[1], start[2])
        if ans != False:
            print("Escaped in", ans, "minute(s).")
        else:
            print("Trapped!")