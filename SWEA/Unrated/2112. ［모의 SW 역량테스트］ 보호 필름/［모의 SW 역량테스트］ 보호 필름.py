import copy

T = int(input())
def dfs(depth, start):
    global ans
    if check():
        ans = min(depth, ans)
        return
    if depth >= ans:
        return
    for i in range(start, N):
        tmp = copy.deepcopy(graph[i])

        for j in range(M):
            graph[i][j] = 1
        dfs(depth + 1, i + 1)

        for j in range(M):
            graph[i][j] = 0
        dfs(depth + 1, i + 1)

        for j in range(M): #그래프 복구
            graph[i][j] = tmp[j]

def check():
    for i in range(M):
        tmp = -1
        cnt = 1
        for j in range(N):
            if tmp != graph[j][i]:
                tmp = graph[j][i]
                cnt = 1
            elif tmp == graph[j][i]:
                cnt += 1
            if cnt >= K:
                break
        if cnt < K:
            return False
    return True

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    ans = N
    if check() or K == 1:
        print("#{} {}".format(tc, 0))
    else:
        dfs(0, 0)
        print("#{} {}".format(tc, ans))