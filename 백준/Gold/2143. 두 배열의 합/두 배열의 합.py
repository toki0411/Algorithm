from bisect import bisect_left, bisect_right

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
aSum = []
bSum = []
for i in range(n):
    a = A[i]
    aSum.append(a)
    for j in range(i+1, n):
        a += A[j]
        aSum.append(a)
for i in range(m):
    b = B[i]
    bSum.append(b)
    for j in range(i+1, m):
        b += B[j]
        bSum.append(b)
aSum.sort()
bSum.sort()
ans = 0

for i in range(len(aSum)):
    v = T - aSum[i]
    aidx = bisect_left(bSum, v)
    bidx = bisect_right(bSum, v)
    ans += (bidx - aidx )

print(ans)