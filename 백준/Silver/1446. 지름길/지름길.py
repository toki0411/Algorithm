def dfs(now, dis):
    global ans
    if now == D:
        ans = min(dis, ans)
        return
    if now > D:
        return
    for g in graph[now]:
        d, l = g[0], g[1]
        dfs(d, dis + l)
    dfs(now + 1, dis + 1)

N, D = map(int, input().split())
ans = 1e9
graph = [[] for _ in range(10000)]
for _ in range(N):
    s, d, l = map(int, input().split())
    graph[s].append([d,l])

dfs(0,0)
print(ans)