def dfs(num, cnt):
    global ans
    if num == k:
        ans = min(cnt, ans)
        return
    if not visited[graph[num]]:
        visited[graph[num]] = 1
        dfs(graph[num], cnt + 1)

n, k = map(int, input().split())
ans = 1e9
graph = [0] * (n+1)
visited = [0] * (n+1)
for i in range(n):
    x = int(input())
    graph[i] = x
visited[0] = 1
dfs(graph[0], 1)
if ans == 1e9:
    print(-1)
else:
    print(ans)