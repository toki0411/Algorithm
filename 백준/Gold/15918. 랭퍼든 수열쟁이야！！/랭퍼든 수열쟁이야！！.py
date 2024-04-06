n, x, y = map(int, input().split())
def dfs(cnt):
    global s
    if cnt == (2*n+1):
        s += 1
        return
    if ans[cnt] == 0:
        for i in range(1, n+1):
            if num[i] > 0 and cnt + 1 + i < 2*n + 1:
                if ans[cnt+ 1 + i] == 0:
                    ans[cnt] = i
                    ans[cnt + 1 + i] = i
                    num[i] -= 2
                    dfs(cnt + 1)
                    num[i] += 2
                    ans[cnt] = 0
                    ans[cnt + 1 + i] = 0

    else:
        dfs(cnt + 1)
s = 0
ans = [0] * (2*n+1)
ans[x] = y-x-1
ans[y] = y-x-1
num = [0] + [2] * (n)
num[y-x-1] -= 2
dfs(1)
print(s)