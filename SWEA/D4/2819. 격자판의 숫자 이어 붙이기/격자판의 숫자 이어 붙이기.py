# import sys
# sys.setrecursionlimit(10**6)
t = int(input())
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def dfs(x, y, num):
    if (len(num)) == 7:
        if ''.join(num) not in ans:
            ans.add(''.join(num))
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, num+[str(graph[nx][ny])])
for tc in range(1, t + 1):
    graph = [list(map(int, input().split())) for _ in range(4)]
    ans = set(); num = []; visited = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            dfs(i, j, num)
    print('#{} {}'.format(tc, len(ans)))
