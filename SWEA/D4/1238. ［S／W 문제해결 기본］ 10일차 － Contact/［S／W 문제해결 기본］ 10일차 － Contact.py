from collections import deque

for tc in range(1, 11):
    n, start = map(int, input().split())
    data = list(map(int, input().split()))
    graph = [[] for _ in range(101)];
    ans = 0
    for i in range(0, len(data), 2):
        a, b = data[i], data[i + 1]
        if b not in graph[a]:
            graph[a].append(b)
    visited = [0] * 101
    q = deque([(start,0)])
    visited[start] = 0

    while q:
        x, cnt = q.popleft()

        for i in graph[x]:
            if not visited[i]:
                visited[i] = cnt+1
                q.append([i,cnt+1])
    max_val = max(visited)

    for i in range(101):
        if visited[i] == max_val:
            ans = max(i, ans)
    print('#{} {}'.format(tc, ans))
