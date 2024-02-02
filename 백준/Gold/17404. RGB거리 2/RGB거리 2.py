import copy

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
MAX_VAL = 1001
ans = 1e9
#R
arr = copy.deepcopy(graph)
arr[0][1] = MAX_VAL; arr[0][2] = MAX_VAL
for i in range(1, N):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])
ans = min(arr[N-1][1], arr[N-1][2], ans)

#G
arr = copy.deepcopy(graph)
arr[0][0] = MAX_VAL; arr[0][2] = MAX_VAL
for i in range(1, N):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])
ans = min(arr[N-1][0], arr[N-1][2], ans)

#B
arr = copy.deepcopy(graph)
arr[0][1] = MAX_VAL; arr[0][0] = MAX_VAL
for i in range(1, N):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])
ans = min(arr[N-1][1], arr[N-1][0], ans)

print(ans)