

def priceMeasure():
    A = []
    B = []
    for i in range(M):
        A.append(board[isSelected[0][0]][isSelected[0][1] + i])
        B.append(board[isSelected[1][0]][isSelected[1][1] + i])
    val = 0
    def subset(H, cnt, selected):
        nonlocal val
        if cnt == len(H):
            total = 0
            tmp = 0
            for i in range(len(H)):
                if selected[i]:
                    total += H[i]
                    tmp += H[i] * H[i]
            if total > C: return
            val = max(val, tmp)
            return

        selected[cnt] = 1
        subset(H, cnt + 1, selected)
        selected[cnt] = 0
        subset(H, cnt + 1, selected)

    selected = [0] * len(A);
    subset(A, 0, selected)
    aHoney = val

    selected = [0] * len(B)
    val = 0
    subset(B, 0, selected)
    bHoney = val

    return aHoney + bHoney

def dfs(cnt, x):
    global ans
    if cnt == 2:
        # print(isSelected)
        price = priceMeasure()
        ans = max(price, ans)
        return
    # y idx 조정
    # if y + M > N:
    #     x += 1
    #     y = 0
    for i in range(x, N):
        for j in range(N-M+1):
            if not visited[i][j]:
                for k in range(M):
                    visited[i][j+k] = 1
                isSelected[cnt] = [i, j]
                dfs(cnt + 1, i+1)
                for k in range(M):
                    visited[i][j + k] = 0

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    isSelected = [0] * (2)
    visited = [[0] * N for _ in range(N)]

    selected = [0]
    dfs(0, 0)
    print("#{} {}".format(tc, ans))