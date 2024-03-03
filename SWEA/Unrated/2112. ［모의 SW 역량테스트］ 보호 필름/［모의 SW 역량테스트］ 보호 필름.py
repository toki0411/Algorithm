import copy
def dfs(cnt, col):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    if cnt >= ans:
        return
    for i in range(col, d):
        origin = copy.deepcopy(graph[i])
        # i번째를 0으로
        for r in range(w):
            graph[i][r] = 0
        dfs(cnt + 1, i + 1)

        # i번째를 1으로
        for r in range(w):
            graph[i][r] = 1
        dfs(cnt + 1, i + 1)

        # 그래프 원래대로
        for r in range(w):
            graph[i][r] = origin[r]
def check():
    for j in range(w):
        cnt = 1
        for i in range(1, d):
            if graph[i][j] == graph[i-1][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                break
        if cnt < k:
            return False
    # print(graph)
    return True

T = int(input())
for tc in range(1, T + 1):
    d, w, k = map(int, input().split())  # 필름의 두께, 가로 크기, 합격 기준
    graph = [list(map(int, input().split())) for _ in range(d)]
    # graph2 = copy.deepcopy(graph)
    ans = d + 1
    if check() or k == 1:
        print('#{} {}'.format(tc, 0))
    else:
        dfs(0, 0)
        print('#{} {}'.format(tc, ans))
