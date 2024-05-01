import sys
input = sys.stdin.readline

def dfs(now, start):
    visited[now] = 1
    next = num[now]
    if not visited[next]:
        dfs(next, start)
    else:
        if next == start:
            ansArr.append(next)
            return

n = int(input())
num = [0]
ans = 0
v = []

ansArr = []
for i in range(1, n+1):
    a = int(input())
    num.append(a)

for i in range(1, n+1):
    visited = [0] * (n+1)
    dfs(i, i)

ansArr.sort()
print(len(ansArr))
for p in ansArr:
    print(p)