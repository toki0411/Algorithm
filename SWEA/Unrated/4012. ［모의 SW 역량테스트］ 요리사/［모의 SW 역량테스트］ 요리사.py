def cook():
    global ans
    B = [i for i in range(N)]
    A = []
    for i in isSelected:
        A.append(i)
        B.remove(i)
    aCnt = 0
    bCnt = 0
    for i in range(N//2):

        for j in range(N//2):
            if A[i] != A[j]:
                aCnt += (board[A[i]][A[j]])
            if B[i] != B[j]:
                bCnt += (board[B[i]][B[j]])
    ans = min(ans, abs(aCnt - bCnt))

def dfs(cnt, start):
    if cnt == N//2:
        cook()
        return
    for i in range(start, N):
        isSelected[cnt] = i
        dfs(cnt + 1, i + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 1e9
    isSelected = [0] * (N//2)
    dfs(0, 0)
    print("#{} {}".format(tc, ans))