n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = [0] * m
isSelected = [0] * n

saved = []
def dfs(depth, start):
    if depth == m:
        tmp = []
        for l in range(m):
            tmp.append(ans[l])
        if tmp not in saved:
            saved.append(tmp)
            print(*tmp)
        return
    for i in range(start, n):
        if not isSelected[i]:
            isSelected[i] = 1
            ans[depth] = num[i]
            dfs(depth + 1, i+1)
            isSelected[i] = 0
dfs(0, 0)