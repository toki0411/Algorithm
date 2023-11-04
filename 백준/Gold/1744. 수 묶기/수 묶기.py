n = int(input())
num = [int(input()) for _ in range(n)]
minus = []
plus = []
for n in num:
    if n <= 0:
        minus.append(n)
    else :
        plus.append(n)

plus.sort(reverse=True); minus.sort(); ans = 0
for i in range(0, len(plus), 2):
    if i+1 == len(plus):
        ans+=plus[i]
        break
    ans += max(plus[i]+plus[i+1], plus[i]*plus[i+1])
for j in range(0, len(minus), 2):
    if j+1 == len(minus):
        ans+=minus[j]
        break
    ans += max(minus[j] + minus[j + 1], minus[j] * minus[j + 1])

print(ans)