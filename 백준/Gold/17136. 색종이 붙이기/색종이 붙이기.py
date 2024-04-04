def dfs(paperCnt, paper, worth):
    global ans, max_worth
    # print(*paper, ans)
    # for i in range(10):
    #     print(graph[i])
    # print()
    if paperCnt >= ans:
        return
    # if worth < max_worth:
    #     return
    if zeroCheck():
        # print(paperCnt, paper)
        ans = min(paperCnt, ans)
        max_worth = max(worth, max_worth)
        return
    for i in range(10):
        for j in range(10):
            if graph[i][j] == 1:
                if paper[4] > 0 and i + 4 < 10 and j + 4 < 10:  # 5*5
                    # 범위 내에 0이 있는지 체크
                    zeroFlag = 0
                    for r in range(i, i + 5):
                        for c in range(j, j + 5):
                            if graph[r][c] == 0:
                                zeroFlag = 1
                        if zeroFlag:
                            break
                    # graph를 색종이로 덮고, graph는 tmp에 저장
                    if not zeroFlag:
                        for r in range(i, i + 5):
                            for c in range(j, j + 5):
                                tmp[r][c] = graph[r][c]
                                graph[r][c] = 0
                        # dfs
                        paper[4] -= 1
                        dfs(paperCnt + 1, paper, worth + 500000)

                        # 원복
                        paper[4] += 1
                        for r in range(i, i + 5):
                            for c in range(j, j + 5):
                                graph[r][c] = tmp[r][c]

                if paper[3] > 0 and i + 3 < 10 and j + 3 < 10:  # 4*4
                    # 범위 내에 0이 있는지 체크
                    zeroFlag = 0
                    for r in range(i, i + 4):
                        for c in range(j, j + 4):
                            if graph[r][c] == 0:
                                zeroFlag = 1
                        if zeroFlag:
                            break
                    # graph를 색종이로 덮고, graph는 tmp에 저장
                    if not zeroFlag:
                        for r in range(i, i + 4):
                            for c in range(j, j + 4):
                                tmp[r][c] = graph[r][c]
                                graph[r][c] = 0
                        # dfs
                        paper[3] -= 1
                        dfs(paperCnt + 1, paper, worth + 40000)

                        # 원복
                        paper[3] += 1
                        for r in range(i, i + 4):
                            for c in range(j, j + 4):
                                graph[r][c] = tmp[r][c]

                if paper[2] > 0 and i + 2 < 10 and j + 2 < 10:  # 3*3
                    # 범위 내에 0이 있는지 체크
                    zeroFlag = 0
                    for r in range(i, i + 3):
                        for c in range(j, j + 3):
                            if graph[r][c] == 0:
                                zeroFlag = 1
                        if zeroFlag:
                            break
                    # graph를 색종이로 덮고, graph는 tmp에 저장
                    if not zeroFlag:
                        for r in range(i, i + 3):
                            for c in range(j, j + 3):
                                tmp[r][c] = graph[r][c]
                                graph[r][c] = 0
                        # dfs
                        paper[2] -= 1
                        dfs(paperCnt + 1, paper, worth + 3000)

                        # 원복
                        paper[2] += 1
                        for r in range(i, i + 3):
                            for c in range(j, j + 3):
                                graph[r][c] = tmp[r][c]

                if paper[1] > 0 and i + 1 < 10 and j + 1 < 10:  # 2*2
                    # 범위 내에 0이 있는지 체크
                    zeroFlag = 0
                    for r in range(i, i + 2):
                        for c in range(j, j + 2):
                            if graph[r][c] == 0:
                                zeroFlag = 1
                        if zeroFlag:
                            break
                    # graph를 색종이로 덮고, graph는 tmp에 저장
                    if not zeroFlag:
                        for r in range(i, i + 2):
                            for c in range(j, j + 2):
                                tmp[r][c] = graph[r][c]
                                graph[r][c] = 0
                        # dfs
                        paper[1] -= 1
                        dfs(paperCnt + 1, paper, worth + 200)

                        # 원복
                        paper[1] += 1
                        for r in range(i, i + 2):
                            for c in range(j, j + 2):
                                graph[r][c] = tmp[r][c]

                if paper[0] > 0 and i < 10 and j < 10:  # 1*1
                    # 범위 내에 0이 있는지 체크
                    zeroFlag = 0
                    for r in range(i, i + 1):
                        for c in range(j, j + 1):
                            if graph[r][c] == 0:
                                zeroFlag = 1
                        if zeroFlag:
                            break
                    # graph를 색종이로 덮고, graph는 tmp에 저장
                    if not zeroFlag:
                        for r in range(i, i + 1):
                            for c in range(j, j + 1):
                                tmp[r][c] = graph[r][c]
                                graph[r][c] = 0
                        # dfs
                        paper[0] -= 1
                        dfs(paperCnt + 1, paper, worth + 10)

                        # 원복
                        paper[0] += 1
                        for r in range(i, i + 1):
                            for c in range(j, j + 1):
                                graph[r][c] = tmp[r][c]
                return


def zeroCheck():
    for i in range(10):
        for j in range(10):
            if graph[i][j]:
                return False
    return True

ans = 1e9
tmp = [[0] * 10 for _ in range(10)]
graph = [list(map(int, input().split())) for _ in range(10)]
paper = [5, 5, 5, 5, 5]  # 1*1, 2*2, 3*3, 4*4, 5*5의 개수
worth = 0
max_worth = 0

dfs(0, paper, 0)
print(ans if ans != 1e9 else -1)