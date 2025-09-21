import copy
import sys

input = sys.stdin.readline


def permutation(cnt):
    if cnt == K:
        rotate()
        return
    for i in range(K):
        if not visited[i]:
            visited[i] = 1
            cmdSeq[cnt] = i
            permutation(cnt + 1)
            visited[i] = 0


def rotate():
    global ans
    graph2 = copy.deepcopy(graph)
    for l in range(K):
        r = cmd[cmdSeq[l]][0]
        c = cmd[cmdSeq[l]][1]
        s = cmd[cmdSeq[l]][2]
        for k in range(s):
            x1, y1 = r - s + k, c - s + k
            x2, y2 = r + s - k, c + s - k
            rotate_layer(x1, y1, x2, y2, graph2)
    for i in range(1, N + 1):
        ans = min(sum(graph2[i]), ans)
    return


def rotate_layer(x1, y1, x2, y2, graph2):
    value = graph2[x1][y1]
    for y in range(y1 + 1, y2 + 1):
        tmp = graph2[x1][y]
        graph2[x1][y] = value
        value = tmp
    for x in range(x1 + 1, x2 + 1):
        tmp = graph2[x][y2]
        graph2[x][y2] = value
        value = tmp
    for y in range(y2 - 1, y1 - 1, -1):
        tmp = graph2[x2][y]
        graph2[x2][y] = value
        value = tmp
    for x in range(x2 - 1, x1 - 1, -1):
        tmp = graph2[x][y1]
        graph2[x][y1] = value
        value = tmp
    return


N, M, K = map(int, input().split())
graph = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, M + 1):
        graph[i][j] = row[j - 1]

cmd = []
for i in range(K):
    r, c, s = map(int, input().split())
    cmd.append([r, c, s])

cmdSeq = [0] * K
visited = [0] * K
ans = 1e9
permutation(0)
print(ans)
