def init():
    for i in range(1, n+1):
        parents[i] = i

def findParents(a):
    if a == parents[a]: return a
    parents[a] = findParents(parents[a])
    return parents[a]
def union(a, b):
    aRoot = findParents(a)
    bRoot = findParents(b)
    if aRoot == bRoot: return True
    if aRoot < bRoot:
        parents[bRoot] = aRoot
    else:
        parents[aRoot] = bRoot

n = int(input())
parents = [0] * (n+1)
init()
for i in range(n-2):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n+1):
    if i== parents[i]:
        print(i, end = " ")