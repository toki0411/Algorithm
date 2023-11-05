
n = int(input())
number = list(map(int,input().split()))
ans = 0; v = 0
number.sort()
for i in range(len(number)):
    ans += (number[i] + v)
    v += number[i]
print(ans)