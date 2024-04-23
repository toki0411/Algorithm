n = int(input())
num = list(map(int, input().split()))
left = 0
right = n-1
ans = 1e9

while left < right:
    val = num[left] + num[right]
    if abs(val) < abs(ans):
        ans = val

    if val < 0 :
        left += 1
    else:
        right -= 1

print(ans)
