t = int(input())
def dfs(idx, k, idx_arr, total):
    global ans
    if total == k:
        ans += 1
        return
    for i in range(idx, len(num)):
        if num[i] + total <= k and i not in idx_arr:
            dfs(i, k, idx_arr + [i], total + num[i])
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    ans = 0
    dfs(0, k, [], 0)
    print('#{} {}'.format(tc, ans))
