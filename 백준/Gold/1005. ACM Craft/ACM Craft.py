from collections import deque

t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	cost = list(map(int, input().split()))
	graph = [[] for _ in range(n+1)]
	indegree = [0] * (n+1)
	dp = [0] * (n+1)
	for l in range(k):
		a, b = map(int, input().split())
		graph[a].append(b)
		indegree[b] += 1
	w = int(input())

	q = deque()
	for i in range(1, n+1):
		if indegree[i] == 0:
			q.append(i)
			dp[i] = cost[i-1]
	while q:
		tmp = q.popleft()
		for i in graph[tmp]:
			indegree[i] -= 1
			dp[i] = max(dp[i], dp[tmp] + cost[i-1])
			if indegree[i] == 0:
				q.append(i)

	print(dp[w])