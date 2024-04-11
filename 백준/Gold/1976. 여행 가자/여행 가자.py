import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def findParents(x):
    if x == parents[x]:
        return x
    parents[x] = findParents(parents[x])
    return parents[x]
def union(aa, bb):
    aRoot = findParents(aa)
    bRoot = findParents(bb)
    if aRoot < bRoot:
        parents[bRoot] = aRoot
    else:
        parents[aRoot] = bRoot

N = int(input())
M = int(input())
parents = [0] * (N+1)
for i in range(1, N+1):
    parents[i] = i
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(i+1, N):
        if arr[j] == 1:
            union(i+1, j+1)

travel = list(map(int, input().split()))
for i in range(len(travel)-1):
    now = travel[i]
    next = travel[i+1]
    if findParents(now) != findParents(next):
        print("NO")
        exit()
print("YES")