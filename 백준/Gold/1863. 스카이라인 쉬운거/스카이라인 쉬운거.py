n = int(input())
s = []
cnt = 0
for l in range(0,n):
    a, b = map(int, input().split())
    while len(s) > 0 and s[-1] > b:
        s.pop()
        cnt += 1
    if len(s) > 0 and s[-1] == b:
        continue
    s.append(b)
while len(s) > 0:
    if s[-1] > 0:
        cnt += 1
    s.pop()
print(cnt)