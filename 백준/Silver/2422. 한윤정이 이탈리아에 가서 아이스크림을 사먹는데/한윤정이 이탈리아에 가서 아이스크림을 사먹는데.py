def dfs(depth, start):
	global cnt
	if depth == 3:
		cnt += 1

		return
	for i in range(start, n+1):
		if not visited[i] and check(i, depth):
			visited[i] = 1
			isSelected[depth] = i
			dfs(depth + 1, i+1)
			visited[i] = 0
def check(x, depth):
	for i in range(depth):
		t = isSelected[i]
		for j in lock[t]:
			if j == x:
				return False
	return True

n, m = map(int, input().split())
lock = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	lock[a].append(b)
	lock[b].append(a)
# print(lock)
isSelected = [0] * 3
visited = [0] * (n+1)
cnt = 0
dfs(0, 1)
print(cnt)