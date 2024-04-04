from collections import deque
dx = [-1,1,0,0]
dy = [0,0,1,-1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    visited = [[100000000] * N for _ in range(N)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            if visited[nx][ny] > visited[x][y] + graph[nx][ny]:
                visited[nx][ny] = visited[x][y] + graph[nx][ny]
                q.append((nx, ny))

    print("#{} {}".format(tc, visited[N-1][N-1]))