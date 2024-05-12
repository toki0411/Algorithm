score = [[0,0]]
for i in range(1,9):
	a = int(input())
	score.append([a,i])
score.sort(key = lambda x: -x[0])
ans = score[:5]
total = 0
for i in range(5):
	total += ans[i][0]
ans.sort(key = lambda x: x[1])
print(total)
for i in range(5):
	print(ans[i][1], end = " ")