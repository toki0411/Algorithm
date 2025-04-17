def dfs(cnt, total):

    if cnt == k :
        if 0 < total <= limit:
            visited[total] = 1
        return
    dfs(cnt + 1, total + num[cnt])
    dfs(cnt + 1, total - num[cnt])
    dfs(cnt + 1, total)

k = int(input())
num = list(map(int, input().split()))
limit = sum(num)
visited = [0] * (limit+1)
dfs(0, 0)
ans = 0
for i in range(1, limit):
    if visited[i] == 0:
        ans += 1
print(ans)