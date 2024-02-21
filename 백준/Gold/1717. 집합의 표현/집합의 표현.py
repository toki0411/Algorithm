import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def unionParent(a, b):
    aParent = getParent(a)
    bParent = getParent(b)
    if aParent < bParent:
        parent[bParent] = aParent
    elif aParent > bParent:
        parent[aParent] = bParent


def getParent(x):  #부모 노드를 찾는 함수
    if parent[x] != x: 
        parent[x] = getParent(parent[x])
    return parent[x]

for _ in range(m):
    x, a, b = map(int, input().split())

    if x == 0:
        unionParent(a,b)
    elif x == 1:
        aParent = getParent(a)
        bParent = getParent(b)
        if aParent == bParent:
            print("YES")
        else:
            print("NO")