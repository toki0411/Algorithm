t = int(input())
def binarySearch(target, b):
    left = 0
    right = len(b) - 1
    idx = -1
    while left <= right:
        mid = (left + right) // 2
        if b[mid] < target:
            idx = mid
            left = mid + 1
        else:
            right = mid - 1
    return idx


for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    cnt = 0
    for i in a:
        cnt += (binarySearch(i, b) + 1)
    print(cnt)

