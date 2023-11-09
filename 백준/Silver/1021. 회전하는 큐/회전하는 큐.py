from collections import deque
n, m = map(int, input().split())
position = list(map(int, input().split()))
q = deque()
for i in range(1,n+1):
    q.append(i)
ans = 0
for po in position:
    while True:
        if po == q[0]:
            q.popleft()
            break
        else:
            if q.index(po) > len(q)/2 : #오른쪽 회전
                while q[0] != po:
                    ans += 1
                    x = q.pop()
                    q.appendleft(x)

            else: #왼쪽 회전
                while q[0] != po:
                    ans += 1
                    x = q.popleft()
                    q.append(x)

print(ans)

