arr = input().split('-');
num = []
for i in arr:
    val = 0
    tmp = i.split('+')
    for j in tmp:
        val += int(j)
    num.append(val)
ans = num[0]
for i in range(1, len(num)):
    ans -= num[i]
print(ans)