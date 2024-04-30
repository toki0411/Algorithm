n = int(input())
num = list(map(int, input().split()))
left = 0
right = n-1
ans = 1e10
val1 = num[left]; val2 = num[right]
while left < right:
    tmp = num[left] + num[right]
    if abs(ans) > abs(tmp):
        ans = tmp
        val1 = num[left]
        val2 = num[right]
    if tmp < 0:
        left += 1
    elif tmp > 0:
        right -= 1
    else:
        break
print(val1, val2)