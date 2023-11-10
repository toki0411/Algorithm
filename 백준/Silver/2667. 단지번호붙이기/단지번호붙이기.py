from collections import deque
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
ans = 0; cnt_arr = []
def bfs(x, y):
    cnt = 1
    q = deque([(x,y)])
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                graph[nx][ny] = 0
                cnt += 1
                q.append([nx, ny])
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt_arr.append(bfs(i,j))
            ans += 1
print(ans)
cnt_arr.sort()
for i in cnt_arr:
    print(i)
