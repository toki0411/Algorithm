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

def make():
    for k in range(N + 1):
        parents[k] = k

N ,M = map(int, input().split())
parents = [0] * (N+1)
edgeList = []
for i in range(M):
    a, b, c = map(int, input().split())
    edgeList.append([a,b,c])

make()
edgeList.sort(key = lambda x: x[2])
cnt = 0
weight = 0
last = 0
for edge in edgeList:
    if not union(edge[0], edge[1]):
        continue
    weight += edge[2]
    cnt += 1
    last = edge[2]
    if cnt == N-1:
        break

print(weight-last)
