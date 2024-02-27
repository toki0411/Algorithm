import copy


def shift(dir):
    global graph
    visited = [[0] * n for _ in range(n)]
    if dir == 0:  # 좌
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 0 : continue
                yy = j
                ny = j + dy[dir]
                while ny >= 0 and ny < n:
                    if graph[i][ny] == graph[i][yy] and visited[i][ny] == 0:
                        graph[i][ny] += graph[i][yy]
                        graph[i][yy] = 0
                        visited[i][ny] = 1
                        break
                    elif graph[i][ny] == 0:
                        graph[i][ny] = graph[i][yy]
                        graph[i][yy] = 0
                        yy = ny
                    else:
                        break;
                    ny += dy[dir]

    elif dir == 1:  # 우
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if graph[i][j] == 0: continue
                yy = j
                ny = j + dy[dir]
                while ny >= 0 and ny < n:
                    if graph[i][ny] == graph[i][yy] and visited[i][ny] == 0:
                        graph[i][ny] += graph[i][yy]
                        graph[i][yy] = 0
                        visited[i][ny] = 1
                        break
                    elif graph[i][ny] == 0:
                        graph[i][ny] = graph[i][yy]
                        graph[i][yy] = 0
                        yy = ny
                    else:
                        break;
                    ny += dy[dir]

    elif dir == 2:  # 상
            for i in range(n):
                for j in range(n):
                    if graph[i][j] == 0: continue
                    xx = i
                    nx = i + dx[dir]
                    while nx >= 0 and nx < n:
                        if graph[nx][j] == graph[xx][j] and visited[nx][j] == 0:
                            graph[nx][j] += graph[xx][j]
                            graph[xx][j] = 0
                            visited[nx][j] = 1
                            break
                        elif graph[nx][j] == 0:
                            graph[nx][j] = graph[xx][j]
                            graph[xx][j] = 0
                            xx = nx
                        else:
                            break;
                        nx += dx[dir]
    else:  # 하
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if graph[i][j] == 0: continue
                xx = i
                nx = i + dx[dir]
                while nx >= 0 and nx < n:
                    if graph[nx][j] == graph[xx][j] and visited[nx][j] == 0:
                        graph[nx][j] += graph[xx][j]
                        graph[xx][j] = 0
                        visited[nx][j] = 1
                        break
                    elif graph[nx][j] == 0:
                        graph[nx][j] = graph[xx][j]
                        graph[xx][j] = 0
                        xx = nx
                    else:
                        break;
                    nx += dx[dir]


def dfs(cnt):
    global graph
    if cnt == 5:
        checkMax()
        return
    tmp = copy.deepcopy(graph)
    for i in range(4):
        shift(i)
        dfs(cnt + 1)
        graph = copy.deepcopy(tmp)


def checkMax():  # 그래프에서 가장 큰 블록을 찾는 함수
    global ans
    for i in range(n):
        for j in range(n):
            ans = max(ans, graph[i][j])


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 2
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dfs(0)
#
print(ans)
# shift(0)
# # shift(2)
# print(graph)