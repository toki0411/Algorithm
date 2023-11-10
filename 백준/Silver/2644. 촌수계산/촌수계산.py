n = int(input())
case_x, case_y = map(int, input().split())
m = int(input())
family = [list(map(int, input().split())) for _ in range(m)]
graph = [ [] for _ in range(n+1) ]; ans = 0
for i in range(m):
    a, b= family[i]
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n+1)
key = False
def dfs(v, target, cnt):
    global ans, key
    if v == target:
        print(cnt)
        key = True
        return cnt
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, target,cnt + 1)
    return cnt
dfs(case_x, case_y, 0)
if not key:
    print(-1)


