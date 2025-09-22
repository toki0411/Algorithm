n = int(input())
num = list(map(int, input().split()))
x = int(input())
cnt = 0
tmp = n-1
num.sort()
for i in range(n):
    for j in range(tmp, i, -1):
        if j == i : break
        val = num[i] + num[j]
        if val == x:
            # print(val, i, j, tmp)
            cnt += 1
            tmp = j - 1
        elif val < x :
            break
print(cnt)