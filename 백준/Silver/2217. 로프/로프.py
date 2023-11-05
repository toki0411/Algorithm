n = int(input())
weight = [int(input()) for _ in range(n)]
weight.sort(reverse=True)
ans = weight[0]
for i in range(1, len(weight)):
    if ans < weight[i] * (i+1):
        ans = weight[i] * (i+1)
print(ans)