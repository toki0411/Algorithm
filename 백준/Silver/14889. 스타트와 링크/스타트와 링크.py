n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
ans = 1e9+1
def dfs(level, idx):
    global ans
    if level == n//2:
        start = link =  0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j] :
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        ans = min(abs(start-link), ans)
        return
    for i in range(idx, n):
       if not visited[i]:
            visited[i] = 1
            dfs(level+1, i+1)
            visited[i] = 0

dfs(0, 0)
print(ans)