t = int(input())

for t_ in range(1,t+1):
    ans = 0
    n, limit = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    def dfs(V, score, cal):
        global ans;
        if cal > limit:
            return
        else:
            ans = max(score, ans)
        for i in range(V, len(ingredients)):
            if not visited[i]:
                visited[i] = 1
                dfs(i, score+ingredients[i][0], cal+ingredients[i][1])
                visited[i] = 0
    dfs(0,0,0)
    print('#{} {}'.format(t_, ans))