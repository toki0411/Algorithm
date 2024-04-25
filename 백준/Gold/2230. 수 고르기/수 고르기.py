n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(input()))
A.sort()
start =0
end = 0
ans = A[-1] - A[0]
while start <= end and start < n and end < n:
    v= abs(A[start] - A[end])
    if v < m:
        end += 1
    else:
        ans = min(v, ans)
        start += 1
print(ans)