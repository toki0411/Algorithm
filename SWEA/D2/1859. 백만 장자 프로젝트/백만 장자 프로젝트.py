
t = int(input())
for tc in range(1, t+1):
    ans = 0
    n = int(input())
    price = list(map(int, input().split()));
    while len(price) != 0:
        max_idx = price.index(max(price))
        cal = price[:max_idx]
        for i in range(len(cal)):
            ans += abs(price[max_idx] - price[i])
        price = price[max_idx+1:]
    print(f'#{tc}', ans)
