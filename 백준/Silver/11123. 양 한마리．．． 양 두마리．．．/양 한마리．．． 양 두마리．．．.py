from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for t in range(T):
    H, W = map(int, input().split())

    grid = [list(input()) for _ in range(H)]

    q = deque()
    visited = [[0] * W for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                q.append([i,j])
                visited[i][j] = 1
                cnt +=1
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >= H or ny >= W: continue
                        if grid[nx][ny] == '#' and not visited[nx][ny]:
                            q.append([nx, ny])
                            visited[nx][ny] =  1

    print(cnt)