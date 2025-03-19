n, m = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = 0
cnt = 0
val = arr[0]

while True :
    if val == m:
        cnt += 1
    if val >= m:
        val -= arr[start]
        start += 1
    else : #val <= m
        if end + 1 < n:
            end += 1
            val += arr[end]
        else:
            break
print(cnt)