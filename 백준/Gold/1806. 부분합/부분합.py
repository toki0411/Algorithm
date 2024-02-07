import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
min_val = sys.maxsize
left = 0
right = 0
sum = 0

while True:
    #총 합이 S를 넘을 때
    if sum >= S:
        min_val = min(right - left, min_val)
        sum -= arr[left]
        left += 1

    elif right == N:
        break;
    #총 합이 S를 넘지 않을 때
    else:
        sum += arr[right]
        right += 1

print(min_val if min_val != sys.maxsize else 0)