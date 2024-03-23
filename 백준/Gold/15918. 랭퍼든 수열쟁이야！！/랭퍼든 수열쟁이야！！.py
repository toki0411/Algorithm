n, x, y = map(int, input().split())
total = 0


def dfs(depth):
    global total
    if depth == (y - x - 1):
        dfs(depth + 1)
    if depth == n + 1:
        total += 1
        return
    for i in range(1, len(ans) - depth - 1):
        if ans[i] == 0 and ans[i + depth + 1] == 0:
            ans[i] = depth
            ans[i + depth + 1] = depth
            dfs(depth + 1)
            ans[i] = 0
            ans[i + depth + 1] = 0


ans = [0] * (2 * n + 1)
ans[y] = y - x - 1
ans[x] = y - x - 1
dfs(1)
print(total)