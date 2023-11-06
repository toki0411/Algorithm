n = int(input())
arr = list(map(int, input().split()))
dp1 = [1] * 1001
dp2 = [1] * 1001

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[j]+1, dp1[i])

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[j]+1, dp2[i])
max = 0
for i in range(n):
    if(max < dp1[i] + dp2[i]):
        max = dp1[i] + dp2[i]

print(max-1)




