import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def diffusion():
    graph2 = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if graph[x][y] > 0:  # 미세먼지가 있는 경우
                tmp = 0
                for i in range(4):  # 4방면으로 퍼짐
                    ax = x + dx[i]
                    ay = y + dy[i]
                    if 0 <= ax < r and 0 <= ay < c:  # board 에서 벗어나지 않는 범위일 경우만
                        if graph[ax][ay] != -1:  # 공기청정기가 아닌 위치만 확산
                            graph2[ax][ay] += graph[x][y] // 5
                            tmp += graph[x][y] // 5
                graph[x][y] -= tmp
    for x in range(r):
        for y in range(c):
            graph[x][y] += graph2[x][y]
def rotation():
    def right():
        d = 1 #오른쪽 방향으로 시작
        before = 0
        x = puri_x1; y = 1
        while True:

            nx = x + dx[d]
            ny = y + dy[d]
            if nx == r or ny == c or nx == -1 or ny == -1:
                d = (d-1)%4
                continue
            if x == puri_x1 and y == 0:  # 공기 청정기가 있는 곳으로 돌아왔음
                break
            graph[x][y], before = before, graph[x][y]
            x, y = nx, ny

    def left():
        d = 1
        before = 0
        x = puri_x2; y = 1
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            if nx == r or ny ==c or nx == -1 or ny == -1:
                d = (d+1) % 4
                continue
            if x == puri_x2 and y == 0: # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            graph[x][y], before = before, graph[x][y]
            x, y = nx, ny
    right()
    left()

#공기 청정기 위치 찾기
puri_x1 = 0
puri_x2 = 0
for i in range(r):
    if graph[i][0] == -1:
        puri_x1 = i
        puri_x2 = i+1
        break

for _ in range(t):
    diffusion()  # 미세먼지 확산
    rotation()  # 공기청정기 작동

ans = 2
for i in range(r):
    ans += sum(graph[i])
print(ans)
