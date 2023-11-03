for tc in range(1, 11):
    ans = 0
    dump = int(input())
    graph = list(map(int, input().split()))
    max_val = min_val = 0
    for i in range(dump):
        if abs(min(graph) - max(graph)) <= 1:
            break
        min_idx = graph.index(min(graph))
        max_idx = graph.index(max(graph))
        graph[min_idx] +=1
        graph[max_idx] -=1

    ans = abs(min(graph) - max(graph))
    print('#{} {}'.format(tc, ans));
