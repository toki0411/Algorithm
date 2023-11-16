from _collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y,target):
    q = deque([(x,y)])
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] == target:
                visited[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1
    if cnt == 0:
        return 1
    else:
        return cnt*cnt

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
w_cnt = b_cnt = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                w_cnt += bfs(i,j,'W')
            else:
                b_cnt += bfs(i,j,'B')
print(w_cnt, b_cnt)
