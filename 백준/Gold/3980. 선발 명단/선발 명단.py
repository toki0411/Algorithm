import sys
input = sys.stdin.readline
def dfs(cnt, score):
    global ans
    if cnt == 11:
        ans = max(score, ans)
        return
    for i in range(11):
        if player[cnt][i] and not visited[i]:
            visited[i] = 1
            dfs(cnt + 1, score + player[cnt][i])
            visited[i] = 0
C = int(input())

for c in range(C):
    player = [list(map(int, input().split())) for _ in range(11)]
    ans = 0
    visited = [0] * 11
    dfs(0, 0)

    print(ans)