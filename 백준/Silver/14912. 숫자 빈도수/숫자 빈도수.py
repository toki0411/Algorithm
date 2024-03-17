n, d = map(int, input().split())
ans = 0
num = [i for i in range(1, n+1)]
for i in num:
    ans += str(i).count(str(d))
print(ans)