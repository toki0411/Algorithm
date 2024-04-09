def findParents(x):
    if x == parents[x]:
        return x
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
N, M = map(int, input().split())
parents = [0] * (N+1)
for k in range(N+1):
    parents[k] = k
edgeList = []
total = 0
for i in range(M):
    a, b, c = map(int, input().split())
    edgeList.append([a,b,c])
    total += c
edgeList.sort(key = lambda x: x[2])
weight = 0

for edge in edgeList:
    if not union(edge[0], edge[1]):
        continue
    weight += edge[2]
root = findParents(1)
for i in range(2, N+1):
    target = findParents(i)
    if root != target:
        print(-1)
        exit()
print(total-weight)