from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def openDoorBfs(x, y):
    ans = []
    q = deque([(x, y)])
    # ans.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = 1
                    ans.append([nx, ny])
                    q.append([nx, ny])
    return ans


n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
key = False
while True:
    visited = [[0] * (n + 1) for _ in range(n)];
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                country = openDoorBfs(i, j)
                if len(country) > 0:
                    flag = True
                    people = sum([graph[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        graph[x][y] = people

    if not flag:
        print(cnt);
        break
    cnt += 1
