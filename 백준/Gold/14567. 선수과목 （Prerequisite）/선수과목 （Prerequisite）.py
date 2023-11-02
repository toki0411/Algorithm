from collections import deque
v,e = map(int, input().split())
graph = [[]for _ in range(v+1)]
indegree = [0] * (v+1)
for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1
ans = [0] * (v+1)

q = deque()
for i in range(1, v+1):
    if indegree[i] == 0:
        q.append([i,1])
while q:
    now, idx = q.popleft()
    ans[now] = idx
    for g in graph[now]:
        indegree[g]-=1
        if indegree[g] == 0:
            q.append([g,idx+1])
for i in range(1,len(ans)):
    print(ans[i], end = ' ')


