n, l= map(int, input().split())
traffic = [list(map(int, input().split())) for _ in range(n)]
ans = 0; red = green = 0; prev_location = 0
for sign in traffic:
    ans += sign[0] - prev_location
    red = sign[1]
    green = sign[2]
    prev_location = sign[0]
    if ans % (red+green) > red: #초록불
        continue
    elif ans % (red+green) < red:
        ans += red - ans % (red+green)

ans += l - prev_location
print(ans)