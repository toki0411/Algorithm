from collections import deque
n, k = map(int, input().split())
q = deque()
for i in range(1,n+1):
    q.append(i)
ans = []

while q:
    cnt =0
    while cnt < k-1:
        x=q.popleft()
        q.append(x)
        cnt += 1
    ans.append(q.popleft())

print('<', end ="")
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end='')
    else:
        print(ans[i], end=", ")
print('>')