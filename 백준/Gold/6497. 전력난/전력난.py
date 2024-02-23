import sys

input = sys.stdin.readline

def union(a, b):
    aRoot = findParent(a)
    bRoot = findParent(b)
    if aRoot == bRoot:
        return False
    if aRoot < bRoot :
        parents[bRoot] = aRoot
    else:
        parents[aRoot] = bRoot
    return True

def findParent(a):
    if parents[a] == a:
        return a
    parents[a] = findParent(parents[a])
    return parents[a]
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    total = 0
    edgeList = []
    parents = [0] * (m + 1)
    for _ in range(n):
        x, y, z = map(int, input().split())
        total += z
        edgeList.append([x,y,z])
    edgeList.sort(key = lambda x: x[2])

    for i in range(m+1):
        parents[i] = i

    weight = 0
    cnt = 0
    for edge in edgeList:
        if not union(edge[0], edge[1]):
            continue
        else:
            weight += edge[2]
            cnt +=1
            if cnt == m-1:
                break;
    print(total - weight)