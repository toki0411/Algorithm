from collections import deque

n = int(input())
q = deque()
for i in range(1,n+1):
	q.append(i)
ans = []
while len(q) > 1 :
	ans.append(q[0])
	q.popleft()
	tmp = q[0]
	q.popleft()
	q.append(tmp)

print(*ans, q[0])