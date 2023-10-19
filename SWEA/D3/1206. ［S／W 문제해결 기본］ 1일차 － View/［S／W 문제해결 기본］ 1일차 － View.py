for t in range(1,11):
    N = int(input()); cnt = 0
    graph = list(map(int, input().split()))
    for i in range(2, N-2):
        left = max(graph[i-1], graph[i-2])
        right = max(graph[i+1], graph[i+2])
        if graph[i] > left and graph[i] > right:
            cnt += graph[i] - max(left, right)
    print('#{}'.format(t), end = '');print(' ', end = '')
    print(cnt)