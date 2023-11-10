n = int(input())
m = int(input())
friend = [list(map(int, input().split())) for _ in range(m)]
graph = [ [] for _ in range(n+1) ]; ans = 0

for i in range(m):
    a, b= friend[i]
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n+1)
visited[1] = 1
def dfs(V, cnt):
    global ans
    if cnt == 2:
        return
    for i in graph[V]:
        if not visited[i]:
            visited[i] = 1
        dfs(i, cnt + 1)

dfs(1, 0)
print(visited.count(1)-1)


