n, k = map(int, input().split())
start = 0
end = 0
num = list(map(int, input().split()))
even = 0 #짝수
odd = 0 #홀수
if num[0] % 2 == 0:
    even += 1
else:
    odd += 1
ans = 0
while end < n:
    # print(start, end)
    if odd > k:
        tmp = num[start]
        if tmp % 2 == 0:
            even -= 1
        else:
            odd -= 1
        start += 1
    else:
        end += 1
        if end < n:
            if num[end] % 2 == 0:
                even += 1
            else:
                odd += 1

    if odd <= k:
        ans = max(ans, even)

print(ans)