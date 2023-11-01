def dfs(idx, row, column):
    global ans, n;
    if idx == n:
        ans +=1
        return
    row[idx] = 1
    for j in range(n):
        if check(idx, j, column):
            dfs(idx+1, row, column+[[idx,j]])
def check(i, j, column):
    for c in column:
        x, y = c
        #가로
        if x == i:
            return False
        #세로
        if y == j:
            return False
        #대각선
        if abs(x-i) == abs(y-j):
            return False
    return True
t = int(input())

for tc in range(1,t+1):
    n = int(input()); ans = 0
    row = [0] * n
    column = []
    if n not in [2,3]:
        dfs(0, row, column)

    print('#{} {}'.format(tc, ans))
