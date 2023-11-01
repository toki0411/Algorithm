t = int(input())

for t_ in range(1,t+1):
    n = int(input())
    ans = 0
    graph = [list(map(int,input()))for _ in range(n)]
    ans += sum(graph[n//2])

    for i in range(n//2):
        for j in range(n//2-i, n//2+1+i):
            ans+= graph[i][j]
    idx = n//2 - 1
    for i in range(n//2+1, n):
        for j in range(n//2-idx, n//2+1+idx):
            ans+= graph[i][j]
        idx -= 1

    print('#{} {}'.format(t_, ans))
