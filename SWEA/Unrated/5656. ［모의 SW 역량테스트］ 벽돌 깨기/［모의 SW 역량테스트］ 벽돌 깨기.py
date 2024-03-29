from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]


T = int(input())
def drop(): #아래로 구슬이 떨어지는 함수
    for i in range(W):
        for j in range(H-1,-1,-1):
            if graph[j][i] != 0:
                nx = j
                for k in range(j+1, H):
                    if graph[k][i] == 0:
                        graph[k][i] = graph[nx][i]
                        graph[nx][i] = 0
                        nx = k

                    else:
                        break

def dfs(depth): #구슬을 떨어뜨릴 중복 순열 (중복허용)
    if depth == N:
        bfs()
        return;
    for i in range(W):
        isSelected[depth] = i
        dfs(depth+1)

def bfs():
    global ans
    #그래프 복사
    for i in range(H):
        for j in range(W):
            graph[i][j] = graph2[i][j]

    q = deque()
    for depth in range(N):
        q.append((0, isSelected[depth], graph[0][isSelected[depth]]))
        graph[0][isSelected[depth]] = 0
        while q:
            x, y, r = q.popleft()
            # print(isSelected, x, y, r)
            if r == 0:
                nx = x + dx[1]
                ny = y + dy[1]
                if nx < 0 or ny < 0 or nx >= H or ny >= W: continue
                q.append((nx, ny, graph[nx][ny]))
            else:
                for i in range(4):
                    nx = x
                    ny = y
                    for j in range(r-1):
                        nx += dx[i]
                        ny += dy[i]
                        if nx < 0 or ny < 0 or nx >= H or ny >= W: continue
                        if graph[nx][ny] != 0:
                            q.append((nx, ny, graph[nx][ny]))
                            graph[nx][ny] = 0

                    graph[x][y] = 0
        drop()

    cnt = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j]:
                cnt += 1

    ans = min(cnt, ans)
for tc in range(1, T+1):
    ans = 1e9
    N, W, H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]

    graph2 = [[0 for _ in range(W)] for __ in range(H)]
    for i in range(H):
        for j in range(W):
            graph2[i][j] = graph[i][j]
    isSelected = [0] * N
    dfs(0)
    print('#{} {}'.format(tc, ans))