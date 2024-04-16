import heapq
T = int(input())

for tc in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for dc in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([s,a])
    visited = [1e8] * (n+1)

    visited[c] = 0


    pq = []
    heapq.heappush(pq, c)
    while pq:
        x = heapq.heappop(pq)
        for node in graph[x]:
            nx = node[1]; time = node[0]
            if visited[nx] > visited[x] + time:
                visited[nx] = visited[x] + time
                heapq.heappush(pq, nx)
    cnt = 0
    timeCnt = 0
    for i in range(1, n+1):
        if visited[i] != 1e8:
            cnt += 1
            timeCnt = max(visited[i], timeCnt)
    print(cnt, timeCnt)