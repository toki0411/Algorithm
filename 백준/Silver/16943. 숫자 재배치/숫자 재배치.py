a, b= map(int, input().split())
str_a = list(str(a))
limit = len(str_a)
visited = [0] * limit
ans = -1
def dfs(level, case):
    global ans
    if level > 0 and case[0] == '0':
        return
    if level == limit:
        num = int(''.join(case))
        if num < b:
            ans = max(num, ans)
        return

    for i in range(limit):
        if not visited[i]:
            visited[i] = 1
            dfs(level+1, case + [str_a[i]])
            visited[i] = 0

dfs(0,[])
print(ans)


