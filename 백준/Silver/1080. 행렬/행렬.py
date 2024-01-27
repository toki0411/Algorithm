n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
answer = [list(map(int, list(input()))) for _ in range(n)]
def reverse(i, j):
    for k in range(i, i + 3):
        for l in range(j, j + 3):
            if graph[k][l] == 0:
                graph[k][l] = 1
            else:
                graph[k][l] = 0;
cnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if graph[i][j] != answer[i][j]:
            cnt += 1
            reverse(i, j)

if graph != answer:
    print(-1)
else:
    print(cnt)
