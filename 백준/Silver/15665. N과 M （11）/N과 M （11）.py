def dfs(depth):
    if depth == m:
        tmp = ' '.join(map(str, isSelected))
        ans.append(tmp)
        return
    for i in range(n):
        isSelected[depth] = num[i]
        dfs(depth + 1)

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []
isSelected = [0] * m
dfs(0)

ans = list(set(ans))
for a in ans:
    print(a)