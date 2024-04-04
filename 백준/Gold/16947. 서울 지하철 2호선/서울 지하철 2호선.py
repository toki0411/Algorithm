from collections import deque
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, start, cnt, arr):
    global key, circle
    if x == start and cnt >= 3:
        key = True
        circle+=arr
        return
    if not key:
        for nx in graph[x]:
            if not visited[x][nx]:
                visited[x][nx] = 1
                visited[nx][x] = 1
                dfs(nx, start, cnt + 1, arr + [nx])
                visited[x][nx] = 0
                visited[nx][x] = 0
def bfs():
    q = deque()
    for c in circle:
        q.append(c)
        visited[c] = 1
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = 1
                ans[nx] = ans[x] + 1
                q.append(nx)

N = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

circle = []  # 순환선
line = [0] * (N + 1)  # 순환선은 1로 지선은 0로
ans = [0] * (N + 1)

# 순환선에 해당하는 노드들을 찾는다.
visited = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    key = False
    dfs(i, i, 0, [])
    if key:  #순환선
        break

# 순환선이 아니라면, bfs를 돌려서 최단경로를 찾는다.
visited = [0] * (N + 1)
bfs()
for i in range(1, N + 1):
    print(ans[i], end=" ")