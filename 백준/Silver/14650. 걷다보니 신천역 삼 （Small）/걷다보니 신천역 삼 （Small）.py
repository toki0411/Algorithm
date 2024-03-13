def dfs(cnt, num, n):
    global ans
    if n == cnt:
        k = int(''.join(num))
        if k % 3 == 0:
            ans += 1
        return
    if cnt == 0:
        for i in range(2):
            dfs(cnt + 1, num+[str(num0[i])], n)
    else:
        for i in range(3):
            dfs(cnt + 1, num+[str(num1[i])], n)

n = int(input())
ans = 0

num0 = [1, 2]
num1 = [0, 1, 2]
dfs(0, [], n)
print(ans)