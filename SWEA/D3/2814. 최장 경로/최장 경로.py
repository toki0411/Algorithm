t = int(input())
def dfs(x, level):
    global ans
    if level > ans :
        ans = level
        return
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, level+1)
            visited[i] = 0

for tc in range(1, t + 1):
    n,m = map(int,input().split())
    if m == 0:
        print('#{} {}'.format(tc, 0))
    else:
        v = [list(map(int, input().split())) for _ in range(m)]
        graph = [[] for i in range(n+1)]
        ans = -1
        for i in range(m):
            a,b = v[i]
            graph[a].append(b)
            graph[b].append(a)
        for i in range(1,n+1):
            visited = [0] * (n+1)
            dfs(i, 0)
        print('#{} {}'.format(tc, ans))



