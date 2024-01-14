t = int(input())
for r in range(1,t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for __ in range(n)]
    arr90 = [[0 for _ in range(n)] for _ in range(n)]
    arr180 = [[0 for _ in range(n)] for _ in range(n)]
    arr270 = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            arr90[i][j] = graph[n-1-j][i]
    for i in range(n):
        for j in range(n):
            arr180[i][j] = arr90[n-1-j][i]
    for i in range(n):
        for j in range(n):
            arr270[i][j] = arr180[n-1-j][i]
    print('#{}'.format(r))
    for i in range(n):
        for j in range(n):
            print(arr90[i][j], end='')
        print(' ', end='')
        for j in range(n):
            print(arr180[i][j], end='')
        print(' ', end='')
        for j in range(n):
            print(arr270[i][j], end='')
        print()


