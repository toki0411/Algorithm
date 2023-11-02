
t = int(input())
def dfs(month, money):
    global ans
    if month >= 12:
        if ans > money:
            ans = money
        return
    dfs(month+1, money + price[0]*plan[month])
    dfs(month+1, money + price[1])
    dfs(month+3, money + price[2])

for tc in range(1, t + 1):
    price = list(map(int,input().split()))
    ans = price[-1]
    plan = list(map(int, input().split()))
    dfs(0, 0)
    print('#{} {}'.format(tc, ans))
