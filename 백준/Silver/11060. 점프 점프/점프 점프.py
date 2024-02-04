from collections import deque

n = int(input())
arr = list(map(int, input().split()))
q = deque();
visited = [0] * n
q.append((0, 0))
visited[0] = 1

while q:
    idx, cnt = q.popleft()
    if idx==n-1:
        print(cnt)
        exit(0)
    for i in range(1, arr[idx] + 1):
        if idx + i <= n-1 and not visited[idx+i]:
            visited[idx+i] = 1
            q.append((idx + i, cnt + 1))
print(-1)