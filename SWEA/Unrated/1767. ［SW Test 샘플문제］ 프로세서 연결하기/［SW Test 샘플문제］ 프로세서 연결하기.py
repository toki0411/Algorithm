dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(coreCnt, lineCnt, t):
    # print(coreCnt, lineCnt, t, visited)
    global maxLine, maxCoreCnt

    # 종료 조건
    if t == len(core):
        # print(coreCnt, lineCnt)
        if coreCnt > maxCoreCnt:
            maxCoreCnt = coreCnt
            maxLine = lineCnt
        elif coreCnt == maxCoreCnt:
            # print(coreCnt, lineCnt)
            maxLine = min(lineCnt, maxLine)
        return

    x = core[t][0];
    y = core[t][1];
    flag = 0
    for i in range(4):
        nx = x + dx[i];
        ny = y + dy[i];
        cnt = 0;
        idx = []
        while nx >= 0 and nx < N and ny < N and ny >= 0:
            if visited[nx][ny]:
                cnt = 0
                break
            idx.append([nx, ny])
            cnt += 1
            nx += dx[i]
            ny += dy[i]

        if cnt > 0:
            flag += 1
            # 그래프 방문처리
            for l in range(cnt):
                mx, my = idx[l][0], idx[l][1]
                visited[mx][my] = 1

            dfs(coreCnt + 1, lineCnt + cnt, t + 1)

            # 복구
            for l in range(cnt):
                mx, my = idx[l][0], idx[l][1]
                visited[mx][my] = 0


    dfs(coreCnt, lineCnt, t + 1)

    # 못가는 경우도 있을 수 있음.


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    core = []
    visited = [[0] * N for _ in range(N)]
    coreCnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                visited[i][j] = 1
                if i == 0 or i == N - 1 or N - 1 == j or j == 0:
                    coreCnt += 1
                else:
                    core.append([i, j])
    maxCoreCnt = coreCnt
    maxLine = 1000000000

    dfs(coreCnt, 0, 0)
    # print(maxCoreCnt, maxLine)
    print('#{} {}'.format(tc, maxLine))
