def dfs(depth, k, start):
    global ans
    if depth == k:
        st= 0 ; link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    st += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        ans = min(abs(st - link), ans)
        return
    for i in range(start, n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, k, i + 1)
            visited[i] = 0

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
num = [i for i in range(n)]
ans = 1e9
for i in range(n):
    visited = [0] * n
    dfs(0,i,0)

print(ans)