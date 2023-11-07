n, m =map(int,input().split())
building = list(map(int, input().split()))
board = [[0] * m for _ in range(n)]
for i in range(m):
    for j in range(building[i]):
        board[j][i] = 1
ans = 0

for i in range(n):
    start = False; cnt =0
    for j in range(m):
        if board[i][j] == 1:
            if start and cnt > 0: #오른쪽 벽
                ans += cnt
                cnt = 0
            start = True
        elif start :
            cnt += 1

print(ans)





