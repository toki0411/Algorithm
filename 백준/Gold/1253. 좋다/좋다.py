from bisect import bisect_left, bisect_right

n = int(input())
num = list(map(int, input().split()))
num.sort()
cnt = 0

for i in range(n):
    target = num[i]
    start = 0
    end = n - 1

    while start < end:
        if num[start] + num[end] == target:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif num[start] + num[end] > target:
            end -= 1
        elif num[start] + num[end] < target:
            start += 1

print(cnt)