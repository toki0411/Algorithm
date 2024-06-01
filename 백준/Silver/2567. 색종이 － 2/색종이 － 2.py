graph = [[ 0 for _ in range(101)] for __ in range(101)]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            graph[i][j] = 1
cnt = 0
for j in range(1, 101):
    for i in range(101):
        if graph[i][j] != graph[i][j-1]:
            cnt += 1

for i in range(1, 101):
    for j in range(101):
        if graph[i][j] != graph[i-1][j]:
            cnt += 1

print(cnt)