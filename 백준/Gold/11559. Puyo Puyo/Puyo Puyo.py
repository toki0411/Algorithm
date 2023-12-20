from collections import deque

graph = [list(input()) for _ in range(12)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
def bfs(x, y):
    candidate = []
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < 12 and 0<= ny < 6 and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                q.append((nx,ny))
                visited[nx][ny] = 1
                candidate.append((nx,ny))
    if len(candidate) >= 4:
        for c in candidate:
            cx, cy = c
            graph[cx][cy] = '.'
        return True
    else:
        return False

while True:
    visited = [[0] * 6 for _ in range(12)]
    # 4개 이상 모여 있는지 체크
    case = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] !='.' and visited[i][j] == 0:
                if bfs(i, j):
                    case=True

    # 모인 것이 없으면 break
    if case == False:
        break
    # 아래로 모음
    reversed_graph = graph[::-1]
    rotated = list(zip(*reversed_graph))

    for idx, r in enumerate(rotated):
        tmp = []
        for i in r:
            if i != '.':
                tmp.append(i)
        num = 12 - len(tmp)
        for _ in range(num):
            tmp.append('.')
 
        for i in range(12):
            graph[11-i][idx] = tmp[i]
    # print(graph)
    #초기화
    cnt += 1
print(cnt)