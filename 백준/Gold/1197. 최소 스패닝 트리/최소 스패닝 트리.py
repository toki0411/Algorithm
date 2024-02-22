def getParent(x):
    if x == parents[x]: return x
    parents[x] = getParent(parents[x])
    return parents[x]

def union(a, b):
    aParent = getParent(a)
    bParent = getParent(b)
    if aParent == bParent: return False
    parents[bParent] = aParent
    return True

v, e = map(int, input().split())
edgeList = []
parents = [0] * (v+1);
for _ in range(e):
    edgeList.append(list(map(int, input().split())))
edgeList.sort(key = lambda x: x[2])

for i in range(v+1):
    parents[i] = i

weight = 0
cnt = 0
for edge in edgeList:
    if not union(edge[0], edge[1]): #사이클 생성되므로 continue
        continue;
    else:
        weight += edge[2]
        cnt += 1
        if cnt == v-1:
            break
print(weight)