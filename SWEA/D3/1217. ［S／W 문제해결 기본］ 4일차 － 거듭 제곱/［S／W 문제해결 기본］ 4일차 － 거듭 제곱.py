def dfs(level, total, n, m):
    global ans
    if level == m:
        ans = total
        return
    dfs(level+1, total*n, n,m)
for tc in range(10):
    t = int(input())
    n, m = map(int, input().split())
    ans = 0
    dfs(0, 1, n, m)
    print('#{} {}'.format(t, ans))

