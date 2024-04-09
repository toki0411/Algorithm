from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def findGuest(tx, ty, f):  # 최단거리로 이동
    q = deque()
    q.append((tx, ty, f))
    visited[tx][ty] = 0
    while q:
        x, y, f = q.popleft()
        if f <= 0: continue #연료 없으면 중단
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            if graph[nx][ny] == 0 and visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny, f - 1))
            # elif graph[nx][ny] == 2 and visited[nx][ny] > visited[x][y] + 1:
            #     visited[nx][ny] = visited[x][y] + 1


N, M, fuel = map(int, input().split())  # 그래프 크기, 사람 명수, 초기 연료
graph = [list((map(int, input().split()))) for _ in range(N)]
tx, ty = map(int, input().split());
tx -= 1; ty -= 1
guest = []
for _ in range(M):
    a, b, c, d = map(int, input().split())
    guest.append([a - 1, b - 1, c - 1, d - 1])
    # graph[a-1][b-1] = 2  # 손님 체크

for _ in range(M):
    # 최단경로로 손님에게 이동. 이동중에 연료가 다 떨어진 경우 -1을 출력한다.
    visited = [[1e8] * N for _ in range(N)]
    findGuest(tx, ty, fuel)
    minDis = 1e9
    # 손님을 고름
    for i in range(len(guest)):
        dis = visited[guest[i][0]][guest[i][1]]
        if dis == 1e8: # 연료 부족으로 못갔을 경우
            print(-1)
            exit()
        if dis < minDis:
            minDis = dis
            gx = guest[i][0]
            gy = guest[i][1]
            ex = guest[i][2]
            ey = guest[i][3]
        elif dis == minDis:  # 거리가 같을 경우 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다.
            if guest[i][0] < gx:
                gx = guest[i][0]
                gy = guest[i][1]
                ex = guest[i][2]
                ey = guest[i][3]
            elif guest[i][0] == gx:
                if guest[i][1] < gy:
                    gx = guest[i][0]
                    gy = guest[i][1]
                    ex = guest[i][2]
                    ey = guest[i][3]
    graph[gx][gy] = 0
    guest.remove([gx,gy,ex,ey])
    # print(gx, gy)
    fuel -= visited[gx][gy]
    tx = gx; ty = gy
    visited = [[1e8] * N for _ in range(N)]
    findGuest(tx, ty, fuel)
    if visited[ex][ey] == 1e8:
        print(-1)
        exit()
    fuel -= visited[ex][ey]
    tx = ex; ty = ey;
    # 연료 충전! 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전
    fuel += (visited[ex][ey] * 2)
    # print(fuel)
print(fuel)