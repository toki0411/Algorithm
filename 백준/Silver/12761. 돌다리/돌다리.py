from collections import deque

a, b, n, m = map(int, input().split())

visited = [False] * 100001
dx_1 = [1, -1, a, -a, b, -b]  #더하기
dx_2 = [a, b]  #곱하기

def bfs(x):
    q = deque([x])
    visited[x] = 0
    while q:
        x = q.popleft()
        for i in dx_1:
            nx = x + i
            if 0<= nx < 100001 and not visited[nx]:
                q.append(nx)
                visited[nx] = visited[x] + 1
        for i in dx_2:
            nx = x * i
            if 0<= nx < 100001 and not visited[nx]:
                q.append(nx)
                visited[nx] = visited[x] + 1

bfs(n)
print(visited[m])
