t = int(input())

for t_ in range(1,t+1):
    ans = 0
    num = list(map(int, input().split()))
    ans = sum(num) - max(num) - min(num)
    ans = round(ans / 8)
    print('#{} {}'.format(t_, ans))
