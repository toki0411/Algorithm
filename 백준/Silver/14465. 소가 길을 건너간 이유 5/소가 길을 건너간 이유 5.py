import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
traffic = [0] * (n+1)
ans = 1e9
for i in range(b):
    idx = int(input())
    traffic[idx] = 1

for i in range(1, n+2 - k):
    tmp = traffic[i:i+k]
    ans = min(tmp.count(1), ans)

print(ans)