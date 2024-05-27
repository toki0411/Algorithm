import heapq

INF = 10000000000
def dijkstra(x):
	distance[x] = 0
	heapq.heappush(pq, [distance[x], x])
	while pq:
		cur_dis, now = heapq.heappop(pq)
		if distance[now] < cur_dis:  # 예시 : cur_dis가 7이고, now가 3일때 1-2-3 으로 가서 걸린 거리 7보다, 이미 존재하는 1-3으로 간 3이 더 작으면 1-2-3을 보지 않는다.
			continue
		for next, next_dis in graph[now]:
			tmp_dis = distance[now] + next_dis
			if tmp_dis < distance[next]:
				distance[next] = tmp_dis
				heapq.heappush(pq, [tmp_dis, next])

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
pq = []
ans = 0
for _ in range(E):
	a, b, c = map(int, input().split())
	graph[a].append([b, c])
	graph[b].append([a, c])
u, v = map(int, input().split())
distance = [INF for _ in range(N + 1)]
key = True
dijkstra(1)
if distance[u] != INF:
	ans += distance[u]
	distance = [INF for _ in range(N + 1)]
	dijkstra(u)
	if distance[v] != INF:
		ans += distance[v]
		distance = [INF for _ in range(N + 1)]
		dijkstra(v)
		if distance[N] != INF:
			ans += distance[N]
		else:
			key = False
	else:
		key = False
else:
	key = False

ans2 = 0
key2 = True
distance = [INF for _ in range(N + 1)]
dijkstra(1)
if distance[v] != INF:
	ans2 += distance[v]
	distance = [INF for _ in range(N + 1)]
	dijkstra(v)
	if distance[u] != INF:
		ans2 += distance[u]
		distance = [INF for _ in range(N + 1)]
		dijkstra(u)
		if distance[N] != INF:
			ans2 += distance[N]
		else:
			key2 = False
	else:
		key2 = False
else:
	key2 = False
if key == False and key2 == False:
	print(-1)
else:
	print(min(ans, ans2))