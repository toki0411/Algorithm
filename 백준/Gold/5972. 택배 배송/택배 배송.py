import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
pq = []
visited = [1e9] * (n+1)
heapq.heappush(pq, [0, 1])
visited[1] = 0
while pq:
    cost, now = heapq.heappop(pq)
    if visited[now] < cost:
        continue
    for g in graph[now]:
        next, dis = g[0], g[1]
        if cost + dis < visited[next]:
            visited[next] = cost + dis
            heapq.heappush(pq, [cost + dis, next])
print(visited[n])