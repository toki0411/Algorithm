T = int(input())
for t in range(T):
    n, d = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    graph2 = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        arr = list(map(int, input().split()))
        for j in range(n):
            graph[i][j+1] = arr[j]
            graph2[i][j+1] = arr[j]
    cnt = abs(d) // 45
    for c in range(cnt):
        mid = int((n + 1) / 2)
        if d > 0:  #양수이면 시계
            for i in range(1,n+1): #주대각선
                graph[i][mid] = graph2[i][i]
            for i in range(1,n+1): #가운데열
                graph[i][n-i+1] = graph2[i][mid]
            for i in range(1,n+1): #부대각선
                graph[mid][n-i+1] = graph2[i][n-i+1]
            for i in range(1,n+1): #가운데행
                graph[i][i] = graph2[mid][i]
        else:  #음수이면 반시계
            for i in range(1,n+1): #주대각선
                graph[mid][i] = graph2[i][i]
            for i in range(1,n+1): #가운데열
                graph[i][i] = graph2[i][mid]
            for i in range(1,n+1): #부대각선
                graph[i][mid] = graph2[i][n-i+1]
            for i in range(1,n+1): #가운데행
                graph[n-i+1][i] = graph2[mid][i]
        for i in range(1,n+1):
            for j in range(1, n+1):
                graph2[i][j] = graph[i][j]


    for i in range(1,n+1):
        for j in range(1,n+1):
            print(graph[i][j], end = " ")

        print()