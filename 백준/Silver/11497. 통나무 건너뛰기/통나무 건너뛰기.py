T = int(input())
for tc in range(T):
    n = int(input())
    wood = list(map(int, input().split()))
    wood.sort()
    arr = [0] * n
    idx = 0
    for i in range(0,n,2):
        if i < n:
            arr[idx] = wood[i]
        if i+1 < n:
            arr[n-idx-1] = wood[i+1]
        idx += 1
    ans = 0
    for i in range(n):
        prev = i-1
        next = i+1
        if prev < 0:
            prev = n-1
        if next >= n:
            next = 0
        ans = max(abs(arr[i] - arr[prev]), abs(arr[i]-arr[next]),ans)
    print(ans)