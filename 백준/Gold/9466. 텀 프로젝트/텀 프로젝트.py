import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)
def dfs(now, s):
    visited.add(now)
    s.append(graph[now])
    if graph[now] not in visited:
        dfs(graph[now], s)

T = int(input())
for tc in range(T):
    ans = 0
    n = int(input())
    st = list(map(int, input().split()))
    graph = [0] * (n + 1)
    visited = set()
    for i in range(n):
        graph[i + 1] = st[i]


    for i in range(1, n + 1):
        if i not in visited:
            path = [i]
            dfs(i, path)
            start = -1
            for j in range(len(path)-1):
                if path[j] == path[-1] :
                    start = j
            # print(i, start)
            if start != -1:
                ans += len(path) - start - 1

    print(n - ans)