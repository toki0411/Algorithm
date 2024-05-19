s = list(input())
keyword = list(input())
idx = 0
ans = 0
while idx < len(s):
	if s[idx] == keyword[0] and idx + len(keyword) <= len(s) :
		flag = True
		for i in range(len(keyword)):
			if s[idx + i] != keyword[i]:
				flag = False
		if flag:
			idx += len(keyword)
			ans += 1
		else:
			idx += 1
	else:
		idx += 1
print(ans)