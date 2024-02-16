import copy

n = int(input())
graph = list(map(int, input().split()))
sumGraph = copy.deepcopy(graph)
for i in range(1, len(graph)):
    sumGraph[i] += sumGraph[i-1]
ans = 0
# 1. 벌 벌 꿀통
for i in range(1, n-1):
    bee1 = sumGraph[n-1] - graph[0] - graph[i];  # 제일 왼쪽에 위치
    bee2 = sumGraph[n-1] - sumGraph[i];
    ans = max(bee1+bee2, ans)

# 2. 꿀통 벌 벌
for i in range(1, n-1):
    bee1 = sumGraph[n-2] - graph[i];  # 제일 오른쪽에 위치
    bee2 = sumGraph[i-1];
    ans = max(bee1+bee2, ans)

# 3. 벌 꿀통 벌
for i in range(1, n-1):
    bee1 = sumGraph[i] - graph[0];  # 제일 왼쪽에 위치
    bee2 = sumGraph[n-2] - sumGraph[i-1];  # 제일 오른쪽에 위치

    ans = max(bee1+bee2, ans)

print(ans)