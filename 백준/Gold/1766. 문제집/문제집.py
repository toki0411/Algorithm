import heapq
n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
pq = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)
answer = []
while pq:
    current = heapq.heappop(pq)
    answer.append(current)
    for i in graph[current]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(pq, i)
print(*answer)