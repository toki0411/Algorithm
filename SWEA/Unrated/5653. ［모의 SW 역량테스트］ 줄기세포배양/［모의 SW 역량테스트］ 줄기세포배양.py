from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

T= int(input())
for tc in range(1, T+1):
    s = set()
    germ = []
    N, M, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                germ.append((i, j, graph[i][j], graph[i][j]))
                s.add((i, j))

    q = deque()
    for time in range(1, K+1):
        # 활성화된 세포들 4방 증식
        breeding = []
        while q:
            g = q.popleft()
            x, y, k, o = g[0], g[1], g[2], g[3]
            for i in range(4):  # 무조건 증식하면 안 됨. 이미 세포가 있는 경우는 빼야함
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx, ny) not in s:
                    breeding.append([nx, ny, time + o , o])
        breeding.sort(key=lambda x: (x[0], x[1], -x[2]))  # 생명력 수치가 높은 순 정렬

        # 동시에 번식하려는 경우, 생명력 수치가 높은 줄기 세포를 살림
        i = 0
        while i < len(breeding) - 1:
            x, y = breeding[i][0], breeding[i][1]
            mx, my = breeding[i + 1][0], breeding[i + 1][1]
            if x == mx and y == my:
                breeding.pop(i + 1)
            else:
                i += 1

        # 증식된 세포들을 germ에 추가
        for i in range(len(breeding)):
            germ.append(breeding[i])
            s.add((breeding[i][0], breeding[i][1]))

        i = 0
        while i < len(germ):
            if germ[i][2] == time: #활성화된 세포만 큐에 넣음
                q.append(germ[i])
                i += 1
            elif germ[i][2] < time and time-germ[i][2] == germ[i][3]:
                germ.pop(i)
            else:
                i += 1
        # print(time, germ, s, q)
    print("#{} {}".format(tc, len(germ)))