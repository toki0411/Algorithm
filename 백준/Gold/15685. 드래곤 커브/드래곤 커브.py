n = int(input())
graph = [[0] * 101 for _ in range(101)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    dir = [d]
    for i in range(g):
        for j in range(len(dir)-1, -1, -1):
            tmp = dir[j] + 1
            if tmp > 3:
                tmp = 0
            dir.append(tmp)
    graph[x][y] = 1
    nx = x; ny = y;
    for i in range(len(dir)):
        nx += dx[dir[i]]
        ny += dy[dir[i]]
        if nx > 100 and ny > 100 and nx < 0 and ny < 0:
            continue
        graph[nx][ny] = 1
ans = 0
#네 꼭짓점이 모두 드래곤 커브의 일부인지 체크
for i in range(101):
    for j in range(101):
        if graph[i][j] == 1:
            val = 1
            if i+1 <= 100 and graph[i+1][j] == 1: val +=1
            if j+1 <= 100 and graph[i][j+1] == 1: val += 1
            if i+1 <= 100 and j+1 <= 100 and graph[i+1][j+1] == 1: val+=1
            if val == 4:
                ans += 1
print(ans)




