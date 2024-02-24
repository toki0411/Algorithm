from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, cnt):
    idx = []
    q = deque()
    q.append((x, y))
    visited[x][y] = cnt
    while q:
        x, y = q.popleft()
        idx.append([x,y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0: continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = cnt
    return idx


def findParents(x):
    if x == parents[x]: return x
    parents[x] = findParents(parents[x])
    return parents[x]

def union(aa, bb):
    aRoot = findParents(aa)
    bRoot = findParents(bb)
    if aRoot == bRoot:
        return False
    if aRoot < bRoot:
        parents[bRoot] = aRoot
    else:
        parents[aRoot] = bRoot
    return True

def widthBridgeCheck(i, j):
    cost = 100000
    for l in range(len(island[i])):
        ix = island[i][l][0]
        iy = island[i][l][1]
        for k in range(len(island[j])):
            jx = island[j][k][0]
            jy = island[j][k][1]
            if ix == jx :
                if iy > jy :
                    key = True
                    for r in range(jy+1, iy):
                        if graph[ix][r] == 1:
                            key = False
                            break
                    if key :
                        tmp = abs(jy-iy)-1
                        if tmp < 2: continue
                        cost = min(abs(jy-iy)-1, cost)
                elif iy < jy:
                    key = True
                    for r in range(iy+1, jy):
                        if graph[ix][r] == 1:
                            key = False
                            break
                    if key:
                        tmp = abs(jy - iy) - 1
                        if tmp < 2: continue
                        cost = min(tmp, cost)
    if cost == 100000:
        return
    else:
        edgeList.append([i, j, cost])
        return
def heightBridgeCheck(i, j):
    cost = 100000
    for l in range(len(island[i])):
        ix = island[i][l][0]
        iy = island[i][l][1]
        for k in range(len(island[j])):
            jx = island[j][k][0]
            jy = island[j][k][1]
            if iy == jy:
                if ix > jx:
                    key = True
                    for r in range(jx+1, ix ):
                        if graph[r][iy] == 1:
                            key = False
                            break
                    if key:
                        tmp = abs(jx - ix) - 1
                        if tmp < 2: continue
                        cost = min(tmp, cost)
                elif ix < jx:
                    key = True
                    for r in range(ix+1, jx):
                        if graph[r][iy] == 1:
                            key = False
                            break
                    if key:
                        tmp = abs(jx - ix) - 1
                        if tmp < 2: continue
                        cost = min(tmp, cost)
    if cost == 100000:
        return
    else:
        edgeList.append([i, j, cost])
        return

def make():
    for k in range(len(island) + 1):
        parents[k] = k

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
island = [[0]]
edgeList = []
cnt = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:  # bfs를 돌면서 섬들의 시작 인덱스와 끝 인덱스를 기록
            idx = bfs(i, j, cnt)
            island.append(idx)
            cnt += 1

# print(visited)
# print("island : ",island)

for i in range(1, len(island)):
    for j in range(i + 1, len(island)):
        widthBridgeCheck(i, j)  # 가로로 다리 건설이 가능한지 체크. 불가능한 경우 -1 리턴
        heightBridgeCheck(i, j)  # 세로로 다리 건설이 가능한지 체크


parents = [0] * (len(island)+1)
make()
edgeList.sort(key = lambda x: x[2])
cnt = 0
weight = 0
# print("edgelist : ", edgeList)
for edge in edgeList:
    if not union(edge[0], edge[1]):
        continue
    weight += edge[2]
    cnt += 1
    if cnt == len(island)-2:
        break
if cnt != len(island)-2:
    print(-1)
elif weight == 0:
    print(-1)
else:
    print(weight)
# print(weight if weight != 0 else -1)
