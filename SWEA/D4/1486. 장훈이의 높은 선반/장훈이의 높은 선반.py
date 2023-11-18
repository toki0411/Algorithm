t = int(input())
def dfs(total, target, start):
    global ans
    if total >= target:
        ans = min(total, ans)
        return
    for i in range(start, n):
        if not visited[i]:
            visited[i] = 1
            dfs(total + height[i], target, i+1)
            visited[i] = 0


for tc in range(1, t+1):
    n,m = map(int,input().split())
    height = list(map(int, input().split()))
    visited = [0] * n
    ans = 1e9
    dfs(0,m, 0)
    print('#{} {}'.format(tc, ans-m))