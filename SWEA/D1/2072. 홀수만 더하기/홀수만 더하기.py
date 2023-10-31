t = int(input())
for t_ in range(1,t+1):
    arr = list(map(int,input().split()))
    ans = 0
    for i in arr:
        if i %2 != 0:
            ans += i
    print('#{} {}'.format(t_, ans))