import sys
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def shift(dir):
    key = False
    bluekey = False

    if dir == 0:  #아래로 구슬이 떨어짐
        for i in range(M):
            for j in range(N-2,0,-1):
                if graph[j][i] == 'R' or graph[j][i] == 'B':
                    nx = j
                    for k in range(j+1, N-1):
                        if graph[k][i] == '.':
                            graph[k][i] = graph[nx][i]
                            graph[nx][i] = '.'
                            nx = k
                        elif graph[k][i] == 'O' and graph[nx][i] == 'R':
                            graph[nx][i] = '.'
                            key = True
                            break
                        elif graph[k][i] == 'O' and graph[nx][i] == 'B':
                            bluekey = True
                            graph[nx][i] = '.'
                            return False
                        else:
                            break


    elif dir == 1: #위로 구슬이 떨어짐
        for i in range(M):
            for j in range(1, N-1):
                if graph[j][i] == 'R' or graph[j][i] == 'B':
                    nx = j
                    for k in range(j-1, 0, -1):
                        if graph[k][i] == '.':
                            graph[k][i] = graph[nx][i]
                            graph[nx][i] = '.'
                            nx = k
                        elif graph[k][i] == 'O'and graph[nx][i] == 'R':
                            graph[nx][i] = '.'
                            key = True
                            break
                        elif graph[k][i] == 'O'and graph[nx][i] == 'B':
                            graph[nx][i] = '.'
                            bluekey = True
                            return False
                        else:
                            break

    elif dir == 2: #왼쪽으로 구슬이 떨어짐
        for i in range(1, N-1):
            for j in range(1, M-1):
                if graph[i][j] == 'R' or graph[i][j] == 'B':
                    ny = j
                    for k in range(j-1, 0, -1):
                        if graph[i][k] == '.':
                            graph[i][k] = graph[i][ny]
                            graph[i][ny] = '.'
                            ny = k
                        elif graph[i][k] == 'O' and graph[i][ny] == 'R':
                            graph[i][ny] = '.'
                            key = True
                            break
                        elif graph[i][k] == 'O' and graph[i][ny] == 'B':
                            graph[i][ny] = '.'
                            bluekey = True

                            return False
                        else:
                            break

    elif dir == 3: #오른쪽으로 구슬이 떨어짐
        for i in range(1, N-1):
            for j in range(M-1, 0, -1):
                if graph[i][j] == 'R' or graph[i][j] == 'B':
                    ny = j
                    for k in range(j+1, M-1):
                        if graph[i][k] == '.':
                            graph[i][k] = graph[i][ny]
                            graph[i][ny] = '.'
                            ny = k
                        elif graph[i][k] == 'O' and graph[i][ny] == 'R':
                            graph[i][ny] = '.'
                            key = True
                            break
                        elif graph[i][k] == 'O' and graph[i][ny] == 'B':
                            graph[i][ny] = '.'
                            bluekey = True
                            return False
                        else:
                            break
    return [key, bluekey]


def dfs(depth, limit, prev): #구슬을 떨어뜨릴 중복 순열 (중복허용)
    if depth == limit:
        for i in range(N):
            for j in range(M):
                graph[i][j] = graph2[i][j]
        for d in range(limit):
            key = shift(isSelected[d])
            if not key: break
            if key[0] and not key[1]:
                print(limit)
                exit(0)

        return
    for i in range(4):
        if i != prev:
            isSelected[depth] = i
            dfs(depth+1, limit, i)


N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
graph2 = [[0 for _ in range(M)] for __ in range(N)]
for i in range(N):
    for j in range(M):
        graph2[i][j] = graph[i][j]
isSelected = [0] * 100
for i in range(1, 11):
    dfs(0, i, -1)
print(-1)