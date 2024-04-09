def dfs(start, price):

    global ans
    if start > N:
        return
    if start <= N:
        ans = max(price, ans)

    for i in range(start, N):
        if schedule[i][0] + start <= N:
            dfs(schedule[i][0] + i , price + schedule[i][1])


N = int(input())
schedule = []
isSelected = [0] * N
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    schedule.append([a,b])

dfs(0, 0)
print(ans)