def dfs(h, cnt): #부분집합을 이용한다.
    global ans
    if cnt == N:
        if h >= B:
            ans = min(ans, h)
        return

    dfs(h + height[cnt], cnt + 1)
    dfs(h , cnt + 1)

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())

    height = list(map(int, input().split()))
    ans = 1e8
    dfs(0,0)
    print("#{} {}".format(tc, ans-B))