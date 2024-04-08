def dfs(cnt,x,y):
    global ans
    if cnt > 3 or cnt > ans:
        return
    if check():
        ans = min(ans, cnt)
        return

    for i in range(x, H):
        if i == x:
            now = y
        else:
            now = 0
        for j in range(now, N-1):
            if not board[i][j]:
                board[i][j] = 1
                dfs(cnt + 1, i, j+2)
                board[i][j] = 0
def check(): # 시뮬레이션 하면서 i번이 i로 끝나는지 체크
    for i in range(N):
        y = i
        for j in range(H):
            #오른쪽
            if board[j][y]:
                y += 1
            #왼쪽
            elif y-1 >= 0 and board[j][y-1]:
                y -= 1
        if y != i:
            return False
    return True

N, M, H = map(int, input().split()) #세로선, 가로선, 세로선마다 가로선을 놓을 수 있는 위치
board = [[0] * N for _ in range(H)]
if M == 0:
    print(0)
    exit()
for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
ans = 4
dfs(0, 0, 0)
print(ans if ans < 4 else -1)