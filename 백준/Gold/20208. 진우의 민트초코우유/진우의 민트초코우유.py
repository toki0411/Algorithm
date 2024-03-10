import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, hp, mCnt):
    global max_milk
    if abs(x - home[0])+abs(y - home[1]) <= hp:
        max_milk = max(mCnt, max_milk)

    for i in range(len(milk)):
        if not visited[i]:
            mx = milk[i][0]
            my = milk[i][1]
            dis = abs(mx - x) + abs(my - y)
            if dis <= hp:
                visited[i] = 1
                dfs(mx, my, hp - dis + h, mCnt + 1)
                visited[i] = 0

n, m, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
home = [0, 0]
max_milk = 0
milk = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home = [i, j]
        elif graph[i][j] == 2:
            milk.append([i,j])

visited = [0] * len(milk)
dfs(home[0], home[1], m, 0)
print(max_milk)