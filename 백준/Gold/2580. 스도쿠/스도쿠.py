graph = [list(map(int, input().split())) for _ in range(9)]


def dfs(cnt):
    if cnt == len(zero):
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end=" ")
            print()
        exit(0)
    x, y = zero[cnt]
    # 들어갈 수 있는 수 체크
    key = False
    for i in range(1, 10):
        key = True
        # 가로
        for j in range(9):
            if graph[x][j] == i:
                key = False
                break
        if not key:
            continue
        # 세로
        for j in range(9):
            if graph[j][y] == i:
                key = False
                break
        if not key:
            continue
        # 3 * 3
        xIdx = x // 3 * 3
        yIdx = y // 3 * 3
        for j in range(xIdx, xIdx + 3):
            for k in range(yIdx, yIdx + 3):
                if graph[j][k] == i:
                    key = False
                    break
                if not key:
                    break
        if not key:
            continue
        graph[x][y] = i
        dfs(cnt + 1)
        graph[x][y] = 0
    if not key:
        return


zero = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero.append([i, j])

dfs(0)