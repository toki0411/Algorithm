from collections import deque
n = int(input())
m = int(input())
friend = [list(map(int, input().split())) for _ in range(m)]
graph = [ [] for _ in range(n+1) ]; ans = 0

for i in range(m):
    a, b= friend[i]
    graph[a].append(b)
    graph[b].append(a)
#
visited = [0] * (n+1)
visited[1] = 1
q = deque([(1,0)])
while q:
    v, cnt = q.popleft()
    for i in graph[v]:
        if cnt+1 <= 2 and not visited[i]:
            ans+=1
            visited[i] = 1
            q.append((i, cnt+1))

print(ans)


