n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]
ans = 1
for i in range(n):
    for j in range(m):
        target = data[i][j];
        for k in range(j+1, m):
            diff = 0
            if target == data[i][k]:
                diff = abs(j - k)
            if diff != 0:

                if i+diff < n:
                    if data[i+diff][j] == data[i+diff][k] == target:
                        ans = max((diff+1) * (diff+1), ans)
print(ans)