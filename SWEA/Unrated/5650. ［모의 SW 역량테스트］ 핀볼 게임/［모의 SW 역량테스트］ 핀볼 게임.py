
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
wall = [1, 0, 3, 2]
def simulate(x, y, k):
    nx = x
    ny = y
    key = False
    d = k
    score = 0
    while True:
        # print(nx, ny, d)

        if nx < 0 or ny < 0 or nx >= n or ny >= n:  # 벽
            nx -= dx[d]
            ny -= dy[d]
            d = wall[d]
            score += 1
        if (graph[nx][ny] == -1) or (nx == x and ny == y) and key:  #블랙홀
            break
        elif graph[nx][ny] >=1 and graph[nx][ny] <=5: #블록
            block = graph[nx][ny]
            if block == 1 :
                if d == 1:
                    d = 3
                elif d == 2:
                    d = 0
                else:  # 5
                    d = wall[d]
            elif block == 2 :
                if d == 0:
                    d = 3
                elif d == 2:
                    d = 1
                else:  # 5
                    d = wall[d]
            elif block == 3 :
                if d == 0:
                    d = 2
                elif d == 3:
                    d = 1
                else:  # 5
                    d = wall[d]
            elif block == 4 :
                if d == 1:
                    d = 2
                elif d == 3:
                    d = 0
                else:  # 5
                    d = wall[d]
            else:  #5
                d = wall[d]
            score+=1
        elif graph[nx][ny] >=6 and graph[nx][ny] <=10: #웜홀
            holeNum = graph[nx][ny]
            otherHole = wormhole[holeNum]
            # print(otherHole)
            for l in range(len(otherHole)):
                # print(otherHole[l])
                if (nx,ny) == otherHole[l] : continue
                else:
                    nx = otherHole[l][0]
                    ny = otherHole[l][1]
                    break
        # print(nx, ny)
        nx += dx[d]
        ny += dy[d]

        key = True
    return score

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    ans = 0
    graph = [list(map(int, input().split())) for _ in range(n)]
    wormhole = [[] for _ in range(11)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] >=6 and graph[i][j] <=10:
                wormhole[graph[i][j]].append((i,j))
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                for k in range(4):
                    val = simulate(i, j, k)
                    ans = max(ans, val)
                    # print(i, j, val)
    print('#{} {}'.format(tc, ans))
