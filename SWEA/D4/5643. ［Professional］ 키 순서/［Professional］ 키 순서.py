from collections import deque

T = int(input())

def bfs(arr, idx):
    visited = [0] * (N + 1)
    q = deque()
    q.append(idx)
    while q:
        x = q.popleft()
        for i in range(len(arr[x])):
            if not visited[arr[x][i]]:
                q.append((arr[x][i]))
                visited[arr[x][i]] = 1
    return visited.count(1)

for tc in range(1, T + 1):
    total = 0
    N = int(input())
    M = int(input())

    adj_out = [[] for _ in range(N + 1)]
    adj_in = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        adj_out[a].append(b)
        adj_in[b].append(a)

    for idx in range(1,N+1):
        if bfs(adj_out, idx) + bfs(adj_in, idx) == N-1:
            total += 1

    print("#{} {}".format(tc, total))
