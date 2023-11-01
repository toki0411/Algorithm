t = int(input())

for t_ in range(1,t+1):
    n, m = map(int, input().split())
    graph = []; ans = 0
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    for i in range(n-m+1):
        for j in range(n-m+1):
            val = 0
            for k in range(i, i+m):
                for l in range(j, j+m):
                    val += graph[k][l]
            ans = max(ans, val)
    print('#{} {}'.format(t_, ans))
