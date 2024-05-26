from collections import deque


n = int(input())
def isPrime(n):
	if n == 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True
for _ in range(n):
	start, end = map(int, input().split())
	q = deque()
	q.append((start, 0))

	visited = [0] * 10000
	visited[start] = 1
	while q:
		x, cnt = q.popleft()
		# print(x, cnt)
		if x == end:
			print(cnt)
			break
		for i in range(4):
			for j in range(10):
				new_x = list(str(x))
				new_x[i] = str(j)
				new_x = int(''.join(new_x))
				if 1000 <= new_x and not visited[new_x] and isPrime(new_x):
					visited[new_x] = 1
					q.append((new_x, cnt + 1))