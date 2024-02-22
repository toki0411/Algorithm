import sys

input = sys.stdin.readline
from collections import deque

sys.setrecursionlimit(10 ** 6)  # 자기 호출 개수 제한
MAX = sys.maxsize

N = int(input())
population = list(map(int, input().split()))
population.insert(0, 0)
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    for k in range(1, arr[0] + 1):
        graph[i].append(arr[k])


def bfs(arr):
    q = deque()
    visited = [False] * (N + 1)
    q.append(arr[0])
    visited[arr[0]] = True
    value = 0
    count = 1
    while q:
        V = q.popleft()
        value += population[V]
        for i in graph[V]:
            if not visited[i] and i in arr:
                q.append(i)
                count += 1
                visited[i] = True
    if count == len(arr):
        return value

def dfs(n, cnt):
    global result
    if cnt == n:
        a, b = [], []
        for i in range(1, N + 1):
            if visited[i]:
                a.append(i)
            else:
                b.append(i)
        x, y = bfs(a), bfs(b)
        if x and y:
            result = min(result, abs(x - y))
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            dfs(n, cnt + 1)
            visited[i] = False

result = MAX
for i in range(1, N // 2 + 1):  # 왜 N/2 ?일까?
    visited = [False] * (N + 1)
    dfs(i, 0)

if result == MAX:
    print(-1)
else:
    print(result)
