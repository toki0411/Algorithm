M, N = map(int, input().split())  # 가로 세로
R, C = map(int, input().split())
robot = [[0]]
cmdList = []
leftDir = [1, 2, 3, 0]
rightDir = [3, 0, 1, 2]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
graph = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(R):
    x, y, d = input().split()
    if d == 'E':
        d = 0
    elif d == 'N':
        d = 1
    elif d == 'W':
        d = 2
    else:
        d = 3
    robot.append([int(x), int(y), d])
    graph[int(x)][int(y)] = i+1
for i in range(C):
    n, d, c = input().split()
    cmdList.append([int(n), d, int(c)])

for command in cmdList:
    robotIdx, cmd, num = command[0], command[1], command[2]
    x, y, dir = robot[robotIdx][0], robot[robotIdx][1], robot[robotIdx][2]
    if cmd == 'F':
        nx = x
        ny = y
        graph[x][y] = 0
        for n in range(num):
            nx = x + dx[dir]
            ny = y + dy[dir]
            # 벽이랑 충돌하는지 체크
            if nx <= 0 or ny <= 0 or nx > M or ny > N:
                print("Robot", robotIdx, "crashes into the wall")
                exit(0)

            # 다른 로봇이랑 충돌하는지 체크
            if graph[nx][ny] != 0:
                print("Robot", robotIdx, "crashes into robot", graph[nx][ny])
                exit(0)

            # graph에 새 로봇 위치 추가
            graph[nx][ny] = robotIdx
            graph[x][y] = 0
            robot[robotIdx] = [nx, ny, dir]
            x = nx
            y = ny
            # print(graph)
        continue
    elif cmd == 'L':
        for n in range(num):
            dir = leftDir[dir]
            robot[robotIdx] = [x, y, dir]
    else:
        for n in range(num):
            dir = rightDir[dir]
            robot[robotIdx] = [x, y, dir]

print("OK")