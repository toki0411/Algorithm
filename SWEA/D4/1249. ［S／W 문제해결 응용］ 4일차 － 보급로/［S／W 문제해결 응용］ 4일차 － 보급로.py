import heapq
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]

    visited = [[1e8] * n for _ in range(n)]
    hq = []
    heapq.heappush(hq,[0,0,0])
    while hq:
        cost,x,y = heapq.heappop(hq)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]==1e8:
                new_cost = cost + graph[nx][ny]
                visited[nx][ny] = new_cost
                heapq.heappush(hq, [new_cost,nx, ny])


    print('#{} {}'.format(tc, visited[n-1][n-1]))
