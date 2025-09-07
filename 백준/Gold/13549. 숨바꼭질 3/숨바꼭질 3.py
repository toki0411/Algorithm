from collections import deque
n, k = map(int, input().split())
visited = [-1] * (100001)
visited[n] = 0
def bfs(v):
    q = deque([v])
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        if 0 <= x-1 <= 100000 and visited[x-1]==-1:
            visited[x - 1] = visited[x] + 1
            q.append(x-1)
        if 0 < x*2 <= 100000 and visited[x*2]==-1:
            visited[x * 2] = visited[x]
            q.appendleft(x*2)
        if 0 <= x+1 <= 100000 and visited[x+1]==-1:
            visited[x + 1] = visited[x] + 1
            q.append(x+1)
bfs(n)
