from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())  # 0 북쪽, 1 동쪽, 2 남쪽, 3 서쪽
graph = [list(map(int, input().split())) for _ in range(n)]
dir = [[(0, -1), (1, 0), (0, 1), (-1, 0), (3, 2, 1, 0)], [(-1, 0), (0, -1), (1, 0), (0, 1), (0, 3, 2, 1)],
       [(0, 1), (-1, 0), (0, -1), (1, 0), (1, 0, 3, 2)], [(1, 0), (0, 1), (-1, 0), (0, -1), (2, 1, 0, 3)]]
back = [[1, 0], [0, -1], [-1, 0], [0, 1]]
q = deque([(r, c, d)])
while q:
    arr = q.popleft()
    x, y, d = arr[0], arr[1], arr[2]
    if graph[x][y] == 0:
        graph[x][y] = 2

    key = False
    for i in range(4):
        nx = x + dir[d][i][0]
        ny = y + dir[d][i][1]
        nd = dir[d][4][i]
        if 0 < nx <= n and 0 < ny <= m and graph[nx][ny] == 0:
            q.append([nx, ny, nd])
            key = True
            break

    if not key:  # 후진
        nx = x + back[d][0]
        ny = y + back[d][1]
        if 0 < nx <= n and 0 < ny <= m and (graph[nx][ny] == 0 or graph[nx][ny] == 2):
            q.append([nx, ny, d])
        else:
            break
ans = 0

for g in graph:
    ans += g.count(2)
print(ans)

# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
# 1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
# 1. 반시계 방향으로 90도 회전한다.
# 2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 3.1번으로 돌아간다.
