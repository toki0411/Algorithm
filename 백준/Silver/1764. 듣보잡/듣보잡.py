n,  m = map(int, input().split())
hear = set()
ans = []

for i in range(n):
    s = input()
    if s not in hear:
        hear.add(s)

for i in range(m):
    s = input()
    if s in hear:
        ans.append(s)
ans.sort()
print(len(ans))
for a in ans:
    print(a)