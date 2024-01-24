n = int(input());
road = list(map(int, input().split()))
city = list(map(int, input().split()))
low_cost = min(city)
ans = 0
for i in range(n-1):
    if i == 0 and city[i] == low_cost : #처음이 가장 싼 경우
        ans = sum(road) * city[i]
        break
    elif i==0 : #처음에는 무조건 다음 목적지만큼 충전
        ans += road[i] * city[i]
    else :
        if city[i-1] < city[i]:
            city[i] = city[i-1]
            ans += city[i] * road[i]
        else :
            ans += city[i] * road[i]

print(ans)

