T = int(input())

for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    ans = 0
    mx = price[-1]
    for i in range(N-2, -1, -1):
        if price[i] >= mx:
            mx = price[i]
        else :
            ans += (mx - price[i])
    print(ans)