N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start = 0
end = len(liquid) - 1
ans = 1e10
left = 0
right = 0
# print(liquid)

while start < end:
    val = liquid[start] + liquid[end]
    if abs(val) < ans:
        ans = abs(val)
        left = liquid[start]
        right = liquid[end]
    if val < 0 :
        start += 1
    elif end > 0:
        end -= 1
    else:
        break
print(left, right)