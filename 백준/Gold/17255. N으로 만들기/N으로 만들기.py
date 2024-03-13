def dfs(method, num):
    global ans
    if len(num) == 1:
        ans.append(method)
        return
    dfs(method + [0], num[1:])
    if num[1:] != num[:-1]:
        dfs(method + [1], num[:-1])

n = int(input())
ans = []
dfs([], list(str(n)))
print(len(ans))