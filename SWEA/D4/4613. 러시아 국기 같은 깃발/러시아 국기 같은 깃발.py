t = int(input())
for tc in range(1, t + 1):
    n, m = map(int,input().split())
    graph = [list(map(str, input())) for _ in range(n)]
    ans = 1e9
    for i in range(n-2):
        for j in range(i+1, n-1):
            cnt = 0
            for s in range(i+1):
                cnt += graph[s].count('W')
            for s in range(i+1, j+1):
                cnt += graph[s].count('B')
            for s in range(j+1, n):
                cnt += graph[s].count('R')

            ans = min(ans, n*m - cnt)
    print('#{} {}'.format(tc, ans))
