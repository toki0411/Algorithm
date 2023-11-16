from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x, y):
    q = deque([(x, y)])
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[x][y] +1 == graph[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt

t = int(input())
for tc in range(1, t+1):
    max_val = 0
    ans = []
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            visited = [[0] * n for _ in range(n)]
            tmp = bfs(i,j)
            if tmp == max_val:
                ans.append(graph[i][j])
            elif tmp > max_val:
                ans.clear()
                max_val = tmp
                ans.append(graph[i][j])
    ans.sort()
    print('#{} {} {}'.format(tc, ans[0], max_val))
