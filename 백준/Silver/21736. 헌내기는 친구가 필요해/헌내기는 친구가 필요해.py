from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [0,0,1,-1]
dy = [-1,1,0,0]

q = deque();
x =0; y = 0
ans = 0
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            x = i;
            y = j;
            q.append((x,y))
            visited[x][y] = 1
            break;

while q:
    a = q.popleft()
    x = a[0]
    y = a[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < m and not visited[nx][ny]:
            if graph[nx][ny] == 'P':
                ans += 1
                q.append((nx,ny))
                visited[nx][ny] = 1
            elif graph[nx][ny] == 'O':
                q.append((nx,ny))
                visited[nx][ny] = 1

print(ans if ans != 0 else "TT")