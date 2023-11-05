from math import ceil

n = int(input())
number = list(map(int,input().split()))
b, c = map(int, input().split())
ans = 0
for i in range(len(number)):
    number[i]-=b
    ans += 1
    if number[i] <= 0:
        continue
    else:
        ans += ceil(number[i]/c)
print(ans)